# Results

- fork: brandtbucher/unbox
- version: 3.14.0a6+
- config: JIT
- commit hash: [1baa231](https://github.com/brandtbucher/cpython/commit/1baa231)
- commit date: 2025-04-01T14:00:50-07:00
- commit merge base: [00f0771e4dbd8c8b66b302ebc16bb21f5d46b304](https://github.com/python/cpython/commit/00f0771e4dbd8c8b66b302ebc16bb21f5d46b304)
- ref: unbox

## linux x86_64 (azure)

- [pystats raw](bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-pystats.json)
- [pystats table](bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-pystats.md)

### vs. base

- [pystats diff](bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14205953320)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231.json)

### vs. 3.10.4

- Geometric mean: 1.417x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-3.10.4.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.093x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-3.12.0.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 58.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-3.13.0.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.032x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-base-mem.svg)
- [📄table](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-base.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6%2B-1baa231-vs-base.svg)

