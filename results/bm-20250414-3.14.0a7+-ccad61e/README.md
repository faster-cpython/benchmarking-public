# Results

- fork: python/ccad61e35d240972d14f
- version: 3.14.0a7+
- config: 
- commit hash: [ccad61e](https://github.com/python/cpython/commit/ccad61e)
- commit date: 2025-04-14T01:49:02+01:00
- commit merge base: [4d3ad0467e5cb145b1f4bde4be5eb776946a4269](https://github.com/python/cpython/commit/4d3ad0467e5cb145b1f4bde4be5eb776946a4269)
- ref: ccad61e35d240972d14f

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14773393070)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e.json)

### vs. 3.10.4

- Geometric mean: 1.468x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e-vs-3.10.4.md)
- [📈time plot](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.132x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e-vs-3.12.0.md)
- [📈time plot](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e-vs-3.13.0.md)
- [📈time plot](bm-20250414-linux-x86_64-python-ccad61e35d240972d14f-3.14.0a7%2B-ccad61e-vs-3.13.0.svg)

