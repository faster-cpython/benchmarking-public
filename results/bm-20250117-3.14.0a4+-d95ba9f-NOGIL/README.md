# Results

- fork: python/d95ba9fa1110534b7247
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [d95ba9f](https://github.com/python/cpython/commit/d95ba9f)
- commit date: 2025-01-17T17:52:18+00:00
- commit merge base: [b5558cd63c62855ed43d66a55907f9d4398134e3](https://github.com/python/cpython/commit/b5558cd63c62855ed43d66a55907f9d4398134e3)
- ref: d95ba9fa1110534b7247

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12836103861)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f.json)

### vs. 3.10.4

- Geometric mean: 1.246x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.10.4.md)
- [📈time plot](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x slower (HPT: reliability of 99.89%, 1.01x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.12.0.md)
- [📈time plot](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.13.0.md)
- [📈time plot](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.137x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-base-mem.svg)
- [📄table](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-base.md)
- [📈time plot](bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-base.svg)

