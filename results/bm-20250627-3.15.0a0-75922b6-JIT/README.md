# Results

- fork: brandtbucher/jit_nops
- version: 3.15.0a0
- config: JIT
- commit hash: [75922b6](https://github.com/brandtbucher/cpython/commit/75922b6)
- commit date: 2025-06-27T13:10:31-07:00
- commit merge base: [c419af9e277bea7dd78f4defefc752fe93b0b8ec](https://github.com/python/cpython/commit/c419af9e277bea7dd78f4defefc752fe93b0b8ec)
- ref: jit_nops

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15936029325)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6.json)

### vs. 3.10.4

- Geometric mean: 1.336x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.md)
- [📈time plot](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.md)
- [📈time plot](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.md)
- [📈time plot](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 88.01%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base-mem.svg)
- [📄table](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.md)
- [📈time plot](bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250627-azure-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-pystats.json)
- [pystats table](bm-20250627-azure-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-pystats.md)

### vs. base

- [pystats diff](bm-20250627-azure-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15936029325)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6.json)

### vs. 3.10.4

- Geometric mean: 1.484x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.142x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 98.50%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base-mem.svg)
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15936029325)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 79.40%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 95.77%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15936029325)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6.json)

### vs. 3.10.4

- Geometric mean: 1.343x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.md)
- [📈time plot](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 94.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.md)
- [📈time plot](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.md)
- [📈time plot](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 99.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base-mem.svg)
- [📄table](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.md)
- [📈time plot](bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6-vs-base.svg)

