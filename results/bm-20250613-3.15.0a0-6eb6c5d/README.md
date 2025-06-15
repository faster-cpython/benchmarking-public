# Results

- fork: python/6eb6c5dbfb528bd07d77
- version: 3.15.0a0
- config: 
- commit hash: [6eb6c5d](https://github.com/python/cpython/commit/6eb6c5d)
- commit date: 2025-06-13T19:57:48+03:00
- commit merge base: [14c1d093d52d8de32c486808c1e1e85e0f61c11c](https://github.com/python/cpython/commit/14c1d093d52d8de32c486808c1e1e85e0f61c11c)
- ref: 6eb6c5dbfb528bd07d77

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15665733105)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.md)
- [📈time plot](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.md)
- [📈time plot](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x slower (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.md)
- [📈time plot](bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250613-azure-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-pystats.json)
- [pystats table](bm-20250613-azure-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15665733105)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.md)
- [📈time plot](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.md)
- [📈time plot](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.md)
- [📈time plot](bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15665733105)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json)

### vs. 3.10.4

- Geometric mean: 1.152x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.md)
- [📈time plot](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x faster (HPT: reliability of 99.68%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.md)
- [📈time plot](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 99.39%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.md)
- [📈time plot](bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15665733105)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json)

### vs. 3.10.4

- Geometric mean: 1.156x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.md)
- [📈time plot](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x slower (HPT: reliability of 97.39%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.md)
- [📈time plot](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.079x slower (HPT: reliability of 82.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.md)
- [📈time plot](bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d-vs-3.13.0.svg)

