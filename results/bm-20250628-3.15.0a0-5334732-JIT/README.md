# Results

- fork: python/5334732f9c8a44722e4b
- version: 3.15.0a0
- config: JIT
- commit hash: [5334732](https://github.com/python/cpython/commit/5334732)
- commit date: 2025-06-28T14:11:31+01:00
- commit merge base: [579acf45629fa0b7787ec78fa4049fc6a6388b71](https://github.com/python/cpython/commit/579acf45629fa0b7787ec78fa4049fc6a6388b71)
- ref: 5334732f9c8a44722e4b

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.115x faster (HPT: reliability of 99.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.113x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x faster (HPT: reliability of 62.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.97%, 1.02x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x faster (HPT: reliability of 72.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.79%, 1.01x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x slower (HPT: reliability of 99.90%, 1.01x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 76.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.049x slower (HPT: reliability of 97.17%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.187x slower (HPT: reliability of 99.96%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.198x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.065x faster (HPT: reliability of 85.69%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x faster (HPT: reliability of 99.95%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x slower (HPT: reliability of 99.22%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.224x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x slower (HPT: reliability of 99.55%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x slower (HPT: reliability of 94.61%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

