# Results vs. base

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-amd64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.002x faster
- HPT reliability: 97.94%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| html5lib       | 38.8 ms                                                                     | 39.1 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 168 ms                                                                      | 166 ms: 1.01x faster                                                              |
| async_tree_none            | 175 ms                                                                      | 173 ms: 1.01x faster                                                              |
| async_tree_memoization     | 205 ms                                                                      | 203 ms: 1.01x faster                                                              |
| coroutines                 | 13.0 ms                                                                     | 13.1 ms: 1.01x slower                                                             |
| asyncio_websockets         | 311 ms                                                                      | 313 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed_tg | 359 ms                                                                      | 363 ms: 1.01x slower                                                              |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                      |

Benchmark hidden because not significant (5): async_tree_io, async_generators, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 44.4 ms                                                                     | 43.6 ms: 1.02x faster                                                             |
| pidigits       | 154 ms                                                                      | 155 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 84.2 ms                                                                     | 83.3 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_process    | 45.1 ms                                                                     | 44.5 ms: 1.01x faster                                                             |
| unpickle_pure_python | 147 us                                                                      | 146 us: 1.01x faster                                                              |
| json_loads           | 19.5 us                                                                     | 19.7 us: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): xml_etree_parse, json_dumps, tomli_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                     | 19.8 ms: 1.02x slower                                                             |
| python_startup         | 25.8 ms                                                                     | 26.9 ms: 1.04x slower                                                             |
| Geometric mean         | (ref)                                                                       | 1.03x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 14.7 ms                                                                     | 14.5 ms: 1.01x faster                                                             |
| genshi_xml     | 31.8 ms                                                                     | 32.0 ms: 1.01x slower                                                             |
| mako           | 7.32 ms                                                                     | 7.58 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| logging_silent             | 60.0 ns                                                                     | 56.6 ns: 1.06x faster                                                             |
| spectral_norm              | 58.4 ms                                                                     | 56.4 ms: 1.04x faster                                                             |
| scimark_sor                | 69.2 ms                                                                     | 67.2 ms: 1.03x faster                                                             |
| hexiom                     | 3.98 ms                                                                     | 3.87 ms: 1.03x faster                                                             |
| deltablue                  | 1.84 ms                                                                     | 1.79 ms: 1.03x faster                                                             |
| crypto_pyaes               | 52.0 ms                                                                     | 50.7 ms: 1.03x faster                                                             |
| scimark_sparse_mat_mult    | 2.55 ms                                                                     | 2.49 ms: 1.02x faster                                                             |
| mdp                        | 1.65 sec                                                                    | 1.61 sec: 1.02x faster                                                            |
| go                         | 71.6 ms                                                                     | 70.3 ms: 1.02x faster                                                             |
| fannkuch                   | 277 ms                                                                      | 272 ms: 1.02x faster                                                              |
| float                      | 44.4 ms                                                                     | 43.6 ms: 1.02x faster                                                             |
| meteor_contest             | 73.3 ms                                                                     | 72.1 ms: 1.02x faster                                                             |
| coverage                   | 53.1 ms                                                                     | 52.3 ms: 1.02x faster                                                             |
| k_core                     | 1.71 sec                                                                    | 1.69 sec: 1.01x faster                                                            |
| pyflate                    | 290 ms                                                                      | 285 ms: 1.01x faster                                                              |
| genshi_text                | 14.7 ms                                                                     | 14.5 ms: 1.01x faster                                                             |
| richards_super             | 32.2 ms                                                                     | 31.8 ms: 1.01x faster                                                             |
| pprint_pformat             | 1.06 sec                                                                    | 1.04 sec: 1.01x faster                                                            |
| raytrace                   | 168 ms                                                                      | 166 ms: 1.01x faster                                                              |
| xml_etree_process          | 45.1 ms                                                                     | 44.5 ms: 1.01x faster                                                             |
| nqueens                    | 62.9 ms                                                                     | 62.1 ms: 1.01x faster                                                             |
| unpickle_pure_python       | 147 us                                                                      | 146 us: 1.01x faster                                                              |
| deepcopy_memo              | 18.9 us                                                                     | 18.7 us: 1.01x faster                                                             |
| richards                   | 28.3 ms                                                                     | 28.0 ms: 1.01x faster                                                             |
| regex_compile              | 84.2 ms                                                                     | 83.3 ms: 1.01x faster                                                             |
| chaos                      | 39.1 ms                                                                     | 38.8 ms: 1.01x faster                                                             |
| async_tree_none_tg         | 168 ms                                                                      | 166 ms: 1.01x faster                                                              |
| pathlib                    | 30.0 ms                                                                     | 29.7 ms: 1.01x faster                                                             |
| bpe_tokeniser              | 3.11 sec                                                                    | 3.08 sec: 1.01x faster                                                            |
| async_tree_none            | 175 ms                                                                      | 173 ms: 1.01x faster                                                              |
| pprint_safe_repr           | 520 ms                                                                      | 516 ms: 1.01x faster                                                              |
| async_tree_memoization     | 205 ms                                                                      | 203 ms: 1.01x faster                                                              |
| sqlglot_normalize          | 191 ms                                                                      | 190 ms: 1.00x faster                                                              |
| sqlglot_transpile          | 1.02 ms                                                                     | 1.02 ms: 1.00x faster                                                             |
| sqlite_synth               | 1.60 us                                                                     | 1.61 us: 1.00x slower                                                             |
| sympy_str                  | 176 ms                                                                      | 176 ms: 1.00x slower                                                              |
| shortest_path              | 350 ms                                                                      | 351 ms: 1.00x slower                                                              |
| pidigits                   | 154 ms                                                                      | 155 ms: 1.00x slower                                                              |
| sympy_expand               | 301 ms                                                                      | 302 ms: 1.01x slower                                                              |
| genshi_xml                 | 31.8 ms                                                                     | 32.0 ms: 1.01x slower                                                             |
| telco                      | 5.10 ms                                                                     | 5.14 ms: 1.01x slower                                                             |
| json_loads                 | 19.5 us                                                                     | 19.7 us: 1.01x slower                                                             |
| coroutines                 | 13.0 ms                                                                     | 13.1 ms: 1.01x slower                                                             |
| html5lib                   | 38.8 ms                                                                     | 39.1 ms: 1.01x slower                                                             |
| connected_components       | 322 ms                                                                      | 324 ms: 1.01x slower                                                              |
| asyncio_websockets         | 311 ms                                                                      | 313 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed_tg | 359 ms                                                                      | 363 ms: 1.01x slower                                                              |
| scimark_fft                | 181 ms                                                                      | 183 ms: 1.01x slower                                                              |
| python_startup_no_site     | 19.4 ms                                                                     | 19.8 ms: 1.02x slower                                                             |
| thrift                     | 543 us                                                                      | 554 us: 1.02x slower                                                              |
| logging_simple             | 6.18 us                                                                     | 6.32 us: 1.02x slower                                                             |
| logging_format             | 6.61 us                                                                     | 6.78 us: 1.03x slower                                                             |
| json                       | 3.55 ms                                                                     | 3.65 ms: 1.03x slower                                                             |
| mako                       | 7.32 ms                                                                     | 7.58 ms: 1.03x slower                                                             |
| python_startup             | 25.8 ms                                                                     | 26.9 ms: 1.04x slower                                                             |
| gc_traversal               | 2.55 ms                                                                     | 2.71 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (38): create_gc_cycles, async_tree_io, xml_etree_parse, json_dumps, async_generators, comprehensions, scimark_monte_carlo, regex_effbot, scimark_lu, regex_v8, deepcopy, sympy_integrate, sphinx, sympy_sum, nbody, generators, tomli_loads, pylint, pickle_pure_python, deepcopy_reduce, sqlglot_parse, xml_etree_iterparse, 2to3, typing_runtime_protocols, xml_etree_generate, bench_thread_pool, async_tree_io_tg, django_template, sqlglot_optimize, regex_dna, dulwich_log, bench_mp_pool, many_optionals, subparsers, docutils, async_tree_memoization_tg, async_tree_cpu_io_mixed, pycparser
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 97.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown