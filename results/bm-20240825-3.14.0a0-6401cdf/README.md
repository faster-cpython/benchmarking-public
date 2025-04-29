# Results

- fork: python/6401cdf90810252a0de1
- version: 3.14.0a0
- config: 
- commit hash: [6401cdf](https://github.com/python/cpython/commit/6401cdf)
- commit date: 2024-08-25T22:11:59-04:00
- commit merge base: [602fcf97df1665538d4e9841f9dc6bc33e38bece](https://github.com/python/cpython/commit/602fcf97df1665538d4e9841f9dc6bc33e38bece)
- ref: 6401cdf90810252a0de1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14715517120)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf.json)

### vs. 3.10.4

- Geometric mean: 1.403x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf-vs-3.10.4.md)
- [📈time plot](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf-vs-3.12.0.md)
- [📈time plot](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 95.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dulwich_log, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf-vs-3.13.0.md)
- [📈time plot](bm-20240825-linux-x86_64-python-6401cdf90810252a0de1-3.14.0a0-6401cdf-vs-3.13.0.svg)

