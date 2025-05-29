# Results

- fork: brandtbucher/yes_underflow
- version: 3.14.0a4+
- config: JIT
- commit hash: [4112331](https://github.com/brandtbucher/cpython/commit/4112331)
- commit date: 2025-02-14T13:56:14-08:00
- commit merge base: [bb5c6875d6e84bf2b4e134ed482141a51d223f09](https://github.com/python/cpython/commit/bb5c6875d6e84bf2b4e134ed482141a51d223f09)
- ref: yes_underflow

## linux x86_64 (azure)

- [pystats raw](bm-20250214-azure-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-pystats.json)
- [pystats table](bm-20250214-azure-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-pystats.md)

### vs. base

- [pystats diff](bm-20250214-azure-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13338178705)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-3.10.4.md)
- [📈time plot](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-3.12.0.md)
- [📈time plot](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 60.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-3.13.0.md)
- [📈time plot](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.026x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-base-mem.svg)
- [📄table](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-base.md)
- [📈time plot](bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4%2B-4112331-vs-base.svg)

