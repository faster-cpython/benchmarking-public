# Results

- fork: faster-cpython/single_point_of_allo
- version: 3.14.0a5+
- config: 
- commit hash: [af468a2](https://github.com/faster%2dcpython/cpython/commit/af468a2)
- commit date: 2025-03-13T15:34:57+00:00
- commit merge base: [155c44b9015089eacc6e2ace449391c12bfb8b8d](https://github.com/python/cpython/commit/155c44b9015089eacc6e2ace449391c12bfb8b8d)
- ref: single_point_of_allo

## linux x86_64 (azure)

- [pystats raw](bm-20250313-azure-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-pystats.json)
- [pystats table](bm-20250313-azure-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13838579891)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2.json)

### vs. 3.10.4

- Geometric mean: 1.365x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-3.10.4.md)
- [📈time plot](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x faster (HPT: reliability of 99.58%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-3.12.0.md)
- [📈time plot](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 99.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-3.13.0.md)
- [📈time plot](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.049x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-base-mem.svg)
- [📄table](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-base.md)
- [📈time plot](bm-20250313-linux-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-af468a2-vs-base.svg)

