# Results

- fork: faster-cpython/tos_caching_1
- version: 3.14.0a6+
- config: CLANG
- commit hash: [5bbc96e](https://github.com/faster%2dcpython/cpython/commit/5bbc96e)
- commit date: 2025-04-08T14:26:05+01:00
- commit merge base: [275056a7fdcbe36aaac494b4183ae59943a338eb](https://github.com/python/cpython/commit/275056a7fdcbe36aaac494b4183ae59943a338eb)
- ref: tos_caching_1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. 3.10.4

- Geometric mean: 1.368x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base-mem.svg)
- [📄table](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-arminc-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. 3.10.4

- Geometric mean: 1.501x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.156x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.081x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base-mem.svg)
- [📄table](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-linux-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. 3.10.4

- Geometric mean: 1.526x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.206x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 98.36%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-pythonperf1-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. 3.10.4

- Geometric mean: 1.485x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.164x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.166x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base-mem.svg)
- [📄table](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-darwin-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

