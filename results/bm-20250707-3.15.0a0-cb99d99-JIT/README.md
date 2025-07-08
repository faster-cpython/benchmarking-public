# Results

- fork: python/cb99d992774b67761441
- version: 3.15.0a0
- config: JIT
- commit hash: [cb99d99](https://github.com/python/cpython/commit/cb99d99)
- commit date: 2025-07-07T11:03:07+02:00
- commit merge base: [d05423a90ce0ee9ad5207dce3dd06ab2397f3d6e](https://github.com/python/cpython/commit/d05423a90ce0ee9ad5207dce3dd06ab2397f3d6e)
- ref: cb99d992774b67761441

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16139562343)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99.json)

### vs. 3.10.4

- Geometric mean: 1.322x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.10.4.md)
- [📈time plot](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.12.0.md)
- [📈time plot](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.13.0.md)
- [📈time plot](bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16139581600)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99.json)

### vs. 3.10.4

- Geometric mean: 1.318x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.10.4.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.12.0.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x faster (HPT: reliability of 88.89%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.13.0.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16139571637)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99.json)

### vs. 3.10.4

- Geometric mean: 1.341x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.10.4.md)
- [📈time plot](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 94.18%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.12.0.md)
- [📈time plot](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.13.0.md)
- [📈time plot](bm-20250707-darwin-arm64-python-cb99d992774b67761441-3.15.0a0-cb99d99-vs-3.13.0.svg)

