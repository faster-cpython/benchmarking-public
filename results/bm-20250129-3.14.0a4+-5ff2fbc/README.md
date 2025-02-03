# Results

- fork: python/5ff2fbc026b14eadd41b
- version: 3.14.0a4+
- config: 
- commit hash: [5ff2fbc](https://github.com/python/cpython/commit/5ff2fbc)
- commit date: 2025-01-29T10:40:51-05:00
- commit merge base: [a29221675e7367608961c3484701ab2671ec6f3c](https://github.com/python/cpython/commit/a29221675e7367608961c3484701ab2671ec6f3c)
- ref: 5ff2fbc026b14eadd41b

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13036666901)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc.json)

### vs. 3.10.4

- Geometric mean: 1.450x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.10.4.md)
- [📈time plot](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.12.0.md)
- [📈time plot](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.13.0.md)
- [📈time plot](bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13118576405)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc.json)

### vs. 3.10.4

- Geometric mean: 1.364x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.10.4.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.12.0.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.069x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.13.0.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4%2B-5ff2fbc-vs-3.13.0.svg)

