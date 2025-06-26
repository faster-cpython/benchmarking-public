# Results

- fork: python/b14986c91464b06e9016
- version: 3.15.0a0
- config: 
- commit hash: [b14986c](https://github.com/python/cpython/commit/b14986c)
- commit date: 2025-06-21T22:03:17+05:30
- commit merge base: [6a16b3c440cf9ecabecd3e90f44310e3b0765780](https://github.com/python/cpython/commit/6a16b3c440cf9ecabecd3e90f44310e3b0765780)
- ref: b14986c91464b06e9016

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909370984)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.357x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250621-azure-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-pystats.json)
- [pystats table](bm-20250621-azure-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909370984)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909370984)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.287x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x faster (HPT: reliability of 78.15%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909370984)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.252x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 94.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x slower (HPT: reliability of 60.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

