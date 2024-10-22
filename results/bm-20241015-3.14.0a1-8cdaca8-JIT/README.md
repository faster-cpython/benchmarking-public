# Results

- fork: python
- version: 3.14.0a1
- config: JIT
- commit hash: [8cdaca8](https://github.com/python/cpython/commit/8cdaca8)
- commit date: 2024-10-15T22:34:54+03:00
- commit merge base: [3ea488aac44887a7cdb30be69580c81a0ca6afe2](https://github.com/python/cpython/commit/3ea488aac44887a7cdb30be69580c81a0ca6afe2)
- ref: v3.14.0a1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 99.97%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log, sphinx
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.88%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 70.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 82.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 60.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 51.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 99.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.05x faster (HPT: reliability of 74.05%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: sphinx
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.04x faster (HPT: reliability of 83.32%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.68%, 1.00x faster at 99th %ile)
- Memory usage: 6.80x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0b2.svg)

