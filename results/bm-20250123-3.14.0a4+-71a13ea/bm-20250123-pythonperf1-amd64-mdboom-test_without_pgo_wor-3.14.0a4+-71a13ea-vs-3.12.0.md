# Results vs. 3.12.0

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-amd64
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.081x slower
- HPT reliability: 84.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'math':
===========================

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody     | 71.9 ms                                                     | 78.5 ms: 1.09x slower                                                       |

All benchmarks:
===============

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody     | 71.9 ms                                                     | 78.5 ms: 1.09x slower                                                       |
Ignored benchmarks (95) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, go, hexiom, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process

- Geometric mean (including insignificant results): 1.081x slower

# HPT report

- Reliability score: 84.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown