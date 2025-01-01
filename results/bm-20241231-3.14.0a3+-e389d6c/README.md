# Results

- fork: python/e389d6c650ddacb55b08
- version: 3.14.0a3+
- config: 
- commit hash: [e389d6c](https://github.com/python/cpython/commit/e389d6c)
- commit date: 2024-12-31T19:10:06+05:30
- commit merge base: [b2ac70a62ad1be8e037ce45ccf5f1b753ea5e64b](https://github.com/python/cpython/commit/b2ac70a62ad1be8e037ce45ccf5f1b753ea5e64b)
- ref: e389d6c650ddacb55b08

## linux x86_64 (azure)

- [pystats raw](bm-20241231-azure-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-pystats.json)
- [pystats table](bm-20241231-azure-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12563796073)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-vs-3.10.4.md)
- [📈time plot](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-vs-3.12.0.md)
- [📈time plot](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-vs-3.13.0.md)
- [📈time plot](bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3%2B-e389d6c-vs-3.13.0.svg)

