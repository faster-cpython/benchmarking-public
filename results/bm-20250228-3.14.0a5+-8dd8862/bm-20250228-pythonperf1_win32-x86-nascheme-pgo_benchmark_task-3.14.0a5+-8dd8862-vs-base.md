# Results vs. base

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-x86
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.008x faster
- HPT reliability: 99.12%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                          | 257 ms: 1.01x faster                                                            |
| docutils       | 1.85 sec                                                                        | 1.84 sec: 1.00x faster                                                          |
| sphinx         | 749 ms                                                                          | 743 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 480 ms                                                                          | 438 ms: 1.10x faster                                                            |
| async_generators           | 310 ms                                                                          | 290 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 497 ms                                                                          | 469 ms: 1.06x faster                                                            |
| async_tree_memoization_tg  | 244 ms                                                                          | 246 ms: 1.01x slower                                                            |
| async_tree_memoization     | 259 ms                                                                          | 262 ms: 1.01x slower                                                            |
| async_tree_none_tg         | 196 ms                                                                          | 198 ms: 1.01x slower                                                            |
| async_tree_none            | 217 ms                                                                          | 220 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): coroutines, async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 200 ms                                                                          | 200 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                          | 115 ms: 1.04x faster                                                            |
| regex_compile  | 109 ms                                                                          | 108 ms: 1.02x faster                                                            |
| regex_v8       | 15.4 ms                                                                         | 15.8 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|---------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 50.8 ms                                                                         | 49.3 ms: 1.03x faster                                                           |
| pickle_pure_python  | 292 us                                                                          | 287 us: 1.02x faster                                                            |
| xml_etree_parse     | 109 ms                                                                          | 107 ms: 1.01x faster                                                            |
| json_dumps          | 7.99 ms                                                                         | 7.90 ms: 1.01x faster                                                           |
| xml_etree_generate  | 68.3 ms                                                                         | 67.7 ms: 1.01x faster                                                           |
| json_loads          | 21.8 us                                                                         | 21.6 us: 1.01x faster                                                           |
| xml_etree_iterparse | 66.4 ms                                                                         | 65.9 ms: 1.01x faster                                                           |
| Geometric mean      | (ref)                                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.1 ms                                                                         | 34.1 ms: 1.03x faster                                                           |
| genshi_text     | 22.7 ms                                                                         | 22.2 ms: 1.02x faster                                                           |
| mako            | 7.94 ms                                                                         | 7.82 ms: 1.01x faster                                                           |
| genshi_xml      | 48.4 ms                                                                         | 47.8 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                           | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250226-pythonperf1_win32-x86-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 480 ms                                                                          | 438 ms: 1.10x faster                                                            |
| telco                      | 6.64 ms                                                                         | 6.15 ms: 1.08x faster                                                           |
| async_generators           | 310 ms                                                                          | 290 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 497 ms                                                                          | 469 ms: 1.06x faster                                                            |
| sqlglot_normalize          | 235 ms                                                                          | 222 ms: 1.06x faster                                                            |
| sqlglot_optimize           | 45.7 ms                                                                         | 43.2 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 654 ms                                                                          | 619 ms: 1.06x faster                                                            |
| pprint_pformat             | 1.33 sec                                                                        | 1.28 sec: 1.04x faster                                                          |
| regex_dna                  | 119 ms                                                                          | 115 ms: 1.04x faster                                                            |
| deepcopy                   | 251 us                                                                          | 242 us: 1.04x faster                                                            |
| sqlglot_parse              | 1.16 ms                                                                         | 1.12 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.40 ms                                                                         | 1.36 ms: 1.03x faster                                                           |
| django_template            | 35.1 ms                                                                         | 34.1 ms: 1.03x faster                                                           |
| xml_etree_process          | 50.8 ms                                                                         | 49.3 ms: 1.03x faster                                                           |
| go                         | 110 ms                                                                          | 107 ms: 1.03x faster                                                            |
| coverage                   | 52.9 ms                                                                         | 51.6 ms: 1.02x faster                                                           |
| comprehensions             | 13.8 us                                                                         | 13.5 us: 1.02x faster                                                           |
| hexiom                     | 5.30 ms                                                                         | 5.18 ms: 1.02x faster                                                           |
| genshi_text                | 22.7 ms                                                                         | 22.2 ms: 1.02x faster                                                           |
| gc_traversal               | 1.81 ms                                                                         | 1.78 ms: 1.02x faster                                                           |
| sympy_expand               | 391 ms                                                                          | 384 ms: 1.02x faster                                                            |
| logging_silent             | 73.0 ns                                                                         | 71.7 ns: 1.02x faster                                                           |
| many_optionals             | 549 us                                                                          | 540 us: 1.02x faster                                                            |
| pickle_pure_python         | 292 us                                                                          | 287 us: 1.02x faster                                                            |
| regex_compile              | 109 ms                                                                          | 108 ms: 1.02x faster                                                            |
| mako                       | 7.94 ms                                                                         | 7.82 ms: 1.01x faster                                                           |
| xml_etree_parse            | 109 ms                                                                          | 107 ms: 1.01x faster                                                            |
| sympy_sum                  | 111 ms                                                                          | 109 ms: 1.01x faster                                                            |
| json_dumps                 | 7.99 ms                                                                         | 7.90 ms: 1.01x faster                                                           |
| sympy_integrate            | 16.2 ms                                                                         | 16.0 ms: 1.01x faster                                                           |
| 2to3                       | 260 ms                                                                          | 257 ms: 1.01x faster                                                            |
| genshi_xml                 | 48.4 ms                                                                         | 47.8 ms: 1.01x faster                                                           |
| spectral_norm              | 73.1 ms                                                                         | 72.3 ms: 1.01x faster                                                           |
| dulwich_log                | 53.6 ms                                                                         | 53.1 ms: 1.01x faster                                                           |
| pathlib                    | 37.2 ms                                                                         | 36.8 ms: 1.01x faster                                                           |
| typing_runtime_protocols   | 149 us                                                                          | 148 us: 1.01x faster                                                            |
| xml_etree_generate         | 68.3 ms                                                                         | 67.7 ms: 1.01x faster                                                           |
| generators                 | 27.1 ms                                                                         | 26.9 ms: 1.01x faster                                                           |
| sympy_str                  | 224 ms                                                                          | 222 ms: 1.01x faster                                                            |
| json_loads                 | 21.8 us                                                                         | 21.6 us: 1.01x faster                                                           |
| sphinx                     | 749 ms                                                                          | 743 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 66.4 ms                                                                         | 65.9 ms: 1.01x faster                                                           |
| subparsers                 | 21.7 ms                                                                         | 21.6 ms: 1.00x faster                                                           |
| docutils                   | 1.85 sec                                                                        | 1.84 sec: 1.00x faster                                                          |
| pidigits                   | 200 ms                                                                          | 200 ms: 1.00x faster                                                            |
| async_tree_memoization_tg  | 244 ms                                                                          | 246 ms: 1.01x slower                                                            |
| pyflate                    | 348 ms                                                                          | 351 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 3.45 sec                                                                        | 3.48 sec: 1.01x slower                                                          |
| mdp                        | 1.77 sec                                                                        | 1.79 sec: 1.01x slower                                                          |
| async_tree_memoization     | 259 ms                                                                          | 262 ms: 1.01x slower                                                            |
| async_tree_none_tg         | 196 ms                                                                          | 198 ms: 1.01x slower                                                            |
| fannkuch                   | 303 ms                                                                          | 307 ms: 1.01x slower                                                            |
| async_tree_none            | 217 ms                                                                          | 220 ms: 1.01x slower                                                            |
| scimark_sor                | 97.5 ms                                                                         | 99.0 ms: 1.02x slower                                                           |
| richards                   | 38.3 ms                                                                         | 39.1 ms: 1.02x slower                                                           |
| raytrace                   | 259 ms                                                                          | 265 ms: 1.02x slower                                                            |
| scimark_fft                | 230 ms                                                                          | 236 ms: 1.03x slower                                                            |
| regex_v8                   | 15.4 ms                                                                         | 15.8 ms: 1.03x slower                                                           |
| deepcopy_memo              | 21.9 us                                                                         | 22.5 us: 1.03x slower                                                           |
| richards_super             | 44.2 ms                                                                         | 45.5 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 3.04 ms                                                                         | 3.14 ms: 1.03x slower                                                           |
| chaos                      | 56.6 ms                                                                         | 58.6 ms: 1.03x slower                                                           |
| crypto_pyaes               | 62.4 ms                                                                         | 64.7 ms: 1.04x slower                                                           |
| scimark_lu                 | 68.3 ms                                                                         | 70.8 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (30): json, pylint, python_startup_no_site, pycparser, unpickle_pure_python, k_core, bench_mp_pool, coroutines, shortest_path, deltablue, logging_simple, python_startup, html5lib, thrift, async_tree_io, create_gc_cycles, logging_format, tomli_loads, nqueens, asyncio_websockets, sqlite_synth, connected_components, meteor_contest, regex_effbot, nbody, float, deepcopy_reduce, scimark_monte_carlo, async_tree_io_tg, bench_thread_pool

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown