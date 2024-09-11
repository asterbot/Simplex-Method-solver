# Simplex-Method-solver

Solves Linear Programs using the [Simplex Algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm) with the python script.

Add the data in `input.txt` using the following format:
```bash
m n
A   # (row-wise)
b   # (single line)
c   # (single line)
y/n # (whether basis is provided)
B   # (if previous line was y, else ignore this line)
z
```
For the linear program of the form: 
>max $c^Tx + z$ \
such that $Ax=b, x \ge 0$ \
\
Basis $B$ if provided \
and $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$, $x \in \mathbb{R}^n$


and run:

```bash
python3 simplex.py < input.txt > output.txt
```

and `output.txt` will contain the steps of solving it as well as the final answer.
