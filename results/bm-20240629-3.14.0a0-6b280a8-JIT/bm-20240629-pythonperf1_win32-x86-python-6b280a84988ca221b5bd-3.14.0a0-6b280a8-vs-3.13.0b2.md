# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-x86
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.48%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 262 ms: 1.12x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.99 sec: 1.10x slower                                                         |
| html5lib       | 45.4 ms                                                             | 51.6 ms: 1.14x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 101 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 536 ms: 1.01x slower                                                           |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.04x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 268 ms: 1.05x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 214 ms: 1.06x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 291 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 505 ms: 1.07x slower                                                           |
| async_tree_io              | 530 ms                                                              | 573 ms: 1.08x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 493 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.2 ms: 1.47x faster                                                          |
| float          | 52.4 ms                                                             | 44.7 ms: 1.17x faster                                                          |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 99.5 ms: 1.00x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| regex_dna      | 118 ms                                                              | 125 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.59 sec: 1.04x faster                                                         |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 220 us: 1.03x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 7.19 ms: 1.05x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 62.8 ms: 1.05x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 162 us: 1.10x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 48.9 ms: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 25.0 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 21.0 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                          |
| genshi_text     | 20.1 ms                                                             | 23.8 ms: 1.18x slower                                                          |
| django_template | 30.1 ms                                                             | 35.8 ms: 1.19x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 56.1 ms: 1.27x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 790 us: 12.32x faster                                                          |
| coverage                   | 307 ms                                                              | 51.1 ms: 6.02x faster                                                          |
| sqlglot_normalize          | 206 ms                                                              | 102 ms: 2.02x faster                                                           |
| nbody                      | 76.9 ms                                                             | 52.2 ms: 1.47x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 16.1 us: 1.46x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.3 ms: 1.44x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.36 ms: 1.21x faster                                                          |
| fannkuch                   | 270 ms                                                              | 225 ms: 1.20x faster                                                           |
| float                      | 52.4 ms                                                             | 44.7 ms: 1.17x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 48.7 ms: 1.15x faster                                                          |
| scimark_fft                | 198 ms                                                              | 174 ms: 1.14x faster                                                           |
| deepcopy                   | 280 us                                                              | 253 us: 1.11x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.67 ms: 1.06x faster                                                          |
| pyflate                    | 308 ms                                                              | 291 ms: 1.06x faster                                                           |
| asyncio_tcp                | 662 ms                                                              | 633 ms: 1.05x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.3 us: 1.04x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 43.4 ms: 1.04x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.59 sec: 1.04x faster                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 592 ms: 1.02x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.21 sec: 1.02x faster                                                         |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 82.9 ms: 1.01x faster                                                          |
| regex_compile              | 99.9 ms                                                             | 99.5 ms: 1.00x faster                                                          |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 536 ms: 1.01x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 979 us: 1.02x slower                                                           |
| json                       | 4.10 ms                                                             | 4.21 ms: 1.03x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 76.4 ms: 1.03x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 220 us: 1.03x slower                                                           |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.04x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 60.0 ns: 1.04x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.25 ms: 1.05x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| json_dumps                 | 6.84 ms                                                             | 7.19 ms: 1.05x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 62.8 ms: 1.05x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 268 ms: 1.05x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| async_tree_none_tg         | 203 ms                                                              | 214 ms: 1.06x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 291 ms: 1.06x slower                                                           |
| regex_dna                  | 118 ms                                                              | 125 ms: 1.06x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.63 us: 1.06x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.96 us: 1.07x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 113 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 505 ms: 1.07x slower                                                           |
| sympy_str                  | 211 ms                                                              | 226 ms: 1.07x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 101 ms: 1.07x slower                                                           |
| sympy_expand               | 375 ms                                                              | 405 ms: 1.08x slower                                                           |
| async_tree_io              | 530 ms                                                              | 573 ms: 1.08x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 75.3 ms: 1.08x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 74.9 ms: 1.09x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.61 ms: 1.09x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.99 sec: 1.10x slower                                                         |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 493 ms: 1.10x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 162 us: 1.10x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 16.3 ms: 1.11x slower                                                          |
| 2to3                       | 233 ms                                                              | 262 ms: 1.12x slower                                                           |
| python_startup             | 22.2 ms                                                             | 25.0 ms: 1.12x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 51.6 ms: 1.14x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 45.4 ms: 1.14x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 21.0 ms: 1.15x slower                                                          |
| pycparser                  | 777 ms                                                              | 899 ms: 1.16x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 48.9 ms: 1.16x slower                                                          |
| chaos                      | 48.0 ms                                                             | 55.7 ms: 1.16x slower                                                          |
| pylint                     | 217 ms                                                              | 254 ms: 1.17x slower                                                           |
| richards                   | 31.2 ms                                                             | 36.9 ms: 1.18x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 23.8 ms: 1.18x slower                                                          |
| django_template            | 30.1 ms                                                             | 35.8 ms: 1.19x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 162 us: 1.19x slower                                                           |
| richards_super             | 35.5 ms                                                             | 42.4 ms: 1.20x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.7 ms: 1.21x slower                                                          |
| go                         | 101 ms                                                              | 122 ms: 1.22x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 56.1 ms: 1.27x slower                                                          |
| async_generators           | 266 ms                                                              | 340 ms: 1.28x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.92 ms: 1.31x slower                                                          |
| raytrace                   | 189 ms                                                              | 253 ms: 1.34x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 80.9 ms: 1.36x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 111 ms: 1.38x slower                                                           |
| generators                 | 21.2 ms                                                             | 29.5 ms: 1.39x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, create_gc_cycles, asyncio_tcp_ssl, deepcopy_reduce, gc_traversal, xml_etree_parse
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.48% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown