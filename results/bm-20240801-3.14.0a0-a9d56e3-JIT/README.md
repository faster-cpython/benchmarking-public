# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [a9d56e3](https://github.com/python/cpython/commit/a9d56e3)
- commit date: 2024-08-01T09:27:26+01:00
- commit merge base: [46f5a4f9e1781ad8d60eb53bbaf6cd8534a286cd](https://github.com/python/cpython/commit/46f5a4f9e1781ad8d60eb53bbaf6cd8534a286cd)
- ref: a9d56e38a08ec198a228

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.md)
- [📈time plot](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.md)
- [📈time plot](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.md)
- [📈time plot](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.md)
- [📈time plot](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.md)
- [📈time plot](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 53.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.md)
- [📈time plot](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.md)
- [📈time plot](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 53.67%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.md)
- [📈time plot](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 63.27%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.md)
- [📈time plot](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 84.32%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 99.62%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.md)
- [📈time plot](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.md)
- [📈time plot](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.11x faster (HPT: reliability of 98.82%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.md)
- [📈time plot](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.md)
- [📈time plot](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.73x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.md)
- [📈time plot](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.md)
- [📈time plot](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3-vs-3.13.0b2.svg)

