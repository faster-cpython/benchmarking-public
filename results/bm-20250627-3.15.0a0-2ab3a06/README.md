# Results

- fork: faster-cpython/never_inline_decref
- version: 3.15.0a0
- config: 
- commit hash: [2ab3a06](https://github.com/faster%2dcpython/cpython/commit/2ab3a06)
- commit date: 2025-06-27T11:57:00+01:00
- commit merge base: [a4625d597f9fc2d083fbb9c22d3ffcec73b2061a](https://github.com/python/cpython/commit/a4625d597f9fc2d083fbb9c22d3ffcec73b2061a)
- ref: never_inline_decref

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15925871614)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06.json)

### vs. 3.10.4

- Geometric mean: 1.361x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.10.4.md)
- [📈time plot](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.12.0.md)
- [📈time plot](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.13.0.md)
- [📈time plot](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base-mem.svg)
- [📄table](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base.md)
- [📈time plot](bm-20250627-pythonperf2-x86_64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15925881203)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06.json)

### vs. 3.10.4

- Geometric mean: 1.273x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.10.4.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 99.79%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.12.0.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 99.56%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.13.0.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 77.47%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base.md)
- [📈time plot](bm-20250627-pythonperf1-amd64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15925893108)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06.json)

### vs. 3.10.4

- Geometric mean: 1.237x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.10.4.md)
- [📈time plot](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x slower (HPT: reliability of 99.48%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.12.0.md)
- [📈time plot](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 95.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.13.0.md)
- [📈time plot](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base-mem.svg)
- [📄table](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base.md)
- [📈time plot](bm-20250627-darwin-arm64-faster%252dcpython-never_inline_decref-3.15.0a0-2ab3a06-vs-base.svg)

