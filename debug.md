<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Espressioni Regolari (Regex)</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="/static/images/favicon.png" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css" rel="stylesheet">
    <link href="/static/css/main.css" rel="stylesheet">
    
    <!-- MathJax Configuration -->
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [['$','$'], ['\\(','\\)']],
                displayMath: [['$$','$$'], ['\\[','\\]']],
                processEscapes: true,
                processEnvironments: false
            },
            TeX: {
                Macros: {
                    argmin: "\\mathop{\\mathrm{argmin}}\\limits",
                    argmax: "\\mathop{\\mathrm{argmax}}\\limits"
                }
            },
            "HTML-CSS": { 
                availableFonts: ["TeX"],
                webFont: "TeX"
            }
        });
    </script>
    <script type="text/javascript" async
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
    </script>
</head>
<body>
    <div class="container mx-auto px-4 py-12 max-w-4xl">
        <header class="text-center mb-12">
            <nav class="mb-8 flex justify-between items-center max-w-2xl mx-auto px-4">
                <div class="space-x-4">
                    <a href="/" class="text-gray-600 hover:text-accent-color transition-colors">Home</a>
                    <a href="/about" class="text-gray-600 hover:text-accent-color transition-colors">About</a>
                </div>
            </nav>
            <h1 class="text-4xl font-bold mb-4 text-gray-800">Espressioni Regolari (Regex)</h1>
        </header>

        <article class="prose max-w-none">
            <h2 id="cosa-sono-le-regex">Cosa sono le Regex?</h2>
<ul>
<li><strong>Definizione</strong>: Sequenze di caratteri che definiscono un pattern di ricerca, utilizzate per individuare, estrarre o sostituire testo. Fanno parte dei <strong>rule-based systems</strong>.</li>
<li><strong>Scopo principale</strong>: Automatizzare operazioni di testo complesse (es. validare email, estrarre dati).</li>
<li><strong>Esempi di utilizzo</strong>:</li>
<li>Ricerca di parole chiave in documenti.</li>
<li>Pulizia di dataset testuali.</li>
<li>Sostituzioni avanzate in editor di codice.</li>
<li><strong>Pattern Matching</strong>: Processo di identificazione di sequenze testuali che corrispondono a un formato specifico definito dal pattern. Le regex permettono di cercare, validare o estrarre porzioni di testo seguendo regole flessibili (es. trovare tutti i numeri in un documento).</li>
</ul>
<h2 id="strumenti-per-testare-le-regex">Strumenti per Testare le Regex</h2>
<ul>
<li><strong>Regex101</strong> (<a href="https://regex101.com/">link</a>): Piattaforma web con debugger integrato e spiegazioni dettagliate.</li>
<li><strong>Python</strong> (<code>re</code> module): Libreria standard per manipolare regex (<a href="https://www.programiz.com/python-programming/regex">esempi</a>).</li>
<li><strong>Java</strong>: Utilizza <code>java.util.regex</code> per operazioni avanzate (<a href="https://www.w3schools.com/java/java_regex.asp">guide</a>).</li>
<li><strong>Perl</strong>: Linguaggio storico per regex, con operatori come <code>s///</code> per sostituzioni.</li>
</ul>
<h2 id="sintassi-base-delle-regex">Sintassi Base delle Regex</h2>
<h3 id="come-funziona-il-pattern-matching">Come Funziona il Pattern Matching</h3>
<p>Il pattern matching con regex si basa su regole di sintassi che combinano:<br />
- <strong>Caratteri letterali</strong>: Cercano corrispondenze esatte (es. <code>cane</code> trova solo &ldquo;cane&rdquo;).<br />
- <strong>Quantificatori</strong>: Specificano quante volte un elemento può ripetersi (es. <code>?</code>, <code>+</code>, <code>*</code>).<br />
- <strong>Ancore</strong>: Definiscono la posizione nel testo (es. <code>^</code> per l&rsquo;inizio riga, <code>\$</code> per la fine).<br />
- <strong>Classi di caratteri</strong>: Raggruppano opzioni valide (es. <code>[aeiou]</code> per vocali).<br />
- <strong>Range</strong>: Definiscono un intervallo di caratteri (es. <code>[a-z]</code> per lettere minuscole).<br />
- <strong>Gruppi</strong>: Isolano parti del pattern con <code>()</code> per riferimenti o operazioni specifiche.<br />
- <strong>Alternanza</strong>: Permettono scelte tra opzioni con <code>|</code> (es. <code>gatto|cane</code>).<br />
- <strong>Escape</strong>: I metacaratteri speciali (es. <code>.</code>, <code>*</code>) richiedono <code>\</code> per essere cercati letteralmente (es. <code>\.</code>).  </p>
<h3 id="caratteri-letterali">Caratteri Letterali</h3>
<ul>
<li><strong>Caratteri Literali</strong>: <code>a</code>, <code>b</code>, <code>c</code>, <code>d</code>, <code>e</code>, <code>f</code>, <code>g</code>, <code>h</code>, <code>i</code>, <code>j</code>, <code>k</code>, <code>l</code>, <code>m</code>, <code>n</code>, <code>o</code>, <code>p</code>, <code>q</code>, <code>r</code>, <code>s</code>, <code>t</code>, <code>u</code>, <code>v</code>, <code>w</code>, <code>x</code>, <code>y</code>, <code>z</code>.</li>
<li><strong>Caratteri Numerici</strong>: <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, <code>6</code>, <code>7</code>, <code>8</code>, <code>9</code>. </li>
<li><strong>Caratteri Speciali</strong>: <code></code>, <code>\t</code>, <code>\n</code>, <code>\r</code>, <code>\f</code>, <code>\b</code>, <code>\a</code>, <code>\e</code>, <code>\0</code>, <code>\xHH</code>, <code>\uHHHH</code>, <code>\UHHHHHHHH</code>.</li>
<li><strong>Carattere di Escape</strong>: <code>\</code>, <code>\\</code>, <code>\n</code>, <code>\t</code>, <code>\r</code>, <code>\f</code>, <code>\b</code>, <code>\a</code>, <code>\e</code>, <code>\0</code>, <code>\xHH</code>, <code>\uHHHH</code>, <code>\UHHHHHHHH</code>.</li>
</ul>
<h3 id="metacaratteri">Metacaratteri</h3>
<table>
<thead>
<tr>
<th>Simbolo</th>
<th>Funzione</th>
<th>Esempio</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>[]</code></td>
<td>Definisce un set di caratteri ammessi.</td>
<td><code>[Aa]mico</code> → &ldquo;Amico&rdquo; o &ldquo;amico&rdquo;</td>
</tr>
<tr>
<td><code>^</code></td>
<td>1) Negazione dentro <code>[]</code>.<br>2) Inizio della riga.</td>
<td><code>[^a-z]</code> → Non lettere minuscole.<br><code>^Ciao</code> → &ldquo;Ciao&rdquo; solo all&rsquo;inizio.</td>
</tr>
<tr>
<td><code>?</code></td>
<td>Zero o una occorrenza del carattere precedente.</td>
<td><code>colou?r</code> → &ldquo;color&rdquo; o &ldquo;colour&rdquo;</td>
</tr>
<tr>
<td><code>.</code></td>
<td>Qualsiasi carattere (tranne newline).</td>
<td><code>b.t</code> → &ldquo;bat&rdquo;, &ldquo;b@t&rdquo;, &ldquo;b3t&rdquo;</td>
</tr>
<tr>
<td><code>*</code></td>
<td>Zero o più occorrenze del carattere precedente.</td>
<td><code>lo*l</code> → &ldquo;ll&rdquo;, &ldquo;lol&rdquo;, &ldquo;loooool&rdquo;</td>
</tr>
<tr>
<td><code>+</code></td>
<td>Una o più occorrenze del carattere precedente.</td>
<td><code>a+</code> → &ldquo;a&rdquo;, &ldquo;aa&rdquo;, &ldquo;aaa&rdquo;</td>
</tr>
<tr>
<td><code>{n,m}</code></td>
<td>Da <code>n</code> a <code>m</code> occorrenze.</td>
<td><code>a{2,4}</code> → &ldquo;aa&rdquo;, &ldquo;aaa&rdquo;, &ldquo;aaaa&rdquo;</td>
</tr>
</tbody>
</table>
<h3 id="alias-utili">Alias Utili</h3>
<ul>
<li><code>\d</code>: Cifra numerica (<code>[0-9]</code>).</li>
<li><code>\w</code>: Carattere alfanumerico o underscore (<code>[a-zA-Z0-9_]</code>).</li>
<li><code>\s</code>: Spazio bianco (spazio, tab, newline).</li>
<li><code>\b</code>: Inizio o fine di una parola.</li>
<li><code>\D</code>, <code>\W</code>, <code>\S</code>, <code>\B</code>: Negazioni dei precedenti.</li>
<li><code>\n</code>: Newline.</li>
<li><code>\t</code>: Tab.</li>
<li><code>\r</code>: Carattere di ritorno.</li>
<li><code>\f</code>: Carattere di fine riga.</li>
<li><code>\*</code>, <code>\+</code>, <code>\?</code>: Alias per <code>*</code>, <code>+</code>, <code>?</code>.</li>
</ul>
<h2 id="gruppi-di-cattura">Gruppi di cattura</h2>
<p>Le <strong>parentesi tonde</strong> <code>()</code> nelle espressioni regolari vengono utilizzate per definire <strong>gruppi di cattura</strong>. Questi gruppi possono essere utilizzati per riferirsi ai sottostringhe cercate e per eseguire operazioni di sostituzione.</p>
<h3 id="esempio">Esempio</h3>
<pre><code class="language-regex">/(\w+) (\w+)/
</code></pre>
<p>Questa espressione cerca due parole separati da uno spazio. Se applicata alla stringa &ldquo;Nome Cognome&rdquo;, cattura &ldquo;Nome&rdquo; e &ldquo;Cognome&rdquo;.</p>
<h2 id="esercizio-guidato-trovare-la-parola-the">Esercizio Guidato: Trovare la Parola &ldquo;the&rdquo;</h2>
<ol>
<li><strong>Primo tentativo</strong>: `/the/ → Trova &ldquo;the&rdquo; ma anche &ldquo;there&rdquo;, &ldquo;other&rdquo; (falsi positivi).**</li>
<li><strong>Matching case-insensitive</strong>: <code>/[tT]he/ → Trova "The" e "the".</code></li>
<li>
<p><strong>Evitare parole contenenti &ldquo;the&rdquo;</strong>:<br />
<code>/[^a-zA-Z][tT]he[^a-zA-Z]/ → " the " in "Catch the ball"</code> ma non in <code>Mathematic</code>. </p>
</li>
<li>
<p><strong>Pattern avanzato</strong>:<br />
<code>/(^|[^a-zA-Z])[tT]he([^a-zA-Z]|$)/ → Considera inizio/fine riga.</code><br><br />
   Cerca la parola &ldquo;the&rdquo; o &ldquo;The&rdquo; solo quando isolata (circondata da caratteri non alfabetici, spazi, punteggiatura, inizio/fine riga) compresi quando inizia o finisce una frase.</p>
</li>
</ol>
<p><strong>Problemi comuni</strong>:<br />
- <strong>Falsi positivi</strong>: Match indesiderati (es. &ldquo;there&rdquo;).<br />
- <strong>Falsi negativi</strong>: Mancato match di &ldquo;The&rdquo; all&rsquo;inizio frase.<br />
- <strong>Bilanciamento</strong>: Aumentare la <strong>precisione</strong> (ridurre falsi positivi) e il <strong>recall</strong> (ridurre falsi negativi).</p>
<h2 id="registri-parentesi-per-riferimenti">Registri (Parentesi per Riferimenti)</h2>
<p>Le <strong>parentesi tonde</strong> <code>()</code> registrano le occorrenze trovate nelle espressioni regolari in dei cosi detti <strong>registri</strong>.</p>
<h3 id="sintassi-di-base">Sintassi di Base</h3>
<p>Un gruppo di cattura è definito con <code>()</code> e può essere richiamato con <code>\n</code>, dove <code>n</code> è il numero del gruppo nell&rsquo;ordine in cui compare.</p>
<p><strong>Esempio</strong>:</p>
<pre><code class="language-regex">/(\d+)-(\d+)/
</code></pre>
<p>Questa regex cattura due numeri separati da un trattino <code>-</code>:<br />
- <code>\1</code> si riferisce al primo numero.<br />
- <code>\2</code> si riferisce al secondo numero.</p>
<p>Se applicata alla stringa <code>2023-2024</code>, cattura <code>2023</code> come <code>\1</code> e <code>2024</code> come <code>\2</code>.</p>
<h3 id="applicazione-riorganizzazione-del-testo">Applicazione: Riorganizzazione del Testo</h3>
<p>I riferimenti ai gruppi catturati vengono utilizzati nelle operazioni di sostituzione.</p>
<p><strong>Esempio</strong>:</p>
<pre><code class="language-regex">s/(\w+) (\w+)/\2 \1/
</code></pre>
<p>Questa espressione inverte la posizione di due parole:<br />
- Input: <code>Nome Cognome</code><br />
- Output: <code>Cognome Nome</code></p>
<h3 id="altri-esempi-di-utilizzo">Altri Esempi di Utilizzo</h3>
<h4 id="1-estrazione-del-dominio-da-unemail">1. Estrazione del Dominio da un&rsquo;Email</h4>
<pre><code class="language-regex">/(\w+)@(\w+\.\w+)/
</code></pre>
<ul>
<li><code>\1</code> rappresenta il nome utente.</li>
<li><code>\2</code> rappresenta il dominio dell&rsquo;email.</li>
</ul>
<p>Se applicata a <code>esempio@email.com</code>, cattura:<br />
- <code>esempio</code> come <code>\1</code><br />
- <code>email.com</code> come <code>\2</code></p>
<h4 id="2-riformattazione-della-data">2. Riformattazione della Data</h4>
<p>Se una data è scritta come <code>2024/03/26</code> e la si vuole convertire in <code>26-03-2024</code>:</p>
<pre><code class="language-regex">s/(\d{4})/(\d{2})/(\d{2})/\3-\2-\1/
</code></pre>
<ul>
<li><code>\1</code> è l&rsquo;anno.</li>
<li><code>\2</code> è il mese.</li>
<li><code>\3</code> è il giorno.</li>
</ul>
<p>Risultato della sostituzione: <code>26-03-2024</code>.</p>
<h3 id="conclusione">Conclusione</h3>
<p>I <strong>registri</strong> e i <strong>gruppi di cattura</strong> sono strumenti potenti per manipolare il testo con le espressioni regolari. Sono utili per:<br />
- Estrarre informazioni specifiche.<br />
- Riordinare parti di una stringa.<br />
- Modificare il formato di dati testuali.</p>
<h2 id="caso-storico-eliza-1966">Caso Storico: ELIZA (1966)</h2>
<p>Descrizione: Primo chatbot che simulava uno psicologo rogersiano.</p>
<p>Funzionamento:</p>
<ul>
<li>
<p>Utilizzava regex semplici per identificare parole chiave (es. &ldquo;madre&rdquo;, &ldquo;triste&rdquo;).</p>
</li>
<li>
<p>Generava risposte predefinite basate su sostituzioni (es. &ldquo;Dimmi di più sulla tua famiglia&rdquo;).</p>
</li>
</ul>
<p>Limitazioni: Nessuna comprensione semantica, solo pattern matching superficiale.</p>
<p><a href="https://www.youtube.com/watch?v=4sngIh0YJtk" target="_blank">ELIZA, video dimostrativo della funzionalità</a></p>
<h2 id="risorse">Risorse</h2>
<ul>
<li>
<p>Libro: Speech and Language Processing (Jurafsky &amp; Martin).</p>
</li>
<li>
<p>Tool online: Regex101 per testare pattern.</p>
</li>
<li>
<p>Etichette: #Regex #NLP #PatternMatching</p>
</li>
<li>
<p>Collegamenti: <span class="broken-link">Introduzione all&rsquo;NLP</span>, <span class="broken-link">Elaborazione del Testo</span></p>
</li>
</ul>
        </article>

        <a href="/" class="back-link text-lg">
            ← Torna alla home
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="/static/js/post.js"></script>
</body>
</html>