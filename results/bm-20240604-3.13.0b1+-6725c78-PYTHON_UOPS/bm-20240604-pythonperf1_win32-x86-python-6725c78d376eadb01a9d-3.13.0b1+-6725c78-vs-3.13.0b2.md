# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                            |
| chameleon      | 5.71 ms                                                             | 6.33 ms: 1.11x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                          |
| html5lib       | 45.4 ms                                                             | 50.7 ms: 1.12x slower                                                           |
| tornado_http   | 94.3 ms                                                             | 99.7 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 456 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 529 ms                                                              | 542 ms: 1.02x slower                                                            |
| async_tree_io              | 530 ms                                                              | 545 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 486 ms: 1.03x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.03x slower                                                            |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.04x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.04x slower                                                            |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 75.2 ms: 1.02x faster                                                           |
| float          | 52.4 ms                                                             | 52.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 124 ms: 1.24x slower                                                            |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.74 ms: 1.01x faster                                                           |
| xml_etree_parse      | 104 ms                                                              | 104 ms: 1.01x faster                                                            |
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                                           |
| unpickle_list        | 2.93 us                                                             | 2.95 us: 1.01x slower                                                           |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                           |
| pickle               | 8.07 us                                                             | 8.25 us: 1.02x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 43.1 ms: 1.02x slower                                                           |
| pickle_list          | 3.57 us                                                             | 3.65 us: 1.02x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 247 us: 1.16x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 172 us: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                             | 22.6 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 7.24 ms: 1.04x slower                                                           |
| genshi_text     | 20.1 ms                                                             | 21.2 ms: 1.05x slower                                                           |
| django_template | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                           |
| genshi_xml      | 44.3 ms                                                             | 50.1 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.08x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp                | 662 ms                                                              | 615 ms: 1.08x faster                                                            |
| telco                      | 6.03 ms                                                             | 5.80 ms: 1.04x faster                                                           |
| nbody                      | 76.9 ms                                                             | 75.2 ms: 1.02x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.93 us: 1.02x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.74 ms: 1.01x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 104 ms: 1.01x faster                                                            |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                                           |
| unpickle_list              | 2.93 us                                                             | 2.95 us: 1.01x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 15.6 ms: 1.01x slower                                                           |
| float                      | 52.4 ms                                                             | 52.9 ms: 1.01x slower                                                           |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| pprint_safe_repr           | 607 ms                                                              | 615 ms: 1.01x slower                                                            |
| create_gc_cycles           | 756 us                                                              | 766 us: 1.01x slower                                                            |
| crypto_pyaes               | 55.8 ms                                                             | 56.6 ms: 1.01x slower                                                           |
| python_startup             | 22.2 ms                                                             | 22.6 ms: 1.02x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                           |
| json                       | 4.10 ms                                                             | 4.18 ms: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 456 ms: 1.02x slower                                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.27 sec: 1.02x slower                                                          |
| pickle                     | 8.07 us                                                             | 8.25 us: 1.02x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 43.1 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 542 ms: 1.02x slower                                                            |
| pickle_list                | 3.57 us                                                             | 3.65 us: 1.02x slower                                                           |
| fannkuch                   | 270 ms                                                              | 277 ms: 1.03x slower                                                            |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 545 ms: 1.03x slower                                                            |
| bench_mp_pool              | 69.4 ms                                                             | 71.4 ms: 1.03x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.69 us: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 486 ms: 1.03x slower                                                            |
| meteor_contest             | 74.1 ms                                                             | 76.4 ms: 1.03x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.41 us: 1.03x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.03x slower                                                            |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.04x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.04x slower                                                            |
| mako                       | 6.94 ms                                                             | 7.24 ms: 1.04x slower                                                           |
| scimark_fft                | 198 ms                                                              | 207 ms: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.01 ms: 1.05x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 71.5 ms: 1.05x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 21.2 ms: 1.05x slower                                                           |
| coverage                   | 307 ms                                                              | 325 ms: 1.06x slower                                                            |
| tornado_http               | 94.3 ms                                                             | 99.7 ms: 1.06x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.02 ms: 1.06x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                            |
| nqueens                    | 68.7 ms                                                             | 73.6 ms: 1.07x slower                                                           |
| async_generators           | 266 ms                                                              | 285 ms: 1.07x slower                                                            |
| sqlglot_transpile          | 1.19 ms                                                             | 1.28 ms: 1.07x slower                                                           |
| django_template            | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.79 us: 1.08x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 147 us: 1.08x slower                                                            |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                            |
| scimark_monte_carlo        | 45.2 ms                                                             | 49.5 ms: 1.10x slower                                                           |
| deepcopy                   | 280 us                                                              | 308 us: 1.10x slower                                                            |
| docutils                   | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.0 ms: 1.11x slower                                                           |
| chameleon                  | 5.71 ms                                                             | 6.33 ms: 1.11x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.1 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 229 ms: 1.11x slower                                                            |
| generators                 | 21.2 ms                                                             | 23.6 ms: 1.12x slower                                                           |
| pylint                     | 217 ms                                                              | 242 ms: 1.12x slower                                                            |
| html5lib                   | 45.4 ms                                                             | 50.7 ms: 1.12x slower                                                           |
| sympy_expand               | 375 ms                                                              | 419 ms: 1.12x slower                                                            |
| sympy_integrate            | 14.6 ms                                                             | 16.4 ms: 1.12x slower                                                           |
| sympy_str                  | 211 ms                                                              | 237 ms: 1.12x slower                                                            |
| sympy_sum                  | 105 ms                                                              | 118 ms: 1.12x slower                                                            |
| go                         | 101 ms                                                              | 113 ms: 1.12x slower                                                            |
| raytrace                   | 189 ms                                                              | 212 ms: 1.13x slower                                                            |
| genshi_xml                 | 44.3 ms                                                             | 50.1 ms: 1.13x slower                                                           |
| pycparser                  | 777 ms                                                              | 882 ms: 1.14x slower                                                            |
| scimark_sor                | 81.0 ms                                                             | 93.0 ms: 1.15x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.7 us: 1.15x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 247 us: 1.16x slower                                                            |
| unpickle_pure_python       | 147 us                                                              | 172 us: 1.17x slower                                                            |
| deepcopy_memo              | 23.5 us                                                             | 27.6 us: 1.17x slower                                                           |
| thrift                     | 9.73 ms                                                             | 11.6 ms: 1.19x slower                                                           |
| pyflate                    | 308 ms                                                              | 371 ms: 1.21x slower                                                            |
| regex_compile              | 99.9 ms                                                             | 124 ms: 1.24x slower                                                            |
| deltablue                  | 2.23 ms                                                             | 2.83 ms: 1.27x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 74.2 ns: 1.28x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 5.66 ms: 1.34x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 80.0 ms: 1.35x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                                    |

Benchmark hidden because not significant (9): richards_super, pidigits, asyncio_tcp_ssl, xml_etree_iterparse, pathlib, flaskblogging, richards, gc_traversal, python_startup_no_site

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown