# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-x86
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 252 ms: 1.08x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.7 ms: 1.03x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 521 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 62.7 ms: 1.20x slower                                                          |
| nbody          | 76.9 ms                                                             | 93.9 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 118 ms: 1.00x faster                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 111 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.33 us: 1.07x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.5 us: 1.01x faster                                                          |
| pickle               | 8.07 us                                                             | 8.00 us: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.3 ms: 1.05x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.07 us: 1.05x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.5 us: 1.08x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.61 ms: 1.11x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 70.2 ms: 1.18x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 51.8 ms: 1.23x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 263 us: 1.24x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 188 us: 1.28x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.8 ms: 1.11x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.5 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| django_template | 30.1 ms                                                             | 34.7 ms: 1.15x slower                                                          |
| mako            | 6.94 ms                                                             | 8.31 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.14x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 743 us: 13.10x faster                                                          |
| coverage                   | 307 ms                                                              | 51.0 ms: 6.03x faster                                                          |
| deepcopy                   | 280 us                                                              | 250 us: 1.12x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.33 us: 1.07x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 723 us: 1.05x faster                                                           |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 521 ms: 1.02x faster                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.41 ms: 1.02x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.5 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| pickle                     | 8.07 us                                                             | 8.00 us: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 118 ms: 1.00x faster                                                           |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.99 us: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.02x slower                                                         |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                              | 384 ms: 1.02x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 46.7 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 87.2 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                           |
| json                       | 4.10 ms                                                             | 4.29 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.3 ms: 1.05x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 3.07 us: 1.05x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 696 ms: 1.05x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 59.0 ms: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.69 sec: 1.06x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 15.6 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.5 us: 1.08x slower                                                          |
| 2to3                       | 233 ms                                                              | 252 ms: 1.08x slower                                                           |
| pylint                     | 217 ms                                                              | 235 ms: 1.08x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 80.6 ms: 1.09x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.91 us: 1.10x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 48.5 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.15 ms: 1.10x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 75.5 ms: 1.10x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 668 ms: 1.10x slower                                                           |
| logging_simple             | 7.47 us                                                             | 8.23 us: 1.10x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 111 ms: 1.11x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| go                         | 101 ms                                                              | 111 ms: 1.11x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 77.0 ms: 1.11x slower                                                          |
| pycparser                  | 777 ms                                                              | 863 ms: 1.11x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.61 ms: 1.11x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.8 ms: 1.11x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.12x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.40 sec: 1.12x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.82 ms: 1.13x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.10 ms: 1.15x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.37 ms: 1.15x slower                                                          |
| django_template            | 30.1 ms                                                             | 34.7 ms: 1.15x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 238 ms: 1.15x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 45.8 ms: 1.15x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 78.6 ms: 1.16x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                         |
| async_generators           | 266 ms                                                              | 310 ms: 1.17x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.9 us: 1.17x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 70.2 ms: 1.18x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 70.5 ms: 1.19x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.5 ms: 1.19x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.31 ms: 1.20x slower                                                          |
| float                      | 52.4 ms                                                             | 62.7 ms: 1.20x slower                                                          |
| pyflate                    | 308 ms                                                              | 370 ms: 1.20x slower                                                           |
| scimark_fft                | 198 ms                                                              | 238 ms: 1.20x slower                                                           |
| chaos                      | 48.0 ms                                                             | 58.0 ms: 1.21x slower                                                          |
| nbody                      | 76.9 ms                                                             | 93.9 ms: 1.22x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 51.8 ms: 1.23x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 263 us: 1.24x slower                                                           |
| fannkuch                   | 270 ms                                                              | 340 ms: 1.26x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.81 ms: 1.26x slower                                                          |
| generators                 | 21.2 ms                                                             | 26.8 ms: 1.27x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.36 ms: 1.27x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 73.7 ns: 1.27x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 188 us: 1.28x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 104 ms: 1.28x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 58.3 ms: 1.29x slower                                                          |
| richards_super             | 35.5 ms                                                             | 46.8 ms: 1.32x slower                                                          |
| richards                   | 31.2 ms                                                             | 41.4 ms: 1.33x slower                                                          |
| raytrace                   | 189 ms                                                              | 252 ms: 1.34x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, deepcopy_memo, async_tree_memoization, deepcopy_reduce, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown