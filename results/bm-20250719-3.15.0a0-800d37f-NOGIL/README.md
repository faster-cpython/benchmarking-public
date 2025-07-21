# Results

- fork: python/800d37feca2e0ea33439
- version: 3.15.0a0
- config: NOGIL
- commit hash: [800d37f](https://github.com/python/cpython/commit/800d37f)
- commit date: 2025-07-19T21:43:50+02:00
- commit merge base: [69ea1b3a8f45fec46add3272ad47f14ff5321ae8](https://github.com/python/cpython/commit/69ea1b3a8f45fec46add3272ad47f14ff5321ae8)
- ref: 800d37feca2e0ea33439

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16394010723)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json)

### vs. 3.10.4

- Geometric mean: 1.143x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.md)
- [📈time plot](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x slower (HPT: reliability of 99.72%, 1.01x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.md)
- [📈time plot](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.089x slower (HPT: reliability of 99.92%, 1.01x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.md)
- [📈time plot](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.122x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base-mem.svg)
- [📄table](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.md)
- [📈time plot](bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16394010723)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json)

### vs. 3.10.4

- Geometric mean: 1.192x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.66x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.md)
- [📈time plot](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x slower (HPT: reliability of 98.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.md)
- [📈time plot](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x slower (HPT: reliability of 96.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.md)
- [📈time plot](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.097x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base-mem.svg)
- [📄table](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.md)
- [📈time plot](bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16394010723)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json)

### vs. 3.10.4

- Geometric mean: 1.142x faster (HPT: reliability of 99.76%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.md)
- [📈time plot](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 98.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.md)
- [📈time plot](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x slower (HPT: reliability of 99.98%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.md)
- [📈time plot](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.121x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.md)
- [📈time plot](bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16394010723)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json)

### vs. 3.10.4

- Geometric mean: 1.294x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.md)
- [📈time plot](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.md)
- [📈time plot](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.135x faster (HPT: reliability of 99.58%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.md)
- [📈time plot](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.105x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.md)
- [📈time plot](bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-vs-base.svg)

