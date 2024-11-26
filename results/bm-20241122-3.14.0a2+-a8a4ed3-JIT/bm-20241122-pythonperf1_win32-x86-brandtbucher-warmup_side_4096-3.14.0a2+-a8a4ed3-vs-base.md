# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-x86
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.004x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                          | 260 ms: 1.04x faster                                                              |
| docutils       | 2.02 sec                                                                        | 1.95 sec: 1.03x faster                                                            |
| sphinx         | 829 ms                                                                          | 801 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                                           | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets      | 356 ms                                                                          | 349 ms: 1.02x faster                                                              |
| async_tree_io_tg        | 550 ms                                                                          | 542 ms: 1.02x faster                                                              |
| async_tree_cpu_io_mixed | 506 ms                                                                          | 500 ms: 1.01x faster                                                              |
| coroutines              | 16.7 ms                                                                         | 16.5 ms: 1.01x faster                                                             |
| async_tree_memoization  | 302 ms                                                                          | 301 ms: 1.00x faster                                                              |
| Geometric mean          | (ref)                                                                           | 1.01x faster                                                                      |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 99.8 ms                                                                         | 94.9 ms: 1.05x faster                                                             |
| pidigits       | 205 ms                                                                          | 203 ms: 1.01x faster                                                              |
| float          | 55.6 ms                                                                         | 56.3 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                                          | 113 ms: 1.11x faster                                                              |
| regex_effbot   | 1.66 ms                                                                         | 1.55 ms: 1.07x faster                                                             |
| regex_v8       | 15.9 ms                                                                         | 15.6 ms: 1.02x faster                                                             |
| regex_compile  | 116 ms                                                                          | 113 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                           | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|---------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse | 69.2 ms                                                                         | 68.3 ms: 1.01x faster                                                             |
| pickle_pure_python  | 298 us                                                                          | 296 us: 1.01x faster                                                              |
| xml_etree_generate  | 73.0 ms                                                                         | 72.7 ms: 1.00x faster                                                             |
| tomli_loads         | 1.83 sec                                                                        | 1.84 sec: 1.01x slower                                                            |
| json_loads          | 20.9 us                                                                         | 21.3 us: 1.02x slower                                                             |
| json_dumps          | 8.82 ms                                                                         | 9.01 ms: 1.02x slower                                                             |
| Geometric mean      | (ref)                                                                           | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 26.7 ms                                                                         | 25.7 ms: 1.04x faster                                                             |
| python_startup_no_site | 20.1 ms                                                                         | 19.5 ms: 1.03x faster                                                             |
| Geometric mean         | (ref)                                                                           | 1.03x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 56.6 ms                                                                         | 57.2 ms: 1.01x slower                                                             |
| django_template | 36.0 ms                                                                         | 37.0 ms: 1.03x slower                                                             |
| Geometric mean  | (ref)                                                                           | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna                | 126 ms                                                                          | 113 ms: 1.11x faster                                                              |
| regex_effbot             | 1.66 ms                                                                         | 1.55 ms: 1.07x faster                                                             |
| bench_mp_pool            | 92.3 ms                                                                         | 87.2 ms: 1.06x faster                                                             |
| nbody                    | 99.8 ms                                                                         | 94.9 ms: 1.05x faster                                                             |
| pylint                   | 237 ms                                                                          | 228 ms: 1.04x faster                                                              |
| python_startup           | 26.7 ms                                                                         | 25.7 ms: 1.04x faster                                                             |
| 2to3                     | 269 ms                                                                          | 260 ms: 1.04x faster                                                              |
| sphinx                   | 829 ms                                                                          | 801 ms: 1.04x faster                                                              |
| sqlglot_transpile        | 1.47 ms                                                                         | 1.42 ms: 1.04x faster                                                             |
| docutils                 | 2.02 sec                                                                        | 1.95 sec: 1.03x faster                                                            |
| fannkuch                 | 340 ms                                                                          | 330 ms: 1.03x faster                                                              |
| many_optionals           | 576 us                                                                          | 560 us: 1.03x faster                                                              |
| python_startup_no_site   | 20.1 ms                                                                         | 19.5 ms: 1.03x faster                                                             |
| richards_super           | 48.7 ms                                                                         | 47.4 ms: 1.03x faster                                                             |
| sqlglot_normalize        | 111 ms                                                                          | 108 ms: 1.03x faster                                                              |
| telco                    | 7.36 ms                                                                         | 7.17 ms: 1.03x faster                                                             |
| regex_v8                 | 15.9 ms                                                                         | 15.6 ms: 1.02x faster                                                             |
| hexiom                   | 7.17 ms                                                                         | 7.00 ms: 1.02x faster                                                             |
| sympy_str                | 239 ms                                                                          | 233 ms: 1.02x faster                                                              |
| sqlglot_optimize         | 52.0 ms                                                                         | 50.8 ms: 1.02x faster                                                             |
| pprint_safe_repr         | 748 ms                                                                          | 731 ms: 1.02x faster                                                              |
| sympy_expand             | 412 ms                                                                          | 403 ms: 1.02x faster                                                              |
| bpe_tokeniser            | 3.86 sec                                                                        | 3.78 sec: 1.02x faster                                                            |
| richards                 | 42.4 ms                                                                         | 41.6 ms: 1.02x faster                                                             |
| asyncio_websockets       | 356 ms                                                                          | 349 ms: 1.02x faster                                                              |
| regex_compile            | 116 ms                                                                          | 113 ms: 1.02x faster                                                              |
| sqlglot_parse            | 1.17 ms                                                                         | 1.15 ms: 1.02x faster                                                             |
| async_tree_io_tg         | 550 ms                                                                          | 542 ms: 1.02x faster                                                              |
| xml_etree_iterparse      | 69.2 ms                                                                         | 68.3 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed  | 506 ms                                                                          | 500 ms: 1.01x faster                                                              |
| mdp                      | 1.87 sec                                                                        | 1.85 sec: 1.01x faster                                                            |
| go                       | 122 ms                                                                          | 121 ms: 1.01x faster                                                              |
| pprint_pformat           | 1.52 sec                                                                        | 1.51 sec: 1.01x faster                                                            |
| pidigits                 | 205 ms                                                                          | 203 ms: 1.01x faster                                                              |
| coroutines               | 16.7 ms                                                                         | 16.5 ms: 1.01x faster                                                             |
| comprehensions           | 18.6 us                                                                         | 18.4 us: 1.01x faster                                                             |
| pickle_pure_python       | 298 us                                                                          | 296 us: 1.01x faster                                                              |
| sqlite_synth             | 1.95 us                                                                         | 1.94 us: 1.01x faster                                                             |
| logging_simple           | 8.46 us                                                                         | 8.40 us: 1.01x faster                                                             |
| subparsers               | 21.6 ms                                                                         | 21.5 ms: 1.01x faster                                                             |
| async_tree_memoization   | 302 ms                                                                          | 301 ms: 1.00x faster                                                              |
| xml_etree_generate       | 73.0 ms                                                                         | 72.7 ms: 1.00x faster                                                             |
| logging_format           | 9.05 us                                                                         | 9.01 us: 1.00x faster                                                             |
| nqueens                  | 99.3 ms                                                                         | 98.9 ms: 1.00x faster                                                             |
| chaos                    | 65.4 ms                                                                         | 65.7 ms: 1.00x slower                                                             |
| pathlib                  | 82.9 ms                                                                         | 83.4 ms: 1.01x slower                                                             |
| raytrace                 | 301 ms                                                                          | 303 ms: 1.01x slower                                                              |
| tomli_loads              | 1.83 sec                                                                        | 1.84 sec: 1.01x slower                                                            |
| scimark_fft              | 248 ms                                                                          | 250 ms: 1.01x slower                                                              |
| thrift                   | 780 us                                                                          | 786 us: 1.01x slower                                                              |
| scimark_sparse_mat_mult  | 3.19 ms                                                                         | 3.21 ms: 1.01x slower                                                             |
| crypto_pyaes             | 66.0 ms                                                                         | 66.7 ms: 1.01x slower                                                             |
| shortest_path            | 316 ms                                                                          | 319 ms: 1.01x slower                                                              |
| pycparser                | 921 ms                                                                          | 931 ms: 1.01x slower                                                              |
| genshi_xml               | 56.6 ms                                                                         | 57.2 ms: 1.01x slower                                                             |
| deepcopy                 | 275 us                                                                          | 278 us: 1.01x slower                                                              |
| connected_components     | 286 ms                                                                          | 289 ms: 1.01x slower                                                              |
| float                    | 55.6 ms                                                                         | 56.3 ms: 1.01x slower                                                             |
| deltablue                | 3.16 ms                                                                         | 3.21 ms: 1.01x slower                                                             |
| dulwich_log              | 49.2 ms                                                                         | 49.8 ms: 1.01x slower                                                             |
| json_loads               | 20.9 us                                                                         | 21.3 us: 1.02x slower                                                             |
| json_dumps               | 8.82 ms                                                                         | 9.01 ms: 1.02x slower                                                             |
| django_template          | 36.0 ms                                                                         | 37.0 ms: 1.03x slower                                                             |
| scimark_monte_carlo      | 62.2 ms                                                                         | 64.1 ms: 1.03x slower                                                             |
| typing_runtime_protocols | 163 us                                                                          | 169 us: 1.03x slower                                                              |
| scimark_lu               | 71.5 ms                                                                         | 74.0 ms: 1.03x slower                                                             |
| deepcopy_reduce          | 2.75 us                                                                         | 2.86 us: 1.04x slower                                                             |
| coverage                 | 52.4 ms                                                                         | 55.0 ms: 1.05x slower                                                             |
| deepcopy_memo            | 22.9 us                                                                         | 24.0 us: 1.05x slower                                                             |
| json                     | 4.37 ms                                                                         | 4.63 ms: 1.06x slower                                                             |
| scimark_sor              | 100 ms                                                                          | 106 ms: 1.06x slower                                                              |
| spectral_norm            | 78.1 ms                                                                         | 83.5 ms: 1.07x slower                                                             |
| generators               | 34.3 ms                                                                         | 36.7 ms: 1.07x slower                                                             |
| logging_silent           | 80.1 ns                                                                         | 87.9 ns: 1.10x slower                                                             |
| Geometric mean           | (ref)                                                                           | 1.00x faster                                                                      |

Benchmark hidden because not significant (20): k_core, gc_traversal, async_tree_none_tg, async_tree_io, bench_thread_pool, xml_etree_parse, async_tree_none, async_tree_memoization_tg, unpickle_pure_python, sympy_integrate, sympy_sum, async_tree_cpu_io_mixed_tg, meteor_contest, async_generators, html5lib, genshi_text, xml_etree_process, mako, pyflate, create_gc_cycles

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown