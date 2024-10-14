# Results vs. 3.13.0b2

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-x86
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 248 ms: 1.06x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.3 ms: 1.04x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 213 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 196 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 519 ms: 1.02x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 459 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| nbody          | 76.9 ms                                                             | 86.7 ms: 1.13x slower                                                          |
| float          | 52.4 ms                                                             | 60.9 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.84 ms: 1.03x faster                                                          |
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.42 us: 1.04x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.89 us: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.1 us: 1.03x slower                                                          |
| pickle_dict          | 20.8 us                                                             | 21.7 us: 1.04x slower                                                          |
| pickle               | 8.07 us                                                             | 8.55 us: 1.06x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.7 ms: 1.07x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 113 ms: 1.08x slower                                                           |
| tomli_loads          | 1.65 sec                                                            | 1.87 sec: 1.13x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 67.7 ms: 1.14x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 48.3 ms: 1.15x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 177 us: 1.20x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 265 us: 1.24x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 9.01 ms: 1.32x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.9 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.7 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 47.0 ms: 1.06x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.5 ms: 1.07x slower                                                          |
| mako            | 6.94 ms                                                             | 7.76 ms: 1.12x slower                                                          |
| django_template | 30.1 ms                                                             | 34.8 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 738 us: 13.18x faster                                                          |
| coverage                   | 307 ms                                                              | 52.7 ms: 5.83x faster                                                          |
| deepcopy                   | 280 us                                                              | 245 us: 1.14x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.3 us: 1.11x faster                                                          |
| async_tree_none            | 228 ms                                                              | 213 ms: 1.07x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.42 us: 1.04x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.49 us: 1.04x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 196 ms: 1.03x faster                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.84 ms: 1.03x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 519 ms: 1.02x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                           |
| unpickle_list              | 2.93 us                                                             | 2.89 us: 1.01x faster                                                          |
| go                         | 101 ms                                                              | 99.3 ms: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.97 us: 1.00x slower                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 139 us: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 459 ms: 1.03x slower                                                           |
| sympy_expand               | 375 ms                                                              | 386 ms: 1.03x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.1 us: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                         |
| create_gc_cycles           | 756 us                                                              | 783 us: 1.04x slower                                                           |
| sympy_str                  | 211 ms                                                              | 219 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.3 ms: 1.04x slower                                                          |
| pickle_dict                | 20.8 us                                                             | 21.7 us: 1.04x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.84 us: 1.05x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 88.1 ms: 1.05x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.57 us: 1.05x slower                                                          |
| pickle                     | 8.07 us                                                             | 8.55 us: 1.06x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.32 sec: 1.06x slower                                                         |
| genshi_xml                 | 44.3 ms                                                             | 47.0 ms: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.71 sec: 1.06x slower                                                         |
| pprint_safe_repr           | 607 ms                                                              | 645 ms: 1.06x slower                                                           |
| 2to3                       | 233 ms                                                              | 248 ms: 1.06x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 74.0 ms: 1.07x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.6 ms: 1.07x slower                                                          |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.7 ms: 1.07x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.5 ms: 1.07x slower                                                          |
| pycparser                  | 777 ms                                                              | 836 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.09 ms: 1.08x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 113 ms: 1.08x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 80.0 ms: 1.08x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 74.7 ms: 1.09x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 74.0 ms: 1.09x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.30 ms: 1.09x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 61.1 ms: 1.10x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.10x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.1 us: 1.11x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.0 ms: 1.11x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.5 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 229 ms: 1.11x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 738 ms: 1.12x slower                                                           |
| mako                       | 6.94 ms                                                             | 7.76 ms: 1.12x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.9 ms: 1.12x slower                                                          |
| nbody                      | 76.9 ms                                                             | 86.7 ms: 1.13x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                                          |
| async_generators           | 266 ms                                                              | 301 ms: 1.13x slower                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.87 sec: 1.13x slower                                                         |
| xml_etree_generate         | 59.6 ms                                                             | 67.7 ms: 1.14x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.7 ms: 1.14x slower                                                          |
| fannkuch                   | 270 ms                                                              | 308 ms: 1.14x slower                                                           |
| chaos                      | 48.0 ms                                                             | 55.0 ms: 1.15x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 48.3 ms: 1.15x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 68.5 ms: 1.15x slower                                                          |
| pyflate                    | 308 ms                                                              | 356 ms: 1.16x slower                                                           |
| django_template            | 30.1 ms                                                             | 34.8 ms: 1.16x slower                                                          |
| scimark_fft                | 198 ms                                                              | 229 ms: 1.16x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.98 ms: 1.16x slower                                                          |
| float                      | 52.4 ms                                                             | 60.9 ms: 1.16x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 67.4 ns: 1.16x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.96 ms: 1.17x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 177 us: 1.20x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.70 ms: 1.21x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 99.4 ms: 1.23x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.9 ms: 1.24x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 265 us: 1.24x slower                                                           |
| richards_super             | 35.5 ms                                                             | 45.3 ms: 1.28x slower                                                          |
| raytrace                   | 189 ms                                                              | 243 ms: 1.29x slower                                                           |
| richards                   | 31.2 ms                                                             | 40.5 ms: 1.30x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 9.01 ms: 1.32x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization_tg, regex_v8, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown