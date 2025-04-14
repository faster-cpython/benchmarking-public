# Results

- fork: iritkatriel/binaryops
- version: 3.14.0a4+
- config: 
- commit hash: [c57fe46](https://github.com/iritkatriel/cpython/commit/c57fe46)
- commit date: 2025-01-16T22:55:52+00:00
- commit merge base: [27494dd9ad6032c29e273cd7f45c204c00d6512c](https://github.com/python/cpython/commit/27494dd9ad6032c29e273cd7f45c204c00d6512c)
- ref: binaryops

## linux x86_64 (azure)

- [pystats raw](bm-20250116-azure-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-pystats.json)
- [pystats table](bm-20250116-azure-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-pystats.md)

### vs. base

- [pystats diff](bm-20250116-azure-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12819104357)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46.json)

### vs. 3.10.4

- Geometric mean: 1.442x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.10.4.md)
- [📈time plot](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.12.0.md)
- [📈time plot](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.13.0.md)
- [📈time plot](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-base-mem.svg)
- [📄table](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-base.md)
- [📈time plot](bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-base.svg)

