# Results

- fork: faster-cpython/tagged_ints_lasti
- version: 3.14.0a7+
- config: 
- commit hash: [33b1fe4](https://github.com/faster%2dcpython/cpython/commit/33b1fe4)
- commit date: 2025-04-11T11:22:32+01:00
- commit merge base: [d87e7f35297d34755026173d84a38eedfbed78de](https://github.com/python/cpython/commit/d87e7f35297d34755026173d84a38eedfbed78de)
- ref: tagged_ints_lasti

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14401839533)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4.json)

### vs. 3.10.4

- Geometric mean: 1.461x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-3.10.4.md)
- [📈time plot](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-3.12.0.md)
- [📈time plot](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-3.13.0.md)
- [📈time plot](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 95.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-base-mem.svg)
- [📄table](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-base.md)
- [📈time plot](bm-20250411-linux-x86_64-faster%252dcpython-tagged_ints_lasti-3.14.0a7%2B-33b1fe4-vs-base.svg)

