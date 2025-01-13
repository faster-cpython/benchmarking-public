# Results

- fork: diegorusso/pthread
- version: 3.14.0a1+
- config: JIT
- commit hash: [f74cd79](https://github.com/diegorusso/cpython/commit/f74cd79)
- commit date: 2024-10-18T17:44:23+01:00
- commit merge base: [37986e830ba25d2c382988b06bbe27410596346c](https://github.com/python/cpython/commit/37986e830ba25d2c382988b06bbe27410596346c)
- ref: pthread

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11469554947)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79.json)

### vs. 3.10.4

- Geometric mean: 1.237x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.10.4.md)
- [📈time plot](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 98.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.12.0.md)
- [📈time plot](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.56%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.13.0.md)
- [📈time plot](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-base-mem.svg)
- [📄table](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-base.md)
- [📈time plot](bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-base.svg)

