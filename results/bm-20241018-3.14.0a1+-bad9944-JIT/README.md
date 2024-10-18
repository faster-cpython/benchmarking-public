# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [bad9944](https://github.com/brandtbucher/cpython/commit/bad9944)
- commit date: 2024-10-18T10:02:10-07:00
- commit merge base: [d8c864816121547338efa43c56e3f75ead98a924](https://github.com/brandtbucher/cpython/commit/d8c864816121547338efa43c56e3f75ead98a924)
- ref: justin_likely

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 98.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 79.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base-mem.svg)
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

