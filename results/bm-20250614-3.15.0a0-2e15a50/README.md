# Results

- fork: python/2e15a50851da66eb8227
- version: 3.15.0a0
- config: 
- commit hash: [2e15a50](https://github.com/python/cpython/commit/2e15a50)
- commit date: 2025-06-14T16:04:16+00:00
- commit merge base: [fc413ecb8f4bf1c59b29932695e3538548eb1a8a](https://github.com/python/cpython/commit/fc413ecb8f4bf1c59b29932695e3538548eb1a8a)
- ref: 2e15a50851da66eb8227

## linux x86_64 (azure)

- [pystats raw](bm-20250614-azure-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-pystats.json)
- [pystats table](bm-20250614-azure-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909433573)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-linux-x86_64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909433573)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.285x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 90.58%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909433573)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json)

### vs. 3.10.4

- Geometric mean: 1.247x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x slower (HPT: reliability of 96.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x slower (HPT: reliability of 72.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.md)
- [📈time plot](bm-20250614-darwin-arm64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50-vs-3.13.0.svg)

