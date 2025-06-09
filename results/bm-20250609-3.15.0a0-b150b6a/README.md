# Results

- fork: python/b150b6aca7b17efe1bb1
- version: 3.15.0a0
- config: 
- commit hash: [b150b6a](https://github.com/python/cpython/commit/b150b6a)
- commit date: 2025-06-09T18:33:18+08:00
- commit merge base: [c19e36cc4eabacaacc359e8b2550b10c2965a31a](https://github.com/python/cpython/commit/c19e36cc4eabacaacc359e8b2550b10c2965a31a)
- ref: b150b6aca7b17efe1bb1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534200254)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.md)
- [📈time plot](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.md)
- [📈time plot](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.md)
- [📈time plot](bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534215930)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json)

### vs. 3.10.4

- Geometric mean: 1.173x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x slower (HPT: reliability of 88.05%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534208033)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json)

### vs. 3.10.4

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.md)
- [📈time plot](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x slower (HPT: reliability of 98.60%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.md)
- [📈time plot](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.082x slower (HPT: reliability of 87.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.md)
- [📈time plot](bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a-vs-3.13.0.svg)

