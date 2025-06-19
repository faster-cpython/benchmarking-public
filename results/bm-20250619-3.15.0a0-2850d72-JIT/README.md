# Results

- fork: faster-cpython/tier_2_tos_caching
- version: 3.15.0a0
- config: JIT
- commit hash: [2850d72](https://github.com/faster%2dcpython/cpython/commit/2850d72)
- commit date: 2025-06-19T14:58:35+01:00
- commit merge base: [9731dd2c8df3509095ea45493bcefabe732eaf60](https://github.com/python/cpython/commit/9731dd2c8df3509095ea45493bcefabe732eaf60)
- ref: tier_2_tos_caching

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15759799729)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json)

### vs. 3.10.4

- Geometric mean: 1.331x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.md)
- [📈time plot](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.050x faster (HPT: reliability of 99.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.md)
- [📈time plot](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.md)
- [📈time plot](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 77.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base-mem.svg)
- [📄table](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.md)
- [📈time plot](bm-20250619-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15759799729)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json)

### vs. 3.10.4

- Geometric mean: 1.470x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.md)
- [📈time plot](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.131x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.md)
- [📈time plot](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.80%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.md)
- [📈time plot](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base-mem.svg)
- [📄table](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.md)
- [📈time plot](bm-20250619-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15759799729)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.md)
- [📈time plot](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.md)
- [📈time plot](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x faster (HPT: reliability of 53.17%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.md)
- [📈time plot](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 96.18%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.md)
- [📈time plot](bm-20250619-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15759799729)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json)

### vs. 3.10.4

- Geometric mean: 1.263x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.md)
- [📈time plot](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x slower (HPT: reliability of 89.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.md)
- [📈time plot](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 54.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.md)
- [📈time plot](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 94.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base-mem.svg)
- [📄table](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.md)
- [📈time plot](bm-20250619-darwin-arm64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-2850d72-vs-base.svg)

