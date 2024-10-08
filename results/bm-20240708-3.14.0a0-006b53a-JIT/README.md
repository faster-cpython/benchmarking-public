# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [006b53a](https://github.com/python/cpython/commit/006b53a)
- commit date: 2024-07-08T14:30:05-06:00
- commit merge base: [2be37ec8e2f68d2c2fce7ea7b9eef73d218a22f9](https://github.com/python/cpython/commit/2be37ec8e2f68d2c2fce7ea7b9eef73d218a22f9)
- ref: 006b53a42f72be83ecdf

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.md)
- [📈time plot](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.md)
- [📈time plot](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240708-azure-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-pystats.json)
- [pystats table](bm-20240708-azure-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.md)
- [📈time plot](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.md)
- [📈time plot](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.md)
- [📈time plot](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 80.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.md)
- [📈time plot](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 67.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.md)
- [📈time plot](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 98.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.md)
- [📈time plot](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 88.12%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.md)
- [📈time plot](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.md)
- [📈time plot](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 78.55%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.md)
- [📈time plot](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.md)
- [📈time plot](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a-vs-3.13.0b2.svg)

