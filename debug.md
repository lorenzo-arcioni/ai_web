<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Automi a Stati Finiti (FSA)</title>
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
            <h1 class="text-4xl font-bold mb-4 text-gray-800">Automi a Stati Finiti (FSA)</h1>
        </header>

        <article class="prose max-w-none">
            <h2>Definizione Formale</h2>
<p>Un automa a stati finiti è una <strong>quintupla</strong> $(Q, \Sigma, \delta, q_0, A)$, dove:<br />
- <strong>$Q$</strong>: Insieme finito di stati (es. $q_0, q_1, q_2$).<br />
- <strong>$\Sigma$</strong>: Alfabeto (simboli consentiti, es. $\{a, b, l\}$).<br />
- <strong>$\delta$</strong>: Funzione di transizione $\delta(q, x) \rightarrow q'$. Definisce come l'automa passa da uno stato $q$ a $q'$ leggendo il simbolo $x$.<br />
- <strong>$q_0$</strong>: Stato iniziale (es. $q_0$).<br />
- <strong>$A$</strong>: Insieme di stati accettanti/finali (es. $\{q_4\}$).</p>
<h2>Esempio: Il "Linguaggio delle Pecore"</h2>
<h3>Descrizione</h3>
<ul>
<li><strong>Linguaggio $L_{\text{sheep}}$</strong>: Stringhe che iniziano con "b", seguite da almeno due "a", e terminano con "!" (es. "baa!", "baaaaa!", ...).</li>
<li><strong>Regex corrispondente</strong>: <code>/baa+!/</code>.</li>
</ul>
<h3>Automa Corrispondente</h3>
<p><img src="/static/images/tikz/c2065ac9f7677b8cda1c2e7e9cba0f18.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" /></p>
<h3>Tabella di Transizione</h3>
<table>
<thead>
<tr>
<th>Stato</th>
<th>$b$</th>
<th>$a$</th>
<th>$!$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$q_0$</td>
<td>$q_1$</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>$q_1$</td>
<td>-</td>
<td>$q_2$</td>
<td>-</td>
</tr>
<tr>
<td>$q_2$</td>
<td>-</td>
<td>$q_3$</td>
<td>-</td>
</tr>
<tr>
<td>$q_3$</td>
<td>-</td>
<td>$q_3$</td>
<td>$q_4$</td>
</tr>
<tr>
<td>$q_4$</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2>Funzionamento di un FSA</h2>
<h3>Processo di Riconoscimento</h3>
<ol>
<li><strong>Input</strong>: "baaa!"</li>
<li>$q_0 \xrightarrow{b} q_1 \xrightarrow{a} q_2 \xrightarrow{a} q_3 \xrightarrow{a} q_3 \xrightarrow{!} q_4$ → <strong>Accettata</strong>.</li>
<li><strong>Input</strong>: "ba!"</li>
<li>$q_0 \xrightarrow{b} q_1 \xrightarrow{a} q_2$ → Esaurimento input in stato non finale → <strong>Rifiutata</strong>.</li>
</ol>
<h2>Accettatori vs. Generatori</h2>
<ul>
<li><strong>Accettatori</strong>: Verificano se una stringa appartiene al linguaggio.</li>
<li><strong>Generatori</strong>: Producono tutte le stringhe valide.<br />
<strong>Esempio generato</strong>:<br />
<img src="/static/images/tikz/dede56224f04bae018c7b65e1093559e.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" /></li>
</ul>
<h2>Relazione tra Regex e FSA</h2>
<h3>Equivalenze</h3>
<table>
<thead>
<tr>
<th>Operazione Regex</th>
<th>Operazione FSA</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RE1\|RE2</code> (Unione)</td>
<td>FSA che accetta $L_1 \cup L_2$</td>
</tr>
<tr>
<td><code>RE1RE2</code> (Concatenazione)</td>
<td>FSA che accetta $L_1L_2$</td>
</tr>
<tr>
<td><code>RE*</code> (Kleene Star)</td>
<td>FSA con loop per ripetizioni</td>
</tr>
</tbody>
</table>
<p><strong>Esempio</strong>: Regex <code>(a|b)*c</code><br />
<img src="/static/images/tikz/eff741d9ebf0391963103c5db1379ad9.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" /></p>
<h2>Esercizio Guidato</h2>
<h3>Dati</h3>
<ul>
<li>$L_1 = \\{\text{nlp}, \text{nat\_lang\_proc}\\}$</li>
<li>$L_2 = \\{\text{\_is\_cool}\\}$</li>
<li>$L_3 = L_1L_2^*$</li>
</ul>
<h3>Soluzione</h3>
<p><strong>FSA per $L_3$</strong>:<br />
<img src="/static/images/tikz/8fc84c381c7c122012ead33381b4da43.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" /></p>
<h2>Applicazioni in NLP</h2>
<h3>Tokenizzazione</h3>
<p><img src="/static/images/tikz/a13c524a49c3e0197788b6ee60c25376.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" /></p>
<blockquote>
<p><strong>Etichette</strong>: #FSA #Regex #LinguaggiFormali<br />
<strong>Collegamenti</strong>: <a href="/post/Algoritmi/Intelligenza Artificiale/Natural Language Processing/Espressioni Regolari" class="simple-link">Espressioni Regolari</a>, <span class="broken-link">Teoria degli Automi</span><br />
<strong>Risorse</strong>:<br />
- <a href="https://web.stanford.edu/~jurafsky/slp3/">Speech and Language Processing (Jurafsky &amp; Martin)</a>  </p>
</blockquote>
        </article>

        <a href="/" class="back-link text-lg">
            ← Torna alla home
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="/static/js/post.js"></script>
</body>
</html>