# Results

- fork: python/e2b35ee22950bc5dc541
- version: 3.14.0a6+
- config: 
- commit hash: [e2b35ee](https://github.com/python/cpython/commit/e2b35ee)
- commit date: 2025-04-08T09:23:48+09:00
- commit merge base: [f5639d87f59043d3075dbd3d9075f30e872dd91a](https://github.com/python/cpython/commit/f5639d87f59043d3075dbd3d9075f30e872dd91a)
- ref: e2b35ee22950bc5dc541

## linux x86_64 (azure)

- [pystats raw](bm-20250408-azure-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-pystats.json)
- [pystats table](bm-20250408-azure-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14324562453)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee.json)

### vs. 3.10.4

- Geometric mean: 1.473x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-vs-3.10.4.md)
- [📈time plot](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.137x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-vs-3.12.0.md)
- [📈time plot](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-vs-3.13.0.md)
- [📈time plot](bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6%2B-e2b35ee-vs-3.13.0.svg)

