# Results

- fork: Fidget-Spinner/pylong_compactadd
- version: 3.15.0a0
- config: 
- commit hash: [4019a15](https://github.com/Fidget%2dSpinner/cpython/commit/4019a15)
- commit date: 2025-06-14T00:28:34+08:00
- commit merge base: [afc5ab6cce9d7095b99c1410a6762bc4a96504dd](https://github.com/python/cpython/commit/afc5ab6cce9d7095b99c1410a6762bc4a96504dd)
- ref: pylong_compactadd

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15639848326)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.md)
- [📈time plot](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x slower (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.md)
- [📈time plot](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.md)
- [📈time plot](bm-20250614-arminc-aarch64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15639848326)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.md)
- [📈time plot](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.md)
- [📈time plot](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.md)
- [📈time plot](bm-20250614-linux-x86_64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15639848326)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15.json)

### vs. 3.10.4

- Geometric mean: 1.168x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.068x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 92.20%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15639848326)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15.json)

### vs. 3.10.4

- Geometric mean: 1.246x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.md)
- [📈time plot](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 92.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.md)
- [📈time plot](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.md)
- [📈time plot](bm-20250614-darwin-arm64-Fidget%252dSpinner-pylong_compactadd-3.15.0a0-4019a15-vs-3.13.0.svg)

