# Results

- fork: mdboom
- version: 3.13.0rc1
- config: 
- commit hash: [2a88001](https://github.com/mdboom/cpython/commit/2a88001)
- commit date: 2024-08-26T12:39:10-04:00
- ref: rc1_mdboom

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10563646888)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001-vs-3.10.4.md)
- [📈time plot](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 81.02%, 1.00x slower at 99th %ile)
- Memory usage: 0.45x
- missing benchmarks: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001-vs-3.12.0.md)
- [📈time plot](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.42x
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001-vs-3.13.0b2.md)
- [📈time plot](bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001-vs-3.13.0b2.svg)

