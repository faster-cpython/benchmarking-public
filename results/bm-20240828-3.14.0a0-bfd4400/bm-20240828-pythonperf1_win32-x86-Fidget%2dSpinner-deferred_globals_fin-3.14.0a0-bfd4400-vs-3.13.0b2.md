# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-x86
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.10x slower                                                                     |
| docutils       | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                                   |
| html5lib       | 45.4 ms                                                             | 48.8 ms: 1.07x slower                                                                    |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 514 ms: 1.03x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                                     |
| async_tree_io              | 530 ms                                                              | 553 ms: 1.04x slower                                                                     |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                                     |
| float          | 52.4 ms                                                             | 62.8 ms: 1.20x slower                                                                    |
| nbody          | 76.9 ms                                                             | 92.7 ms: 1.21x slower                                                                    |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                                    |
| regex_v8       | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                                    |
| regex_compile  | 99.9 ms                                                             | 109 ms: 1.10x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.04x slower                                                                     |
| json_loads           | 20.5 us                                                             | 21.3 us: 1.04x slower                                                                    |
| xml_etree_iterparse  | 64.2 ms                                                             | 69.8 ms: 1.09x slower                                                                    |
| json_dumps           | 6.84 ms                                                             | 7.47 ms: 1.09x slower                                                                    |
| xml_etree_generate   | 59.6 ms                                                             | 68.1 ms: 1.14x slower                                                                    |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                                   |
| unpickle_pure_python | 147 us                                                              | 178 us: 1.21x slower                                                                     |
| xml_etree_process    | 42.1 ms                                                             | 51.2 ms: 1.22x slower                                                                    |
| pickle_pure_python   | 213 us                                                              | 262 us: 1.23x slower                                                                     |
| Geometric mean       | (ref)                                                               | 1.13x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                                    |
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                                    |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.6 ms: 1.10x slower                                                                    |
| django_template | 30.1 ms                                                             | 33.2 ms: 1.10x slower                                                                    |
| genshi_text     | 20.1 ms                                                             | 23.1 ms: 1.15x slower                                                                    |
| mako            | 6.94 ms                                                             | 8.27 ms: 1.19x slower                                                                    |
| Geometric mean  | (ref)                                                               | 1.13x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 749 us: 12.98x faster                                                                    |
| coverage                   | 307 ms                                                              | 54.0 ms: 5.69x faster                                                                    |
| deepcopy                   | 280 us                                                              | 252 us: 1.11x faster                                                                     |
| deepcopy_reduce            | 2.59 us                                                             | 2.50 us: 1.04x faster                                                                    |
| async_tree_io_tg           | 529 ms                                                              | 514 ms: 1.03x faster                                                                     |
| deepcopy_memo              | 23.5 us                                                             | 23.0 us: 1.02x faster                                                                    |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                                     |
| gc_traversal               | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                                    |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                                                   |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                                     |
| pathlib                    | 83.9 ms                                                             | 86.5 ms: 1.03x slower                                                                    |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.04x slower                                                                     |
| sympy_expand               | 375 ms                                                              | 389 ms: 1.04x slower                                                                     |
| json_loads                 | 20.5 us                                                             | 21.3 us: 1.04x slower                                                                    |
| json                       | 4.10 ms                                                             | 4.25 ms: 1.04x slower                                                                    |
| regex_v8                   | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                                    |
| async_tree_io              | 530 ms                                                              | 553 ms: 1.04x slower                                                                     |
| logging_format             | 8.13 us                                                             | 8.49 us: 1.04x slower                                                                    |
| bench_mp_pool              | 69.4 ms                                                             | 73.1 ms: 1.05x slower                                                                    |
| sympy_str                  | 211 ms                                                              | 222 ms: 1.05x slower                                                                     |
| bench_thread_pool          | 985 us                                                              | 1.04 ms: 1.06x slower                                                                    |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                                   |
| crypto_pyaes               | 55.8 ms                                                             | 59.5 ms: 1.07x slower                                                                    |
| sympy_sum                  | 105 ms                                                              | 112 ms: 1.07x slower                                                                     |
| logging_simple             | 7.47 us                                                             | 7.99 us: 1.07x slower                                                                    |
| docutils                   | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                                   |
| sympy_integrate            | 14.6 ms                                                             | 15.7 ms: 1.07x slower                                                                    |
| html5lib                   | 45.4 ms                                                             | 48.8 ms: 1.07x slower                                                                    |
| telco                      | 6.03 ms                                                             | 6.49 ms: 1.08x slower                                                                    |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                                    |
| pylint                     | 217 ms                                                              | 236 ms: 1.09x slower                                                                     |
| xml_etree_iterparse        | 64.2 ms                                                             | 69.8 ms: 1.09x slower                                                                    |
| asyncio_tcp                | 662 ms                                                              | 722 ms: 1.09x slower                                                                     |
| json_dumps                 | 6.84 ms                                                             | 7.47 ms: 1.09x slower                                                                    |
| regex_compile              | 99.9 ms                                                             | 109 ms: 1.10x slower                                                                     |
| meteor_contest             | 74.1 ms                                                             | 81.2 ms: 1.10x slower                                                                    |
| genshi_xml                 | 44.3 ms                                                             | 48.6 ms: 1.10x slower                                                                    |
| python_startup_no_site     | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                                    |
| pycparser                  | 777 ms                                                              | 857 ms: 1.10x slower                                                                     |
| django_template            | 30.1 ms                                                             | 33.2 ms: 1.10x slower                                                                    |
| 2to3                       | 233 ms                                                              | 258 ms: 1.10x slower                                                                     |
| pprint_safe_repr           | 607 ms                                                              | 672 ms: 1.11x slower                                                                     |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                                     |
| typing_runtime_protocols   | 136 us                                                              | 152 us: 1.12x slower                                                                     |
| chaos                      | 48.0 ms                                                             | 54.0 ms: 1.13x slower                                                                    |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.13x slower                                                                    |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.24 ms: 1.13x slower                                                                    |
| sqlglot_optimize           | 39.7 ms                                                             | 45.0 ms: 1.13x slower                                                                    |
| sqlglot_normalize          | 206 ms                                                              | 233 ms: 1.13x slower                                                                     |
| sqlglot_parse              | 964 us                                                              | 1.10 ms: 1.14x slower                                                                    |
| pprint_pformat             | 1.24 sec                                                            | 1.41 sec: 1.14x slower                                                                   |
| xml_etree_generate         | 59.6 ms                                                             | 68.1 ms: 1.14x slower                                                                    |
| async_generators           | 266 ms                                                              | 304 ms: 1.15x slower                                                                     |
| genshi_text                | 20.1 ms                                                             | 23.1 ms: 1.15x slower                                                                    |
| spectral_norm              | 68.0 ms                                                             | 78.4 ms: 1.15x slower                                                                    |
| tomli_loads                | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                                   |
| nqueens                    | 68.7 ms                                                             | 81.6 ms: 1.19x slower                                                                    |
| mako                       | 6.94 ms                                                             | 8.27 ms: 1.19x slower                                                                    |
| scimark_lu                 | 59.4 ms                                                             | 71.0 ms: 1.20x slower                                                                    |
| float                      | 52.4 ms                                                             | 62.8 ms: 1.20x slower                                                                    |
| coroutines                 | 15.5 ms                                                             | 18.6 ms: 1.20x slower                                                                    |
| nbody                      | 76.9 ms                                                             | 92.7 ms: 1.21x slower                                                                    |
| pyflate                    | 308 ms                                                              | 372 ms: 1.21x slower                                                                     |
| raytrace                   | 189 ms                                                              | 228 ms: 1.21x slower                                                                     |
| comprehensions             | 11.9 us                                                             | 14.4 us: 1.21x slower                                                                    |
| unpickle_pure_python       | 147 us                                                              | 178 us: 1.21x slower                                                                     |
| scimark_fft                | 198 ms                                                              | 241 ms: 1.21x slower                                                                     |
| xml_etree_process          | 42.1 ms                                                             | 51.2 ms: 1.22x slower                                                                    |
| go                         | 101 ms                                                              | 122 ms: 1.22x slower                                                                     |
| fannkuch                   | 270 ms                                                              | 329 ms: 1.22x slower                                                                     |
| pickle_pure_python         | 213 us                                                              | 262 us: 1.23x slower                                                                     |
| deltablue                  | 2.23 ms                                                             | 2.76 ms: 1.23x slower                                                                    |
| richards_super             | 35.5 ms                                                             | 45.0 ms: 1.27x slower                                                                    |
| generators                 | 21.2 ms                                                             | 27.0 ms: 1.28x slower                                                                    |
| scimark_sor                | 81.0 ms                                                             | 104 ms: 1.28x slower                                                                     |
| richards                   | 31.2 ms                                                             | 40.0 ms: 1.28x slower                                                                    |
| hexiom                     | 4.23 ms                                                             | 5.42 ms: 1.28x slower                                                                    |
| scimark_monte_carlo        | 45.2 ms                                                             | 58.9 ms: 1.30x slower                                                                    |
| logging_silent             | 57.9 ns                                                             | 75.6 ns: 1.31x slower                                                                    |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                             |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, regex_dna, async_tree_memoization, create_gc_cycles
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown