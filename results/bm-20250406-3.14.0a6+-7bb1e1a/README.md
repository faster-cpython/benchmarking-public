# Results

- fork: python/7bb1e1a23634bae81bf7
- version: 3.14.0a6+
- config: 
- commit hash: [7bb1e1a](https://github.com/python/cpython/commit/7bb1e1a)
- commit date: 2025-04-06T16:37:37+00:00
- commit merge base: [c0661df42ad20e488dbfa3e0fec22462833fc3d6](https://github.com/python/cpython/commit/c0661df42ad20e488dbfa3e0fec22462833fc3d6)
- ref: 7bb1e1a23634bae81bf7

## linux x86_64 (azure)

- [pystats raw](bm-20250406-azure-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-pystats.json)
- [pystats table](bm-20250406-azure-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14297206278)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a.json)

### vs. 3.10.4

- Geometric mean: 1.480x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.10.4.md)
- [📈time plot](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.142x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.12.0.md)
- [📈time plot](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.13.0.md)
- [📈time plot](bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14315692379)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a.json)

### vs. 3.10.4

- Geometric mean: 1.365x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.10.4.md)
- [📈time plot](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.12.0.md)
- [📈time plot](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.13.0.md)
- [📈time plot](bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6%2B-7bb1e1a-vs-3.13.0.svg)

