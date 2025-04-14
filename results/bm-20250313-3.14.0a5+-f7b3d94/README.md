# Results

- fork: kumaraditya303/fast_asyncio
- version: 3.14.0a5+
- config: 
- commit hash: [f7b3d94](https://github.com/kumaraditya303/cpython/commit/f7b3d94)
- commit date: 2025-03-13T19:23:23+00:00
- commit merge base: [dd6d24e9d20407ea31a3bb653eab252ee0d41ffa](https://github.com/python/cpython/commit/dd6d24e9d20407ea31a3bb653eab252ee0d41ffa)
- ref: fast_asyncio

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13843006240)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94.json)

### vs. 3.10.4

- Geometric mean: 1.294x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-3.10.4.md)
- [📈time plot](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.455x slower (HPT: reliability of 100.00%, 1.76x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-3.12.0.md)
- [📈time plot](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.488x slower (HPT: reliability of 100.00%, 1.93x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-3.13.0.md)
- [📈time plot](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-base-mem.svg)
- [📄table](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-base.md)
- [📈time plot](bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5%2B-f7b3d94-vs-base.svg)

