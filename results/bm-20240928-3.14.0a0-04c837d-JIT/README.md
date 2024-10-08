# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [04c837d](https://github.com/python/cpython/commit/04c837d)
- commit date: 2024-09-28T15:15:43-07:00
- commit merge base: [69a4063ca516360b5eb96f5432ad9f9dfc32a72e](https://github.com/python/cpython/commit/69a4063ca516360b5eb96f5432ad9f9dfc32a72e)
- ref: 04c837d9d8a474777ef9

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.95%, 1.02x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base-mem.svg)
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 94.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base-mem.svg)
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 65.24%, 1.00x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 70.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 97.19%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base-mem.svg)
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 83.34%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.64%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.05x faster (HPT: reliability of 77.44%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.md)
- [📈time plot](bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.29%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x faster (HPT: reliability of 97.58%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.md)
- [📈time plot](bm-20240928-pythonperf1_win32-x86-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 71.16%, 1.00x faster at 99th %ile)
- Memory usage: 0.84x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.68x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base-mem.svg)
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-base.svg)

