# Results

- fork: python/27494dd9ad6032c29e27
- version: 3.14.0a4+
- config: 
- commit hash: [27494dd](https://github.com/python/cpython/commit/27494dd)
- commit date: 2025-01-16T13:29:16-08:00
- commit merge base: [211f41316b7f205d18eb65c1ececd7f7fb30b02d](https://github.com/python/cpython/commit/211f41316b7f205d18eb65c1ececd7f7fb30b02d)
- ref: 27494dd9ad6032c29e27

## linux x86_64 (azure)

- [pystats raw](bm-20250116-azure-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-pystats.json)
- [pystats table](bm-20250116-azure-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12819104357)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd.json)

### vs. 3.10.4

- Geometric mean: 1.448x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.10.4.md)
- [📈time plot](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.12.0.md)
- [📈time plot](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.13.0.md)
- [📈time plot](bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.13.0.svg)

