# Results

- fork: python/e119526edface001ad7d
- version: 3.14.0a4+
- config: 
- commit hash: [e119526](https://github.com/python/cpython/commit/e119526)
- commit date: 2025-01-25T15:36:58+02:00
- commit merge base: [c39ae8922bad3e5ceeafa05891536c1584b6f3db](https://github.com/python/cpython/commit/c39ae8922bad3e5ceeafa05891536c1584b6f3db)
- ref: e119526edface001ad7d

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13118655121)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526.json)

### vs. 3.10.4

- Geometric mean: 1.345x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.64x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526-vs-3.10.4.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526-vs-3.12.0.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526-vs-3.13.0.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4%2B-e119526-vs-3.13.0.svg)

