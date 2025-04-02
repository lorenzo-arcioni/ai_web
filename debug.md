<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Convessità</title>
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
            <h1 class="text-4xl font-bold mb-4 text-gray-800">Convessità</h1>
        </header>

        <article class="prose max-w-none">
            <h2 id="introduzione">Introduzione</h2>
<p>Nel contesto dell&rsquo;ottimizzazione, il problema generale che vogliamo risolvere è:</p>
$$
\min_{\Theta} \ell(\Theta)
$$
<p>dove $\Theta$ rappresenta i parametri del modello e $\ell(\Theta)$ è la funzione di perdita. Trovare i minimizzatori per una funzione di perdita generale è un problema aperto nel campo dell&rsquo;ottimizzazione. Il metodo di ottimizzazione dipende dalle proprietà specifiche della funzione di perdita e, in alcuni casi, potrebbero esserci vincoli sui parametri. Tuttavia, tratteremo principalmente problemi non vincolati.</p>
<h2 id="funzioni-convesse">Funzioni Convesse</h2>
<p>Una classe di funzioni particolarmente facile da minimizzare (o massimizzare) è quella delle <strong>funzioni convesse</strong>, definite dalla <strong>disuguaglianza di Jensen</strong>:</p>
$$
f(\alpha x + (1 - \alpha)y) \leq \alpha f(x) + (1 - \alpha)f(y), \quad \forall x, y \text{ e } \alpha \in [0, 1]
$$
<p>Questa disuguaglianza afferma che la trasformazione convessa di una media è minore o uguale alla media applicata dopo la trasformazione convessa. Per due punti, significa che la linea secante di una funzione convessa giace sopra il grafico della funzione.</p>
<p><img alt="Jensen's Inequality" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ConvexFunction.svg/1200px-ConvexFunction.svg.png" /></p>
<p><em>Figura 2.4: La disuguaglianza di Jensen generalizza l&rsquo;affermazione che la linea secante di una funzione convessa giace sopra il grafico.</em></p>
<h2 id="perche-le-funzioni-convesse-sono-facili-da-minimizzare">Perché le funzioni convesse sono facili da minimizzare?</h2>
<p>Guardando il grafico sopra, possiamo intuire che esiste sempre un <strong>minimo unico</strong>. Se ricordiamo un po&rsquo; di calcolo delle scuole superiori, sappiamo anche che il punto in cui tale minimo è raggiunto è il punto (ancora unico) in cui la derivata della funzione è zero.</p>
<p>Un&rsquo;importante assunzione che spesso facciamo è che la funzione di perdita $\ell$ sia <strong>differenziabile</strong>, in modo da poter calcolare la sua derivata $\frac{d\ell}{dx}$ in tutti i punti $x$.</p>
<h2 id="formalizzazione-della-convessita">Formalizzazione della Convessità</h2>
<p>Per spiegare formalmente, riscriviamo la disuguaglianza di Jensen in una forma diversa:</p>
$$
f(x + \alpha(y - x)) \leq (1 - \alpha)f(x) + \alpha f(y), \quad \forall x, y \text{ e } \alpha \in (0, 1)
$$
<p>Effettuando alcune manipolazioni algebriche, otteniamo:</p>
$$
\frac{f(x + \alpha(y - x))}{\alpha} \leq \frac{(1 - \alpha)f(x) + \alpha f(y)}{\alpha}
$$
$$
\frac{f(x + \alpha(y - x))}{\alpha} \leq \frac{f(x)}{\alpha} - f(x) + f(y) \quad (\text{espandendo il prodotto } (1 - \alpha)f(x))
$$
$$
\frac{f(x + \alpha(y - x)) - f(x)}{\alpha} + f(x) \leq f(y)
$$
<p>Prendendo il limite per $\alpha \to 0$, notiamo che l&rsquo;espressione assomiglia alla definizione di derivata di una funzione, ovvero il limite del rapporto incrementale:</p>
$$
\frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$
<p>Per completare l&rsquo;espressione, abbiamo bisogno di un fattore $(y - x)$:</p>
$$
\lim_{\alpha \to 0} \frac{f(x + \alpha(y - x)) - f(x)}{\alpha(y - x)} (y - x) + f(x) \leq f(y), \quad \forall x, y
$$
<p>Poiché $(y - x)$ è uno scalare, possiamo estrarlo dal limite, e l&rsquo;intero limite rappresenta la derivata di $f$:</p>
$$
\frac{df(x)}{dx} (y - x) + f(x) \leq f(y), \quad \forall x, y
$$
<p>Notiamo che il lato sinistro della disuguaglianza è l&rsquo;approssimazione di Taylor del primo ordine di $f$ nel punto $x$, ovvero la migliore approssimazione lineare di $f$ in quel punto.</p>
<p><img alt="Taylor Approximation" src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Taylor_Approximation_of_sin%28x%29.jpeg" /></p>
<p><em>Figura 2.5: Approssimazione di Taylor.</em></p>
<h2 id="minimizzazione-di-funzioni-convesse">Minimizzazione di Funzioni Convesse</h2>
<p>Se vogliamo trovare un minimizzatore per una funzione convessa $f$, basta calcolare la sua derivata $\frac{df}{dx}$, imporla $= 0$ e risolvere per $x$. Come abbiamo mostrato, il punto $x$ soddisfa la disuguaglianza:</p>
$$
\underbrace{\frac{df(x)}{dx} (y - x)}_{=0} + f(x) \leq f(y), \quad \forall y
$$
<p>quindi</p>
$$
f(x) \leq f(y), \quad \forall y
$$
<p>e dunque $x$ è il <strong>minimizzatore globale</strong> della funzione.</p>
<p>In generale, per trovare un minimizzatore per una funzione convessa $f$, è sufficiente calcolare la sua derivata $\frac{df}{dx}$, impostarla a zero e risolvere per $x$. Il punto $x$ sarà quindi il minimizzatore globale della funzione.</p>
<h2 id="convessita-e-la-seconda-derivata">Convessità e la Seconda Derivata</h2>
<h3 id="nel-caso-univariato">Nel Caso Univariato</h3>
<p>Se $f(x)$ è due volte differenziabile, il <strong>test della seconda derivata</strong> stabilisce che:</p>
<ul>
<li>Se $f''(x) \geq 0$ per ogni $x$, la funzione è convessa.</li>
<li>Se $f''(x) > 0$ per ogni $x$, la funzione è strettamente convessa.</li>
</ul>
<p><strong>Spiegazione Dettagliata e Motivazione Matematica</strong></p>
<p>In questa sezione approfondiremo, dal punto di vista matematico, perché le proprietà relative alla curvatura, alla tangente e alla monotonia del gradiente garantiscono la convessità di una funzione $f(x)$.</p>
<h4 id="1-curvatura-e-seconda-derivata">1. Curvatura e Seconda Derivata</h4>
<p><strong>Concetto:</strong><br />
La seconda derivata $f''(x)$ misura la curvatura della funzione. Se $f''(x) \geq 0$ in ogni punto, la funzione &ldquo;si piega verso l&rsquo;alto&rdquo; ovunque.</p>
<p><strong>Motivazione Matematica:</strong></p>
<p>Consideriamo la definizione di derivata seconda:<br />
$$
f''(x) = \lim_{h \to 0} \frac{f'(x+h) - f'(x)}{h}.
$$<br />
Se $f''(x) \geq 0$ per ogni $x$, significa che per ogni incremento $h > 0$ (piccolo), il valore $f'(x+h)$ è almeno pari a $f'(x)$. Quindi il gradiente non diminuisce mai: $f'(x)$ è <strong>monotono non decrescente</strong>.</p>
<p><strong>Interpretazione:</strong><br />
- Quando la funzione è &ldquo;piegata verso l&rsquo;alto&rdquo;, la variazione del suo tasso di crescita è tale da non permettere inversioni di curvatura che potrebbero generare minimi o massimi locali multipli.<br />
- In termini geometrici, il grafico di $f(x)$ non può avere &ldquo;fianchi discendenti&rdquo; improvvisi che si ripiegano verso il basso, garantendo l&rsquo;unicità del minimo (se esiste).</p>
<h4 id="2-tangente-e-approssimazione-lineare">2. Tangente e Approssimazione Lineare</h4>
<p><strong>Concetto:</strong><br />
La retta tangente a $f(x)$ in un punto $x_0$ è data da:<br />
$$
L(x) = f(x_0) + f'(x_0)(x - x_0).
$$<br />
Se $f''(x) \geq 0$, il grafico di $f(x)$ si trova sempre al di sopra della retta tangente in $x_0$.</p>
<p><strong>Motivazione Matematica (Teorema di Taylor):</strong></p>
<p>Utilizziamo l&rsquo;espansione in serie di Taylor al primo ordine per $f(x)$ intorno a $x_0$. Per un $x$ arbitrario, esiste un punto $\xi$ compreso tra $x_0$ e $x$ tale che:<br />
$$
f(x) = \underbrace{f(x_0) + f'(x_0)(x - x_0)}_{L(x)} + \frac{1}{2} f''(\xi)(x - x_0)^2.
$$<br />
Se $f''(\xi) \geq 0$, allora<br />
$$
\frac{1}{2} f''(\xi)(x - x_0)^2 \geq 0.
$$<br />
Pertanto:<br />
$$
\underbrace{f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2} f''(\xi)(x - x_0)^2}_{f(x)} \geq f(x_0) + f'(x_0)(x - x_0) = L(x).
$$<br />
Questo mostra che la retta tangente $L(x)$ è un <strong>supporto</strong> per $f(x)$ – il grafico della funzione non scende mai al di sotto della sua tangente. Questa proprietà è essenziale per la convessità, perché implica che la funzione è sempre &ldquo;sopra&rdquo; ogni approssimazione lineare locale.</p>
<h4 id="3-monotonia-del-gradiente">3. Monotonia del Gradiente</h4>
<p><strong>Concetto:</strong><br />
La condizione $f''(x) \geq 0$ implica che il gradiente $f'(x)$ è monotono non decrescente.</p>
<p><strong>Motivazione Matematica (<a href="/post/Calcolo/Teorema di Lagrange" class="simple-link">Teorema di Lagrange</a> o del Valore Medio):</strong></p>
<p>Sia $x_1 < x_2$ e applichiamo il Teorema del Valore Medio a $f'(x)$ su $[x_1, x_2]$. Esiste un punto $\xi \in (x_1, x_2)$ tale che:<br />
$$
f'(x_2) - f'(x_1) = f''(\xi)(x_2 - x_1).
$$<br />
Poiché $x_2 - x_1 > 0$ e $f''(\xi) \geq 0$, ne consegue che:<br />
$$
f'(x_2) - f'(x_1) \geq 0 \quad \Rightarrow \quad f'(x_2) \geq f'(x_1).
$$<br />
Quindi, il gradiente non diminuisce mai al crescere di $x$. Questa monotonia del gradiente è fondamentale perché significa che, una volta che il gradiente raggiunge il valore zero, non può tornare a valori negativi che indicherebbero una nuova discesa. Così, se $f'(x_0) = 0$ per qualche $x_0$, $x_0$ è il <strong>minimo globale</strong>.</p>
<h4 id="sintesi-della-motivazione-matematica">Sintesi della Motivazione Matematica</h4>
<ul>
<li>
<p><strong>Curvatura:</strong><br />
  La condizione $f''(x) \geq 0$ assicura che la funzione non abbia inversioni di curvatura, mantenendo una forma &ldquo;aperta verso l&rsquo;alto&rdquo; e prevenendo l&rsquo;esistenza di multipli minimi locali.</p>
</li>
<li>
<p><strong>Tangente:</strong><br />
  L&rsquo;approssimazione lineare (tangente) fornisce un limite inferiore al grafico di $f(x)$ quando $f''(x) \geq 0$. Questo significa che il grafico di $f(x)$ è sempre al di sopra della sua tangente, caratteristica che semplifica l&rsquo;analisi della funzione e l&rsquo;identificazione del minimo globale.</p>
</li>
<li>
<p><strong>Monotonia del Gradiente:</strong><br />
  Con $f''(x) \geq 0$, il gradiente $f'(x)$ cresce o rimane costante. Questo impedisce oscillazioni che potrebbero generare più soluzioni stazionarie, garantendo così l&rsquo;unicità del punto in cui $f'(x) = 0$ e rendendo quel punto il minimo globale.</p>
</li>
</ul>
<p>Questi punti, insieme, formano la base teorica che spiega perché le funzioni con $f''(x) \geq 0$ sono convexi e perché questa condizione rende il problema di ottimizzazione (ovvero, trovare il minimo globale) molto più semplice da risolvere.</p>
<h3 id="estensione-al-caso-multivariato">Estensione al Caso Multivariato</h3>
<p>Per una funzione $f: \mathbb{R}^n \to \mathbb{R}$ due volte differenziabile, la condizione di convessità si generalizza attraverso la <strong>Hessiana</strong> $\nabla^2 f(\mathbf{x})$, la matrice delle derivate seconde. La funzione $f$ è convessa se e solo se, per ogni vettore $\mathbf{v} \in \mathbb{R}^n$:</p>
$$
\mathbf{v}^\top \nabla^2 f(\mathbf{x}) \, \mathbf{v} \geq 0, \quad \forall \mathbf{x}.
$$
<p>Questo significa che la Hessiana è <strong>positiva semidefinita</strong>. L&rsquo;interpretazione è la stessa: la funzione ha una curvatura non negativa in tutte le direzioni, estendendo il concetto della seconda derivata non negativa dal caso univariato.</p>
<h2 id="riassunto-intuitivo">Riassunto Intuitivo</h2>
<ul>
<li>
<p><strong>Funzioni a Una Variabile:</strong><br />
  Se $f''(x) \geq 0$ in ogni punto, la funzione è sempre &ldquo;inclinata verso l&rsquo;alto&rdquo;. La retta tangente in ogni punto funge da supporto, e la funzione non presenta inversioni di curvatura. Quindi, il punto in cui $f'(x) = 0$ è il minimo globale.</p>
</li>
<li>
<p><strong>Funzioni Multivariate:</strong><br />
  Se la Hessiana $\nabla^2 f(\mathbf{x})$ è positiva semidefinita, la funzione possiede una curvatura non negativa in ogni direzione. Questo garantisce l&rsquo;unicità del minimo locale (che è anche globale) e semplifica la risoluzione dei problemi di ottimizzazione.</p>
</li>
</ul>
<h2 id="conclusione">Conclusione</h2>
<p>La caratterizzazione della convessità mediante la disuguaglianza di Jensen e il test della seconda derivata (o della Hessiana nel caso multivariato) fornisce strumenti fondamentali per l&rsquo;analisi e la risoluzione di problemi di ottimizzazione. Le funzioni convesse, avendo un unico minimo globale, permettono l&rsquo;utilizzo di algoritmi efficienti e garantiscono che ogni minimo locale sia effettivamente globale, semplificando notevolmente il processo di minimizzazione.</p>
<p><em>Nota: Questa spiegazione si basa su concetti classici dell&rsquo;analisi matematica e dell&rsquo;ottimizzazione. Per ulteriori approfondimenti si consiglia lo studio di testi specifici di calcolo avanzato e teoria dell&rsquo;ottimizzazione.</em></p>
        </article>

        <a href="/" class="back-link text-lg">
            ← Torna alla home
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="/static/js/post.js"></script>
</body>
</html>
