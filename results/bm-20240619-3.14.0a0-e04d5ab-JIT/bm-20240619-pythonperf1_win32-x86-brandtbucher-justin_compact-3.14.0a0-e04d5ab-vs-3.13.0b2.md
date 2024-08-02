# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.04x faster
- HPT reliability: 98.61%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                         |
| html5lib       | 45.4 ms                                                             | 48.0 ms: 1.06x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 97.9 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg          | 529 ms                                                              | 544 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed   | 471 ms                                                              | 486 ms: 1.03x slower                                                           |
| async_tree_io             | 530 ms                                                              | 552 ms: 1.04x slower                                                           |
| async_tree_none           | 228 ms                                                              | 238 ms: 1.04x slower                                                           |
| async_tree_memoization_tg | 254 ms                                                              | 266 ms: 1.05x slower                                                           |
| async_tree_none_tg        | 203 ms                                                              | 214 ms: 1.06x slower                                                           |
| async_tree_memoization    | 275 ms                                                              | 292 ms: 1.06x slower                                                           |
| Geometric mean            | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.4 ms: 1.47x faster                                                          |
| float          | 52.4 ms                                                             | 42.5 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.3 ms: 1.06x faster                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.65 sec                                                            | 1.46 sec: 1.13x faster                                                         |
| xml_etree_iterparse | 64.2 ms                                                             | 62.0 ms: 1.04x faster                                                          |
| unpickle_list       | 2.93 us                                                             | 2.86 us: 1.02x faster                                                          |
| xml_etree_generate  | 59.6 ms                                                             | 58.4 ms: 1.02x faster                                                          |
| pickle_pure_python  | 213 us                                                              | 209 us: 1.02x faster                                                           |
| pickle_dict         | 20.8 us                                                             | 20.5 us: 1.01x faster                                                          |
| xml_etree_parse     | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| pickle              | 8.07 us                                                             | 8.14 us: 1.01x slower                                                          |
| json_dumps          | 6.84 ms                                                             | 6.97 ms: 1.02x slower                                                          |
| xml_etree_process   | 42.1 ms                                                             | 43.2 ms: 1.03x slower                                                          |
| json_loads          | 20.5 us                                                             | 21.4 us: 1.04x slower                                                          |
| unpickle            | 9.79 us                                                             | 10.8 us: 1.10x slower                                                          |
| pickle_list         | 3.57 us                                                             | 4.05 us: 1.13x slower                                                          |
| Geometric mean      | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.8 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.7 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.34 ms: 1.30x faster                                                          |
| genshi_text     | 20.1 ms                                                             | 21.2 ms: 1.06x slower                                                          |
| django_template | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 48.5 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 9.73 ms                                                             | 757 us: 12.85x faster                                                          |
| coverage                  | 307 ms                                                              | 51.2 ms: 6.00x faster                                                          |
| deepcopy_memo             | 23.5 us                                                             | 15.5 us: 1.52x faster                                                          |
| nbody                     | 76.9 ms                                                             | 52.4 ms: 1.47x faster                                                          |
| spectral_norm             | 68.0 ms                                                             | 48.2 ms: 1.41x faster                                                          |
| mako                      | 6.94 ms                                                             | 5.34 ms: 1.30x faster                                                          |
| float                     | 52.4 ms                                                             | 42.5 ms: 1.23x faster                                                          |
| deepcopy                  | 280 us                                                              | 234 us: 1.19x faster                                                           |
| fannkuch                  | 270 ms                                                              | 228 ms: 1.18x faster                                                           |
| crypto_pyaes              | 55.8 ms                                                             | 48.0 ms: 1.16x faster                                                          |
| scimark_sparse_mat_mult   | 2.87 ms                                                             | 2.48 ms: 1.16x faster                                                          |
| scimark_fft               | 198 ms                                                              | 172 ms: 1.15x faster                                                           |
| tomli_loads               | 1.65 sec                                                            | 1.46 sec: 1.13x faster                                                         |
| pyflate                   | 308 ms                                                              | 279 ms: 1.10x faster                                                           |
| asyncio_tcp               | 662 ms                                                              | 608 ms: 1.09x faster                                                           |
| telco                     | 6.03 ms                                                             | 5.66 ms: 1.07x faster                                                          |
| pprint_safe_repr          | 607 ms                                                              | 572 ms: 1.06x faster                                                           |
| regex_compile             | 99.9 ms                                                             | 94.3 ms: 1.06x faster                                                          |
| comprehensions            | 11.9 us                                                             | 11.2 us: 1.06x faster                                                          |
| pprint_pformat            | 1.24 sec                                                            | 1.18 sec: 1.05x faster                                                         |
| deepcopy_reduce           | 2.59 us                                                             | 2.47 us: 1.05x faster                                                          |
| sqlglot_parse             | 964 us                                                              | 921 us: 1.05x faster                                                           |
| scimark_monte_carlo       | 45.2 ms                                                             | 43.6 ms: 1.04x faster                                                          |
| xml_etree_iterparse       | 64.2 ms                                                             | 62.0 ms: 1.04x faster                                                          |
| sqlite_synth              | 1.96 us                                                             | 1.90 us: 1.03x faster                                                          |
| unpickle_list             | 2.93 us                                                             | 2.86 us: 1.02x faster                                                          |
| bench_thread_pool         | 985 us                                                              | 964 us: 1.02x faster                                                           |
| xml_etree_generate        | 59.6 ms                                                             | 58.4 ms: 1.02x faster                                                          |
| pickle_pure_python        | 213 us                                                              | 209 us: 1.02x faster                                                           |
| pickle_dict               | 20.8 us                                                             | 20.5 us: 1.01x faster                                                          |
| logging_simple            | 7.47 us                                                             | 7.39 us: 1.01x faster                                                          |
| logging_format            | 8.13 us                                                             | 8.05 us: 1.01x faster                                                          |
| logging_silent            | 57.9 ns                                                             | 57.3 ns: 1.01x faster                                                          |
| pidigits                  | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| pathlib                   | 83.9 ms                                                             | 83.4 ms: 1.01x faster                                                          |
| xml_etree_parse           | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| sqlglot_transpile         | 1.19 ms                                                             | 1.18 ms: 1.01x faster                                                          |
| meteor_contest            | 74.1 ms                                                             | 74.2 ms: 1.00x slower                                                          |
| pickle                    | 8.07 us                                                             | 8.14 us: 1.01x slower                                                          |
| hexiom                    | 4.23 ms                                                             | 4.28 ms: 1.01x slower                                                          |
| json_dumps                | 6.84 ms                                                             | 6.97 ms: 1.02x slower                                                          |
| mdp                       | 1.60 sec                                                            | 1.64 sec: 1.03x slower                                                         |
| xml_etree_process         | 42.1 ms                                                             | 43.2 ms: 1.03x slower                                                          |
| async_tree_io_tg          | 529 ms                                                              | 544 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed   | 471 ms                                                              | 486 ms: 1.03x slower                                                           |
| sympy_str                 | 211 ms                                                              | 219 ms: 1.04x slower                                                           |
| nqueens                   | 68.7 ms                                                             | 71.2 ms: 1.04x slower                                                          |
| tornado_http              | 94.3 ms                                                             | 97.9 ms: 1.04x slower                                                          |
| json_loads                | 20.5 us                                                             | 21.4 us: 1.04x slower                                                          |
| async_tree_io             | 530 ms                                                              | 552 ms: 1.04x slower                                                           |
| sympy_expand              | 375 ms                                                              | 391 ms: 1.04x slower                                                           |
| sympy_sum                 | 105 ms                                                              | 110 ms: 1.04x slower                                                           |
| async_tree_none           | 228 ms                                                              | 238 ms: 1.04x slower                                                           |
| async_tree_memoization_tg | 254 ms                                                              | 266 ms: 1.05x slower                                                           |
| regex_effbot              | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| html5lib                  | 45.4 ms                                                             | 48.0 ms: 1.06x slower                                                          |
| genshi_text               | 20.1 ms                                                             | 21.2 ms: 1.06x slower                                                          |
| async_tree_none_tg        | 203 ms                                                              | 214 ms: 1.06x slower                                                           |
| pycparser                 | 777 ms                                                              | 823 ms: 1.06x slower                                                           |
| docutils                  | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                         |
| async_tree_memoization    | 275 ms                                                              | 292 ms: 1.06x slower                                                           |
| typing_runtime_protocols  | 136 us                                                              | 146 us: 1.07x slower                                                           |
| richards_super            | 35.5 ms                                                             | 38.2 ms: 1.08x slower                                                          |
| richards                  | 31.2 ms                                                             | 33.7 ms: 1.08x slower                                                          |
| sqlglot_optimize          | 39.7 ms                                                             | 43.0 ms: 1.08x slower                                                          |
| django_template           | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| bench_mp_pool             | 69.4 ms                                                             | 75.9 ms: 1.09x slower                                                          |
| sympy_integrate           | 14.6 ms                                                             | 16.1 ms: 1.10x slower                                                          |
| genshi_xml                | 44.3 ms                                                             | 48.5 ms: 1.10x slower                                                          |
| go                        | 101 ms                                                              | 111 ms: 1.10x slower                                                           |
| unpickle                  | 9.79 us                                                             | 10.8 us: 1.10x slower                                                          |
| 2to3                      | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| python_startup            | 22.2 ms                                                             | 24.8 ms: 1.12x slower                                                          |
| async_generators          | 266 ms                                                              | 298 ms: 1.12x slower                                                           |
| pylint                    | 217 ms                                                              | 244 ms: 1.13x slower                                                           |
| sqlglot_normalize         | 206 ms                                                              | 233 ms: 1.13x slower                                                           |
| chaos                     | 48.0 ms                                                             | 54.2 ms: 1.13x slower                                                          |
| python_startup_no_site    | 18.2 ms                                                             | 20.7 ms: 1.13x slower                                                          |
| pickle_list               | 3.57 us                                                             | 4.05 us: 1.13x slower                                                          |
| coroutines                | 15.5 ms                                                             | 17.6 ms: 1.14x slower                                                          |
| json                      | 4.10 ms                                                             | 4.84 ms: 1.18x slower                                                          |
| scimark_sor               | 81.0 ms                                                             | 96.9 ms: 1.20x slower                                                          |
| deltablue                 | 2.23 ms                                                             | 2.73 ms: 1.22x slower                                                          |
| raytrace                  | 189 ms                                                              | 232 ms: 1.23x slower                                                           |
| scimark_lu                | 59.4 ms                                                             | 75.2 ms: 1.27x slower                                                          |
| generators                | 21.2 ms                                                             | 27.6 ms: 1.31x slower                                                          |
| Geometric mean            | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (7): gc_traversal, create_gc_cycles, regex_v8, regex_dna, unpickle_pure_python, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging

# HPT report

- Reliability score: 98.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown