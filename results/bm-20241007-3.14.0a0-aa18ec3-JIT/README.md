# Results

- fork: nick-arm
- version: 3.14.0a0
- config: JIT
- commit hash: [aa18ec3](https://github.com/nick%2darm/cpython/commit/aa18ec3)
- commit date: 2024-10-07T16:18:44+00:00
- commit merge base: [5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7](https://github.com/nick%2darm/cpython/commit/5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7)
- ref: codecache

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11255467323)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base-mem.svg)
- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-arminc-aarch64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11255467323)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 54.44%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.80%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base-mem.svg)
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11255467323)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 62.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 84.33%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base-mem.svg)
- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11255467323)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.40x
- missing benchmarks: 🔴 sphinx
- [🧠memory plot](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base-mem.svg)
- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-darwin-arm64-nick%252darm-codecache-3.14.0a0-aa18ec3-vs-3.13.0b2.svg)

