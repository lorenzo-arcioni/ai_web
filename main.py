import os
import re
from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import markdown
import urllib.parse

# Inizializza FastAPI
app = FastAPI()

# Aggiungi gestione file statici
app.mount("/static", StaticFiles(directory="static"), name="static")

# Percorso della cartella contenente i file markdown
CONTENT_DIR = os.path.join(os.getcwd(), "content")

# Inizializza Jinja2
env = Environment(loader=FileSystemLoader('templates'))

def protect_math_content(md_content):
    math_blocks = []
    
    # Pattern per blocchi matematici $$
    pattern_block = re.compile(r'(\$\$.*?\$\$)', re.DOTALL)
    # Pattern per equazioni inline $
    pattern_inline = re.compile(r'(?<!\\)\$([^\$]*?(?<!\\))\$')
    
    def replace_block(match):
        math_blocks.append(match.group(1))
        return f'@@MATH_BLOCK_{len(math_blocks)-1}@@'
    
    def replace_inline(match):
        math_blocks.append(match.group(0))  # Preserva i $
        return f'@@MATH_INLINE_{len(math_blocks)-1}@@'
    
    # Sostituisci prima i blocchi, poi gli inline
    protected = pattern_block.sub(replace_block, md_content)
    protected = pattern_inline.sub(replace_inline, protected)
    
    return protected, math_blocks

def restore_math_content(html_content, math_blocks):
    for i, math in enumerate(math_blocks):
        html_content = html_content.replace(f'@@MATH_BLOCK_{i}@@', math)
        html_content = html_content.replace(f'@@MATH_INLINE_{i}@@', math)
    return html_content

def remove_math_paragraphs(html_content):
    # Rimuove i paragrafi attorno ai blocchi $$
    html_content = re.sub(
        r'<p>\s*(\$\$.*?\$\$)\s*</p>',
        r'\1',
        html_content,
        flags=re.DOTALL
    )
    # Rimuove i paragrafi attorno agli inline $
    html_content = re.sub(
        r'<p>\s*(\$.*?\$)\s*</p>',
        r'\1',
        html_content,
        flags=re.DOTALL
    )
    return html_content

def find_markdown_file(name):
    """Cerca un file Markdown nell'albero delle directory."""
    # Normalizza il nome rimuovendo spazi e estensioni .md
    normalized_name = name.strip().lower().removesuffix('.md')
    target_filename = f"{normalized_name}.md"

    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            # Confronta i nomi in modo case-insensitive
            if file.lower() == target_filename:
                return os.path.relpath(os.path.join(root, file), CONTENT_DIR)
    return None

def extract_title_from_markdown(md_content):
    """Estrae il primo titolo (H1) dal contenuto Markdown."""
    # Cerca il primo titolo H1 che inizia con #
    match = re.search(r'^# (.+)', md_content, re.MULTILINE)
    return match.group(1) if match else "Titolo non trovato"

def process_obsidian_links(html_content):
    """Sostituisce i link Obsidian con link funzionanti."""
    def replace_link(match):
        file_name = match.group(1).strip()  # Rimuove spazi accidentali
        display_text = match.group(2).strip() if match.group(2) else file_name

        file_path = find_markdown_file(file_name)
        
        if file_path:
            link = f"/post/{file_path.removesuffix('.md')}"
            return f'<a href="{link}" class="simple-link">{display_text}</a>'
        return f'<span class="broken-link">{display_text}</span>'
    
    return re.sub(
        r'\[\[(.*?)(?:\|(.*?))?\]\]',  # Pattern migliorato
        replace_link, 
        html_content, 
        flags=re.DOTALL
    )

def build_hierarchy(categories):
    hierarchy = {'subcategories': {}, 'files': []}
    
    for path, files in categories.items():
        parts = path.split(os.sep)
        current_node = hierarchy
        
        for part in parts:
            if part not in current_node['subcategories']:
                current_node['subcategories'][part] = {
                    'subcategories': {},
                    'files': []
                }
            current_node = current_node['subcategories'][part]
        
        current_node['files'] = files
    
    return hierarchy['subcategories']  # Restituisce solo le sottocategorie radice

@app.get("/", response_class=HTMLResponse)
def home():
    categories = {}
    for root, _, files in os.walk(CONTENT_DIR):
        relative_path = os.path.relpath(root, CONTENT_DIR)
        if relative_path == '.' or relative_path.split(os.sep)[0] == 'imgs':
            continue
            
        filtered_files = [f for f in files if f.endswith(".md") and f != "tmp.md"]
        if filtered_files:
            categories[relative_path] = filtered_files

    category_tree = build_hierarchy(categories)
    template = env.get_template("index.html")
    return template.render(categories=category_tree)

@app.get("/post/{full_path:path}", response_class=HTMLResponse)
def get_article(full_path: str):
    # Decodifica il percorso per gestire %20 e altri caratteri speciali
    full_path = urllib.parse.unquote(full_path)
    
    # Costruisci il percorso completo del file
    file_path = os.path.join(CONTENT_DIR, full_path + ".md")
    
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Articolo non trovato.")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        # Estrai il titolo dal contenuto Markdown
        title = extract_title_from_markdown(md_content)

        # Salta la prima riga
        md_content = "\n".join(md_content.split("\n")[1:])

        # Sostituisci i path delle immagini con il percorso corretto
        md_content = re.sub(
            '/home/lorenzo/Documenti/GitHub/my-obsidian-vault/images',
            '/static/images/posts',
            md_content
        )

        md_content = md_content.replace('`$`', '`\\$`')  # Escape del $ nei blocchi di codice
        
        # Proteggi i blocchi matematici
        protected_content, math_blocks = protect_math_content(md_content)
        
        # Converti Markdown
        html_content = markdown.markdown(
            protected_content, 
            extensions=[
                        'fenced_code',
                        'tables',
                        'nl2br',
                        'md_in_html',
                        'extra',
                        'attr_list',
                        'smarty',
                        'toc',
                        'admonition',
                        'def_list',
                        'footnotes',
                        'sane_lists',
                    ]
        )

        # Ripristina i blocchi matematici
        html_content = restore_math_content(html_content, math_blocks)

        # Rimuovi \_ dal codice HTML
        html_content = html_content.replace('\\_', '_')
        
        # Rimuovi paragrafi attorno alle equazioni
        html_content = remove_math_paragraphs(html_content)
        
        # Processa i link Obsidian
        html_content = process_obsidian_links(html_content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    template = env.get_template("post.html")

    with open("debug.md", "w", encoding="utf-8") as f:
        f.write(template.render(title=title, content=html_content))
    
    return template.render(title=title, content=html_content)

@app.get("/about", response_class=HTMLResponse)
def about():
    template = env.get_template("about.html")
    return template.render()

@app.get("/prova.html", response_class=HTMLResponse)
def prova():
    template = env.get_template("prova.html")
    
    return template.render()