# Results

- fork: kumaraditya303/fast_state
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [7de6e22](https://github.com/kumaraditya303/cpython/commit/7de6e22)
- commit date: 2025-01-07T13:18:23+00:00
- commit merge base: [2228e92da31ca7344a163498f848973a1b356597](https://github.com/python/cpython/commit/2228e92da31ca7344a163498f848973a1b356597)
- ref: fast_state

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.081x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x slower (HPT: reliability of 99.56%, 1.01x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.83%, 1.01x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

