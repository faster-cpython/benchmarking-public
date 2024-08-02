# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-x86
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 263 ms: 1.13x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.97 sec: 1.09x slower                                                         |
| html5lib       | 45.4 ms                                                             | 51.1 ms: 1.12x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 98.3 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 538 ms: 1.02x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 494 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                           |
| async_tree_none            | 228 ms                                                              | 240 ms: 1.05x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 292 ms: 1.06x slower                                                           |
| async_tree_io              | 530 ms                                                              | 577 ms: 1.09x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| float          | 52.4 ms                                                             | 67.9 ms: 1.30x slower                                                          |
| nbody          | 76.9 ms                                                             | 102 ms: 1.33x slower                                                           |
| Geometric mean | (ref)                                                               | 1.20x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 116 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.02x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 70.0 ms: 1.09x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.91 ms: 1.16x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.97 sec: 1.19x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 72.5 ms: 1.22x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 52.5 ms: 1.25x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 193 us: 1.31x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 285 us: 1.34x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.17x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.0 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 35.4 ms: 1.18x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 25.2 ms: 1.25x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 55.7 ms: 1.26x slower                                                          |
| mako            | 6.94 ms                                                             | 8.86 ms: 1.28x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.24x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 787 us: 12.37x faster                                                          |
| coverage                   | 307 ms                                                              | 51.1 ms: 6.01x faster                                                          |
| deepcopy                   | 280 us                                                              | 264 us: 1.06x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 741 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 84.3 ms: 1.01x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 538 ms: 1.02x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.02x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 71.3 ms: 1.03x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| python_startup             | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.04x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 98.3 ms: 1.04x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.0 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 494 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.73 us: 1.05x slower                                                          |
| async_tree_none            | 228 ms                                                              | 240 ms: 1.05x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.69 sec: 1.05x slower                                                         |
| async_tree_memoization     | 275 ms                                                              | 292 ms: 1.06x slower                                                           |
| json                       | 4.10 ms                                                             | 4.42 ms: 1.08x slower                                                          |
| deepcopy_memo              | 23.5 us                                                             | 25.5 us: 1.09x slower                                                          |
| async_tree_io              | 530 ms                                                              | 577 ms: 1.09x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.97 sec: 1.09x slower                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 70.0 ms: 1.09x slower                                                          |
| pylint                     | 217 ms                                                              | 237 ms: 1.09x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 115 ms: 1.09x slower                                                           |
| sympy_expand               | 375 ms                                                              | 410 ms: 1.09x slower                                                           |
| sympy_str                  | 211 ms                                                              | 232 ms: 1.10x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.69 ms: 1.11x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.3 ms: 1.11x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 82.6 ms: 1.12x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 51.1 ms: 1.12x slower                                                          |
| 2to3                       | 233 ms                                                              | 263 ms: 1.13x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 78.4 ms: 1.14x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.56 us: 1.15x slower                                                          |
| logging_format             | 8.13 us                                                             | 9.35 us: 1.15x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 64.5 ms: 1.15x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.91 ms: 1.16x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.45 sec: 1.17x slower                                                         |
| regex_compile              | 99.9 ms                                                             | 116 ms: 1.17x slower                                                           |
| async_generators           | 266 ms                                                              | 310 ms: 1.17x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 18.1 ms: 1.17x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 711 ms: 1.17x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 79.8 ms: 1.17x slower                                                          |
| pycparser                  | 777 ms                                                              | 913 ms: 1.18x slower                                                           |
| django_template            | 30.1 ms                                                             | 35.4 ms: 1.18x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 46.9 ms: 1.18x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 245 ms: 1.19x slower                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.97 sec: 1.19x slower                                                         |
| pyflate                    | 308 ms                                                              | 374 ms: 1.21x slower                                                           |
| chaos                      | 48.0 ms                                                             | 58.2 ms: 1.21x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 165 us: 1.21x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 72.5 ms: 1.22x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.51 ms: 1.22x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.46 ms: 1.23x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 52.5 ms: 1.25x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.20 ms: 1.25x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 25.2 ms: 1.25x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 55.7 ms: 1.26x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 75.0 ms: 1.26x slower                                                          |
| richards_super             | 35.5 ms                                                             | 44.9 ms: 1.27x slower                                                          |
| go                         | 101 ms                                                              | 128 ms: 1.27x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.86 ms: 1.28x slower                                                          |
| comprehensions             | 11.9 us                                                             | 15.2 us: 1.28x slower                                                          |
| raytrace                   | 189 ms                                                              | 242 ms: 1.28x slower                                                           |
| fannkuch                   | 270 ms                                                              | 349 ms: 1.29x slower                                                           |
| scimark_fft                | 198 ms                                                              | 256 ms: 1.29x slower                                                           |
| float                      | 52.4 ms                                                             | 67.9 ms: 1.30x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.90 ms: 1.30x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 106 ms: 1.31x slower                                                           |
| richards                   | 31.2 ms                                                             | 40.9 ms: 1.31x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 193 us: 1.31x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 5.56 ms: 1.32x slower                                                          |
| nbody                      | 76.9 ms                                                             | 102 ms: 1.33x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 285 us: 1.34x slower                                                           |
| generators                 | 21.2 ms                                                             | 28.6 ms: 1.35x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 62.1 ms: 1.37x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 79.9 ns: 1.38x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.09x slower                                                                   |

Benchmark hidden because not significant (4): regex_dna, asyncio_tcp_ssl, gc_traversal, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown