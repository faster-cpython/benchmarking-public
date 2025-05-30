# Results

- fork: iritkatriel/tuple
- version: 3.14.0a6+
- config: JIT
- commit hash: [50dd66b](https://github.com/iritkatriel/cpython/commit/50dd66b)
- commit date: 2025-03-26T22:45:06+00:00
- commit merge base: [52b5eb95b770fa00ebbd449ba40cab4a0e7c7df7](https://github.com/python/cpython/commit/52b5eb95b770fa00ebbd449ba40cab4a0e7c7df7)
- ref: tuple

## linux x86_64 (azure)

- [pystats raw](bm-20250326-azure-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-pystats.json)
- [pystats table](bm-20250326-azure-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-pystats.md)

### vs. base

- [pystats diff](bm-20250326-azure-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14115511011)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-3.10.4.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 96.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-3.12.0.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-3.13.0.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 58.18%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-base-mem.svg)
- [📄table](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-base.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6%2B-50dd66b-vs-base.svg)

