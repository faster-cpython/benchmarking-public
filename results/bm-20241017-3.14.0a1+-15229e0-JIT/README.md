# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [15229e0](https://github.com/brandtbucher/cpython/commit/15229e0)
- commit date: 2024-10-17T16:34:26-07:00
- commit merge base: [d8c864816121547338efa43c56e3f75ead98a924](https://github.com/brandtbucher/cpython/commit/d8c864816121547338efa43c56e3f75ead98a924)
- ref: justin_unlikely

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 65.70%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 99.94%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 94.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0b2.svg)

