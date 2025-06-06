# Results

- fork: brandtbucher/jit_unknown_syms
- version: 3.14.0a6+
- config: JIT
- commit hash: [88219fd](https://github.com/brandtbucher/cpython/commit/88219fd)
- commit date: 2025-03-19T12:16:59-07:00
- commit merge base: [fd545d735d5f9c048f99767c700f72853a9b7acd](https://github.com/python/cpython/commit/fd545d735d5f9c048f99767c700f72853a9b7acd)
- ref: jit_unknown_syms

## linux x86_64 (azure)

- [pystats raw](bm-20250319-azure-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-pystats.json)
- [pystats table](bm-20250319-azure-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-pystats.md)

### vs. base

- [pystats diff](bm-20250319-azure-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13954909592)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd.json)

### vs. 3.10.4

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-3.10.4.md)
- [📈time plot](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-3.12.0.md)
- [📈time plot](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-3.13.0.md)
- [📈time plot](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [🧠memory plot](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-base-mem.svg)
- [📄table](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-base.md)
- [📈time plot](bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6%2B-88219fd-vs-base.svg)

