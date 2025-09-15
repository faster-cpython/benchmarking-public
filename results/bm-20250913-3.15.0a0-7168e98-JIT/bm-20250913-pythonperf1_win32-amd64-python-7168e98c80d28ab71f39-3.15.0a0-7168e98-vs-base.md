# Results vs. base

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 216 ms                                                                                                                     | 214 ms: 1.01x faster                                                                                                           |
| html5lib       | 38.5 ms                                                                                                                    | 38.0 ms: 1.01x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 164 ms                                                                                                                     | 159 ms: 1.03x faster                                                                                                           |
| async_tree_io              | 388 ms                                                                                                                     | 380 ms: 1.02x faster                                                                                                           |
| asyncio_tcp                | 494 ms                                                                                                                     | 484 ms: 1.02x faster                                                                                                           |
| async_tree_none            | 172 ms                                                                                                                     | 168 ms: 1.02x faster                                                                                                           |
| async_tree_cpu_io_mixed_tg | 331 ms                                                                                                                     | 332 ms: 1.00x slower                                                                                                           |
| async_tree_cpu_io_mixed    | 324 ms                                                                                                                     | 327 ms: 1.01x slower                                                                                                           |
| async_tree_memoization_tg  | 204 ms                                                                                                                     | 209 ms: 1.02x slower                                                                                                           |
| asyncio_tcp_ssl            | 1.32 sec                                                                                                                   | 1.37 sec: 1.04x slower                                                                                                         |
| coroutines                 | 14.7 ms                                                                                                                    | 15.3 ms: 1.04x slower                                                                                                          |
| async_generators           | 227 ms                                                                                                                     | 242 ms: 1.07x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.00x slower                                                                                                                   |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.3 ms                                                                                                                    | 53.1 ms: 1.23x faster                                                                                                          |
| float          | 42.7 ms                                                                                                                    | 43.5 ms: 1.02x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.4 ms                                                                                                                    | 13.3 ms: 1.08x faster                                                                                                          |
| regex_effbot   | 1.61 ms                                                                                                                    | 1.55 ms: 1.04x faster                                                                                                          |
| regex_dna      | 120 ms                                                                                                                     | 115 ms: 1.04x faster                                                                                                           |
| regex_compile  | 79.8 ms                                                                                                                    | 76.9 ms: 1.04x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 135 us                                                                                                                     | 103 us: 1.31x faster                                                                                                           |
| tomli_loads          | 1.35 sec                                                                                                                   | 1.08 sec: 1.25x faster                                                                                                         |
| xml_etree_process    | 38.7 ms                                                                                                                    | 34.6 ms: 1.12x faster                                                                                                          |
| xml_etree_generate   | 55.4 ms                                                                                                                    | 50.8 ms: 1.09x faster                                                                                                          |
| pickle_pure_python   | 212 us                                                                                                                     | 196 us: 1.08x faster                                                                                                           |
| unpickle_list        | 2.84 us                                                                                                                    | 2.69 us: 1.05x faster                                                                                                          |
| xml_etree_parse      | 88.9 ms                                                                                                                    | 84.5 ms: 1.05x faster                                                                                                          |
| xml_etree_iterparse  | 63.9 ms                                                                                                                    | 61.5 ms: 1.04x faster                                                                                                          |
| json_loads           | 14.3 us                                                                                                                    | 13.7 us: 1.04x faster                                                                                                          |
| json_dumps           | 5.46 ms                                                                                                                    | 5.35 ms: 1.02x faster                                                                                                          |
| unpickle             | 8.52 us                                                                                                                    | 8.65 us: 1.02x slower                                                                                                          |
| pickle_dict          | 19.7 us                                                                                                                    | 20.2 us: 1.03x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.5 ms                                                                                                                    | 24.8 ms: 1.03x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.51 ms                                                                                                                    | 5.27 ms: 1.23x faster                                                                                                          |
| genshi_xml     | 35.2 ms                                                                                                                    | 33.9 ms: 1.04x faster                                                                                                          |
| genshi_text    | 15.8 ms                                                                                                                    | 15.5 ms: 1.02x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 135 us                                                                                                                     | 103 us: 1.31x faster                                                                                                           |
| fannkuch                   | 268 ms                                                                                                                     | 209 ms: 1.28x faster                                                                                                           |
| tomli_loads                | 1.35 sec                                                                                                                   | 1.08 sec: 1.25x faster                                                                                                         |
| mako                       | 6.51 ms                                                                                                                    | 5.27 ms: 1.23x faster                                                                                                          |
| nbody                      | 65.3 ms                                                                                                                    | 53.1 ms: 1.23x faster                                                                                                          |
| richards                   | 27.0 ms                                                                                                                    | 22.2 ms: 1.22x faster                                                                                                          |
| scimark_fft                | 178 ms                                                                                                                     | 146 ms: 1.22x faster                                                                                                           |
| bpe_tokeniser              | 2.97 sec                                                                                                                   | 2.50 sec: 1.19x faster                                                                                                         |
| pprint_safe_repr           | 488 ms                                                                                                                     | 412 ms: 1.18x faster                                                                                                           |
| richards_super             | 31.0 ms                                                                                                                    | 26.2 ms: 1.18x faster                                                                                                          |
| pprint_pformat             | 992 ms                                                                                                                     | 841 ms: 1.18x faster                                                                                                           |
| telco                      | 4.23 ms                                                                                                                    | 3.74 ms: 1.13x faster                                                                                                          |
| scimark_sparse_mat_mult    | 2.55 ms                                                                                                                    | 2.28 ms: 1.12x faster                                                                                                          |
| xml_etree_process          | 38.7 ms                                                                                                                    | 34.6 ms: 1.12x faster                                                                                                          |
| pyflate                    | 282 ms                                                                                                                     | 253 ms: 1.12x faster                                                                                                           |
| xml_etree_generate         | 55.4 ms                                                                                                                    | 50.8 ms: 1.09x faster                                                                                                          |
| regex_v8                   | 14.4 ms                                                                                                                    | 13.3 ms: 1.08x faster                                                                                                          |
| pickle_pure_python         | 212 us                                                                                                                     | 196 us: 1.08x faster                                                                                                           |
| k_core                     | 1.70 sec                                                                                                                   | 1.59 sec: 1.07x faster                                                                                                         |
| crypto_pyaes               | 47.6 ms                                                                                                                    | 44.7 ms: 1.07x faster                                                                                                          |
| sqlglot_v2_parse           | 816 us                                                                                                                     | 771 us: 1.06x faster                                                                                                           |
| logging_silent             | 56.5 ns                                                                                                                    | 53.4 ns: 1.06x faster                                                                                                          |
| unpickle_list              | 2.84 us                                                                                                                    | 2.69 us: 1.05x faster                                                                                                          |
| xml_etree_parse            | 88.9 ms                                                                                                                    | 84.5 ms: 1.05x faster                                                                                                          |
| raytrace                   | 178 ms                                                                                                                     | 170 ms: 1.05x faster                                                                                                           |
| regex_effbot               | 1.61 ms                                                                                                                    | 1.55 ms: 1.04x faster                                                                                                          |
| regex_dna                  | 120 ms                                                                                                                     | 115 ms: 1.04x faster                                                                                                           |
| dulwich_log                | 40.4 ms                                                                                                                    | 38.8 ms: 1.04x faster                                                                                                          |
| xml_etree_iterparse        | 63.9 ms                                                                                                                    | 61.5 ms: 1.04x faster                                                                                                          |
| sqlglot_v2_transpile       | 1.01 ms                                                                                                                    | 973 us: 1.04x faster                                                                                                           |
| json_loads                 | 14.3 us                                                                                                                    | 13.7 us: 1.04x faster                                                                                                          |
| connected_components       | 331 ms                                                                                                                     | 318 ms: 1.04x faster                                                                                                           |
| genshi_xml                 | 35.2 ms                                                                                                                    | 33.9 ms: 1.04x faster                                                                                                          |
| regex_compile              | 79.8 ms                                                                                                                    | 76.9 ms: 1.04x faster                                                                                                          |
| sqlite_synth               | 1.57 us                                                                                                                    | 1.51 us: 1.04x faster                                                                                                          |
| comprehensions             | 10.9 us                                                                                                                    | 10.6 us: 1.04x faster                                                                                                          |
| pycparser                  | 710 ms                                                                                                                     | 687 ms: 1.03x faster                                                                                                           |
| shortest_path              | 362 ms                                                                                                                     | 351 ms: 1.03x faster                                                                                                           |
| asyncio_websockets         | 164 ms                                                                                                                     | 159 ms: 1.03x faster                                                                                                           |
| mdp                        | 810 ms                                                                                                                     | 789 ms: 1.03x faster                                                                                                           |
| python_startup             | 25.5 ms                                                                                                                    | 24.8 ms: 1.03x faster                                                                                                          |
| coverage                   | 50.8 ms                                                                                                                    | 49.5 ms: 1.03x faster                                                                                                          |
| deltablue                  | 2.21 ms                                                                                                                    | 2.15 ms: 1.02x faster                                                                                                          |
| deepcopy_reduce            | 1.80 us                                                                                                                    | 1.76 us: 1.02x faster                                                                                                          |
| bench_mp_pool              | 89.9 ms                                                                                                                    | 87.9 ms: 1.02x faster                                                                                                          |
| scimark_monte_carlo        | 39.3 ms                                                                                                                    | 38.5 ms: 1.02x faster                                                                                                          |
| async_tree_io              | 388 ms                                                                                                                     | 380 ms: 1.02x faster                                                                                                           |
| asyncio_tcp                | 494 ms                                                                                                                     | 484 ms: 1.02x faster                                                                                                           |
| genshi_text                | 15.8 ms                                                                                                                    | 15.5 ms: 1.02x faster                                                                                                          |
| logging_format             | 6.55 us                                                                                                                    | 6.43 us: 1.02x faster                                                                                                          |
| sqlglot_v2_normalize       | 70.7 ms                                                                                                                    | 69.3 ms: 1.02x faster                                                                                                          |
| nqueens                    | 61.8 ms                                                                                                                    | 60.6 ms: 1.02x faster                                                                                                          |
| async_tree_none            | 172 ms                                                                                                                     | 168 ms: 1.02x faster                                                                                                           |
| json_dumps                 | 5.46 ms                                                                                                                    | 5.35 ms: 1.02x faster                                                                                                          |
| chaos                      | 40.4 ms                                                                                                                    | 39.7 ms: 1.02x faster                                                                                                          |
| sympy_sum                  | 86.8 ms                                                                                                                    | 85.2 ms: 1.02x faster                                                                                                          |
| typing_runtime_protocols   | 104 us                                                                                                                     | 103 us: 1.02x faster                                                                                                           |
| go                         | 75.7 ms                                                                                                                    | 74.7 ms: 1.01x faster                                                                                                          |
| html5lib                   | 38.5 ms                                                                                                                    | 38.0 ms: 1.01x faster                                                                                                          |
| generators                 | 19.3 ms                                                                                                                    | 19.1 ms: 1.01x faster                                                                                                          |
| deepcopy                   | 165 us                                                                                                                     | 163 us: 1.01x faster                                                                                                           |
| 2to3                       | 216 ms                                                                                                                     | 214 ms: 1.01x faster                                                                                                           |
| create_gc_cycles           | 1.29 ms                                                                                                                    | 1.27 ms: 1.01x faster                                                                                                          |
| sympy_str                  | 168 ms                                                                                                                     | 166 ms: 1.01x faster                                                                                                           |
| meteor_contest             | 72.2 ms                                                                                                                    | 71.8 ms: 1.01x faster                                                                                                          |
| subparsers                 | 29.6 ms                                                                                                                    | 29.5 ms: 1.00x faster                                                                                                          |
| async_tree_cpu_io_mixed_tg | 331 ms                                                                                                                     | 332 ms: 1.00x slower                                                                                                           |
| async_tree_cpu_io_mixed    | 324 ms                                                                                                                     | 327 ms: 1.01x slower                                                                                                           |
| sympy_expand               | 286 ms                                                                                                                     | 289 ms: 1.01x slower                                                                                                           |
| many_optionals             | 553 us                                                                                                                     | 560 us: 1.01x slower                                                                                                           |
| gc_traversal               | 2.06 ms                                                                                                                    | 2.09 ms: 1.01x slower                                                                                                          |
| unpickle                   | 8.52 us                                                                                                                    | 8.65 us: 1.02x slower                                                                                                          |
| hexiom                     | 4.00 ms                                                                                                                    | 4.07 ms: 1.02x slower                                                                                                          |
| float                      | 42.7 ms                                                                                                                    | 43.5 ms: 1.02x slower                                                                                                          |
| async_tree_memoization_tg  | 204 ms                                                                                                                     | 209 ms: 1.02x slower                                                                                                           |
| scimark_lu                 | 57.7 ms                                                                                                                    | 59.1 ms: 1.03x slower                                                                                                          |
| pickle_dict                | 19.7 us                                                                                                                    | 20.2 us: 1.03x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.32 sec                                                                                                                   | 1.37 sec: 1.04x slower                                                                                                         |
| coroutines                 | 14.7 ms                                                                                                                    | 15.3 ms: 1.04x slower                                                                                                          |
| spectral_norm              | 63.4 ms                                                                                                                    | 66.0 ms: 1.04x slower                                                                                                          |
| unpack_sequence            | 31.1 ns                                                                                                                    | 32.8 ns: 1.05x slower                                                                                                          |
| async_generators           | 227 ms                                                                                                                     | 242 ms: 1.07x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (20): bench_thread_pool, logging_simple, thrift, sphinx, async_tree_none_tg, pylint, async_tree_io_tg, pathlib, json, pickle, async_tree_memoization, docutils, scimark_sor, pickle_list, python_startup_no_site, deepcopy_memo, sqlglot_v2_optimize, pidigits, sympy_integrate, django_template

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown