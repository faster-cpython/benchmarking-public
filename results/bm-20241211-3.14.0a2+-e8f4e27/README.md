# Results

- fork: python/e8f4e272cc828f2b79fa
- version: 3.14.0a2+
- config: 
- commit hash: [e8f4e27](https://github.com/python/cpython/commit/e8f4e27)
- commit date: 2024-12-11T19:32:54+01:00
- commit merge base: [bc262de06b10a2d119c28bac75060bf00301697a](https://github.com/python/cpython/commit/bc262de06b10a2d119c28bac75060bf00301697a)
- ref: e8f4e272cc828f2b79fa

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12282375165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27.json)

### vs. 3.10.4

- Geometric mean: 1.425x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27-vs-3.10.4.md)
- [📈time plot](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27-vs-3.12.0.md)
- [📈time plot](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27-vs-3.13.0.md)
- [📈time plot](bm-20241211-linux-x86_64-python-e8f4e272cc828f2b79fa-3.14.0a2%2B-e8f4e27-vs-3.13.0.svg)

