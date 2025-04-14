# Results

- fork: brandtbucher/trace_load_attr_prop
- version: 3.14.0a4+
- config: JIT
- commit hash: [9b7a6a6](https://github.com/brandtbucher/cpython/commit/9b7a6a6)
- commit date: 2025-02-07T14:01:22-08:00
- commit merge base: [5fa7e1b7fd57e8c6297e9eb79d79cede42e5ce0f](https://github.com/python/cpython/commit/5fa7e1b7fd57e8c6297e9eb79d79cede42e5ce0f)
- ref: trace_load_attr_prop

## linux x86_64 (azure)

- [pystats raw](bm-20250207-azure-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-pystats.json)
- [pystats table](bm-20250207-azure-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-pystats.md)

### vs. base

- [pystats diff](bm-20250207-azure-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13210442412)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6.json)

### vs. 3.10.4

- Geometric mean: 1.447x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-3.10.4.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-3.12.0.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-3.13.0.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 68.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-base-mem.svg)
- [📄table](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-base.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4%2B-9b7a6a6-vs-base.svg)

