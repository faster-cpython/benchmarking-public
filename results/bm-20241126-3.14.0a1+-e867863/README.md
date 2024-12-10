# Results

- fork: python/e8678632077a75f9ad27
- version: 3.14.0a1+
- config: 
- commit hash: [e867863](https://github.com/python/cpython/commit/e867863)
- commit date: 2024-11-26T00:20:05+00:00
- commit merge base: [d00878b06a05ea04790813dba70b09cc1d11bf45](https://github.com/python/cpython/commit/d00878b06a05ea04790813dba70b09cc1d11bf45)
- ref: e8678632077a75f9ad27

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12021751115)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863.json)

### vs. 3.10.4

- Geometric mean: 1.409x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-3.10.4.md)
- [📈time plot](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-3.12.0.md)
- [📈time plot](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 83.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-3.13.0.md)
- [📈time plot](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-base-mem.svg)
- [📄table](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-base.md)
- [📈time plot](bm-20241126-linux-x86_64-python-e8678632077a75f9ad27-3.14.0a1%2B-e867863-vs-base.svg)

