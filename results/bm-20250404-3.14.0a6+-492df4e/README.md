# Results

- fork: faster-cpython/tos_caching_1
- version: 3.14.0a6+
- config: 
- commit hash: [492df4e](https://github.com/faster%2dcpython/cpython/commit/492df4e)
- commit date: 2025-04-04T12:59:49+01:00
- commit merge base: [275056a7fdcbe36aaac494b4183ae59943a338eb](https://github.com/python/cpython/commit/275056a7fdcbe36aaac494b4183ae59943a338eb)
- ref: tos_caching_1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14266922219)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e.json)

### vs. 3.10.4

- Geometric mean: 1.458x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.10.4.md)
- [📈time plot](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.12.0.md)
- [📈time plot](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.13.0.md)
- [📈time plot](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-base-mem.svg)
- [📄table](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-base.md)
- [📈time plot](bm-20250404-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14264844030)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e.json)

### vs. 3.10.4

- Geometric mean: 1.250x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.10.4.md)
- [📈time plot](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 96.62%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.12.0.md)
- [📈time plot](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 99.65%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.13.0.md)
- [📈time plot](bm-20250404-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14266936556)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e.json)

### vs. 3.10.4

- Geometric mean: 1.218x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.10.4.md)
- [📈time plot](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x slower (HPT: reliability of 99.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.12.0.md)
- [📈time plot](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 99.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.13.0.md)
- [📈time plot](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.083x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-base-mem.svg)
- [📄table](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-base.md)
- [📈time plot](bm-20250404-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-492df4e-vs-base.svg)

