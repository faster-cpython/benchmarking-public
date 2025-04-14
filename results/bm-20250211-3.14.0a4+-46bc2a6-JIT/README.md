# Results

- fork: brandtbucher/for_iter_dict_items
- version: 3.14.0a4+
- config: JIT
- commit hash: [46bc2a6](https://github.com/brandtbucher/cpython/commit/46bc2a6)
- commit date: 2025-02-11T16:35:07-08:00
- commit merge base: [f72977b2f4a29063ae3019e50360f4af869f4149](https://github.com/python/cpython/commit/f72977b2f4a29063ae3019e50360f4af869f4149)
- ref: for_iter_dict_items

## linux x86_64 (azure)

- [pystats raw](bm-20250211-azure-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-pystats.json)
- [pystats table](bm-20250211-azure-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-pystats.md)

### vs. base

- [pystats diff](bm-20250211-azure-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13276944029)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6.json)

### vs. 3.10.4

- Geometric mean: 1.446x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-3.10.4.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-3.12.0.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-3.13.0.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 61.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-base-mem.svg)
- [📄table](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-base.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4%2B-46bc2a6-vs-base.svg)

