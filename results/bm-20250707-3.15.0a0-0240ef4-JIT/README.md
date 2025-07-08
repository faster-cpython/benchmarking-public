# Results

- fork: python/0240ef4705d835e27beb
- version: 3.15.0a0
- config: JIT
- commit hash: [0240ef4](https://github.com/python/cpython/commit/0240ef4)
- commit date: 2025-07-07T23:30:27+05:30
- commit merge base: [fe187fae8d8321f1b8d3c9560a35efe904de4217](https://github.com/python/cpython/commit/fe187fae8d8321f1b8d3c9560a35efe904de4217)
- ref: 0240ef4705d835e27beb

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16131305975)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json)

### vs. 3.10.4

- Geometric mean: 1.287x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.10.4.md)
- [📈time plot](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 99.60%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.12.0.md)
- [📈time plot](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x faster (HPT: reliability of 98.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.13.0.md)
- [📈time plot](bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250707-azure-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-pystats.json)
- [pystats table](bm-20250707-azure-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-pystats.md)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16131305975)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json)

### vs. 3.10.4

- Geometric mean: 1.320x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.10.4.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.126x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.12.0.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x faster (HPT: reliability of 90.73%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.13.0.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16131305975)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json)

### vs. 3.10.4

- Geometric mean: 1.343x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.10.4.md)
- [📈time plot](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 94.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.12.0.md)
- [📈time plot](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.13.0.md)
- [📈time plot](bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-vs-3.13.0.svg)

