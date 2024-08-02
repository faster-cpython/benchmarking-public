# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [4717aaa](https://github.com/python/cpython/commit/4717aaa)
- commit date: 2024-06-22T10:58:35-07:00
- commit merge base: [e21347549535b16f51a39986b78a2c2cd4ed09f4](https://github.com/python/cpython/commit/e21347549535b16f51a39986b78a2c2cd4ed09f4)
- ref: 4717aaa1a72d1964f153

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.24x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.60x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base-mem.svg)
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.19x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.48x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.62x slower (HPT: reliability of 100.00%, 1.39x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base-mem.svg)
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.48x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base-mem.svg)
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.27x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.37x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.39x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base-mem.svg)
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.svg)

