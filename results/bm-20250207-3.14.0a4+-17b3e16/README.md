# Results

- fork: faster-cpython/account_for_escapes_
- version: 3.14.0a4+
- config: 
- commit hash: [17b3e16](https://github.com/faster%2dcpython/cpython/commit/17b3e16)
- commit date: 2025-02-07T11:53:09+00:00
- commit merge base: [58a4357e29a15135e6fd99f320c60f8ea0472d27](https://github.com/python/cpython/commit/58a4357e29a15135e6fd99f320c60f8ea0472d27)
- ref: account_for_escapes_

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13199380023)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16.json)

### vs. 3.10.4

- Geometric mean: 1.349x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-3.10.4.md)
- [📈time plot](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-3.12.0.md)
- [📈time plot](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-3.13.0.md)
- [📈time plot](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 93.41%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-base-mem.svg)
- [📄table](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-base.md)
- [📈time plot](bm-20250207-pythonperf2-x86_64-faster%252dcpython-account_for_escapes_-3.14.0a4%2B-17b3e16-vs-base.svg)

