# Results

- fork: brandtbucher/jit_peephole
- version: 3.14.0a7+
- config: JIT
- commit hash: [edb68e1](https://github.com/brandtbucher/cpython/commit/edb68e1)
- commit date: 2025-04-08T14:16:39-07:00
- commit merge base: [8421b648e91981e393a740dd9fb7b7dbf4cf07dc](https://github.com/python/cpython/commit/8421b648e91981e393a740dd9fb7b7dbf4cf07dc)
- ref: jit_peephole

## linux x86_64 (azure)

- [pystats raw](bm-20250408-azure-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-pystats.json)
- [pystats table](bm-20250408-azure-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-pystats.md)

### vs. base

- [pystats diff](bm-20250408-azure-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14343794442)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1.json)

### vs. 3.10.4

- Geometric mean: 1.476x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-3.10.4.md)
- [📈time plot](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.138x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-3.12.0.md)
- [📈time plot](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-3.13.0.md)
- [📈time plot](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 93.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-base-mem.svg)
- [📄table](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-base.md)
- [📈time plot](bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7%2B-edb68e1-vs-base.svg)

