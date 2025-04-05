# The Berkeley Restaurant Project (BERP) Corpus

## Descrizione Generale
Il **BERP** (Berkeley Restaurant Project) è un corpus utilizzato nell'ambito del **Natural Language Processing (NLP)**, in particolare per modellare e analizzare il linguaggio in contesti legati al cibo e alla ristorazione.  
Il corpus contiene query poste dagli utenti, per esempio:  
- *I’m looking for Cantonese food*  
- *I’d like to eat dinner someplace nearby*  
- *Tell me about Chez Panisse*  
- *I’m looking for a good place to eat breakfast*  

Questo dataset è impiegato per sviluppare modelli probabilistici del linguaggio, permettendo di stimare la probabilità di frasi, analizzare le frequenze delle parole (unigrammi) e le associazioni tra di esse (bigrammi).

## Modellazione Probabilistica con N-grammi

### Calcolo della Probabilità con il Modello Bigram
Assumendo l'indipendenza dei bigrammi e applicando la regola della catena, la probabilità di una frase viene approssimata moltiplicando le probabilità condizionali dei singoli bigrammi.  
Per esempio, per la frase modificata:
$$
P(\text{<s> I want Chinese food </s>}) \approx P(I|\text{<s>}) \cdot P(want|I) \cdot P(Chinese|want) \cdot P(food|Chinese) \cdot P(</s>|food)
$$

## Tabelle di Conteggio

### Conteggio degli Unigrammi

|        | $<s>$ | i    | want | to   | eat  | chinese | food | lunch | spend | $</s>$ |
|--------|-----|------|------|------|------|---------|------|-------|-------|------|
| Count  | $N$   | 2533 | 927  | 2417 | 746  | 158     | 1093 | 341   | 278   | $N$    |

Chiameremo questo vettore $\mathbf{u}$.

### Conteggio dei Bigrammi

In questa tabella includiamo `<s>` come riga iniziale e `</s>` come colonna finale. I conteggi per i bigrammi che coinvolgono `<s>` e `</s>` dipenderanno dal corpus, quindi li indicheremo genericamente con $B_{<s>, \cdot}$ e $B_{\cdot, </s>}$:

|            | $<s>$          | i   | want | to  | eat | chinese | food | lunch | spend | $</s>$         |
|------------|--------------|-----|------|-----|-----|---------|------|-------|-------|--------------|
| **$<s>$**      | –            | $a$  | $b$  | $c$  | $d$  | $e$     | $f$  | $g$   | $h$   | –            |
| **i**      | $i_{<s>}$  | 5   | 827  | 0   | 9   | 0       | 0    | 0     | 2     | $i_{</s>}$  |
| **want**   | $w_{<s>}$  | 2   | 0    | 608 | 1   | 6       | 6    | 5     | 1     | $w_{</s>}$  |
| **to**     | $t_{<s>}$  | 2   | 0    | 4   | 686 | 2       | 0    | 6     | 211   | $t_{</s>}$  |
| **eat**    | $e_{<s>}$  | 0   | 0    | 2   | 0   | 16      | 2    | 42    | 0     | $e_{</s>}$  |
| **chinese**| $c_{<s>}$  | 1   | 0    | 0   | 0   | 0       | 82   | 1     | 0     | $c_{</s>}$  |
| **food**   | $f_{<s>}$  | 15  | 0    | 15  | 0   | 1       | 4    | 0     | 0     | $f_{</s>}$  |
| **lunch**  | $l_{<s>}$  | 2   | 0    | 0   | 0   | 0       | 1    | 0     | 0     | $l_{</s>}$  |
| **spend**  | $s_{<s>}$  | 1   | 0    | 1   | 0   | 0       | 0    | 0     | 0     | $s_{</s>}$  |

Chiameremo questa matrice $\mathbf{B}$.

### Probabilità dei Bigrammi (conteggio normalizzato)

Per ottenere le probabilità dei bigrammi, si divide il conteggio del bigramma per il conteggio dell'unigramma del prefisso. Ad esempio, per il bigramma "i want" abbiamo:

$$
P(\text{want} \mid \text{i}) = \frac{827}{2533} \approx 0.33
$$

La matrice normalizzata $\mathbf{N}$ (contenente le probabilità) sarà strutturata in modo analogo, includendo le colonne e righe per `<s>` e `</s>`:

|            | <s>          | i     | want  | to    | eat   | chinese | food  | lunch | spend | </s>         |
|------------|--------------|-------|-------|-------|-------|---------|-------|-------|-------|--------------|
| **<s>**      | –            | $P(a)$ | $P(b)$ | $P(c)$ | $P(d)$ | $P(e)$   | $P(f)$ | $P(g)$ | $P(h)$ | –            |
| **i**      | $P(i_{<s>})$  | 0.002 | 0.33  | 0     | 0.0036 | 0       | 0     | 0     | 0.00079 | $P(i_{</s>})$  |
| **want**   | $P(w_{<s>})$  | 0.0022 | 0    | 0.66  | 0.0011 | 0.0065  | 0.0065 | 0.0054 | 0.0011 | $P(w_{</s>})$  |
| **to**     | $P(t_{<s>})$  | 0.00083| 0   | 0.0017| 0.28   | 0.00083 | 0     | 0.0025| 0.087  | $P(t_{</s>})$  |
| **eat**    | $P(e_{<s>})$  | 0     | 0    | 0.0027| 0      | 0.021  | 0.0027| 0.056 | 0     | $P(e_{</s>})$  |
| **chinese**| $P(c_{<s>})$  | 0.0063| 0   | 0     | 0      | 0      | 0.52  | 0.0063| 0     | $P(c_{</s>})$  |
| **food**   | $P(f_{<s>})$  | 0.014 | 0   | 0.014 | 0      | 0.00092| 0.0037| 0     | 0     | $P(f_{</s>})$  |
| **lunch**  | $P(l_{<s>})$  | 0.0059| 0   | 0     | 0      | 0      | 0.0029| 0     | 0     | $P(l_{</s>})$  |
| **spend**  | $P(s_{<s>})$  | 0.0036| 0   | 0.0036| 0      | 0      | 0     | 0     | 0     | $P(s_{</s>})$  |

Questa matrice $\mathbf N$ è ottenuta:
$$
\mathbf N_{ij} = \frac{\mathbf B_{ij}}{\mathbf u_i}
$$

## Calcolo della Probabilità di Frasi Specifiche

### Frase: "I want English food"
La probabilità si calcola come:
$$
P(\text{<s> I want English food </s>}) = P(I|\text{<s>}) \cdot P(want|I) \cdot P(English|want) \cdot P(food|English) \cdot P(</s>|food)
$$
Con i seguenti valori:
- $P(I|\text{<s>}) = 0.25$
- $P(want|I) = 0.33$
- $P(English|want) = 0.0011$
- $P(food|English) = 0.5$
- $P(</s>|food) = 0.68$

Pertanto:
$$
P(\text{<s> I want English food </s>}) \approx 0.25 \times 0.33 \times 0.0011 \times 0.5 \times 0.68 \approx 0.000031
$$

### Frase: "I want Chinese food"
La probabilità si calcola come:
$$
P(\text{<s> I want Chinese food </s>}) = P(I|\text{<s>}) \cdot P(want|I) \cdot P(Chinese|want) \cdot P(food|Chinese) \cdot P(</s>|food)
$$
Con i seguenti valori:
- $P(I|\text{<s>}) = 0.25$
- $P(want|I) = 0.33$
- $P(Chinese|want) = 0.0065$
- $P(food|Chinese) = 0.52$
- $P(</s>|food) = 0.68$

Pertanto:
$$
P(\text{<s> I want Chinese food </s>}) \approx 0.25 \times 0.33 \times 0.0065 \times 0.52 \times 0.68 \approx 0.00019
$$

## Conclusioni: Cosa Ci Insegnano gli N-grammi
Nonostante la semplicità, i modelli basati su N-grammi riescono a catturare informazioni interessanti riguardo al linguaggio:
- **Fatti Linguistici:**  
  Ad esempio:  
  - $P(English | want) = 0.0011$  
  - $P(Chinese | want) = 0.0065$  
  - $P(to | want) = 0.66$
- **Conoscenza del Mondo:**  
  Ad esempio:  
  - $P(eat | to) = 0.28$  
  - $P(food | to) = 0$
- **Sintassi:**  
  Ad esempio:  
  - $P(want | spend) = 0$  
  - $P(I | \text{<s>}) = 0.25$
- **Discorso:**  
  Le probabilità aiutano anche a comprendere le relazioni contestuali e di flusso nel discorso.


## Conclusione

Questa è una breve panoramica sul corpus BERP e sulle tecniche di modellazione del linguaggio basate sugli N-grammi, che evidenzia come questi metodi possano essere utilizzati per valutare e interpretare la probabilità di frasi in linguaggio naturale.
