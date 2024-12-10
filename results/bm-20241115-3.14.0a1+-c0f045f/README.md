# Results

- fork: python/c0f045f7fd3bb7ccf982
- version: 3.14.0a1+
- config: 
- commit hash: [c0f045f](https://github.com/python/cpython/commit/c0f045f)
- commit date: 2024-11-15T08:59:01+00:00
- commit merge base: [d9e251223e8314ca726fc0be8b834362184b0aad](https://github.com/python/cpython/commit/d9e251223e8314ca726fc0be8b834362184b0aad)
- ref: c0f045f7fd3bb7ccf982

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11861697962)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f.json)

### vs. 3.10.4

- Geometric mean: 1.401x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f-vs-3.10.4.md)
- [📈time plot](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f-vs-3.12.0.md)
- [📈time plot](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 79.16%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f-vs-3.13.0.md)
- [📈time plot](bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1%2B-c0f045f-vs-3.13.0.svg)

