# Results

- fork: python/128cc47fbd44e3e09c50
- version: 3.14.0a3+
- config: 
- commit hash: [128cc47](https://github.com/python/cpython/commit/128cc47)
- commit date: 2024-12-20T16:52:20+00:00
- commit merge base: [78ffba4221dcb2e39fd5db80c297d1777588bb59](https://github.com/python/cpython/commit/78ffba4221dcb2e39fd5db80c297d1777588bb59)
- ref: 128cc47fbd44e3e09c50

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12436085426)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47-vs-3.10.4.md)
- [📈time plot](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47-vs-3.12.0.md)
- [📈time plot](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47-vs-3.13.0.md)
- [📈time plot](bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3%2B-128cc47-vs-3.13.0.svg)

