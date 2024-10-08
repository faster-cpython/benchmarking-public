# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
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

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.49x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.55x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.04x slower (HPT: reliability of 99.19%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.32x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.09x slower (HPT: reliability of 99.98%, 1.05x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.39x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.38x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.43x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.14x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 0.68x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.32x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 0.66x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.42x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

