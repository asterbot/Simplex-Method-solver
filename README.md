# Simplex-Method-solver

Solves Linear Programs using the [Simplex Algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)

Add the data in `input.txt` using the following format:
```
m n
A(row-wise)
b(single line)
c(single line)
y/n 
B(if y, else ignore this line)
z
```
For the linear program of the form: 
>max $c^Tx + z$ \
such that $Ax=b, x \ge 0$ \
\
Basis $B$ if provided \
and $A \in \R^{m \times n}$, $b \in \R^m$, $x \in \R^n$


and run:

```bash
python3 simplex.py < input.txt > output.txt
```

and `output.txt` will contain the steps of solving it as well as the final answer.
