# Results

- fork: faster-cpython/virtual_iterators
- version: 3.14.0a7+
- config: 
- commit hash: [a4b740d](https://github.com/faster%2dcpython/cpython/commit/a4b740d)
- commit date: 2025-04-16T10:47:00+01:00
- commit merge base: [844596c09fc812a58ac1b381b51bee12d327da31](https://github.com/python/cpython/commit/844596c09fc812a58ac1b381b51bee12d327da31)
- ref: virtual_iterators

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14490400673)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d.json)

### vs. 3.10.4

- Geometric mean: 1.367x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.md)
- [📈time plot](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.md)
- [📈time plot](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.md)
- [📈time plot](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 98.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base-mem.svg)
- [📄table](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.md)
- [📈time plot](bm-20250416-arminc-aarch64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250416-azure-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-pystats.json)
- [pystats table](bm-20250416-azure-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-pystats.md)

### vs. base

- [pystats diff](bm-20250416-azure-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14490400673)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d.json)

### vs. 3.10.4

- Geometric mean: 1.476x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.md)
- [📈time plot](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.136x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.md)
- [📈time plot](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.md)
- [📈time plot](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 84.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base-mem.svg)
- [📄table](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.md)
- [📈time plot](bm-20250416-linux-x86_64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14490400673)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.md)
- [📈time plot](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.md)
- [📈time plot](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 87.81%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.md)
- [📈time plot](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 94.68%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [📄table](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.md)
- [📈time plot](bm-20250416-pythonperf1-amd64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14490400673)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d.json)

### vs. 3.10.4

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.md)
- [📈time plot](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x slower (HPT: reliability of 99.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.md)
- [📈time plot](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 93.30%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.md)
- [📈time plot](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 96.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base-mem.svg)
- [📄table](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.md)
- [📈time plot](bm-20250416-darwin-arm64-faster%252dcpython-virtual_iterators-3.14.0a7%2B-a4b740d-vs-base.svg)

