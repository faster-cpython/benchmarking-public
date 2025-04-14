# Results

- fork: python/f0f7b978be84c432139d
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [f0f7b97](https://github.com/python/cpython/commit/f0f7b97)
- commit date: 2025-01-20T15:49:15+00:00
- commit merge base: [e1fa2fcc7c1bf5291a7f71300b7828b49be9ab72](https://github.com/python/cpython/commit/e1fa2fcc7c1bf5291a7f71300b7828b49be9ab72)
- ref: f0f7b978be84c432139d

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12914042474)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97.json)

### vs. 3.10.4

- Geometric mean: 1.238x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97-vs-3.10.4.md)
- [📈time plot](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x slower (HPT: reliability of 99.96%, 1.02x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97-vs-3.12.0.md)
- [📈time plot](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.097x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97-vs-3.13.0.md)
- [📈time plot](bm-20250120-linux-x86_64-python-f0f7b978be84c432139d-3.14.0a4%2B-f0f7b97-vs-3.13.0.svg)

