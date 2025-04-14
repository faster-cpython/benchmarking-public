# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.005x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| html5lib       | 41.3 ms                                                                     | 40.6 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators       | 240 ms                                                                      | 222 ms: 1.08x faster                                                                  |
| async_tree_memoization | 220 ms                                                                      | 216 ms: 1.02x faster                                                                  |
| async_tree_none        | 188 ms                                                                      | 185 ms: 1.01x faster                                                                  |
| async_tree_none_tg     | 177 ms                                                                      | 175 ms: 1.01x faster                                                                  |
| asyncio_websockets     | 312 ms                                                                      | 318 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 59.7 ms                                                                     | 62.2 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                                      | 118 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.48 ms                                                                     | 1.46 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_process    | 37.4 ms                                                                     | 36.0 ms: 1.04x faster                                                                 |
| xml_etree_generate   | 52.7 ms                                                                     | 50.9 ms: 1.03x faster                                                                 |
| xml_etree_parse      | 92.1 ms                                                                     | 90.9 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 63.8 ms                                                                     | 62.9 ms: 1.01x faster                                                                 |
| pickle_pure_python   | 219 us                                                                      | 218 us: 1.01x faster                                                                  |
| tomli_loads          | 1.24 sec                                                                    | 1.25 sec: 1.01x slower                                                                |
| unpickle_pure_python | 116 us                                                                      | 117 us: 1.01x slower                                                                  |
| json_loads           | 14.6 us                                                                     | 14.9 us: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 20.2 ms                                                                     | 20.7 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text    | 17.1 ms                                                                     | 17.0 ms: 1.01x faster                                                                 |
| mako           | 5.35 ms                                                                     | 5.46 ms: 1.02x slower                                                                 |
| genshi_xml     | 37.5 ms                                                                     | 38.3 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators         | 240 ms                                                                      | 222 ms: 1.08x faster                                                                  |
| regex_dna                | 126 ms                                                                      | 118 ms: 1.07x faster                                                                  |
| go                       | 91.5 ms                                                                     | 86.9 ms: 1.05x faster                                                                 |
| richards_super           | 34.7 ms                                                                     | 33.4 ms: 1.04x faster                                                                 |
| xml_etree_process        | 37.4 ms                                                                     | 36.0 ms: 1.04x faster                                                                 |
| xml_etree_generate       | 52.7 ms                                                                     | 50.9 ms: 1.03x faster                                                                 |
| typing_runtime_protocols | 110 us                                                                      | 106 us: 1.03x faster                                                                  |
| logging_silent           | 66.0 ns                                                                     | 63.8 ns: 1.03x faster                                                                 |
| meteor_contest           | 76.7 ms                                                                     | 74.2 ms: 1.03x faster                                                                 |
| richards                 | 30.6 ms                                                                     | 29.7 ms: 1.03x faster                                                                 |
| pyflate                  | 281 ms                                                                      | 273 ms: 1.03x faster                                                                  |
| nqueens                  | 62.9 ms                                                                     | 61.2 ms: 1.03x faster                                                                 |
| fannkuch                 | 250 ms                                                                      | 244 ms: 1.02x faster                                                                  |
| scimark_fft              | 156 ms                                                                      | 152 ms: 1.02x faster                                                                  |
| async_tree_memoization   | 220 ms                                                                      | 216 ms: 1.02x faster                                                                  |
| deepcopy_reduce          | 1.99 us                                                                     | 1.95 us: 1.02x faster                                                                 |
| regex_effbot             | 1.48 ms                                                                     | 1.46 ms: 1.02x faster                                                                 |
| comprehensions           | 11.5 us                                                                     | 11.3 us: 1.02x faster                                                                 |
| html5lib                 | 41.3 ms                                                                     | 40.6 ms: 1.02x faster                                                                 |
| mdp                      | 1.58 sec                                                                    | 1.55 sec: 1.02x faster                                                                |
| pycparser                | 750 ms                                                                      | 739 ms: 1.01x faster                                                                  |
| async_tree_none          | 188 ms                                                                      | 185 ms: 1.01x faster                                                                  |
| xml_etree_parse          | 92.1 ms                                                                     | 90.9 ms: 1.01x faster                                                                 |
| dulwich_log              | 43.7 ms                                                                     | 43.1 ms: 1.01x faster                                                                 |
| xml_etree_iterparse      | 63.8 ms                                                                     | 62.9 ms: 1.01x faster                                                                 |
| async_tree_none_tg       | 177 ms                                                                      | 175 ms: 1.01x faster                                                                  |
| deepcopy                 | 189 us                                                                      | 187 us: 1.01x faster                                                                  |
| genshi_text              | 17.1 ms                                                                     | 17.0 ms: 1.01x faster                                                                 |
| logging_format           | 7.07 us                                                                     | 7.00 us: 1.01x faster                                                                 |
| pathlib                  | 32.2 ms                                                                     | 31.9 ms: 1.01x faster                                                                 |
| scimark_sparse_mat_mult  | 2.18 ms                                                                     | 2.16 ms: 1.01x faster                                                                 |
| sympy_expand             | 308 ms                                                                      | 306 ms: 1.01x faster                                                                  |
| pickle_pure_python       | 219 us                                                                      | 218 us: 1.01x faster                                                                  |
| hexiom                   | 4.46 ms                                                                     | 4.43 ms: 1.01x faster                                                                 |
| tomli_loads              | 1.24 sec                                                                    | 1.25 sec: 1.01x slower                                                                |
| unpickle_pure_python     | 116 us                                                                      | 117 us: 1.01x slower                                                                  |
| scimark_sor              | 87.4 ms                                                                     | 88.2 ms: 1.01x slower                                                                 |
| deepcopy_memo            | 20.1 us                                                                     | 20.3 us: 1.01x slower                                                                 |
| sqlglot_parse            | 853 us                                                                      | 865 us: 1.01x slower                                                                  |
| scimark_monte_carlo      | 45.6 ms                                                                     | 46.5 ms: 1.02x slower                                                                 |
| mako                     | 5.35 ms                                                                     | 5.46 ms: 1.02x slower                                                                 |
| asyncio_websockets       | 312 ms                                                                      | 318 ms: 1.02x slower                                                                  |
| json_loads               | 14.6 us                                                                     | 14.9 us: 1.02x slower                                                                 |
| many_optionals           | 454 us                                                                      | 463 us: 1.02x slower                                                                  |
| generators               | 20.3 ms                                                                     | 20.7 ms: 1.02x slower                                                                 |
| genshi_xml               | 37.5 ms                                                                     | 38.3 ms: 1.02x slower                                                                 |
| python_startup_no_site   | 20.2 ms                                                                     | 20.7 ms: 1.02x slower                                                                 |
| nbody                    | 59.7 ms                                                                     | 62.2 ms: 1.04x slower                                                                 |
| spectral_norm            | 62.5 ms                                                                     | 66.6 ms: 1.07x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (40): gc_traversal, sqlglot_transpile, pylint, logging_simple, k_core, async_tree_cpu_io_mixed_tg, subparsers, sympy_integrate, scimark_lu, sqlite_synth, sphinx, async_tree_cpu_io_mixed, async_tree_io, django_template, deltablue, thrift, pidigits, shortest_path, bpe_tokeniser, python_startup, connected_components, async_tree_memoization_tg, json_dumps, bench_thread_pool, async_tree_io_tg, crypto_pyaes, sympy_str, bench_mp_pool, sympy_sum, regex_compile, telco, raytrace, chaos, coroutines, float, coverage, json, 2to3, create_gc_cycles, regex_v8
Ignored benchmarks (5) of results/bm-20250306-3.14.0a5+-052cb71-JIT/bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71.json: docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown