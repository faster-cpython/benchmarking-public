# Results

- fork: faster-cpython/fix_132508
- version: 3.14.0a7+
- config: 
- commit hash: [b1b1252](https://github.com/faster%2dcpython/cpython/commit/b1b1252)
- commit date: 2025-04-15T10:24:30+01:00
- commit merge base: [844596c09fc812a58ac1b381b51bee12d327da31](https://github.com/python/cpython/commit/844596c09fc812a58ac1b381b51bee12d327da31)
- ref: fix_132508

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14466008992)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252.json)

### vs. 3.10.4

- Geometric mean: 1.465x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.10.4.md)
- [📈time plot](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.12.0.md)
- [📈time plot](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.13.0.md)
- [📈time plot](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 53.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-base-mem.svg)
- [📄table](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-base.md)
- [📈time plot](bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-base.svg)

