# Results

- fork: python/2228e92da31ca7344a16
- version: 3.14.0a3+
- config: 
- commit hash: [2228e92](https://github.com/python/cpython/commit/2228e92)
- commit date: 2025-01-05T12:07:18+00:00
- commit merge base: [ae23a012e6c8aadc4a588101cbe7bc86ede45627](https://github.com/python/cpython/commit/ae23a012e6c8aadc4a588101cbe7bc86ede45627)
- ref: 2228e92da31ca7344a16

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12671793870)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.205x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 52.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

