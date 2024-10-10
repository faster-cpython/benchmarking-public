# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [9940093](https://github.com/python/cpython/commit/9940093)
- commit date: 2024-10-09T16:44:03-07:00
- commit merge base: [942916378aa6a0946b1385c2c7ca6935620d710a](https://github.com/python/cpython/commit/942916378aa6a0946b1385c2c7ca6935620d710a)
- ref: 99400930ac1d4e5e10a5

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11273317937)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.md)
- [📈time plot](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 0.76x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.md)
- [📈time plot](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 88.04%, 1.00x slower at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0b2.md)
- [📈time plot](bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093-vs-3.13.0b2.svg)

