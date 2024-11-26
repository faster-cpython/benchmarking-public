# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.005x slower
- HPT reliability: 76.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tornado_http   | 145 ms                                                                   | 148 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|---------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg        | 458 ms                                                                   | 442 ms: 1.04x faster                                                        |
| async_tree_memoization    | 608 ms                                                                   | 595 ms: 1.02x faster                                                        |
| async_tree_memoization_tg | 546 ms                                                                   | 535 ms: 1.02x faster                                                        |
| async_tree_none           | 474 ms                                                                   | 465 ms: 1.02x faster                                                        |
| async_tree_io_tg          | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                      |
| Geometric mean            | (ref)                                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (6): async_tree_io, async_tree_cpu_io_mixed_tg, coroutines, async_generators, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 115 ms                                                                   | 119 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.1 ms                                                                  | 30.9 ms: 1.04x faster                                                       |
| regex_dna      | 249 ms                                                                   | 251 ms: 1.01x slower                                                        |
| regex_compile  | 173 ms                                                                   | 176 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python | 400 us                                                                   | 387 us: 1.03x faster                                                        |
| xml_etree_parse    | 190 ms                                                                   | 186 ms: 1.02x faster                                                        |
| xml_etree_generate | 113 ms                                                                   | 111 ms: 1.01x faster                                                        |
| xml_etree_process  | 81.8 ms                                                                  | 80.9 ms: 1.01x faster                                                       |
| tomli_loads        | 2.62 sec                                                                 | 2.67 sec: 1.02x slower                                                      |
| Geometric mean     | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.5 ms                                                                  | 14.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.68 ms                                                                  | 8.77 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.9 ms                                                                  | 52.3 ms: 1.03x slower                                                       |
| mako            | 13.3 ms                                                                  | 13.7 ms: 1.03x slower                                                       |
| genshi_xml      | 81.8 ms                                                                  | 84.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                    | 1.03x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|---------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8                  | 32.1 ms                                                                  | 30.9 ms: 1.04x faster                                                       |
| pathlib                   | 22.1 ms                                                                  | 21.3 ms: 1.04x faster                                                       |
| async_tree_none_tg        | 458 ms                                                                   | 442 ms: 1.04x faster                                                        |
| pickle_pure_python        | 400 us                                                                   | 387 us: 1.03x faster                                                        |
| async_tree_memoization    | 608 ms                                                                   | 595 ms: 1.02x faster                                                        |
| gc_traversal              | 6.39 ms                                                                  | 6.26 ms: 1.02x faster                                                       |
| async_tree_memoization_tg | 546 ms                                                                   | 535 ms: 1.02x faster                                                        |
| async_tree_none           | 474 ms                                                                   | 465 ms: 1.02x faster                                                        |
| xml_etree_parse           | 190 ms                                                                   | 186 ms: 1.02x faster                                                        |
| thrift                    | 979 us                                                                   | 963 us: 1.02x faster                                                        |
| xml_etree_generate        | 113 ms                                                                   | 111 ms: 1.01x faster                                                        |
| generators                | 59.0 ms                                                                  | 58.3 ms: 1.01x faster                                                       |
| xml_etree_process         | 81.8 ms                                                                  | 80.9 ms: 1.01x faster                                                       |
| async_tree_io_tg          | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                      |
| scimark_fft               | 455 ms                                                                   | 450 ms: 1.01x faster                                                        |
| regex_dna                 | 249 ms                                                                   | 251 ms: 1.01x slower                                                        |
| python_startup            | 14.5 ms                                                                  | 14.6 ms: 1.01x slower                                                       |
| sympy_expand              | 584 ms                                                                   | 590 ms: 1.01x slower                                                        |
| python_startup_no_site    | 8.68 ms                                                                  | 8.77 ms: 1.01x slower                                                       |
| sqlglot_normalize         | 155 ms                                                                   | 156 ms: 1.01x slower                                                        |
| create_gc_cycles          | 3.61 ms                                                                  | 3.65 ms: 1.01x slower                                                       |
| sqlalchemy_declarative    | 186 ms                                                                   | 188 ms: 1.01x slower                                                        |
| regex_compile             | 173 ms                                                                   | 176 ms: 1.01x slower                                                        |
| fannkuch                  | 503 ms                                                                   | 510 ms: 1.02x slower                                                        |
| go                        | 182 ms                                                                   | 185 ms: 1.02x slower                                                        |
| bpe_tokeniser             | 5.95 sec                                                                 | 6.04 sec: 1.02x slower                                                      |
| sqlglot_parse             | 1.70 ms                                                                  | 1.73 ms: 1.02x slower                                                       |
| tomli_loads               | 2.62 sec                                                                 | 2.67 sec: 1.02x slower                                                      |
| pprint_safe_repr          | 1.21 sec                                                                 | 1.23 sec: 1.02x slower                                                      |
| tornado_http              | 145 ms                                                                   | 148 ms: 1.02x slower                                                        |
| dulwich_log               | 76.7 ms                                                                  | 78.8 ms: 1.03x slower                                                       |
| django_template           | 50.9 ms                                                                  | 52.3 ms: 1.03x slower                                                       |
| mako                      | 13.3 ms                                                                  | 13.7 ms: 1.03x slower                                                       |
| hexiom                    | 10.2 ms                                                                  | 10.5 ms: 1.03x slower                                                       |
| pprint_pformat            | 2.52 sec                                                                 | 2.61 sec: 1.03x slower                                                      |
| genshi_xml                | 81.8 ms                                                                  | 84.5 ms: 1.03x slower                                                       |
| nbody                     | 115 ms                                                                   | 119 ms: 1.03x slower                                                        |
| chaos                     | 85.4 ms                                                                  | 88.3 ms: 1.03x slower                                                       |
| crypto_pyaes              | 88.7 ms                                                                  | 92.0 ms: 1.04x slower                                                       |
| telco                     | 9.29 ms                                                                  | 9.67 ms: 1.04x slower                                                       |
| scimark_sor               | 157 ms                                                                   | 164 ms: 1.04x slower                                                        |
| nqueens                   | 126 ms                                                                   | 132 ms: 1.05x slower                                                        |
| sqlalchemy_imperative     | 18.2 ms                                                                  | 19.2 ms: 1.05x slower                                                       |
| pyflate                   | 612 ms                                                                   | 645 ms: 1.05x slower                                                        |
| Geometric mean            | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (47): bench_mp_pool, async_tree_io, json, async_tree_cpu_io_mixed_tg, coroutines, scimark_lu, async_generators, sympy_str, json_dumps, deepcopy_memo, sphinx, async_tree_cpu_io_mixed, pycparser, unpickle_pure_python, asyncio_websockets, html5lib, mdp, deltablue, meteor_contest, float, xml_etree_iterparse, raytrace, regex_effbot, logging_silent, sympy_integrate, pylint, coverage, sqlglot_optimize, deepcopy, scimark_sparse_mat_mult, 2to3, deepcopy_reduce, richards_super, json_loads, logging_format, pidigits, bench_thread_pool, logging_simple, spectral_norm, scimark_monte_carlo, docutils, sympy_sum, comprehensions, typing_runtime_protocols, genshi_text, richards, sqlglot_transpile

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 76.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x