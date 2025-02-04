# Results

- fork: iritkatriel/binary_subscr_to_op
- version: 3.14.0a4+
- config: 
- commit hash: [a12fd2e](https://github.com/iritkatriel/cpython/commit/a12fd2e)
- commit date: 2025-02-04T13:57:55+00:00
- commit merge base: [d3c54f37889436ded4520e78e4e59d3f3350aa44](https://github.com/python/cpython/commit/d3c54f37889436ded4520e78e4e59d3f3350aa44)
- ref: binary_subscr_to_op

## linux x86_64 (azure)

- [pystats raw](bm-20250204-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-pystats.json)
- [pystats table](bm-20250204-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-pystats.md)

### vs. base

- [pystats diff](bm-20250204-azure-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13137089910)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e.json)

### vs. 3.10.4

- Geometric mean: 1.459x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-3.10.4.md)
- [📈time plot](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-3.12.0.md)
- [📈time plot](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-3.13.0.md)
- [📈time plot](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 78.31%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-base-mem.svg)
- [📄table](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-base.md)
- [📈time plot](bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4%2B-a12fd2e-vs-base.svg)

