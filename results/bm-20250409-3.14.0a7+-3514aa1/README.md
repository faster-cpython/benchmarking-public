# Results

- fork: faster-cpython/trashcan_in_dealloc
- version: 3.14.0a7+
- config: 
- commit hash: [3514aa1](https://github.com/faster%2dcpython/cpython/commit/3514aa1)
- commit date: 2025-04-09T15:46:52+01:00
- commit merge base: [c5e856a5dc8eed4813ecb8fbf4120411af9a6130](https://github.com/python/cpython/commit/c5e856a5dc8eed4813ecb8fbf4120411af9a6130)
- ref: trashcan_in_dealloc

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14360452060)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.md)
- [📈time plot](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.md)
- [📈time plot](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.md)
- [📈time plot](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base-mem.svg)
- [📄table](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.md)
- [📈time plot](bm-20250409-arminc-aarch64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14360452060)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1.json)

### vs. 3.10.4

- Geometric mean: 1.456x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.md)
- [📈time plot](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.md)
- [📈time plot](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.md)
- [📈time plot](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base-mem.svg)
- [📄table](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.md)
- [📈time plot](bm-20250409-linux-x86_64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14360452060)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.md)
- [📈time plot](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.md)
- [📈time plot](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 58.24%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.md)
- [📈time plot](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x faster (HPT: reliability of 91.70%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.md)
- [📈time plot](bm-20250409-pythonperf1-amd64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14360452060)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1.json)

### vs. 3.10.4

- Geometric mean: 1.384x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.md)
- [📈time plot](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.md)
- [📈time plot](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.088x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.md)
- [📈time plot](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base-mem.svg)
- [📄table](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.md)
- [📈time plot](bm-20250409-darwin-arm64-faster%252dcpython-trashcan_in_dealloc-3.14.0a7%2B-3514aa1-vs-base.svg)

