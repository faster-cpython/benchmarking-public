# Results

- fork: iritkatriel/cmq
- version: 3.14.0a3+
- config: 
- commit hash: [82b084a](https://github.com/iritkatriel/cpython/commit/82b084a)
- commit date: 2025-01-09T19:15:25+00:00
- commit merge base: [004f9fd1f22643100aa8163cc9f7bcde7df54973](https://github.com/python/cpython/commit/004f9fd1f22643100aa8163cc9f7bcde7df54973)
- ref: cmq

## linux x86_64 (azure)

- [pystats raw](bm-20250109-azure-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-pystats.json)
- [pystats table](bm-20250109-azure-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-pystats.md)

### vs. base

- [pystats diff](bm-20250109-azure-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696973549)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a.json)

### vs. 3.10.4

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-3.10.4.md)
- [📈time plot](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.115x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-3.12.0.md)
- [📈time plot](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-3.13.0.md)
- [📈time plot](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 57.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-base-mem.svg)
- [📄table](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-base.md)
- [📈time plot](bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3%2B-82b084a-vs-base.svg)

