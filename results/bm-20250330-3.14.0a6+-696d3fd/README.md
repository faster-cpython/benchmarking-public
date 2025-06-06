# Results

- fork: brandtbucher/unbox
- version: 3.14.0a6+
- config: 
- commit hash: [696d3fd](https://github.com/brandtbucher/cpython/commit/696d3fd)
- commit date: 2025-03-30T11:33:33-07:00
- commit merge base: [00f0771e4dbd8c8b66b302ebc16bb21f5d46b304](https://github.com/python/cpython/commit/00f0771e4dbd8c8b66b302ebc16bb21f5d46b304)
- ref: unbox

## linux x86_64 (azure)

- [pystats raw](bm-20250330-azure-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-pystats.json)
- [pystats table](bm-20250330-azure-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-pystats.md)

### vs. base

- [pystats diff](bm-20250330-azure-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14162635393)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd.json)

### vs. 3.10.4

- Geometric mean: 1.403x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 2.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-3.10.4.md)
- [📈time plot](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 2.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-3.12.0.md)
- [📈time plot](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 62.45%, 1.00x slower at 99th %ile)
- Memory usage: 1.80x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-3.13.0.md)
- [📈time plot](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.032x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.99x
- [🧠memory plot](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-base-mem.svg)
- [📄table](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-base.md)
- [📈time plot](bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-696d3fd-vs-base.svg)

