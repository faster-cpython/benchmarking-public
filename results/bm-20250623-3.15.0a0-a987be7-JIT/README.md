# Results

- fork: brandtbucher/justin_hot
- version: 3.15.0a0
- config: JIT
- commit hash: [a987be7](https://github.com/brandtbucher/cpython/commit/a987be7)
- commit date: 2025-06-23T15:44:45-07:00
- commit merge base: [0f866cbfefd797b4dae25962457c5579bb90dde5](https://github.com/python/cpython/commit/0f866cbfefd797b4dae25962457c5579bb90dde5)
- ref: justin_hot

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15837284041)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.md)
- [📈time plot](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.27%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.md)
- [📈time plot](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.20%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.md)
- [📈time plot](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 65.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base-mem.svg)
- [📄table](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.md)
- [📈time plot](bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15837284041)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7.json)

### vs. 3.10.4

- Geometric mean: 1.476x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.md)
- [📈time plot](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.135x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.md)
- [📈time plot](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.md)
- [📈time plot](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base-mem.svg)
- [📄table](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.md)
- [📈time plot](bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15837284041)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.085x faster (HPT: reliability of 71.29%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 97.44%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15837284041)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7.json)

### vs. 3.10.4

- Geometric mean: 1.250x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.md)
- [📈time plot](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 92.77%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.md)
- [📈time plot](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 51.63%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.md)
- [📈time plot](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 99.11%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base-mem.svg)
- [📄table](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.md)
- [📈time plot](bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7-vs-base.svg)

