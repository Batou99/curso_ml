# Dia 1

## El interprete de python

### Python REPL
```
python3

>>> from numpy.random import randn
>>> data = {i : randn() for i in range(7)}
>>> print(data)
{0: -1.5948255432744511, 1: 0.10569006472787983, 2: 1.972367135977295, 3: 0.15455217573074576, 4: -0.24058577449429575, 5: -1.2904897053651216, 6: 0.3308507317325902}
```

### iPython REPL
```
ipython3

In [5]: import numpy as np
In [6]: data = {i : np.random.randn() for i in range(7)}
In [7]: data
Out[7]:
{0: -0.20470765948471295,
 1: 0.47894333805754824,
 2: -0.5194387150567381,
 3: -0.55573030434749,
 4: 1.9657805725027142,
 5: 1.3934058329729904,
 6: 0.09290787674371767}
```

### Jupyter
```
$ jupyter notebook
[I 15:20:52.739 NotebookApp] Serving notebooks from local directory:
/home/wesm/code/pydata-book
[I 15:20:52.739 NotebookApp] 0 active kernels
[I 15:20:52.739 NotebookApp] The Jupyter Notebook is running at:
http://localhost:8888/
[I 15:20:52.740 NotebookApp] Use Control-C to stop this server and shut down
all kernels (twice to skip confirmation).
Created new window in existing browser session.
```

* Tab completion
* Introspection
* `%run command`
* `%load`
* `%paste/cpaste`
* `%timeit`
* `%debug`
* `%pwd`
* `%reset`

## Basic Python

* Indentation (no braces)
...

## Data structures, functions and files

* Tuples, unpacking
* List
* Build-in sequence functions
    * enumerate
    * sorted
    * zip
    * reversed
* Dict
    * from sequence
    * from tuples
    * d.get(key), d.get(key, defvalue)
    * valid dict key types (immutable)
* Set

