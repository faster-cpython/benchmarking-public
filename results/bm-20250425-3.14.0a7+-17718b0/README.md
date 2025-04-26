# Results

- fork: python/17718b0503e5d1c98725
- version: 3.14.0a7+
- config: 
- commit hash: [17718b0](https://github.com/python/cpython/commit/17718b0)
- commit date: 2025-04-25T14:57:01+00:00
- commit merge base: [670b6cc096886a9154604456417a7fd306675bd0](https://github.com/python/cpython/commit/670b6cc096886a9154604456417a7fd306675bd0)
- ref: 17718b0503e5d1c98725

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673719246)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0.json)

### vs. 3.10.4

- Geometric mean: 1.448x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.md)
- [📈time plot](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.md)
- [📈time plot](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.md)
- [📈time plot](bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673719246)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0.json)

### vs. 3.10.4

- Geometric mean: 1.272x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.md)
- [📈time plot](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.md)
- [📈time plot](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 98.60%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.md)
- [📈time plot](bm-20250425-pythonperf1-amd64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673719246)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0.json)

### vs. 3.10.4

- Geometric mean: 1.405x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.md)
- [📈time plot](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.md)
- [📈time plot](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.md)
- [📈time plot](bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.svg)

