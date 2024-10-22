# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [8a284e1](https://github.com/python/cpython/commit/8a284e1)
- commit date: 2024-09-18T10:39:11+02:00
- commit merge base: [81480e6edb34774d783d018d1f0e61ab5c3f0a9a](https://github.com/python/cpython/commit/81480e6edb34774d783d018d1f0e61ab5c3f0a9a)
- ref: 8a284e189673582e2627

## linux x86_64 (azure)

- [pystats raw](bm-20240918-azure-x86_64-python-8a284e189673582e2627-3.14.0a0-8a284e1-pystats.json)
- [pystats table](bm-20240918-azure-x86_64-python-8a284e189673582e2627-3.14.0a0-8a284e1-pystats.md)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10943794936)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.10.4.md)
- [📈time plot](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.79x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.12.0.md)
- [📈time plot](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.13.0.md)
- [📈time plot](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.13.0b2.md)
- [📈time plot](bm-20240918-darwin-arm64-python-8a284e189673582e2627-3.14.0a0-8a284e1-vs-3.13.0b2.svg)

