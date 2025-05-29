# Results vs. base

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-x86
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.001x faster
- HPT reliability: 78.07%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 235 ms                                                                          | 229 ms: 1.03x faster                                                                  |
| html5lib       | 40.9 ms                                                                         | 41.3 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 441 ms                                                                          | 436 ms: 1.01x faster                                                                  |
| async_generators        | 233 ms                                                                          | 231 ms: 1.01x faster                                                                  |
| async_tree_none         | 174 ms                                                                          | 172 ms: 1.01x faster                                                                  |
| Geometric mean          | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, coroutines, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 46.3 ms                                                                         | 45.8 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 88.8 ms                                                                         | 88.5 ms: 1.00x faster                                                                 |
| regex_effbot   | 1.93 ms                                                                         | 1.92 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 154 us                                                                          | 153 us: 1.00x faster                                                                  |
| xml_etree_parse      | 113 ms                                                                          | 114 ms: 1.01x slower                                                                  |
| xml_etree_iterparse  | 72.6 ms                                                                         | 73.1 ms: 1.01x slower                                                                 |
| tomli_loads          | 1.39 sec                                                                        | 1.41 sec: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                           | 1.00x slower                                                                          |

Benchmark hidden because not significant (5): pickle_pure_python, json_loads, xml_etree_generate, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 36.3 ms                                                                         | 36.0 ms: 1.01x faster                                                                 |
| genshi_text     | 16.1 ms                                                                         | 16.0 ms: 1.00x faster                                                                 |
| django_template | 27.0 ms                                                                         | 27.3 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                           | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|--------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| bench_thread_pool        | 1.32 ms                                                                         | 1.18 ms: 1.12x faster                                                                 |
| many_optionals           | 489 us                                                                          | 471 us: 1.04x faster                                                                  |
| 2to3                     | 235 ms                                                                          | 229 ms: 1.03x faster                                                                  |
| subparsers               | 18.8 ms                                                                         | 18.3 ms: 1.02x faster                                                                 |
| pprint_safe_repr         | 532 ms                                                                          | 525 ms: 1.01x faster                                                                  |
| telco                    | 5.98 ms                                                                         | 5.90 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed  | 441 ms                                                                          | 436 ms: 1.01x faster                                                                  |
| float                    | 46.3 ms                                                                         | 45.8 ms: 1.01x faster                                                                 |
| deepcopy_reduce          | 1.94 us                                                                         | 1.92 us: 1.01x faster                                                                 |
| async_generators         | 233 ms                                                                          | 231 ms: 1.01x faster                                                                  |
| fannkuch                 | 280 ms                                                                          | 277 ms: 1.01x faster                                                                  |
| typing_runtime_protocols | 124 us                                                                          | 122 us: 1.01x faster                                                                  |
| async_tree_none          | 174 ms                                                                          | 172 ms: 1.01x faster                                                                  |
| gc_traversal             | 2.45 ms                                                                         | 2.43 ms: 1.01x faster                                                                 |
| genshi_xml               | 36.3 ms                                                                         | 36.0 ms: 1.01x faster                                                                 |
| unpickle_pure_python     | 154 us                                                                          | 153 us: 1.00x faster                                                                  |
| regex_compile            | 88.8 ms                                                                         | 88.5 ms: 1.00x faster                                                                 |
| genshi_text              | 16.1 ms                                                                         | 16.0 ms: 1.00x faster                                                                 |
| regex_effbot             | 1.93 ms                                                                         | 1.92 ms: 1.00x faster                                                                 |
| bpe_tokeniser            | 3.29 sec                                                                        | 3.30 sec: 1.00x slower                                                                |
| crypto_pyaes             | 58.4 ms                                                                         | 58.6 ms: 1.00x slower                                                                 |
| mdp                      | 1.79 sec                                                                        | 1.79 sec: 1.00x slower                                                                |
| richards_super           | 36.0 ms                                                                         | 36.2 ms: 1.01x slower                                                                 |
| xml_etree_parse          | 113 ms                                                                          | 114 ms: 1.01x slower                                                                  |
| xml_etree_iterparse      | 72.6 ms                                                                         | 73.1 ms: 1.01x slower                                                                 |
| logging_simple           | 7.10 us                                                                         | 7.16 us: 1.01x slower                                                                 |
| tomli_loads              | 1.39 sec                                                                        | 1.41 sec: 1.01x slower                                                                |
| html5lib                 | 40.9 ms                                                                         | 41.3 ms: 1.01x slower                                                                 |
| django_template          | 27.0 ms                                                                         | 27.3 ms: 1.01x slower                                                                 |
| deepcopy                 | 187 us                                                                          | 190 us: 1.01x slower                                                                  |
| richards                 | 32.0 ms                                                                         | 32.5 ms: 1.01x slower                                                                 |
| shortest_path            | 279 ms                                                                          | 283 ms: 1.02x slower                                                                  |
| Geometric mean           | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (62): spectral_norm, pickle_pure_python, connected_components, deltablue, scimark_fft, pycparser, async_tree_none_tg, k_core, bench_mp_pool, coverage, sqlglot_parse, sympy_sum, sqlglot_normalize, python_startup, json_loads, sympy_expand, sympy_integrate, create_gc_cycles, sqlite_synth, comprehensions, logging_silent, nbody, async_tree_memoization, xml_etree_generate, scimark_lu, coroutines, scimark_sor, scimark_sparse_mat_mult, scimark_monte_carlo, pyflate, logging_format, dulwich_log, docutils, deepcopy_memo, sqlglot_transpile, python_startup_no_site, regex_dna, generators, nqueens, pidigits, meteor_contest, pprint_pformat, raytrace, sympy_str, regex_v8, xml_etree_process, sphinx, asyncio_websockets, go, async_tree_cpu_io_mixed_tg, json_dumps, hexiom, pylint, async_tree_io_tg, chaos, sqlglot_optimize, mako, json, thrift, async_tree_io, async_tree_memoization_tg, pathlib
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 78.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown