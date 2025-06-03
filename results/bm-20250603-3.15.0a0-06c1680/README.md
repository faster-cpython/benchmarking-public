# Results

- fork: faster-cpython/specialize_for_iter_
- version: 3.15.0a0
- config: 
- commit hash: [06c1680](https://github.com/faster%2dcpython/cpython/commit/06c1680)
- commit date: 2025-06-03T10:56:16+01:00
- commit merge base: [ec12559ebafca01ded22c9013de64abe535c838d](https://github.com/python/cpython/commit/ec12559ebafca01ded22c9013de64abe535c838d)
- ref: specialize_for_iter_

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680.json)

### vs. 3.10.4

- Geometric mean: 1.228x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.md)
- [📈time plot](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.md)
- [📈time plot](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.md)
- [📈time plot](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 97.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base-mem.svg)
- [📄table](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.md)
- [📈time plot](bm-20250603-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250603-azure-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-pystats.json)
- [pystats table](bm-20250603-azure-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-pystats.md)

### vs. base

- [pystats diff](bm-20250603-azure-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.md)
- [📈time plot](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.md)
- [📈time plot](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 98.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.md)
- [📈time plot](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 93.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base-mem.svg)
- [📄table](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.md)
- [📈time plot](bm-20250603-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680.json)

### vs. 3.10.4

- Geometric mean: 1.175x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x slower (HPT: reliability of 70.55%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680.json)

### vs. 3.10.4

- Geometric mean: 1.148x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.md)
- [📈time plot](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x slower (HPT: reliability of 99.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.md)
- [📈time plot](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.086x slower (HPT: reliability of 90.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.md)
- [📈time plot](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.067x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base-mem.svg)
- [📄table](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.md)
- [📈time plot](bm-20250603-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-06c1680-vs-base.svg)

