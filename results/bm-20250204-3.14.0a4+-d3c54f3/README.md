# Results

- fork: python/d3c54f37889436ded452
- version: 3.14.0a4+
- config: 
- commit hash: [d3c54f3](https://github.com/python/cpython/commit/d3c54f3)
- commit date: 2025-02-04T10:38:06+00:00
- commit merge base: [0664c1af9b29a5af2404e04a522f8e9e175ba05a](https://github.com/python/cpython/commit/0664c1af9b29a5af2404e04a522f8e9e175ba05a)
- ref: d3c54f37889436ded452

## linux x86_64 (azure)

- [pystats raw](bm-20250204-azure-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-pystats.json)
- [pystats table](bm-20250204-azure-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13137089910)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3.json)

### vs. 3.10.4

- Geometric mean: 1.460x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-vs-3.10.4.md)
- [📈time plot](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-vs-3.12.0.md)
- [📈time plot](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-vs-3.13.0.md)
- [📈time plot](bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4%2B-d3c54f3-vs-3.13.0.svg)

