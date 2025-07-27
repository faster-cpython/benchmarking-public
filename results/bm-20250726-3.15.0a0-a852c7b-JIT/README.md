# Results

- fork: python/a852c7bdd48979218a0c
- version: 3.15.0a0
- config: JIT
- commit hash: [a852c7b](https://github.com/python/cpython/commit/a852c7b)
- commit date: 2025-07-26T18:01:51+01:00
- commit merge base: [d5fa437dfb50e2e47632cdc994e3257608688f30](https://github.com/python/cpython/commit/d5fa437dfb50e2e47632cdc994e3257608688f30)
- ref: a852c7bdd48979218a0c

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16545162009)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json)

### vs. 3.10.4

- Geometric mean: 1.288x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)
- [📈time plot](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x faster (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)
- [📈time plot](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 98.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)
- [📈time plot](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg)
- [📄table](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)
- [📈time plot](bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16545162009)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json)

### vs. 3.10.4

- Geometric mean: 1.332x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 73.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg)
- [📄table](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16545162009)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json)

### vs. 3.10.4

- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)
- [📈time plot](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)
- [📈time plot](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x faster (HPT: reliability of 82.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)
- [📈time plot](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.033x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)
- [📈time plot](bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16545162009)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json)

### vs. 3.10.4

- Geometric mean: 1.458x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)
- [📈time plot](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.478x faster (HPT: reliability of 100.00%, 1.43x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)
- [📈time plot](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.275x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)
- [📈time plot](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)
- [📈time plot](bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16545162009)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json)

### vs. 3.10.4

- Geometric mean: 1.192x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)
- [📈time plot](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)
- [📈time plot](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x slower (HPT: reliability of 99.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)
- [📈time plot](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 99.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg)
- [📄table](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)
- [📈time plot](bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)

