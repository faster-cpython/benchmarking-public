# Results

- fork: python/dd6d24e9d20407ea31a3
- version: 3.14.0a5+
- config: NOGIL
- commit hash: [dd6d24e](https://github.com/python/cpython/commit/dd6d24e)
- commit date: 2025-03-13T14:28:49+08:00
- commit merge base: [f7ac656c8ea9738bd430bfaa43b6c65fd9d9ad11](https://github.com/python/cpython/commit/f7ac656c8ea9738bd430bfaa43b6c65fd9d9ad11)
- ref: dd6d24e9d20407ea31a3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13843009504)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e.json)

### vs. 3.10.4

- Geometric mean: 1.372x slower (HPT: reliability of 100.00%, 1.50x slower at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-3.10.4.md)
- [📈time plot](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.509x slower (HPT: reliability of 100.00%, 2.01x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-3.12.0.md)
- [📈time plot](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.541x slower (HPT: reliability of 100.00%, 2.12x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-3.13.0.md)
- [📈time plot](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-base-mem.svg)
- [📄table](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-base.md)
- [📈time plot](bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5%2B-dd6d24e-vs-base.svg)

