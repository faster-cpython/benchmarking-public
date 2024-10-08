# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [401fff7](https://github.com/python/cpython/commit/401fff7)
- commit date: 2024-09-14T14:29:55-04:00
- commit merge base: [9dacf430c2f4af2acd870291a649b7b957efcd2c](https://github.com/python/cpython/commit/9dacf430c2f4af2acd870291a649b7b957efcd2c)
- ref: 401fff7423ca3c8bf1d0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.12x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240914-azure-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-pystats.json)
- [pystats table](bm-20240914-azure-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-pystats.md)

### vs. base

- [pystats diff](bm-20240914-azure-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 68.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 86.70%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 89.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 75.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 97.21%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 98.56%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.05x faster (HPT: reliability of 94.14%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 88.66%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x faster (HPT: reliability of 98.55%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 0.62x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 91.64%, 1.00x faster at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

