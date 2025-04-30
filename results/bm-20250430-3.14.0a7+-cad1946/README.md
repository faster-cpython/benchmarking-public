# Results

- fork: faster-cpython/virtual_iterators
- version: 3.14.0a7+
- config: 
- commit hash: [cad1946](https://github.com/faster%2dcpython/cpython/commit/cad1946)
- commit date: 2025-04-30T11:42:51+01:00
- commit merge base: [44e4c479fbf2c28605bd39303b1ce484753f6177](https://github.com/python/cpython/commit/44e4c479fbf2c28605bd39303b1ce484753f6177)
- ref: virtual_iterators

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14753375162)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946.json)

### vs. 3.10.4

- Geometric mean: 1.348x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.md)
- [📈time plot](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.md)
- [📈time plot](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.md)
- [📈time plot](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 77.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base-mem.svg)
- [📄table](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.md)
- [📈time plot](bm-20250430-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250430-azure-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-pystats.json)
- [pystats table](bm-20250430-azure-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-pystats.md)

### vs. base

- [pystats diff](bm-20250430-azure-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14753375162)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946.json)

### vs. 3.10.4

- Geometric mean: 1.452x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.md)
- [📈time plot](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.md)
- [📈time plot](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.md)
- [📈time plot](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 81.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base-mem.svg)
- [📄table](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.md)
- [📈time plot](bm-20250430-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14753375162)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946.json)

### vs. 3.10.4

- Geometric mean: 1.282x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.md)
- [📈time plot](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.md)
- [📈time plot](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 84.88%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.md)
- [📈time plot](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 96.46%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [📄table](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.md)
- [📈time plot](bm-20250430-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14753375162)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946.json)

### vs. 3.10.4

- Geometric mean: 1.227x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.md)
- [📈time plot](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.md)
- [📈time plot](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x slower (HPT: reliability of 94.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.md)
- [📈time plot](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base-mem.svg)
- [📄table](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.md)
- [📈time plot](bm-20250430-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-cad1946-vs-base.svg)

