# Results vs. 3.13.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-x86
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.10x faster
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                              |
| docutils       | 1.82 sec                                                        | 1.95 sec: 1.07x slower                                                            |
| html5lib       | 48.3 ms                                                         | 46.4 ms: 1.04x faster                                                             |
| tornado_http   | 104 ms                                                          | 106 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 671 ms: 1.26x faster                                                              |
| async_tree_memoization_tg | 287 ms                                                          | 246 ms: 1.17x faster                                                              |
| async_tree_none_tg        | 219 ms                                                          | 194 ms: 1.13x faster                                                              |
| async_tree_none           | 246 ms                                                          | 219 ms: 1.12x faster                                                              |
| async_tree_memoization    | 302 ms                                                          | 271 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 471 ms: 1.05x faster                                                              |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                            |
| async_tree_io             | 537 ms                                                          | 544 ms: 1.01x slower                                                              |
| async_generators          | 274 ms                                                          | 310 ms: 1.13x slower                                                              |
| coroutines                | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                             |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                                      |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 53.1 ms: 1.54x faster                                                             |
| float          | 57.8 ms                                                         | 42.9 ms: 1.35x faster                                                             |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 95.3 ms: 1.08x faster                                                             |
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                             |
| regex_effbot   | 1.81 ms                                                         | 2.00 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.46 sec: 1.18x faster                                                            |
| pickle_pure_python   | 238 us                                                          | 217 us: 1.10x faster                                                              |
| unpickle_pure_python | 162 us                                                          | 149 us: 1.09x faster                                                              |
| json_dumps           | 7.40 ms                                                         | 7.00 ms: 1.06x faster                                                             |
| xml_etree_generate   | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                                             |
| xml_etree_iterparse  | 65.1 ms                                                         | 64.1 ms: 1.02x faster                                                             |
| xml_etree_process    | 45.0 ms                                                         | 44.7 ms: 1.01x faster                                                             |
| json_loads           | 21.0 us                                                         | 21.2 us: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.9 ms: 1.01x faster                                                             |
| python_startup_no_site | 19.9 ms                                                         | 20.1 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.41 ms: 1.35x faster                                                             |
| django_template | 32.7 ms                                                         | 32.2 ms: 1.01x faster                                                             |
| genshi_text     | 22.4 ms                                                         | 22.8 ms: 1.01x slower                                                             |
| genshi_xml      | 49.5 ms                                                         | 51.4 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 725 us: 14.00x faster                                                             |
| coverage                  | 333 ms                                                          | 52.8 ms: 6.30x faster                                                             |
| deepcopy_memo             | 26.2 us                                                         | 15.7 us: 1.66x faster                                                             |
| nbody                     | 81.9 ms                                                         | 53.1 ms: 1.54x faster                                                             |
| spectral_norm             | 71.3 ms                                                         | 47.3 ms: 1.51x faster                                                             |
| mako                      | 7.31 ms                                                         | 5.41 ms: 1.35x faster                                                             |
| float                     | 57.8 ms                                                         | 42.9 ms: 1.35x faster                                                             |
| deepcopy                  | 307 us                                                          | 237 us: 1.29x faster                                                              |
| asyncio_tcp               | 842 ms                                                          | 671 ms: 1.26x faster                                                              |
| scimark_fft               | 206 ms                                                          | 167 ms: 1.23x faster                                                              |
| pyflate                   | 326 ms                                                          | 264 ms: 1.23x faster                                                              |
| fannkuch                  | 293 ms                                                          | 238 ms: 1.23x faster                                                              |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.37 ms: 1.23x faster                                                             |
| crypto_pyaes              | 58.2 ms                                                         | 48.7 ms: 1.19x faster                                                             |
| tomli_loads               | 1.73 sec                                                        | 1.46 sec: 1.18x faster                                                            |
| deepcopy_reduce           | 2.85 us                                                         | 2.42 us: 1.18x faster                                                             |
| async_tree_memoization_tg | 287 ms                                                          | 246 ms: 1.17x faster                                                              |
| telco                     | 6.67 ms                                                         | 5.77 ms: 1.16x faster                                                             |
| scimark_monte_carlo       | 50.3 ms                                                         | 44.0 ms: 1.14x faster                                                             |
| async_tree_none_tg        | 219 ms                                                          | 194 ms: 1.13x faster                                                              |
| sqlglot_parse             | 1.05 ms                                                         | 936 us: 1.12x faster                                                              |
| async_tree_none           | 246 ms                                                          | 219 ms: 1.12x faster                                                              |
| comprehensions            | 12.7 us                                                         | 11.4 us: 1.12x faster                                                             |
| async_tree_memoization    | 302 ms                                                          | 271 ms: 1.12x faster                                                              |
| pprint_safe_repr          | 644 ms                                                          | 582 ms: 1.11x faster                                                              |
| pickle_pure_python        | 238 us                                                          | 217 us: 1.10x faster                                                              |
| pycparser                 | 869 ms                                                          | 796 ms: 1.09x faster                                                              |
| meteor_contest            | 77.0 ms                                                         | 70.8 ms: 1.09x faster                                                             |
| unpickle_pure_python      | 162 us                                                          | 149 us: 1.09x faster                                                              |
| regex_compile             | 103 ms                                                          | 95.3 ms: 1.08x faster                                                             |
| pprint_pformat            | 1.30 sec                                                        | 1.20 sec: 1.08x faster                                                            |
| sqlglot_transpile         | 1.29 ms                                                         | 1.21 ms: 1.07x faster                                                             |
| json_dumps                | 7.40 ms                                                         | 7.00 ms: 1.06x faster                                                             |
| logging_simple            | 7.87 us                                                         | 7.47 us: 1.05x faster                                                             |
| logging_format            | 8.57 us                                                         | 8.13 us: 1.05x faster                                                             |
| xml_etree_generate        | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 471 ms: 1.05x faster                                                              |
| logging_silent            | 61.6 ns                                                         | 59.0 ns: 1.04x faster                                                             |
| html5lib                  | 48.3 ms                                                         | 46.4 ms: 1.04x faster                                                             |
| pidigits                  | 202 ms                                                          | 196 ms: 1.03x faster                                                              |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                            |
| xml_etree_iterparse       | 65.1 ms                                                         | 64.1 ms: 1.02x faster                                                             |
| django_template           | 32.7 ms                                                         | 32.2 ms: 1.01x faster                                                             |
| python_startup            | 24.3 ms                                                         | 23.9 ms: 1.01x faster                                                             |
| nqueens                   | 75.1 ms                                                         | 74.3 ms: 1.01x faster                                                             |
| mdp                       | 1.67 sec                                                        | 1.66 sec: 1.01x faster                                                            |
| xml_etree_process         | 45.0 ms                                                         | 44.7 ms: 1.01x faster                                                             |
| pathlib                   | 89.4 ms                                                         | 88.8 ms: 1.01x faster                                                             |
| hexiom                    | 4.64 ms                                                         | 4.62 ms: 1.00x faster                                                             |
| chaos                     | 51.2 ms                                                         | 51.6 ms: 1.01x slower                                                             |
| python_startup_no_site    | 19.9 ms                                                         | 20.1 ms: 1.01x slower                                                             |
| json_loads                | 21.0 us                                                         | 21.2 us: 1.01x slower                                                             |
| async_tree_io             | 537 ms                                                          | 544 ms: 1.01x slower                                                              |
| sympy_expand              | 375 ms                                                          | 380 ms: 1.01x slower                                                              |
| genshi_text               | 22.4 ms                                                         | 22.8 ms: 1.01x slower                                                             |
| tornado_http              | 104 ms                                                          | 106 ms: 1.02x slower                                                              |
| regex_v8                  | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                             |
| 2to3                      | 253 ms                                                          | 258 ms: 1.02x slower                                                              |
| sqlglot_optimize          | 42.5 ms                                                         | 43.6 ms: 1.03x slower                                                             |
| go                        | 111 ms                                                          | 115 ms: 1.04x slower                                                              |
| genshi_xml                | 49.5 ms                                                         | 51.4 ms: 1.04x slower                                                             |
| bench_mp_pool             | 74.3 ms                                                         | 77.4 ms: 1.04x slower                                                             |
| richards_super            | 38.0 ms                                                         | 39.5 ms: 1.04x slower                                                             |
| sympy_integrate           | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                             |
| typing_runtime_protocols  | 136 us                                                          | 146 us: 1.07x slower                                                              |
| sqlglot_normalize         | 220 ms                                                          | 236 ms: 1.07x slower                                                              |
| docutils                  | 1.82 sec                                                        | 1.95 sec: 1.07x slower                                                            |
| create_gc_cycles          | 713 us                                                          | 769 us: 1.08x slower                                                              |
| raytrace                  | 205 ms                                                          | 226 ms: 1.10x slower                                                              |
| regex_effbot              | 1.81 ms                                                         | 2.00 ms: 1.10x slower                                                             |
| pylint                    | 225 ms                                                          | 248 ms: 1.10x slower                                                              |
| deltablue                 | 2.41 ms                                                         | 2.71 ms: 1.13x slower                                                             |
| async_generators          | 274 ms                                                          | 310 ms: 1.13x slower                                                              |
| coroutines                | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                             |
| scimark_sor               | 91.8 ms                                                         | 107 ms: 1.16x slower                                                              |
| scimark_lu                | 63.5 ms                                                         | 78.9 ms: 1.24x slower                                                             |
| generators                | 22.1 ms                                                         | 28.2 ms: 1.28x slower                                                             |
| Geometric mean            | (ref)                                                           | 1.10x faster                                                                      |

Benchmark hidden because not significant (11): xml_etree_parse, regex_dna, async_tree_cpu_io_mixed_tg, async_tree_io_tg, richards, sympy_sum, sympy_str, gc_traversal, dulwich_log, bench_thread_pool, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown