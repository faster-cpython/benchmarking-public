# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [342e654](https://github.com/python/cpython/commit/342e654)
- commit date: 2024-09-20T13:37:49+00:00
- commit merge base: [1a577729e347714eb819fa3a3a00149406c24e5e](https://github.com/python/cpython/commit/1a577729e347714eb819fa3a3a00149406c24e5e)
- ref: 342e654b8eda24c68da6

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.49x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.55x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.04x slower (HPT: reliability of 99.28%, 1.00x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.33x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-linux-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.09x slower (HPT: reliability of 99.98%, 1.05x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.39x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.38x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.42x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976602788)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json)

### vs. 3.10.4

- Geometric mean: 1.12x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.30x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 0.76x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.37x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 0.78x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base-mem.svg)
- [📄table](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.md)
- [📈time plot](bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654-vs-base.svg)

