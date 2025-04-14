# Results

- fork: python/a3d5aab9a89e311cded9
- version: 3.14.0a4+
- config: 
- commit hash: [a3d5aab](https://github.com/python/cpython/commit/a3d5aab)
- commit date: 2025-02-07T12:06:11+01:00
- commit merge base: [ae132edc296d27c6ed04fe4d400c67e3cfb622e8](https://github.com/python/cpython/commit/ae132edc296d27c6ed04fe4d400c67e3cfb622e8)
- ref: a3d5aab9a89e311cded9

## linux x86_64 (azure)

- [pystats raw](bm-20250207-azure-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-pystats.json)
- [pystats table](bm-20250207-azure-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13199187682)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab.json)

### vs. 3.10.4

- Geometric mean: 1.457x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-vs-3.10.4.md)
- [📈time plot](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-vs-3.12.0.md)
- [📈time plot](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-vs-3.13.0.md)
- [📈time plot](bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4%2B-a3d5aab-vs-3.13.0.svg)

