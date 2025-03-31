# Automi a Stati Finiti (FSA)

## Definizione Formale
Un automa a stati finiti è una **quintupla** $(Q, \Sigma, \delta, q_0, A)$, dove:
- **$Q$**: Insieme finito di stati (es. $q_0, q_1, q_2$).
- **$\Sigma$**: Alfabeto (simboli consentiti, es. $\{a, b, l\}$).
- **$\delta$**: Funzione di transizione $\delta(q, x) \rightarrow q'$. Definisce come l'automa passa da uno stato $q$ a $q'$ leggendo il simbolo $x$.
- **$q_0$**: Stato iniziale (es. $q_0$).
- **$A$**: Insieme di stati accettanti/finali (es. $\{q_4\}$).

---

## Esempio: Il "Linguaggio delle Pecore"
### Descrizione
- **Linguaggio $L_{\text{sheep}}$**: Stringhe che iniziano con "b", seguite da almeno due "a", e terminano con "!" (es. "baa!", "baaaaa!", ...).
- **Regex corrispondente**: `/baa+!/`.

### Automa Corrispondente
<img src="/static/images/tikz/c2065ac9f7677b8cda1c2e7e9cba0f18.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" />

### Tabella di Transizione
| Stato | $b$      | $a$      | $!$      |
|-------|----------|----------|----------|
| $q_0$ | $q_1$    | -        | -        |
| $q_1$ | -        | $q_2$    | -        |
| $q_2$ | -        | $q_3$    | -        |
| $q_3$ | -        | $q_3$    | $q_4$    |
| $q_4$ | -        | -        | -        |

---

## Funzionamento di un FSA
### Processo di Riconoscimento
1. **Input**: "baaa!"
   - $q_0 \xrightarrow{b} q_1 \xrightarrow{a} q_2 \xrightarrow{a} q_3 \xrightarrow{a} q_3 \xrightarrow{!} q_4$ → **Accettata**.
2. **Input**: "ba!"
   - $q_0 \xrightarrow{b} q_1 \xrightarrow{a} q_2$ → Esaurimento input in stato non finale → **Rifiutata**.

---

## Accettatori vs. Generatori
- **Accettatori**: Verificano se una stringa appartiene al linguaggio.
- **Generatori**: Producono tutte le stringhe valide.  
**Esempio generato**:  
<img src="/static/images/tikz/dede56224f04bae018c7b65e1093559e.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" />

---

## Relazione tra Regex e FSA
### Equivalenze
| Operazione Regex      | Operazione FSA                  |
|-----------------------|---------------------------------|
| `RE1\|RE2` (Unione)     | FSA che accetta $L_1 \cup L_2$ |
| `RE1RE2` (Concatenazione)| FSA che accetta $L_1L_2$     |
| `RE*` (Kleene Star)   | FSA con loop per ripetizioni    |

**Esempio**: Regex `(a|b)*c`  
<img src="/static/images/tikz/eff741d9ebf0391963103c5db1379ad9.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" />

---

## Esercizio Guidato
### Dati
- $L_1 = \\{\text{nlp}, \text{nat\_lang\_proc}\\}$
- $L_2 = \\{\text{\_is\_cool}\\}$
- $L_3 = L_1L_2^*$

### Soluzione
**FSA per $L_3$**:  
<img src="/static/images/tikz/8fc84c381c7c122012ead33381b4da43.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" />

---

## Applicazioni in NLP
### Tokenizzazione
<img src="/static/images/tikz/a13c524a49c3e0197788b6ee60c25376.svg" style="width: 100%; height: auto; max-height: 600px;" class="tikz-svg" />

---

> **Etichette**: #FSA #Regex #LinguaggiFormali  
> **Collegamenti**: [[Espressioni Regolari]], [[Teoria degli Automi]]  
> **Risorse**:  
> - [Speech and Language Processing (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/)  
> - [Simulatore FSA Online](https://ivanzuzak.info/noam/webapps/fsm_simulator/)
