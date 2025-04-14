# Results

- fork: brandtbucher/compact_alt
- version: 3.14.0a4+
- config: JIT
- commit hash: [d1a7426](https://github.com/brandtbucher/cpython/commit/d1a7426)
- commit date: 2025-02-11T11:35:56-08:00
- commit merge base: [f72977b2f4a29063ae3019e50360f4af869f4149](https://github.com/python/cpython/commit/f72977b2f4a29063ae3019e50360f4af869f4149)
- ref: compact_alt

## linux x86_64 (azure)

- [pystats raw](bm-20250211-azure-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-pystats.json)
- [pystats table](bm-20250211-azure-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-pystats.md)

### vs. base

- [pystats diff](bm-20250211-azure-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271271258)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426.json)

### vs. 3.10.4

- Geometric mean: 1.410x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-3.10.4.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-3.12.0.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 80.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, pycparser, tornado_http
- [📄table](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-3.13.0.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pycparser
- [🧠memory plot](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-base-mem.svg)
- [📄table](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-base.md)
- [📈time plot](bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4%2B-d1a7426-vs-base.svg)

