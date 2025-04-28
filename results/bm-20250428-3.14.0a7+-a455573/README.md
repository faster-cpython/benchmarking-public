# Results

- fork: faster-cpython/get_iter_stats
- version: 3.14.0a7+
- config: 
- commit hash: [a455573](https://github.com/faster%2dcpython/cpython/commit/a455573)
- commit date: 2025-04-28T18:14:38+01:00
- commit merge base: [844596c09fc812a58ac1b381b51bee12d327da31](https://github.com/python/cpython/commit/844596c09fc812a58ac1b381b51bee12d327da31)
- ref: get_iter_stats

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14713743645)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573.json)

### vs. 3.10.4

- Geometric mean: 1.374x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.10.4.md)
- [📈time plot](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.12.0.md)
- [📈time plot](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.13.0.md)
- [📈time plot](bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.13.0.svg)

