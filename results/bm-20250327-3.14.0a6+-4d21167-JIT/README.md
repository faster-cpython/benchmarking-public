# Results

- fork: brandtbucher/jit_up_10_10
- version: 3.14.0a6+
- config: JIT
- commit hash: [4d21167](https://github.com/brandtbucher/cpython/commit/4d21167)
- commit date: 2025-03-27T21:32:58-07:00
- commit merge base: [a1232459860235f4fb7896cc95966d87a51cbe32](https://github.com/python/cpython/commit/a1232459860235f4fb7896cc95966d87a51cbe32)
- ref: jit_up_10_10

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14122048519)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167.json)

### vs. 3.10.4

- Geometric mean: 1.430x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-3.10.4.md)
- [📈time plot](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-3.12.0.md)
- [📈time plot](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 94.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-3.13.0.md)
- [📈time plot](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 99.71%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-base-mem.svg)
- [📄table](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-base.md)
- [📈time plot](bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6%2B-4d21167-vs-base.svg)

