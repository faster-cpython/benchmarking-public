# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [3597642](https://github.com/python/cpython/commit/3597642)
- commit date: 2024-09-10T16:07:30+01:00
- commit merge base: [07f0bf5aa4ca34e692c16e14129d79c161ee206f](https://github.com/python/cpython/commit/07f0bf5aa4ca34e692c16e14129d79c161ee206f)
- ref: 3597642ed57d184511ca

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10890711250)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.10.4.md)
- [📈time plot](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.12.0.md)
- [📈time plot](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.13.0b2.md)
- [📈time plot](bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240910-azure-x86_64-python-3597642ed57d184511ca-3.14.0a0-3597642-pystats.json)
- [pystats table](bm-20240910-azure-x86_64-python-3597642ed57d184511ca-3.14.0a0-3597642-pystats.md)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10890714433)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 0.83x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.10.4.md)
- [📈time plot](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 84.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.76x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.12.0.md)
- [📈time plot](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.63x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.13.0b2.md)
- [📈time plot](bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642-vs-3.13.0b2.svg)

