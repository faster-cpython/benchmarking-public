# Results

- fork: iritkatriel/binary_subscr_to_op
- version: 3.14.0a4+
- config: 
- commit hash: [dda3d1f](https://github.com/iritkatriel/cpython/commit/dda3d1f)
- commit date: 2025-02-06T15:15:27+00:00
- commit merge base: [cdcacec79f7a216c3c988baa4dc31ce4e76c97ac](https://github.com/python/cpython/commit/cdcacec79f7a216c3c988baa4dc31ce4e76c97ac)
- ref: binary_subscr_to_op

## linux x86_64 (azure)

- [pystats raw](bm-20250206-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-pystats.json)
- [pystats table](bm-20250206-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-pystats.md)

### vs. base

- [pystats diff](bm-20250206-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13181958329)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f.json)

### vs. 3.10.4

- Geometric mean: 1.461x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-3.10.4.md)
- [📈time plot](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-3.12.0.md)
- [📈time plot](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-3.13.0.md)
- [📈time plot](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 74.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-base-mem.svg)
- [📄table](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-base.md)
- [📈time plot](bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-dda3d1f-vs-base.svg)

