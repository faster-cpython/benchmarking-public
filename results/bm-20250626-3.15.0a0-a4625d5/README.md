# Results

- fork: python/a4625d597f9fc2d083fb
- version: 3.15.0a0
- config: 
- commit hash: [a4625d5](https://github.com/python/cpython/commit/a4625d5)
- commit date: 2025-06-26T15:18:32+01:00
- commit merge base: [0d76dccc3b4376ba075a1737f58809e3d83aaaa3](https://github.com/python/cpython/commit/0d76dccc3b4376ba075a1737f58809e3d83aaaa3)
- ref: a4625d597f9fc2d083fb

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15924058434)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json)

### vs. 3.10.4

- Geometric mean: 1.380x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.10.4.md)
- [📈time plot](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.12.0.md)
- [📈time plot](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.13.0.md)
- [📈time plot](bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15924070484)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json)

### vs. 3.10.4

- Geometric mean: 1.275x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.10.4.md)
- [📈time plot](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.12.0.md)
- [📈time plot](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 98.74%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.13.0.md)
- [📈time plot](bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15924064427)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json)

### vs. 3.10.4

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.10.4.md)
- [📈time plot](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x slower (HPT: reliability of 97.63%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.12.0.md)
- [📈time plot](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 69.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.13.0.md)
- [📈time plot](bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5-vs-3.13.0.svg)

