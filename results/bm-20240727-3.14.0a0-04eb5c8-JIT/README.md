# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [04eb5c8](https://github.com/python/cpython/commit/04eb5c8)
- commit date: 2024-07-27T21:33:38+03:00
- commit merge base: [ae192262ad1cffb6ece9d16e67804386c382be0c](https://github.com/python/cpython/commit/ae192262ad1cffb6ece9d16e67804386c382be0c)
- ref: 04eb5c8db1e24cabd0cb

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10127289024)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.md)
- [📈time plot](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.md)
- [📈time plot](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base-mem.svg)
- [📄table](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.md)
- [📈time plot](bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10127289024)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.md)
- [📈time plot](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.md)
- [📈time plot](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 82.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base-mem.svg)
- [📄table](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.md)
- [📈time plot](bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10127289024)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 82.06%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 82.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 90.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base-mem.svg)
- [📄table](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10127289024)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 74.59%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x faster (HPT: reliability of 73.45%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10127289024)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 97.93%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x faster (HPT: reliability of 50.43%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10127289024)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.md)
- [📈time plot](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.45x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.md)
- [📈time plot](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 94.35%, 1.00x slower at 99th %ile)
- Memory usage: 0.42x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.68%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- [🧠memory plot](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base-mem.svg)
- [📄table](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.md)
- [📈time plot](bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8-vs-base.svg)

