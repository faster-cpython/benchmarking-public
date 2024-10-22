# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [16cd6cc](https://github.com/python/cpython/commit/16cd6cc)
- commit date: 2024-10-05T09:56:44+02:00
- commit merge base: [a5fc50994a3fae46d0c3d496c4e1d5e00548a1b8](https://github.com/python/cpython/commit/a5fc50994a3fae46d0c3d496c4e1d5e00548a1b8)
- ref: 16cd6cc86b3ba20074ae

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11197259037)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json)

### vs. 3.10.4

- Geometric mean: 1.20x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.md)
- [📈time plot](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.51x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.md)
- [📈time plot](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.55x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log
- [📄table](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.md)
- [📈time plot](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.43x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base-mem.svg)
- [📄table](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.md)
- [📈time plot](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.md)
- [📈time plot](bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11197259037)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json)

### vs. 3.10.4

- Geometric mean: 1.06x slower (HPT: reliability of 99.88%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.md)
- [📈time plot](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.35x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.md)
- [📈time plot](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.md)
- [📈time plot](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 67.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base-mem.svg)
- [📄table](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.md)
- [📈time plot](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.md)
- [📈time plot](bm-20241005-linux-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11197259037)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 99.99%, 1.05x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.md)
- [📈time plot](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.41x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.md)
- [📈time plot](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.41x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.md)
- [📈time plot](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base-mem.svg)
- [📄table](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.md)
- [📈time plot](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.md)
- [📈time plot](bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11197259037)
- cpu model: missing
- platform: macOS-15.0-arm64-arm-64bit-Mach-O
- [raw results](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json)

### vs. 3.10.4

- Geometric mean: 1.12x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 0.60x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.md)
- [📈time plot](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.30x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.md)
- [📈time plot](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.28x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.md)
- [📈time plot](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base-mem.svg)
- [📄table](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.md)
- [📈time plot](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.md)
- [📈time plot](bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc-vs-3.13.0b2.svg)

