# Results

- fork: iritkatriel/binary_subscr_to_op
- version: 3.14.0a4+
- config: 
- commit hash: [0474adc](https://github.com/iritkatriel/cpython/commit/0474adc)
- commit date: 2025-02-03T23:44:01+00:00
- commit merge base: [5ab9604683a58e613c6eba309ed89ed2092e3e2d](https://github.com/python/cpython/commit/5ab9604683a58e613c6eba309ed89ed2092e3e2d)
- ref: binary_subscr_to_op

## linux x86_64 (azure)

- [pystats raw](bm-20250203-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-pystats.json)
- [pystats table](bm-20250203-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-pystats.md)

### vs. base

- [pystats diff](bm-20250203-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13125128215)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc.json)

### vs. 3.10.4

- Geometric mean: 1.457x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-3.10.4.md)
- [📈time plot](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-3.12.0.md)
- [📈time plot](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-3.13.0.md)
- [📈time plot](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-base-mem.svg)
- [📄table](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-base.md)
- [📈time plot](bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-0474adc-vs-base.svg)

