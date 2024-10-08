# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-x86
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.05x faster
- HPT reliability: 74.38%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.7 ms: 1.05x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 97.7 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 501 ms: 1.06x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 195 ms: 1.04x faster                                                           |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 469 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 54.9 ms: 1.40x faster                                                          |
| float          | 52.4 ms                                                             | 43.2 ms: 1.21x faster                                                          |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 96.0 ms: 1.04x faster                                                          |
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| xml_etree_iterparse | 64.2 ms                                                             | 61.4 ms: 1.05x faster                                                          |
| xml_etree_generate  | 59.6 ms                                                             | 62.1 ms: 1.04x slower                                                          |
| json_dumps          | 6.84 ms                                                             | 7.15 ms: 1.05x slower                                                          |
| json_loads          | 20.5 us                                                             | 21.6 us: 1.05x slower                                                          |
| xml_etree_process   | 42.1 ms                                                             | 44.4 ms: 1.06x slower                                                          |
| Geometric mean      | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.45 ms: 1.27x faster                                                          |
| django_template | 30.1 ms                                                             | 32.6 ms: 1.08x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.6 ms: 1.13x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.2 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 753 us: 12.93x faster                                                          |
| coverage                   | 307 ms                                                              | 51.1 ms: 6.01x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.2 us: 1.55x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 48.2 ms: 1.41x faster                                                          |
| nbody                      | 76.9 ms                                                             | 54.9 ms: 1.40x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.45 ms: 1.27x faster                                                          |
| float                      | 52.4 ms                                                             | 43.2 ms: 1.21x faster                                                          |
| deepcopy                   | 280 us                                                              | 237 us: 1.18x faster                                                           |
| scimark_fft                | 198 ms                                                              | 168 ms: 1.18x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.45 ms: 1.17x faster                                                          |
| fannkuch                   | 270 ms                                                              | 233 ms: 1.16x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 48.3 ms: 1.16x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| deepcopy_reduce            | 2.59 us                                                             | 2.37 us: 1.09x faster                                                          |
| pyflate                    | 308 ms                                                              | 283 ms: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                              | 609 ms: 1.09x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 560 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.9 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.15 sec: 1.07x faster                                                         |
| telco                      | 6.03 ms                                                             | 5.64 ms: 1.07x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.2 us: 1.06x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 501 ms: 1.06x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.4 ms: 1.05x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 195 ms: 1.04x faster                                                           |
| regex_compile              | 99.9 ms                                                             | 96.0 ms: 1.04x faster                                                          |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                           |
| sqlglot_parse              | 964 us                                                              | 941 us: 1.02x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 82.3 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| logging_format             | 8.13 us                                                             | 8.05 us: 1.01x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 57.3 ns: 1.01x faster                                                          |
| logging_simple             | 7.47 us                                                             | 7.40 us: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 74.6 ms: 1.01x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.21 ms: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                              | 385 ms: 1.03x slower                                                           |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                                           |
| python_startup             | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 97.7 ms: 1.04x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.04x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 62.1 ms: 1.04x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.15 ms: 1.05x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 469 ms: 1.05x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 47.7 ms: 1.05x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 72.2 ms: 1.05x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.6 us: 1.05x slower                                                          |
| richards                   | 31.2 ms                                                             | 32.9 ms: 1.05x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 44.4 ms: 1.06x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                         |
| bench_mp_pool              | 69.4 ms                                                             | 73.6 ms: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                         |
| pycparser                  | 777 ms                                                              | 834 ms: 1.07x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.56 ms: 1.08x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.9 ms: 1.08x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.6 ms: 1.08x slower                                                          |
| richards_super             | 35.5 ms                                                             | 38.6 ms: 1.09x slower                                                          |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 43.7 ms: 1.10x slower                                                          |
| json                       | 4.10 ms                                                             | 4.56 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 241 ms: 1.11x slower                                                           |
| chaos                      | 48.0 ms                                                             | 53.5 ms: 1.12x slower                                                          |
| go                         | 101 ms                                                              | 113 ms: 1.12x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.6 ms: 1.13x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 153 us: 1.13x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 236 ms: 1.15x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 17.8 ms: 1.15x slower                                                          |
| async_generators           | 266 ms                                                              | 308 ms: 1.16x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 53.2 ms: 1.20x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.74 ms: 1.23x slower                                                          |
| raytrace                   | 189 ms                                                              | 233 ms: 1.23x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 100 ms: 1.24x slower                                                           |
| generators                 | 21.2 ms                                                             | 27.6 ms: 1.30x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 77.8 ms: 1.31x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.05x faster                                                                   |

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_memoization, bench_thread_pool, unpickle_pure_python, gc_traversal, asyncio_tcp_ssl, create_gc_cycles, xml_etree_parse, pickle_pure_python, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 74.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown