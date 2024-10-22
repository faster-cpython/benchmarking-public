# Results

- fork: python
- version: 3.14.0a0
- config: T2
- commit hash: [315a933](https://github.com/python/cpython/commit/315a933)
- commit date: 2024-08-14T11:38:29+01:00
- commit merge base: [fe3e623562fb058ef7b8fd6d90ac5098a3b05816](https://github.com/python/cpython/commit/fe3e623562fb058ef7b8fd6d90ac5098a3b05816)
- ref: main

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10386118752)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.10.4.md)
- [📈time plot](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 99.87%, 1.02x slower at 99th %ile)
- Memory usage: 0.47x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.12.0.md)
- [📈time plot](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.13.0.md)
- [📈time plot](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.13.0b2.md)
- [📈time plot](bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933-vs-3.13.0b2.svg)

