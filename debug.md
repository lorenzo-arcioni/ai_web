<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Problema della Classificazione Binaria: Interpretazione Probabilistica</title>
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
            <h1 class="text-4xl font-bold mb-4 text-gray-800">Problema della Classificazione Binaria: Interpretazione Probabilistica</h1>
        </header>

        <article class="prose max-w-none">
            <p>La <strong>classificazione binaria</strong> è un problema in cui un&rsquo;istanza $\mathbf{x} \in \mathbb{R}^d$ deve essere assegnata a una delle due classi possibili, generalmente denotate come $y \in \{0,1\}$.</p>
<p>Un approccio comune è utilizzare un <strong>modello probabilistico</strong> che stima la probabilità condizionale di una classe dato un vettore di caratteristiche $\mathbf{x}$:<br />
$$
p(y=1 \mid \mathbf{x}) = f(\mathbf{x})
$$<br />
Dove $f(\mathbf{x})$ è una funzione che restituisce una probabilità tra 0 e 1.</p>
<hr />
<h2 id="likelihood-e-posteriori"><strong>Likelihood e Posteriori</strong></h2>
<p>Per stimare la probabilità della classe, possiamo applicare il <strong>Teorema di Bayes</strong>:<br />
$$
p(y \mid \mathbf{x}) = \frac{p(\mathbf{x} \mid y) p(y)}{p(\mathbf{x})}
$$</p>
<ul>
<li>$p(y)$ è la probabilità a priori della classe $y$.</li>
<li>$p(\mathbf{x} \mid y)$ è la <strong>verosimiglianza</strong> (<em>likelihood</em>), che modella come le caratteristiche $\mathbf{x}$ sono distribuite all&rsquo;interno di ciascuna classe.</li>
<li>$p(\mathbf{x}) = \sum_{y \in \{0,1\}} p(\mathbf{x} \mid y) p(y)$ è la probabilità marginale dei dati.</li>
</ul>
<p>In pratica, possiamo stimare $p(y \mid \mathbf{x})$ attraverso un modello parametrico che approssima la distribuzione dei dati.</p>
<hr />
<h2 id="il-concetto-di-logit-e-la-funzione-sigmoide"><strong>Il Concetto di Logit e la Funzione Sigmoide</strong></h2>
<p>Come abbiamo visto, nella classificazione binaria, possiamo esprimere la probabilità che un&rsquo;osservazione $\mathbf x \in \mathbb R^d$ appartenga alla classe 1 come: $p(y = 1 \mid \mathbf{x}) = \frac{p(\mathbf{x} \mid y) p(y)}{p(\mathbf{x})}$. Introduciamo ora il concetto di logit: una misura logaritmica di quanto verosimile sia la classe 1 rispetto alla classe 0 (logaritmicamente):</p>
$$\begin{align*}
logit(p(y = 1 \mid \mathbf{x})) = a &= \log \frac{p(y = 1 \mid \mathbf{x})}{\underbrace{p(y = 0 \mid \mathbf{x})}_{= 1 - p(y = 1 \mid \mathbf{x})}}\\
e^a &= \frac{p(y = 1 \mid \mathbf{x})}{p(y = 0 \mid \mathbf{x})}\\
p(y = 1 \mid \mathbf{x}) &= e^a p(y = 0 \mid \mathbf{x})\\
\end{align*}
$$
<p>E dato che $p(y = 0 \mid \mathbf{x}) + p(y = 1 \mid \mathbf{x}) = 1$,</p>
$$\begin{align*}
e^a p(y = 0 \mid \mathbf{x}) + p(y = 0 \mid \mathbf{x}) &= 1\\
p(y = 0 \mid \mathbf{x}) (e^a + 1) &= 1\\
p(y = 0 \mid \mathbf{x}) &= \frac{1}{e^a + 1}\\
\end{align*}
$$
<p>E ora, usando il fatto che $p(y=1 \mid \mathbf x) = e^a \cdot p(y=0\mid\mathbf x)$, otteniamo:</p>
$$\begin{align*}
    p(y=1 \mid\mathbf x) &= e^a \cdot \frac{1}{1 + e^a}\\
    p(y=1 \mid\mathbf x) &= \frac{e^a}{1 + e^a}\\
    p(y=1 \mid\mathbf x) &= \frac{\frac{e^a}{e^a}}{\frac{1}{e^a} + \frac{e^a}{e^a}}\\
    p(y=1 \mid\mathbf x) &= \frac{1}{1 + e^{-a}} = \sigma(a) \ \text{La funzione sigmoide.}\\
\end{align*}
$$
<p>Questa funzione si chiama <strong>funzione sigmoide</strong> e viene utilizzata per ottenere la probabilità di una classe dato un vettore di caratteristiche. Sarebbe quindi l&rsquo;inverso della funzione logit, in quanto abbiamo ricavato la $x$ (che nel nostro caso era $p(y = 1 \mid \mathbf{x})$) dalla funzione $logit(x)$. Infatti,</p>
$$
\begin{align*}
\text{Partendo da } p &= \sigma(x) = \frac{1}{1 + e^{-x}} \\
\frac{1}{p} &= 1 + e^{-x} \quad \text{(Reciproco di entrambi i lati)} \\
\frac{1}{p} - 1 &= e^{-x} \quad \text{(Isolare } e^{-x}) \\
\frac{1 - p}{p} &= e^{-x} \quad \text{(Semplificare)} \\
\ln\left(\frac{1 - p}{p}\right) &= -x \quad \text{(Applicare il logaritmo naturale)} \\
x &= -\ln\left(\frac{1 - p}{p}\right) = \ln\left(\frac{p}{1 - p}\right) \quad \text{(Risolvere per } x) \\
\text{Quindi otteniamo alla fine: }\\
\sigma^{-1}(p) &= \ln\left(\frac{p}{1 - p}\right).
\end{align*}
$$
<p>Questo perché il logit trasforma un rapporto di probabilità $\in [0, 1]$ in un valore $\in (-\infty, +\infty)$. Mentre la funzione sigmoide trasforma un valore $\in (-\infty, +\infty)$ in un rapporto di probabilità $\in [0, 1]$. In altre parole, il logit controlla quanto le features in input influenzano la probabilità di appartenenza alla classe 1 rispetto alla classe 0.</p>
<h2 id="collegamento-con-la-regressione-logistica"><strong>Collegamento con la Regressione Logistica</strong></h2>
<p>La regressione logistica è un modello <strong>discriminativo</strong>, che apprende direttamente $p(y \mid \mathbf{x})$ senza modellare $p(\mathbf{x} \mid y)$. Può essere vista come un caso particolare dell&rsquo;<strong>Analisi Discriminante Lineare (LDA)</strong> sotto certe assunzioni sulle distribuzioni dei dati.</p>
        </article>

        <a href="/" class="back-link text-lg">
            ← Torna alla home
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="/static/js/post.js"></script>
</body>
</html>