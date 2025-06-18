# Results

- fork: faster-cpython/specialize_for_compa
- version: 3.15.0a0
- config: 
- commit hash: [e27d994](https://github.com/faster%2dcpython/cpython/commit/e27d994)
- commit date: 2025-06-18T12:19:23+01:00
- commit merge base: [8dd8b5c2f0785675b9282b719256341448d49967](https://github.com/python/cpython/commit/8dd8b5c2f0785675b9282b719256341448d49967)
- ref: specialize_for_compa

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15733751827)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994.json)

### vs. 3.10.4

- Geometric mean: 1.351x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.md)
- [📈time plot](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.md)
- [📈time plot](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.md)
- [📈time plot](bm-20250618-arminc-aarch64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250618-azure-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-pystats.json)
- [pystats table](bm-20250618-azure-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-pystats.md)

### vs. base

- [pystats diff](bm-20250618-azure-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15733751827)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994.json)

### vs. 3.10.4

- Geometric mean: 1.460x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.md)
- [📈time plot](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.md)
- [📈time plot](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.md)
- [📈time plot](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base-mem.svg)
- [📄table](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base.md)
- [📈time plot](bm-20250618-linux-x86_64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15733751827)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994.json)

### vs. 3.10.4

- Geometric mean: 1.268x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.md)
- [📈time plot](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x faster (HPT: reliability of 99.45%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.md)
- [📈time plot](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.24%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.md)
- [📈time plot](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base.md)
- [📈time plot](bm-20250618-pythonperf1-amd64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15733751827)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994.json)

### vs. 3.10.4

- Geometric mean: 1.249x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.md)
- [📈time plot](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 95.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.md)
- [📈time plot](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 62.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.md)
- [📈time plot](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 89.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base-mem.svg)
- [📄table](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base.md)
- [📈time plot](bm-20250618-darwin-arm64-faster%252dcpython-specialize_for_compa-3.15.0a0-e27d994-vs-base.svg)

