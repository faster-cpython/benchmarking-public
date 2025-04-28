# Results

- fork: python/348012432155271cfbee
- version: 3.14.0a3+
- config: 
- commit hash: [3480124](https://github.com/python/cpython/commit/3480124)
- commit date: 2024-12-30T08:19:38-08:00
- commit merge base: [2bd5a7ab0f4a1f65ab8043001bd6e8416c5079bd](https://github.com/python/cpython/commit/2bd5a7ab0f4a1f65ab8043001bd6e8416c5079bd)
- ref: 348012432155271cfbee

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673984817)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124.json)

### vs. 3.10.4

- Geometric mean: 1.421x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.10.4.md)
- [📈time plot](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.12.0.md)
- [📈time plot](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.13.0.md)
- [📈time plot](bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.13.0.svg)

