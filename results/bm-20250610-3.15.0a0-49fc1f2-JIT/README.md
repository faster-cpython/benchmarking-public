# Results

- fork: python/49fc1f215aeb0f714455
- version: 3.15.0a0
- config: JIT
- commit hash: [49fc1f2](https://github.com/python/cpython/commit/49fc1f2)
- commit date: 2025-06-10T01:05:06+01:00
- commit merge base: [2e1ad6eb26871a379e5d3aa626d6fc93eba72a86](https://github.com/python/cpython/commit/2e1ad6eb26871a379e5d3aa626d6fc93eba72a86)
- ref: 49fc1f215aeb0f714455

## linux x86_64 (azure)

- [pystats raw](bm-20250610-azure-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-pystats.json)
- [pystats table](bm-20250610-azure-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15551644491)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-vs-3.10.4.md)
- [📈time plot](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-vs-3.12.0.md)
- [📈time plot](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 97.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-vs-3.13.0.md)
- [📈time plot](bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2-vs-3.13.0.svg)

