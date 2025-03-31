<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Discesa del Gradiente</title>
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
            <h1 class="text-4xl font-bold mb-4 text-gray-800">Discesa del Gradiente</h1>
        </header>

        <article class="prose max-w-none">
            <p>La discesa del gradiente (<em>Gradient Descent</em>, GD) è un algoritmo iterativo di minimizzazione del primo ordine. Viene definito <strong>iterativo</strong> poiché esegue una sequenza di aggiornamenti successivi per determinare un minimo locale della funzione obiettivo, a partire da una condizione iniziale.</p>
<p>Un aspetto cruciale della discesa del gradiente è che, nel caso di funzioni <strong>non convesse</strong>, non possiamo garantire che l&rsquo;algoritmo trovi il minimo globale. Infatti, tali funzioni possono presentare <strong>molteplici minimi locali</strong>, e il punto di convergenza dipenderà dalle condizioni iniziali del modello.</p>
<p>L&rsquo;intuizione alla base della discesa del gradiente è piuttosto semplice:<br />
1. Si parte da un punto iniziale nello spazio dei parametri.<br />
2. Si calcola il gradiente della funzione obiettivo in quel punto, il quale indica la direzione di massima crescita.<br />
3. Per minimizzare la funzione, ci si sposta nella direzione opposta a quella del gradiente, effettuando un &ldquo;passo&rdquo; in quella direzione.<br />
4. Questo processo viene ripetuto fino al raggiungimento di un criterio di arresto (convergenza).</p>
<p><img src="/static/images/posts/gradient-descent.jpg" alt="Gradient Descent"></p>
<p><em>Figura 1.0: Discesa del Gradiente su una funzione loss non convessa</em></p>
<p>Formalmente, il processo di aggiornamento iterativo può essere espresso come:</p>
$$
\Theta^{(t+1)} \leftarrow \Theta^{(t)} - \alpha \nabla \ell(\Theta^{(t)})
$$
<p>dove:<br />
- $\Theta^{(t)}$ rappresenta i parametri del modello all&rsquo;iterazione $t$,<br />
- $\alpha$ è il <strong>tasso di apprendimento</strong> (<em>learning rate</em>), un iperparametro che determina l&rsquo;ampiezza del passo nella direzione del gradiente,<br />
- $\nabla \ell(\Theta^{(t)})$ è il gradiente della funzione di perdita $\ell$ rispetto ai parametri $\Theta$.</p>
<p>Il criterio di arresto più comune è la verifica della norma del gradiente:</p>
$$
\|\nabla \ell(\Theta^{(t)})\| \leq \epsilon
$$
<p>dove $\epsilon$ è una soglia positiva molto piccola che determina il livello di precisione desiderato.</p>
<h2 id="interpretazione-geometrica">Interpretazione Geometrica</h2>
<p>Dal punto di vista geometrico, la discesa del gradiente segue una traiettoria nello spazio dei parametri, cercando il punto in cui la funzione di perdita assume un valore minimo. Se la funzione è convessa, l&rsquo;algoritmo convergerà al minimo globale; altrimenti, si fermerà in un minimo locale. </p>
<p>È importante notare che, a causa della precisione finita delle macchine, difficilmente si raggiungerà un punto esattamente stazionario, ma ci si fermerà quando la variazione della funzione di perdita diventa trascurabile.</p>
<h2 id="proprieta-del-gradiente">Proprietà del Gradiente</h2>
<h3 id="ortogonalita-e-massima-crescita">Ortogonalità e Massima Crescita</h3>
<p>Non abbiamo ancora fornito una giustificazione formale dell&rsquo;affermazione secondo cui il gradiente di una funzione in un dato punto rappresenta la direzione di massima crescita della funzione stessa.</p>
<p>Per comprendere meglio questo concetto, introduciamo la <strong>derivata direzionale</strong>, una generalizzazione della derivata tradizionale nel dominio unidimensionale $\mathbb{R}$. Mentre nella retta reale esiste un&rsquo;unica direzione lungo cui calcolare la derivata, in $\mathbb{R}^n$ (per $n \geq 2$) non esiste una direzione privilegiata per valutare la variazione di una funzione.</p>
<p>La derivata direzionale di una funzione differenziabile $f: \mathbb{R}^n \to \mathbb{R}$ lungo una direzione unitaria $\mathbf{v}$ è definita come:</p>
$$
D_{\mathbf{v}} f(\mathbf{x}) = \lim_{h \to 0} \frac{f(\mathbf{x} + h \mathbf{v}) - f(\mathbf{x})}{h}.
$$
<p>Questa definizione generalizza la derivata parziale $\frac{\partial f}{\partial x}$, che assume che la direzione considerata sia allineata con uno degli assi canonici (ovvero, solo una variabile cambia alla volta mentre le altre restano fisse). Al contrario, la derivata direzionale consente una variazione simultanea di tutte le variabili lungo una direzione arbitraria $\mathbf{v}$.</p>
<h3 id="relazione-tra-curve-di-livello-derivata-direzionale-e-gradiente">Relazione tra Curve di Livello, Derivata Direzionale e Gradiente</h3>
<p>Le <strong>curve di livello</strong> di una funzione sono le curve (o ipersuperfici) lungo le quali la funzione assume lo stesso valore. Ciò implica che la derivata direzionale della funzione in un punto appartenente alla curva, lungo una direzione tangente alla curva stessa, sia nulla, poiché la funzione non varia localmente in quella direzione.</p>
<p>Formalmente, se $\mathbf{v}$ è un vettore tangente alla curva di livello di $f$, allora</p>
$$
\langle \nabla f, \mathbf{v} \rangle = 0.
$$
<p>Questo risultato implica che il <strong>gradiente è ortogonale alla curva di livello</strong> e punta nella direzione di massima crescita della funzione. Inoltre, si può dimostrare che esso è orientato verso curve di livello con valori maggiori della funzione (ovvero, verso l&rsquo;incremento della funzione stessa).</p>
<p>Questo concetto è riassunto nella seguente rappresentazione grafica:</p>
<ul>
<li>Le curve di livello rappresentano i punti di uguale valore della funzione.</li>
<li>Il gradiente è sempre perpendicolare a tali curve.</li>
<li>La discesa del gradiente segue la direzione opposta al gradiente stesso per minimizzare la funzione.</li>
</ul>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necessario per i plot 3D

# Definizione della funzione f(x, y)
def f(x, y):
    &quot;&quot;&quot;
    Esempio di funzione con più minimi locali.
    Puoi modificarla come preferisci.
    &quot;&quot;&quot;
    return 0.2 * (x**2 + y**2) + 2.0 * np.sin(x) * np.sin(y)

# Definizione del gradiente di f(x, y)
def grad_f(x, y):
    &quot;&quot;&quot;
    Calcola il gradiente di f(x, y): restituisce (df/dx, df/dy).
    &quot;&quot;&quot;
    dfdx = 0.4 * x + 2.0 * np.cos(x) * np.sin(y)
    dfdy = 0.4 * y + 2.0 * np.sin(x) * np.cos(y)
    return dfdx, dfdy

# Creazione della griglia di punti per i plot
N = 200  # Numero di punti per dimensione
x_vals = np.linspace(-3, 3, N)
y_vals = np.linspace(-3, 3, N)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)

# Calcolo del gradiente su una griglia più rada per la visualizzazione del campo vettoriale
step = 15  # Passo per la selezione dei punti per il campo vettoriale
x_quiver = X[::step, ::step]
y_quiver = Y[::step, ::step]
dfdx, dfdy = grad_f(x_quiver, y_quiver)

# Creazione della figura con 2 righe e 2 colonne, usando width_ratios per modificare le dimensioni dei subplot in alto
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(2, 2, width_ratios=[3, 2])

# -------------------------------------------------------------------------
# Pannello 1 (in alto a sinistra): Plot 3D della superficie (più grande)
# -------------------------------------------------------------------------
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
ax1.set_title('Superficie 3D')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# -------------------------------------------------------------------------
# Pannello 2 (in alto a destra): Mappa di colore e curve di livello (più quadrato)
# -------------------------------------------------------------------------
ax2 = fig.add_subplot(gs[0, 1])
cont = ax2.contourf(X, Y, Z, levels=30, cmap='viridis')
ax2.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5)
ax2.set_title('Mappa di colore e curve di livello')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_aspect('equal', adjustable='box')  # Forza un aspetto quadrato
cbar = plt.colorbar(cont, ax=ax2)
cbar.set_label('Valore di f(x, y)')

# -------------------------------------------------------------------------
# Pannello 3 (in basso a sinistra): Campo vettoriale del gradiente positivo
# -------------------------------------------------------------------------
ax3 = fig.add_subplot(gs[1, 0])
ax3.contourf(X, Y, Z, levels=30, cmap='viridis', alpha=0.7)
ax3.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5, alpha=0.5)
Q = ax3.quiver(x_quiver, y_quiver, dfdx, dfdy, color='red', scale=50)
ax3.set_title('Campo vettoriale del gradiente')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_aspect('equal')

# -------------------------------------------------------------------------
# Pannello 4 (in basso a destra): Campo vettoriale del gradiente negativo
# -------------------------------------------------------------------------
ax4 = fig.add_subplot(gs[1, 1])
ax4.contourf(X, Y, Z, levels=30, cmap='viridis', alpha=0.7)
ax4.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5, alpha=0.5)
Q2 = ax4.quiver(x_quiver, y_quiver, -dfdx, -dfdy, color='red', scale=50)
ax4.set_title('Campo vettoriale del gradiente negativo')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_aspect('equal')

plt.tight_layout()
plt.savefig('./images/gradient.jpg', 
           dpi=300, 
           bbox_inches='tight',
           pad_inches=0.05,  # Aggiungere questo parametro
           #facecolor=fig.get_facecolor(),  # Mantenere il colore di sfondo
           transparent=False)  # Disabilitare la trasparenza
plt.show()
</code></pre>
<p><img src="/static/images/posts/gradient.jpg" alt="Gradient Descent"></p>
<p><em>Figura 1.1: Visualizzazione della funzione $f(x,y)$ con la sua superficie 3D, mappa di livello e campi vettoriali del gradiente positivo e negativo, evidenziando le direzioni di massima variazione.</em></p>
<p>Questa proprietà è fondamentale nelle tecniche di ottimizzazione basate sul gradiente, in quanto garantisce che muovendosi nella direzione opposta al gradiente si riduce il valore della funzione obiettivo.</p>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione e del suo gradiente
def f(x, y):
    return 0.5 * x**2 + y**2

def grad_f(x, y):
    return x, 2 * y

# Creazione della griglia di punti
N = 200
x_vals = np.linspace(-2, 2, N)
y_vals = np.linspace(-2, 2, N)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)

# Punto di interesse P0
P0 = (1, 1)
gx, gy = grad_f(P0[0], P0[1])  # gradiente in P0

# Calcolo della direzione tangente (v) a partire dalla condizione: &lt;grad, v&gt; = 0
# Scegliamo v = (2, -1) che è ortogonale a (1,2) (poichè 1*2 + 2*(-1) = 0)
v = np.array([2, -1], dtype=float)
v = v / np.linalg.norm(v)  # normalizzo

# Calcolo del vettore -gradiente in P0 (direzione di discesa)
neg_grad = -np.array([gx, gy])
if np.linalg.norm(neg_grad) &gt; 1e-10:
    neg_grad_unit = neg_grad / np.linalg.norm(neg_grad)
else:
    neg_grad_unit = neg_grad

# Lunghezze per le frecce
arrow_len = 0.5

# Creazione della figura con 3 pannelli affiancati
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# ---------------------------
# Pannello 1: Curva di livello + vettore tangente (df/dv = 0)
# ---------------------------
ax1 = axes[0]
cont1 = ax1.contour(X, Y, Z, levels=15, cmap='viridis')
ax1.plot(P0[0], P0[1], 'ko', label=r'$P_0$')
# Calcolo del punto finale per la freccia tangente
P1 = (P0[0] + arrow_len * v[0], P0[1] + arrow_len * v[1])
ax1.annotate('', xy=P1, xytext=P0, 
             arrowprops=dict(arrowstyle='-&gt;', color='blue', lw=2))
ax1.set_title(r'Vettore tangente: $\frac{df}{dv}(P_0)=0$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_aspect('equal')

# ---------------------------
# Pannello 2: Curva di livello + vettore -gradiente
# ---------------------------
ax2 = axes[1]
cont2 = ax2.contour(X, Y, Z, levels=15, cmap='viridis')
ax2.plot(P0[0], P0[1], 'ko', label=r'$P_0$')
# Punto finale per la freccia -gradiente
P2 = (P0[0] + arrow_len * neg_grad_unit[0], P0[1] + arrow_len * neg_grad_unit[1])
ax2.annotate('', xy=P2, xytext=P0,
             arrowprops=dict(arrowstyle='-&gt;', color='red', lw=2))
ax2.set_title(r'Vettore -$\nabla f$ in $P_0$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_aspect('equal')

# ---------------------------
# Pannello 3: Campo vettoriale dell'intero gradiente
# ---------------------------
ax3 = axes[2]
cont3 = ax3.contourf(X, Y, Z, levels=15, cmap='viridis', alpha=0.7)
ax3.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5, alpha=0.5)
# Campo vettoriale (quiver) per il gradiente
step = 10
xq = X[::step, ::step]
yq = Y[::step, ::step]
gxq, gyq = grad_f(xq, yq)
ax3.quiver(xq, yq, gxq, gyq, color='red', scale=30)
ax3.set_title(r'Campo vettoriale: $\nabla f$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_aspect('equal')

plt.tight_layout()
plt.savefig('./images/gradient.jpg', 
           dpi=300, 
           bbox_inches='tight',
           pad_inches=0.05,  # Aggiungere questo parametro
           #facecolor=fig.get_facecolor(),  # Mantenere il colore di sfondo
           transparent=False)  # Disabilitare la trasparenza
plt.show()
</code></pre>
<p><img src="/static/images/posts/gradient-orthogonal.jpg" alt="Gradient Descent 2"></p>
<p><em>Figura 1.2: Ortogonalità tra il vettore tangente alla curva di livello e il vettore -gradiente</em></p>
        </article>

        <a href="/" class="back-link text-lg">
            ← Torna alla home
        </a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script src="/static/js/post.js"></script>
</body>
</html>