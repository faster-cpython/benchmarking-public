# Results

- fork: python/49234c065cf2b1ea32c5
- version: 3.14.0a6+
- config: 
- commit hash: [49234c0](https://github.com/python/cpython/commit/49234c0)
- commit date: 2025-03-18T14:31:13+01:00
- commit merge base: [8cb57dc3678a8b26772d0fffce525762fee4f234](https://github.com/python/cpython/commit/8cb57dc3678a8b26772d0fffce525762fee4f234)
- ref: 49234c065cf2b1ea32c5

## linux x86_64 (azure)

- [pystats raw](bm-20250318-azure-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-pystats.json)
- [pystats table](bm-20250318-azure-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14023445404)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-vs-3.10.4.md)
- [📈time plot](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-vs-3.12.0.md)
- [📈time plot](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-vs-3.13.0.md)
- [📈time plot](bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6%2B-49234c0-vs-3.13.0.svg)

