# Results

- fork: python/4f18916c5c28321f363e
- version: 3.14.0a7+
- config: NOGIL
- commit hash: [4f18916](https://github.com/python/cpython/commit/4f18916)
- commit date: 2025-04-26T18:43:23-04:00
- commit merge base: [ee033d455577dd7af6c5421f3365eba1c9af1087](https://github.com/python/cpython/commit/ee033d455577dd7af6c5421f3365eba1c9af1087)
- ref: 4f18916c5c28321f363e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14686301064)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916.json)

### vs. 3.10.4

- Geometric mean: 1.184x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)
- [📈time plot](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x slower (HPT: reliability of 99.63%, 1.01x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)
- [📈time plot](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 99.82%, 1.01x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)
- [📈time plot](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg)
- [📄table](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)
- [📈time plot](bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14686301064)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)
- [📈time plot](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.037x faster (HPT: reliability of 63.18%, 1.00x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)
- [📈time plot](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)
- [📈time plot](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.072x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.18x
- [🧠memory plot](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg)
- [📄table](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)
- [📈time plot](bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14686301064)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916.json)

### vs. 3.10.4

- Geometric mean: 1.250x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)
- [📈time plot](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x slower (HPT: reliability of 99.91%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)
- [📈time plot](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 93.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)
- [📈time plot](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.087x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg)
- [📄table](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)
- [📈time plot](bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14686301064)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916.json)

### vs. 3.10.4

- Geometric mean: 1.183x faster (HPT: reliability of 99.98%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)
- [📈time plot](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 86.48%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)
- [📈time plot](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x slower (HPT: reliability of 99.88%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)
- [📈time plot](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.079x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)
- [📈time plot](bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14686301064)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916.json)

### vs. 3.10.4

- Geometric mean: 1.034x faster (HPT: reliability of 55.46%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)
- [📈time plot](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.068x faster (HPT: reliability of 99.59%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)
- [📈time plot](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x slower (HPT: reliability of 99.99%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)
- [📈time plot](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.118x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)
- [📈time plot](bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14686301064)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916.json)

### vs. 3.10.4

- Geometric mean: 1.370x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)
- [📈time plot](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 98.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)
- [📈time plot](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)
- [📈time plot](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 96.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg)
- [📄table](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)
- [📈time plot](bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)

