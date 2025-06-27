# Results

- fork: python/cebae977a63f32c3c03d
- version: 3.15.0a0
- config: 
- commit hash: [cebae97](https://github.com/python/cpython/commit/cebae97)
- commit date: 2025-06-01T00:33:02+03:00
- commit merge base: [3704171415c1ea6ebbeb2f992758b6565f42e378](https://github.com/python/cpython/commit/3704171415c1ea6ebbeb2f992758b6565f42e378)
- ref: cebae977a63f32c3c03d

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927041291)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927041291)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.296x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 68.44%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

