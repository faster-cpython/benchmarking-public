# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [6e06e01](https://github.com/python/cpython/commit/6e06e01)
- commit date: 2024-09-12T20:24:15+01:00
- commit merge base: [a53812df126b99bca25187441a123c7785ee82a0](https://github.com/python/cpython/commit/a53812df126b99bca25187441a123c7785ee82a0)
- ref: 6e06e01881dcffbeef5b

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.md)
- [📈time plot](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 89.52%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.md)
- [📈time plot](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240912-azure-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-pystats.json)
- [pystats table](bm-20240912-azure-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json)

### vs. 3.10.4

- Geometric mean: 1.41x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.md)
- [📈time plot](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.md)
- [📈time plot](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.md)
- [📈time plot](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 87.45%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.md)
- [📈time plot](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.md)
- [📈time plot](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 87.05%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.md)
- [📈time plot](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.md)
- [📈time plot](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.md)
- [📈time plot](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.68x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.md)
- [📈time plot](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.md)
- [📈time plot](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 75.82%, 1.00x slower at 99th %ile)
- Memory usage: 0.51x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01-vs-3.13.0b2.svg)

