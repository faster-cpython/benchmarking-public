# Results

- fork: python/85bc489b649fe261f962
- version: 3.14.0a6+
- config: NOGIL
- commit hash: [85bc489](https://github.com/python/cpython/commit/85bc489)
- commit date: 2025-04-05T15:56:01-07:00
- commit merge base: [ad6a032cebf59d1668caa7e726aa5da72e1cbb5c](https://github.com/python/cpython/commit/ad6a032cebf59d1668caa7e726aa5da72e1cbb5c)
- ref: 85bc489b649fe261f962

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14286973937)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489.json)

### vs. 3.10.4

- Geometric mean: 1.175x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.60x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)
- [📈time plot](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x slower (HPT: reliability of 99.90%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)
- [📈time plot](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x slower (HPT: reliability of 99.93%, 1.02x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)
- [📈time plot](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.125x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base-mem.svg)
- [📄table](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)
- [📈time plot](bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14286973937)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489.json)

### vs. 3.10.4

- Geometric mean: 1.345x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)
- [📈time plot](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 83.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)
- [📈time plot](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 97.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)
- [📈time plot](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base-mem.svg)
- [📄table](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)
- [📈time plot](bm-20250405-linux-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14286973937)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.56x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)
- [📈time plot](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 97.60%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)
- [📈time plot](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x slower (HPT: reliability of 92.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)
- [📈time plot](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base-mem.svg)
- [📄table](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)
- [📈time plot](bm-20250405-pythonperf2-x86_64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14286973937)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489.json)

### vs. 3.10.4

- Geometric mean: 1.158x faster (HPT: reliability of 99.96%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)
- [📈time plot](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x slower (HPT: reliability of 96.70%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)
- [📈time plot](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x slower (HPT: reliability of 99.95%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)
- [📈time plot](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.116x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)
- [📈time plot](bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14286973937)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489.json)

### vs. 3.10.4

- Geometric mean: 1.078x faster (HPT: reliability of 92.75%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)
- [📈time plot](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)
- [📈time plot](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.93%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)
- [📈time plot](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)
- [📈time plot](bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14286973937)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489.json)

### vs. 3.10.4

- Geometric mean: 1.247x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)
- [📈time plot](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.005x slower (HPT: reliability of 96.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)
- [📈time plot](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 73.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)
- [📈time plot](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.098x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base-mem.svg)
- [📄table](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)
- [📈time plot](bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg)

