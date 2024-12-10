# Results

- fork: python/30aeb00d367d0cc9e5a7
- version: 3.14.0a1+
- config: 
- commit hash: [30aeb00](https://github.com/python/cpython/commit/30aeb00)
- commit date: 2024-11-19T10:35:17+00:00
- commit merge base: [899fdb213db6c5881c5f9c6760ead6fd713d2070](https://github.com/python/cpython/commit/899fdb213db6c5881c5f9c6760ead6fd713d2070)
- ref: 30aeb00d367d0cc9e5a7

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11914363012)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00.json)

### vs. 3.10.4

- Geometric mean: 1.401x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00-vs-3.10.4.md)
- [📈time plot](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00-vs-3.12.0.md)
- [📈time plot](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 73.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00-vs-3.13.0.md)
- [📈time plot](bm-20241119-linux-x86_64-python-30aeb00d367d0cc9e5a7-3.14.0a1%2B-30aeb00-vs-3.13.0.svg)

