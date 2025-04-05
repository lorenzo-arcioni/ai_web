<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Modelli di Linguaggio</title>
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
            <h1 class="text-4xl font-bold mb-4 text-gray-800">Modelli di Linguaggio</h1>
        </header>

        <article class="prose max-w-none">
            <p>I modelli di linguaggio sono sistemi di intelligenza artificiale addestrati per comprendere, generare e manipolare il linguaggio umano. Utilizzano architetture avanzate (come i <strong><span class="broken-link">transformers</span></strong>) per prevedere sequenze di parole o caratteri basandosi sul contesto. In particolare, sono distribuzioni probabilistiche sulle sequenze di parole, che permettono di prevedere il prossimo token in base al contesto precedente.</p>
<p>Per un approfondimento sui linguaggi, <span class="broken-link">qui</span>.</p>
<h2 id="perche-distribuzioni-probabilistiche">Perché Distribuzioni Probabilistiche?</h2>
<h3 id="limiti-delle-grammatiche-formali">Limiti delle Grammatiche Formali</h3>
<ul>
<li><strong>Modelli &ldquo;Binari&rdquo;</strong>:<br />
  Le grammatiche formali (es. regolari, context-free) definiscono regole rigide per determinare se una frase è <em>legal</em> o meno in una lingua (approccio <strong>0/1</strong>).<br />
  → <strong>Problema</strong>: Il linguaggio naturale è ambiguo, flessibile e dipendente dal contesto.<br />
  Esempio: <em>&ldquo;Leggo un libro sul volo&rdquo;</em> può essere interpretato in modo diverso (lettura <em>su</em> un argomento vs. lettura <em>fisicamente sopra</em> un oggetto).</li>
</ul>
<h3 id="vantaggi-dei-modelli-probabilistici">Vantaggi dei Modelli Probabilistici</h3>
<ol>
<li>
<p><strong>Gestione dell&rsquo;incertezza</strong>:<br />
   Assegnano una <strong>probabilità</strong> a ogni frase/stringa, riflettendo la sua &ldquo;naturalezza&rdquo; o plausibilità nel contesto reale.<br />
   → Utile per: disambiguazione, ranking di ipotesi, generazione fluida.</p>
</li>
<li>
<p><strong>Adattabilità al mondo reale</strong>:<br />
   - Modellano variazioni linguistiche (dialetti, errori ortografici, slang).<br />
   - Tengono conto di correlazioni statistiche tra parole (es. <em>&ldquo;caffè&rdquo;</em> → alta probabilità di <em>&ldquo;bere&rdquo;</em> o <em>&ldquo;tazzina&rdquo;</em>).</p>
</li>
<li>
<p><strong>Fondamento per NLP moderno</strong>:<br />
   Consentono di:<br />
   - Addestrare modelli su corpora non perfetti (es. web text con rumore).<br />
   - Ottimizzare task come traduzione o riconoscimento vocale tramite massimizzazione della likelihood.</p>
</li>
</ol>
<blockquote>
<p>📊 <strong>Esempio Pratico</strong>:<br />
Un modello probabilistico può assegnare:<br />
- P(<em>&ldquo;Il gatto corre sul tetto&rdquo;</em>) = 0.85<br />
- P(<em>&ldquo;Il tetto corre sul gatto&rdquo;</em>) = 0.02<br />
Pur essendo entrambe frasi <em>sintatticamente corrette</em>, la probabilità riflette la plausibilità semantica.</p>
</blockquote>
<h3 id="confronto-chiave">Confronto Chiave</h3>
<table>
<thead>
<tr>
<th><strong>Approccio</strong></th>
<th>Grammatiche Formali</th>
<th>Modelli Probabilistici</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Output</strong></td>
<td>Binario (accetta/rigetta)</td>
<td>Probabilità continua</td>
</tr>
<tr>
<td><strong>Flessibilità</strong></td>
<td>Bassa (regole fisse)</td>
<td>Alta (apprendimento dati)</td>
</tr>
<tr>
<td><strong>Gestione Ambiguità</strong></td>
<td>Limitata</td>
<td>Ottimizzata</td>
</tr>
<tr>
<td><strong>Use Case</strong></td>
<td>Compilatori, parser semplici</td>
<td>NLP, generazione testo</td>
</tr>
</tbody>
</table>
<p>Prima di proseguire, è bene aver compreso a pieno le <a href="/post/Probabilità/Basi di Probabilità" class="simple-link">Basi di Probabilità</a>.</p>
<h2 id="previsione-probabilistica-del-completamento-delle-frasi">Previsione Probabilistica del completamento delle frasi</h2>
<p>Un modello linguistico supporta la previsione del completamento di una frase:<br />
- <strong>Esempi</strong>:<br />
  - <em>Please turn off your cell _____</em><br />
  - <em>Your program does not ______</em><br />
  - I sistemi di input predittivo possono indovinare ciò che stai scrivendo e suggerire opzioni di completamento.</p>
<h3 id="approccio-statistico-alla-previsione-delle-parole">Approccio statistico alla previsione delle parole</h3>
<p>L&rsquo;obiettivo è prevedere la parola successiva in una frase o correggere un errore ortografico utilizzando <strong>probabilità condizionate</strong> basate sul contesto precedente.</p>
<p><strong>Definizioni</strong>:</p>
<ul>
<li>
$w$: una data parola.</p>
</li>
<li>
<p>$\mathbb{P}(w_1, \ldots, w_n)$: rappresenta la <strong>probabilità congiunta</strong> dell’intera sequenza di parole $(w_1, w_2, \dots, w_n)$, ovvero la probabilità di ottenere proprio questa specifica sequenza di parole in un dato contesto (per esempio, un modello di linguaggio).</p>
</li>
<li>$\mathbb P(w_n | w_1, w_2, ..., w_{n-1})$: è la probabilità che, data la sequenza di parole $w_1, \ldots, w_{n-1}$ (già presenti nel contesto), la prossima parola sia $w_n$.</li>
</ul>
<p><strong>Esempio</strong>: Se consideriamo una frase come <em>&ldquo;oggi piove molto&rdquo;</em>, la probabilità congiunta $\mathbb{P}(\text{"oggi"}, \text{"piove"}, \text{"molto"})$ indica quanto questa sequenza sia comune nel linguaggio naturale.</p>
<p><strong>Esempio</strong>: Se consideriamo una frase come <em>&ldquo;the pen is on the&rdquo;</em>, la probabilità che la prossima parola sia &ldquo;table&rdquo; è $\mathbb P("table" | "the", "pen", "is", "on")$.</p>
<h3 id="stima-delle-frequenze-relative">Stima delle frequenze relative</h3>
<p>Per stimare queste probabilità su un <strong>corpus molto ampio</strong>:<br />
1. <strong>Probabilità congiunta</strong> (sequenza completa). Si conta il numero totale di parole $N$:<br />
   $$\mathbb P(w_1, ..., w_n) = \frac{\text{Conteggio della sequenza } w_1, ..., w_n}{\text{Conteggio della sequenza } w_1, ..., w_{n-1}} = \frac{C(w_1, ..., w_n)}{N}$$<br />
2. <strong>Probabilità condizionata</strong> (parola successiva). Si conta quante volte una sequenza specifica occorre:<br />
   $$\mathbb P(w_n | w_1, ..., w_{n-1}) = \frac{\text{Conteggio della sequenza } w_1, ..., w_n}{\text{Conteggio della sequenza } w_1, ..., w_{n-1}} = \frac{C(w_1, ..., w_{n-1}, w_n)}{C(w_1, ..., w_{n-1})}$$<br />
   Questo metodo è chiamato <strong>stima della frequenza relativa</strong>.</p>
<h3 id="vantaggi-e-svantaggi-della-stima-a-frequenza-relativa">Vantaggi e svantaggi della stima a frequenza relativa</h3>
<p><strong>Vantaggi</strong>:<br />
- La stima a frequenza relativa è una <em>Stima di Massima Verosimiglianza (MLE)</em>:<br />
  - Dato un modello, l&rsquo;MLE produce la probabilità massima ottenibile dai dati disponibili.</p>
<p><strong>Svantaggi</strong>:<br />
- Richiede un corpus <strong>ESTREMAMENTE GRANDE</strong> per stime accurate.<br />
- Computazionalmente impraticabile per sequenze lunghe o contesti complessi.</p>
<p>Ci serve un modo più efficiente per stimare $\mathbb{P}(w_1, \ldots, w_n)$.</p>
<h3 id="math_inline_27-grams-models">$N$-grams models</h3>
<p>L&rsquo;idea alla base dei modelli N-grams è <strong>semplificare il calcolo delle probabilità linguistiche</strong> evitando di considerare l&rsquo;intera storia del contesto. Si utilizza invece un&rsquo;approssimazione basata sulla <strong>proprietà di Markov</strong>:</p>
<blockquote>
<p>&ldquo;La probabilità di una parola dipende solo dalle ultime $N-1$ parole precedenti&rdquo;</p>
</blockquote>
<p><strong>Formula generale</strong>:<br />
$$\mathbb P(w_n | w_1, ..., w_{n-1}) \approx P(w_n | w_{n-N+1}, ..., w_{n-1})$$
<p>Utilizziamo l&rsquo;indice $N-1$ perché $N$ rappresenta il numero di parole considerate, ma dato che una è l&rsquo;$n$-esima (quella che dobbiamo predire), dobbiamo considerare il contesto precedente di $N-1$ parole. </p>
<p>Questo significa che per predire la prossima parola $w_n$, ci basiamo sulle $N-1$ precedenti, ovvero $w_{n-N+1}, ..., w_{n-1}$. Che intuitivamente ha senso, in quanto la parola $w_n$ sarà molto più fortemente influenzata dalle precedenti più vicine che da quelle più distanti.</p>
<p>Quindi, grazie alla <strong>proprietà di Markov</strong>, abbiamo che </p>
$$
\mathbb{P}(w_1, \ldots, w_n) \approx \prod_{k=1}^n \mathbb P(w_k \mid w_{k-N+1}, \ldots, w_{k-1})
$$
<p>Qui stiamo approssimando la probabilità congiunta usando un&rsquo;ipotesi di dipendenza limitata. </p>
<p>Cosa significa questa espressione?<br />
- Si tratta di un <strong>prodotto</strong> di probabilità condizionate.<br />
- Ogni termine $\mathbb{P}(w_k \mid w_{k-N+1}, \ldots, w_{k-1})$ rappresenta <strong>la probabilità che la parola $w_k$ appaia, dato il contesto delle $N-1$ parole precedenti</strong>.<br />
- Stiamo assumendo che la probabilità di una parola dipenda solo dalle ultime $N-1$ parole, e non dall&rsquo;intera sequenza precedente.  </p>
<p><strong>Interpretazione intuitiva</strong>:<br />
- Invece di considerare tutta la sequenza passata, <strong>usiamo solo una finestra di dimensione $N-1$</strong> per predire la parola successiva.<br />
- Questo semplifica i calcoli e rende il modello computazionalmente gestibile.  </p>
<p><strong>Esempio</strong> (modello bigramma, $N=2$):<br />
Se vogliamo stimare la probabilità di <em>&ldquo;oggi piove molto&rdquo;</em>, e assumiamo che ogni parola dipenda solo dalla precedente (<strong>modello bigramma</strong>), la formula diventa:  </p>
$$
\mathbb{P}(\text{"oggi"}, \text{"piove"}, \text{"molto"}) \approx \mathbb{P}(\text{"oggi"}) \cdot \mathbb{P}(\text{"piove"} \mid \text{"oggi"}) \cdot \mathbb{P}(\text{"molto"} \mid \text{"piove"})
$$
<ul>
<li><strong>$\mathbb{P}(\text{"oggi"})$</strong>: probabilità che inizi la frase con &ldquo;oggi&rdquo;.  </li>
<li><strong>$\mathbb{P}(\text{"piove"} \mid \text{"oggi"})$</strong>: probabilità che &ldquo;piove&rdquo; segua &ldquo;oggi&rdquo;.  </li>
<li><strong>$\mathbb{P}(\text{"molto"} \mid \text{"piove"})$</strong>: probabilità che &ldquo;molto&rdquo; segua &ldquo;piove&rdquo;.  </li>
</ul>
<p>In un <strong>modello trigramma</strong> ($N=3$), invece, avremmo:  </p>
$$
\mathbb{P}(\text{"oggi"}, \text{"piove"}, \text{"molto"}) \approx \mathbb{P}(\text{"oggi"}) \cdot \mathbb{P}(\text{"piove"} \mid \text{"oggi"}) \cdot \mathbb{P}(\text{"molto"} \mid \text{"oggi"}, \text{"piove"})
$$
<p>Qui, ogni parola dipende <strong>da entrambe le precedenti</strong>, anziché solo dall&rsquo;ultima.  </p>
<h3 id="perche-questa-approssimazione">Perché questa approssimazione?</h3>
<ul>
<li><strong>Motivazione computazionale</strong>: Calcolare la probabilità esatta di una sequenza lunga è <strong>impraticabile</strong> perché: </li>
<li>Se il nostro vocabolario ha, per esempio, <strong>20.000 parole</strong>, allora una sequenza di 5 parole può teoricamente assumere $20.000^5 = 3.2 \times 10^{23}$ combinazioni possibili! Questo significa che per stimare accuratamente tutte le probabilità congiunte necessarie, dovremmo raccogliere un <strong>enorme numero di esempi</strong> per coprire tutte le possibili frasi. Con questa approssimazione, invece, <strong>riduciamo drasticamente la complessità</strong>, poiché stimiamo ogni parola solo in base a un numero <strong>limitato</strong> di parole precedenti.  </li>
<li><strong>Motivazione linguistica</strong>: In molti casi il contesto rilevante è <strong>localizzato</strong> (es. in italiano &ldquo;fare ___ colazione&rdquo; richiede quasi sempre &ldquo;la&rdquo;) e molti costrutti grammaticali si basano solo su &ldquo;poche&rdquo; parole precedenti. Questo significa che la <strong>proprietà di Markov</strong> funziona bene per stimare le probabilità linguistiche.</li>
</ul>
<h3 id="differenze-nei-valori-di-math_inline_48">Differenze nei valori di $N$</h3>
<p>Un aspetto fondamentale nei modelli basati su n-grammi è la scelta del valore di $N$. Questo parametro determina quante parole precedenti vengono considerate nel calcolo della probabilità di una parola successiva.  </p>
<ul>
<li><strong>Un valore più grande di $N$ implica che:</strong>  </li>
<li>Il modello ha <strong>più informazioni sul contesto</strong>, poiché considera una finestra più ampia di parole precedenti.  </li>
<li>Questo porta a una <strong>maggiore capacità discriminativa</strong>, cioè il modello è più preciso nel prevedere la parola successiva in base a un contesto più dettagliato.  </li>
<li>
<p>Tuttavia, <strong>cresce il problema della scarsità dei dati</strong> (<em>data sparseness</em>):  </p>
<ul>
<li>Le combinazioni di parole diventano più numerose, quindi molte sequenze potrebbero non comparire mai nel dataset di addestramento.  </li>
<li>Questo porta a difficoltà nella stima delle probabilità, poiché alcuni n-grammi potrebbero avere conteggi molto bassi o addirittura nulli.  </li>
</ul>
</li>
<li>
<p><strong>Un valore più piccolo di $N$ implica che:</strong>  </p>
</li>
<li>Il modello ha <strong>meno precisione</strong>, poiché considera un contesto più limitato.  </li>
<li>Tuttavia, ci sono <strong>più esempi nel dataset</strong> che corrispondono a ciascun n-gramma.  </li>
<li>Questo rende le <strong>stime probabilistiche più affidabili</strong>, poiché è meno probabile che ci siano sequenze con frequenza nulla.  </li>
</ul>
<p>In pratica, c&rsquo;è un <strong>compromesso</strong> nella scelta di $N$:<br />
- Un valore più grande di $N$ aiuta a catturare meglio la struttura del linguaggio ma aumenta il rischio di dati insufficienti.<br />
- Un valore più piccolo riduce la precisione ma garantisce un modello più stabile e generalizzabile.  </p>
<p>Per affrontare il problema della scarsità dei dati nei modelli con $N$ elevato, si utilizzano tecniche come <strong>smoothing</strong>, <strong>backoff</strong> e <strong>modelli neurali</strong> come le reti ricorrenti (<em>RNN</em>) o i Transformer.</p>
<h3 id="riassumendo">Riassumendo</h3>
<p>I modelli <strong>N-gram</strong> approssimano la probabilità di sequenze di parole utilizzando contesti limitati di $N-1$ parole precedenti.  Se consideriamo una sequenza di parole $w_{1}^n = w_1, w_2, ..., w_n$ con $n$ parole, abbiamo:<br />
- <strong>Regola della catena delle probabilità</strong>:<br />
  $$
  P(w_1^n) = \prod_{k=1}^n P(w_k \mid w_1^{k-1})
  $$<br />
  Calcola la probabilità di una frase scomponendola in probabilità condizionate di ogni parola dato l&rsquo;intero contesto precedente.  </p>
<ul>
<li><strong>Approssimazioni</strong>:  </li>
<li><strong>Bigramma</strong> ($N=2$): Considera solo la parola precedente:<br />
    $$
    P(w_1^n) = \prod_{k=1}^n P(w_k \mid w_{k-1})
    $$  </li>
<li><strong>N-gramma</strong> ($N$ generico): Utilizza le ultime $N-1$ parole:<br />
    $$
    P(w_1^n) = \prod_{k=1}^n P(w_k \mid w_{k-N+1}^{k-1})
    $$  </li>
</ul>
<h4 id="stima-delle-probabilita-con-frequenze-relative">Stima delle Probabilità con Frequenze Relative</h4>
<p>Le probabilità condizionate si stimano dai conteggi delle sequenze nel corpus:<br />
- <strong>Bigramma</strong>:<br />
  $$
  P(w_n \mid w_{n-1}) = \frac{C(w_{n-1}w_n)}{C(w_{n-1})}
  $$<br />
  Esempio: Se &ldquo;cane&rdquo; appare 100 volte e &ldquo;cane abbaia&rdquo; 30 volte, $P(\text{abbaia} \mid \text{cane}) = 0.3$.  </p>
<ul>
<li><strong>N-gramma</strong>:<br />
  $$
  P(w_n \mid w_{n-N+1}^{n-1}) = \frac{C(w_{n-N+1}^{n-1}w_n)}{C(w_{n-N+1}^{n-1})}
  $$<br />
  Esempio: Per un trigramma ($N=3$), $P(\text{mangia} \mid \text{il, cane}) = \frac{C(\text{il cane mangia})}{C(\text{il cane})}$.  </li>
</ul>
<p>Questo approccio si basa sulla <strong>frequenza relativa</strong> delle sequenze, rendendolo semplice ma sensibile alla sparsità dei dati per $N$ elevati. </p>
<p>This <span class="broken-link">The Berkeley Restourant Project (BERP) Corpus</span> is an exercise for you!</p>
<h3 id="legge-di-zipf">Legge di Zipf</h3>
<h4 id="introduzione">Introduzione</h4>
<p>La <strong>Legge di Zipf</strong> (dal linguista George Kingsley Zipf, 1902-1950) è un principio empirico che descrive la relazione tra la frequenza di un elemento e la sua posizione (&ldquo;rango&rdquo;) in una lista ordinata. Nella linguistica, stabilisce che:</p>
<blockquote>
<p>&ldquo;La frequenza di una parola è inversamente proporzionale al suo rango.&rdquo;</p>
</blockquote>
<p>Il <strong>rango</strong> ($r$) di una parola è la sua posizione in una lista ordinata per frequenza decrescente.</p>
<h4 id="formulazione-matematica">Formulazione Matematica</h4>
<p>Per un corpus testuale, la legge è espressa come:</p>
$$
f(r) = \frac{C}{r^s}
$$
<p>Dove:<br />
- $f(r)$: frequenza della parola di rango $r$<br />
- $C$: costante di normalizzazione<br />
- $s$: esponente caratteristico (≈1 per molte lingue naturali)</p>
<p>In termini semplificati:<br />
- La parola più frequente ($r=1$) occorrerà circa 2 volte più spesso della seconda ($r=2$), 3 volte più spesso della terza ($r=3$), ecc.</p>
<h4 id="esempi-pratici">Esempi Pratici</h4>
<table>
<thead>
<tr>
<th>Rango</th>
<th>Parola (Inglese)</th>
<th>Frequenza Relativa</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>the</td>
<td>7%</td>
</tr>
<tr>
<td>2</td>
<td>of</td>
<td>3.5%</td>
</tr>
<tr>
<td>3</td>
<td>and</td>
<td>2.3%</td>
</tr>
<tr>
<td>10</td>
<td>they</td>
<td>0.7%</td>
</tr>
</tbody>
</table>
<p><img src="/static/images/posts/Zipf's_law_on_War_and_Peace.png" alt="Zipf's law on War and Peace" width="80%" style="display: block; margin-left: auto; margin-right: auto; align: center"></p>
<p><em>Figura 1: Nelle lingue, in generale, si osserva la presenza di un piccolo numero di parole con frequenza elevata (rango piu basso) e un grande numero di parole con frequenza bassa (rango piu alto).</em></p>
<h4 id="applicazioni">Applicazioni</h4>
<p>La legge si osserva in:<br />
1. <strong>Linguistica</strong>: distribuzione parole nei testi<br />
2. <strong>Demografia</strong>: dimensione delle città<br />
3. <strong>Informatica</strong>: frequenza accessi a pagine web<br />
4. <strong>Economia</strong>: distribuzione del reddito</p>
<h4 id="limiti">Limiti</h4>
<ul>
<li>Funziona meglio su grandi dataset</li>
<li>L&rsquo;esponente $s$ può variare tra 0.8-1.2</li>
<li>Non spiega il &ldquo;perché&rdquo; del fenomeno</li>
</ul>
$$
\begin{aligned}
\text{Per } s=1: \quad &f(r) \propto \frac{1}{r} \\
& \sum_{r=1}^{\infty} \frac{1}{r} \to \infty \quad (\text{Serie armonica divergente})
\end{aligned}
$$
<h4 id="curiosita">Curiosità</h4>
<p>Lo stesso Zipf paragonò il fenomeno al &ldquo;principio del minimo sforzo&rdquo; in natura. Studi recenti lo collegano a:<br />
- Dinamiche di ottimizzazione<br />
- Processi stocastici<br />
- Auto-organizzazione critica</p>
<h2 id="limiti-e-problematiche">Limiti e Problematiche</h2>
<p>I modelli linguistici basati su n-grammi presentano diverse limitazioni intrinseche:</p>
<h3 id="1-sparse-data-e-zero-probability">1. Sparse Data e Zero Probability</h3>
<ul>
<li><strong>N-grammi non osservati</strong>:<br />
  Sequenze plausibili ma assenti nel training set ricevono probabilità zero:<br />
  $$P(w_n | w_{n-N+1}, ..., w_{n-1}) = 0 \quad \text{se } C(w_{n-N+1}, ..., w_n) = 0$$<br />
  → <strong>Impatto</strong>:  </li>
<li>Frasi valide nel test set ottengono perplexity infinita.  </li>
<li>Impossibilità di generalizzare a combinazioni non viste (es. <em>&ldquo;cane mangia kiwi&rdquo;</em>).  <blockquote>
<p><em>Soluzione</em>: Tecniche di smoothing (approfondite in dettaglio <span class="broken-link">qui</span>).</p>
</blockquote>
</li>
</ul>
<h3 id="2-finestra-contestuale-limitata">2. Finestra Contestuale Limitata</h3>
<ul>
<li><strong>Dipendenza da N fissato</strong>:  </li>
<li>Con N=3 (trigrammi), il modello ignora parole oltre le ultime 2:<br />
<em>&ldquo;Ieri ho visitato il museo egizio che ___&rdquo;</em> → Il contesto rilevante (&ldquo;museo&rdquo;) potrebbe essere troppo lontano.  </li>
<li><strong>Esempio</strong>: In <em>&ldquo;La ragazza con gli occhiali da sole che ___&rdquo;</em>, la scelta di &ldquo;indossava&rdquo; vs &ldquo;rompe&rdquo; dipende da &ldquo;occhiali&rdquo;, non dalle ultime 2 parole (&ldquo;che&rdquo; e &ldquo;sole&rdquo;).</li>
</ul>
<h3 id="3-incapacita-di-modellare-strutture-complesse">3. Incapacità di Modellare Strutture Complesse</h3>
<ul>
<li><strong>Dipendenza dall&rsquo;ordine locale</strong>:<br />
  Non catturano fenomeni linguistici che richiedono memoria a lungo termine:  </li>
<li>Accordi verbali: <em>&ldquo;Le donne che hanno ___&rdquo;</em> (richiede accordo plurale)  </li>
<li>
<p>Riferimenti anaforici: <em>&ldquo;Marco disse a Luca di comprare il pane. Poi ___ uscì&rdquo;</em> (chi uscì?)</p>
</li>
<li>
<p><strong>Ambiguità lessicale</strong>:<br />
  Non distinguono significati multipli in base al contesto globale:<br />
  $$P(\text{bank} | \text{river}) ≈ P(\text{bank} | \text{money})$$<br />
  (manca comprensione semantica di &ldquo;bank&rdquo; come &ldquo;sponda&rdquo; vs &ldquo;banca&rdquo;).</p>
</li>
</ul>
<h3 id="4-overhead-computazionale">4. Overhead Computazionale</h3>
<ul>
<li><strong>Crescita esponenziale dello spazio</strong>:<br />
  Per un vocabolario di 50k parole:  </li>
<li>Bigrammi: $50k^2 = 2.5$ miliardi di parametri  </li>
<li>
<p>Trigrammi: $50k^3 = 125$ trilioni di parametri<br />
  → <strong>Problema</strong>: Memorizzazione e query inefficienti anche per N moderati.</p>
<p>→ <strong>Soluzione</strong>: Utilizzare tecniche di compressione (es. Huffman coding) e pruning.</p>
</li>
</ul>
<h3 id="5-sensibilita-al-corpus-di-training">5. Sensibilità al Corpus di Training</h3>
<ul>
<li><strong>Bias statistici</strong>:<br />
  Riproducono stereotipi presenti nei dati:  </li>
<li><em>&ldquo;L&rsquo;infermiere ___&rdquo;</em> → Probabilità alta per &ldquo;lei&rdquo; (se il corpus ha prevalenza femminile nel ruolo)  </li>
<li>
<p><em>&ldquo;Il CEO di successo ___&rdquo;</em> → Associazioni di genere/culturali distorte  </p>
</li>
<li>
<p><strong>Out-Of-Vocabulary (OOV)</strong>:<br />
  Parole nuove (slang, nomi propri, errori) non presenti nel training set vengono gestite male:<br />
  $$P(\text{"Il nuovo NFT ___"}) = 0 \quad \text{se "NFT" non è nel vocabolario}$$</p>
</li>
</ul>
<h3 id="6-apprendimento-superficiale">6. Apprendimento Superficiale</h3>
<ul>
<li><strong>Modellano correlazioni, non causalità</strong>:<br />
  Apprendono pattern statistici senza comprensione logica:  </li>
<li><em>&ldquo;Se piove, prendo l&rsquo;ombrello&rdquo;</em> → Alta probabilità  </li>
<li>
<p><em>&ldquo;Se prendo l&rsquo;ombrello, piove&rdquo;</em> → Probabilità simile (manca relazione causale)  </p>
</li>
<li>
<p><strong>Assenza di world knowledge</strong>:<br />
  Non integrano informazioni esterne:<br />
  $$P(\text{"Roma"} | \text{"capitale d'Italia è"}) = P(\text{"Roma"} | \text{"capitale d'Italia è"})$$<br />
  Anche se &ldquo;Roma&rdquo; è l&rsquo;unica risposta corretta, il modello assegna probabilità basate solo sui bigrammi/trigrammi osservati.</p>
</li>
</ul>
<h2 id="argomrnti-collegati">Argomrnti Collegati</h2>
<ul>
<li><a href="/post/Algoritmi/Intelligenza Artificiale/Natural Language Processing/Valutazione dei Modelli di Linguaggio" class="simple-link">Valutazione dei Modelli di Linguaggio</a></li>
</ul>
<h2 id="conclusione">Conclusione</h2>
        </article>

        <a href="/" class="back-link text-lg">
            ← Torna alla home
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="/static/js/post.js"></script>
</body>
</html>