# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.01x faster
- HPT reliability: 78.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 245 ms: 1.05x slower                                                            |
| chameleon      | 5.71 ms                                                             | 6.12 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                          |
| html5lib       | 45.4 ms                                                             | 45.2 ms: 1.00x faster                                                           |
| tornado_http   | 94.3 ms                                                             | 96.7 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none | 228 ms                                                              | 225 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 54.6 ms: 1.41x faster                                                           |
| float          | 52.4 ms                                                             | 41.2 ms: 1.27x faster                                                           |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 93.9 ms: 1.06x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.95 ms: 1.04x slower                                                           |
| regex_dna      | 118 ms                                                              | 123 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.39 sec: 1.18x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 135 us: 1.09x faster                                                            |
| xml_etree_generate   | 59.6 ms                                                             | 55.6 ms: 1.07x faster                                                           |
| pickle_pure_python   | 213 us                                                              | 199 us: 1.07x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.1 ms: 1.05x faster                                                           |
| xml_etree_process    | 42.1 ms                                                             | 40.4 ms: 1.04x faster                                                           |
| json_dumps           | 6.84 ms                                                             | 6.68 ms: 1.02x faster                                                           |
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.02x faster                                                            |
| unpickle_list        | 2.93 us                                                             | 2.96 us: 1.01x slower                                                           |
| pickle_list          | 3.57 us                                                             | 3.63 us: 1.02x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): pickle, pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                           |
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.35 ms: 1.30x faster                                                           |
| django_template | 30.1 ms                                                             | 30.7 ms: 1.02x slower                                                           |
| genshi_text     | 20.1 ms                                                             | 21.4 ms: 1.06x slower                                                           |
| genshi_xml      | 44.3 ms                                                             | 51.7 ms: 1.17x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                    | 76.9 ms                                                             | 54.6 ms: 1.41x faster                                                           |
| spectral_norm            | 68.0 ms                                                             | 48.4 ms: 1.40x faster                                                           |
| mako                     | 6.94 ms                                                             | 5.35 ms: 1.30x faster                                                           |
| float                    | 52.4 ms                                                             | 41.2 ms: 1.27x faster                                                           |
| tomli_loads              | 1.65 sec                                                            | 1.39 sec: 1.18x faster                                                          |
| scimark_fft              | 198 ms                                                              | 168 ms: 1.18x faster                                                            |
| fannkuch                 | 270 ms                                                              | 229 ms: 1.18x faster                                                            |
| scimark_sparse_mat_mult  | 2.87 ms                                                             | 2.45 ms: 1.17x faster                                                           |
| crypto_pyaes             | 55.8 ms                                                             | 48.3 ms: 1.16x faster                                                           |
| deepcopy_memo            | 23.5 us                                                             | 20.6 us: 1.14x faster                                                           |
| scimark_monte_carlo      | 45.2 ms                                                             | 40.7 ms: 1.11x faster                                                           |
| telco                    | 6.03 ms                                                             | 5.49 ms: 1.10x faster                                                           |
| unpickle_pure_python     | 147 us                                                              | 135 us: 1.09x faster                                                            |
| pprint_pformat           | 1.24 sec                                                            | 1.14 sec: 1.09x faster                                                          |
| pprint_safe_repr         | 607 ms                                                              | 563 ms: 1.08x faster                                                            |
| xml_etree_generate       | 59.6 ms                                                             | 55.6 ms: 1.07x faster                                                           |
| pickle_pure_python       | 213 us                                                              | 199 us: 1.07x faster                                                            |
| regex_compile            | 99.9 ms                                                             | 93.9 ms: 1.06x faster                                                           |
| asyncio_tcp              | 662 ms                                                              | 625 ms: 1.06x faster                                                            |
| sqlglot_parse            | 964 us                                                              | 916 us: 1.05x faster                                                            |
| xml_etree_iterparse      | 64.2 ms                                                             | 61.1 ms: 1.05x faster                                                           |
| comprehensions           | 11.9 us                                                             | 11.4 us: 1.04x faster                                                           |
| xml_etree_process        | 42.1 ms                                                             | 40.4 ms: 1.04x faster                                                           |
| logging_silent           | 57.9 ns                                                             | 55.6 ns: 1.04x faster                                                           |
| logging_format           | 8.13 us                                                             | 7.82 us: 1.04x faster                                                           |
| logging_simple           | 7.47 us                                                             | 7.19 us: 1.04x faster                                                           |
| sqlite_synth             | 1.96 us                                                             | 1.90 us: 1.03x faster                                                           |
| json_dumps               | 6.84 ms                                                             | 6.68 ms: 1.02x faster                                                           |
| meteor_contest           | 74.1 ms                                                             | 72.5 ms: 1.02x faster                                                           |
| richards_super           | 35.5 ms                                                             | 34.9 ms: 1.02x faster                                                           |
| xml_etree_parse          | 104 ms                                                              | 103 ms: 1.02x faster                                                            |
| pidigits                 | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| async_tree_none          | 228 ms                                                              | 225 ms: 1.01x faster                                                            |
| pathlib                  | 83.9 ms                                                             | 83.3 ms: 1.01x faster                                                           |
| richards                 | 31.2 ms                                                             | 31.0 ms: 1.01x faster                                                           |
| sqlglot_transpile        | 1.19 ms                                                             | 1.18 ms: 1.01x faster                                                           |
| sympy_str                | 211 ms                                                              | 210 ms: 1.01x faster                                                            |
| html5lib                 | 45.4 ms                                                             | 45.2 ms: 1.00x faster                                                           |
| mdp                      | 1.60 sec                                                            | 1.61 sec: 1.00x slower                                                          |
| gc_traversal             | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                           |
| unpickle_list            | 2.93 us                                                             | 2.96 us: 1.01x slower                                                           |
| sympy_sum                | 105 ms                                                              | 106 ms: 1.01x slower                                                            |
| coroutines               | 15.5 ms                                                             | 15.7 ms: 1.01x slower                                                           |
| pycparser                | 777 ms                                                              | 789 ms: 1.02x slower                                                            |
| create_gc_cycles         | 756 us                                                              | 768 us: 1.02x slower                                                            |
| regex_v8                 | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                           |
| pickle_list              | 3.57 us                                                             | 3.63 us: 1.02x slower                                                           |
| django_template          | 30.1 ms                                                             | 30.7 ms: 1.02x slower                                                           |
| tornado_http             | 94.3 ms                                                             | 96.7 ms: 1.03x slower                                                           |
| json                     | 4.10 ms                                                             | 4.22 ms: 1.03x slower                                                           |
| docutils                 | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                          |
| regex_effbot             | 1.88 ms                                                             | 1.95 ms: 1.04x slower                                                           |
| regex_dna                | 118 ms                                                              | 123 ms: 1.04x slower                                                            |
| typing_runtime_protocols | 136 us                                                              | 141 us: 1.04x slower                                                            |
| pyflate                  | 308 ms                                                              | 321 ms: 1.04x slower                                                            |
| sqlglot_optimize         | 39.7 ms                                                             | 41.6 ms: 1.05x slower                                                           |
| 2to3                     | 233 ms                                                              | 245 ms: 1.05x slower                                                            |
| unpickle                 | 9.79 us                                                             | 10.3 us: 1.05x slower                                                           |
| thrift                   | 9.73 ms                                                             | 10.3 ms: 1.05x slower                                                           |
| deepcopy_reduce          | 2.59 us                                                             | 2.73 us: 1.06x slower                                                           |
| sympy_integrate          | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                           |
| genshi_text              | 20.1 ms                                                             | 21.4 ms: 1.06x slower                                                           |
| chameleon                | 5.71 ms                                                             | 6.12 ms: 1.07x slower                                                           |
| sqlglot_normalize        | 206 ms                                                              | 221 ms: 1.07x slower                                                            |
| coverage                 | 307 ms                                                              | 332 ms: 1.08x slower                                                            |
| hexiom                   | 4.23 ms                                                             | 4.57 ms: 1.08x slower                                                           |
| go                       | 101 ms                                                              | 109 ms: 1.08x slower                                                            |
| generators               | 21.2 ms                                                             | 23.0 ms: 1.09x slower                                                           |
| pylint                   | 217 ms                                                              | 236 ms: 1.09x slower                                                            |
| python_startup           | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                           |
| async_generators         | 266 ms                                                              | 291 ms: 1.10x slower                                                            |
| deepcopy                 | 280 us                                                              | 307 us: 1.10x slower                                                            |
| bench_mp_pool            | 69.4 ms                                                             | 76.4 ms: 1.10x slower                                                           |
| chaos                    | 48.0 ms                                                             | 52.9 ms: 1.10x slower                                                           |
| python_startup_no_site   | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                           |
| raytrace                 | 189 ms                                                              | 209 ms: 1.11x slower                                                            |
| scimark_sor              | 81.0 ms                                                             | 90.1 ms: 1.11x slower                                                           |
| deltablue                | 2.23 ms                                                             | 2.55 ms: 1.14x slower                                                           |
| genshi_xml               | 44.3 ms                                                             | 51.7 ms: 1.17x slower                                                           |
| scimark_lu               | 59.4 ms                                                             | 72.4 ms: 1.22x slower                                                           |
| Geometric mean           | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (15): async_tree_memoization, async_tree_io, nqueens, async_tree_io_tg, pickle, pickle_dict, asyncio_tcp_ssl, flaskblogging, sympy_expand, async_tree_cpu_io_mixed, async_tree_none_tg, json_loads, bench_thread_pool, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 78.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown