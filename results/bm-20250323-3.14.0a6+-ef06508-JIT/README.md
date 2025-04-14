# Results

- fork: python/ef06508f8ef1d2943b2f
- version: 3.14.0a6+
- config: JIT
- commit hash: [ef06508](https://github.com/python/cpython/commit/ef06508)
- commit date: 2025-03-23T19:56:03+05:30
- commit merge base: [5fc889ffbfd271c651f563ab0afe2d345bacbca5](https://github.com/python/cpython/commit/5fc889ffbfd271c651f563ab0afe2d345bacbca5)
- ref: ef06508f8ef1d2943b2f

## linux x86_64 (azure)

- [pystats raw](bm-20250323-azure-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-pystats.json)
- [pystats table](bm-20250323-azure-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14045757818)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508.json)

### vs. 3.10.4

- Geometric mean: 1.443x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-vs-3.10.4.md)
- [📈time plot](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.115x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-vs-3.12.0.md)
- [📈time plot](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-vs-3.13.0.md)
- [📈time plot](bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6%2B-ef06508-vs-3.13.0.svg)

