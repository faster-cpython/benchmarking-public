# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [cc98bb5](https://github.com/faster%2dcpython/cpython/commit/cc98bb5)
- commit date: 2024-07-31T17:00:43+01:00
- commit merge base: [d27a53fc02a87e76066fc4e15ff1fff3922a482d](https://github.com/faster%2dcpython/cpython/commit/d27a53fc02a87e76066fc4e15ff1fff3922a482d)
- ref: experimental_branch_

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10185683529)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 80.60%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 96.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base-mem.svg)
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10185683529)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 94.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base-mem.svg)
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10185683529)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 82.78%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base-mem.svg)
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10185683529)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 99.93%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 89.05%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10185683529)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5.json)

### vs. 3.10.4

- Geometric mean: 1.11x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-cc98bb5-vs-base.svg)

