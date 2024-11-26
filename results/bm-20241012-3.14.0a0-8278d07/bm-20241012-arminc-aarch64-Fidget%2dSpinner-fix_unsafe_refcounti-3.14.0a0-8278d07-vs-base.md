# Results vs. base

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-aarch64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.002x faster
- HPT reliability: 98.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 722 ms                                                                  | 709 ms: 1.02x faster                                                              |
| asyncio_tcp_ssl         | 2.21 sec                                                                | 2.20 sec: 1.01x faster                                                            |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (11): async_tree_none, async_tree_io_tg, async_tree_io, async_tree_none_tg, asyncio_tcp, async_generators, coroutines, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 94.6 ms                                                                 | 93.9 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 260 ms                                                                  | 254 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 198 ms                                                                  | 187 ms: 1.06x faster                                                              |
| xml_etree_iterparse | 153 ms                                                                  | 146 ms: 1.04x faster                                                              |
| pickle              | 13.9 us                                                                 | 13.6 us: 1.03x faster                                                             |
| pickle_pure_python  | 364 us                                                                  | 358 us: 1.02x faster                                                              |
| pickle_list         | 5.17 us                                                                 | 5.23 us: 1.01x slower                                                             |
| Geometric mean      | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (9): xml_etree_process, unpickle_list, unpickle_pure_python, json_loads, xml_etree_generate, pickle_dict, tomli_loads, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.68 ms                                                                 | 8.61 ms: 1.01x faster                                                             |
| python_startup         | 13.0 ms                                                                 | 13.0 ms: 1.00x faster                                                             |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.6 ms                                                                 | 13.6 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse         | 198 ms                                                                  | 187 ms: 1.06x faster                                                              |
| xml_etree_iterparse     | 153 ms                                                                  | 146 ms: 1.04x faster                                                              |
| scimark_monte_carlo     | 84.5 ms                                                                 | 82.3 ms: 1.03x faster                                                             |
| pickle                  | 13.9 us                                                                 | 13.6 us: 1.03x faster                                                             |
| scimark_sparse_mat_mult | 6.60 ms                                                                 | 6.44 ms: 1.02x faster                                                             |
| regex_dna               | 260 ms                                                                  | 254 ms: 1.02x faster                                                              |
| scimark_fft             | 441 ms                                                                  | 432 ms: 1.02x faster                                                              |
| scimark_sor             | 161 ms                                                                  | 158 ms: 1.02x faster                                                              |
| pickle_pure_python      | 364 us                                                                  | 358 us: 1.02x faster                                                              |
| async_tree_cpu_io_mixed | 722 ms                                                                  | 709 ms: 1.02x faster                                                              |
| fannkuch                | 471 ms                                                                  | 464 ms: 1.02x faster                                                              |
| chaos                   | 70.5 ms                                                                 | 69.6 ms: 1.01x faster                                                             |
| hexiom                  | 7.11 ms                                                                 | 7.03 ms: 1.01x faster                                                             |
| python_startup_no_site  | 8.68 ms                                                                 | 8.61 ms: 1.01x faster                                                             |
| float                   | 94.6 ms                                                                 | 93.9 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl         | 2.21 sec                                                                | 2.20 sec: 1.01x faster                                                            |
| python_startup          | 13.0 ms                                                                 | 13.0 ms: 1.00x faster                                                             |
| mako                    | 13.6 ms                                                                 | 13.6 ms: 1.01x slower                                                             |
| sqlite_synth            | 3.90 us                                                                 | 3.95 us: 1.01x slower                                                             |
| pickle_list             | 5.17 us                                                                 | 5.23 us: 1.01x slower                                                             |
| json                    | 5.57 ms                                                                 | 5.69 ms: 1.02x slower                                                             |
| dulwich_log             | 58.0 ms                                                                 | 59.3 ms: 1.02x slower                                                             |
| logging_format          | 7.55 us                                                                 | 7.72 us: 1.02x slower                                                             |
| gc_traversal            | 5.09 ms                                                                 | 5.22 ms: 1.03x slower                                                             |
| logging_simple          | 6.96 us                                                                 | 7.19 us: 1.03x slower                                                             |
| unpack_sequence         | 51.2 ns                                                                 | 55.8 ns: 1.09x slower                                                             |
| Geometric mean          | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (71): html5lib, deepcopy_reduce, async_tree_none, sqlglot_parse, async_tree_io_tg, xml_etree_process, richards_super, typing_runtime_protocols, nbody, async_tree_io, sqlglot_transpile, regex_effbot, richards, meteor_contest, sympy_sum, deepcopy, thrift, nqueens, async_tree_none_tg, unpickle_list, sympy_integrate, pprint_pformat, pprint_safe_repr, pyflate, generators, sympy_str, spectral_norm, asyncio_tcp, unpickle_pure_python, json_loads, crypto_pyaes, regex_v8, docutils, bpe_tokeniser, sqlglot_optimize, xml_etree_generate, async_generators, pycparser, coroutines, sympy_expand, pidigits, coverage, scimark_lu, tornado_http, pickle_dict, async_tree_memoization, mdp, deltablue, comprehensions, tomli_loads, asyncio_websockets, 2to3, bench_thread_pool, async_tree_cpu_io_mixed_tg, pylint, telco, django_template, genshi_text, create_gc_cycles, json_dumps, regex_compile, raytrace, deepcopy_memo, pathlib, go, sqlglot_normalize, async_tree_memoization_tg, logging_silent, unpickle, genshi_xml, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 98.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x