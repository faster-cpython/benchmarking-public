# Results

- fork: python/37986e830ba25d2c3829
- version: 3.14.0a1+
- config: JIT
- commit hash: [37986e8](https://github.com/python/cpython/commit/37986e8)
- commit date: 2024-10-17T08:20:30-04:00
- commit merge base: [dbcc5ac4709dfd8dfaf323d51f135f2218d14068](https://github.com/python/cpython/commit/dbcc5ac4709dfd8dfaf323d51f135f2218d14068)
- ref: 37986e830ba25d2c3829

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11469554947)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8.json)

### vs. 3.10.4

- Geometric mean: 1.238x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.42x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.10.4.md)
- [📈time plot](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 97.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.12.0.md)
- [📈time plot](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.13.0.md)
- [📈time plot](bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.13.0.svg)

