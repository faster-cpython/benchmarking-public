# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-x86
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 253 ms: 1.08x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.89 sec: 1.04x slower                                                        |
| html5lib       | 45.4 ms                                                             | 49.9 ms: 1.10x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 95.2 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 495 ms: 1.07x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 190 ms: 1.07x faster                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 242 ms: 1.05x faster                                                          |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 459 ms: 1.03x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                  |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                          |
| float          | 52.4 ms                                                             | 60.9 ms: 1.16x slower                                                         |
| nbody          | 76.9 ms                                                             | 93.6 ms: 1.22x slower                                                         |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                         |
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.03x slower                                                         |
| regex_dna      | 118 ms                                                              | 124 ms: 1.05x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 106 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.1 ms: 1.05x slower                                                         |
| json_dumps           | 6.84 ms                                                             | 7.29 ms: 1.07x slower                                                         |
| tomli_loads          | 1.65 sec                                                            | 1.82 sec: 1.10x slower                                                        |
| xml_etree_generate   | 59.6 ms                                                             | 66.0 ms: 1.11x slower                                                         |
| pickle_pure_python   | 213 us                                                              | 245 us: 1.15x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 48.6 ms: 1.16x slower                                                         |
| unpickle_pure_python | 147 us                                                              | 171 us: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                         |
| python_startup_no_site | 18.2 ms                                                             | 18.8 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                               | 1.03x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 47.6 ms: 1.08x slower                                                         |
| genshi_text     | 20.1 ms                                                             | 22.0 ms: 1.09x slower                                                         |
| django_template | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                         |
| mako            | 6.94 ms                                                             | 8.10 ms: 1.17x slower                                                         |
| Geometric mean  | (ref)                                                               | 1.12x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 763 us: 12.75x faster                                                         |
| coverage                   | 307 ms                                                              | 51.5 ms: 5.97x faster                                                         |
| deepcopy                   | 280 us                                                              | 249 us: 1.12x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 21.6 us: 1.09x faster                                                         |
| async_tree_io_tg           | 529 ms                                                              | 495 ms: 1.07x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 190 ms: 1.07x faster                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 242 ms: 1.05x faster                                                          |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 749 us: 1.01x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.57 us: 1.01x faster                                                         |
| tornado_http               | 94.3 ms                                                             | 95.2 ms: 1.01x slower                                                         |
| bench_mp_pool              | 69.4 ms                                                             | 70.5 ms: 1.02x slower                                                         |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.02x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                         |
| sympy_expand               | 375 ms                                                              | 382 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 459 ms: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                          |
| python_startup             | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                         |
| telco                      | 6.03 ms                                                             | 6.23 ms: 1.03x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.03x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 18.8 ms: 1.03x slower                                                         |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.03x slower                                                         |
| json                       | 4.10 ms                                                             | 4.24 ms: 1.04x slower                                                         |
| docutils                   | 1.81 sec                                                            | 1.89 sec: 1.04x slower                                                        |
| crypto_pyaes               | 55.8 ms                                                             | 58.2 ms: 1.04x slower                                                         |
| mdp                        | 1.60 sec                                                            | 1.67 sec: 1.04x slower                                                        |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.1 ms: 1.05x slower                                                         |
| pylint                     | 217 ms                                                              | 227 ms: 1.05x slower                                                          |
| regex_dna                  | 118 ms                                                              | 124 ms: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                                         |
| regex_compile              | 99.9 ms                                                             | 106 ms: 1.06x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.29 ms: 1.07x slower                                                         |
| meteor_contest             | 74.1 ms                                                             | 79.4 ms: 1.07x slower                                                         |
| logging_format             | 8.13 us                                                             | 8.75 us: 1.08x slower                                                         |
| genshi_xml                 | 44.3 ms                                                             | 47.6 ms: 1.08x slower                                                         |
| logging_simple             | 7.47 us                                                             | 8.04 us: 1.08x slower                                                         |
| pprint_safe_repr           | 607 ms                                                              | 653 ms: 1.08x slower                                                          |
| pycparser                  | 777 ms                                                              | 838 ms: 1.08x slower                                                          |
| 2to3                       | 233 ms                                                              | 253 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.12 ms: 1.08x slower                                                         |
| pprint_pformat             | 1.24 sec                                                            | 1.35 sec: 1.09x slower                                                        |
| genshi_text                | 20.1 ms                                                             | 22.0 ms: 1.09x slower                                                         |
| scimark_fft                | 198 ms                                                              | 217 ms: 1.10x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 49.9 ms: 1.10x slower                                                         |
| async_generators           | 266 ms                                                              | 292 ms: 1.10x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.31 ms: 1.10x slower                                                         |
| tomli_loads                | 1.65 sec                                                            | 1.82 sec: 1.10x slower                                                        |
| sqlglot_normalize          | 206 ms                                                              | 228 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.0 ms: 1.11x slower                                                         |
| xml_etree_generate         | 59.6 ms                                                             | 66.0 ms: 1.11x slower                                                         |
| pyflate                    | 308 ms                                                              | 342 ms: 1.11x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                         |
| coroutines                 | 15.5 ms                                                             | 17.3 ms: 1.12x slower                                                         |
| chaos                      | 48.0 ms                                                             | 53.7 ms: 1.12x slower                                                         |
| spectral_norm              | 68.0 ms                                                             | 76.4 ms: 1.12x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 153 us: 1.13x slower                                                          |
| richards_super             | 35.5 ms                                                             | 40.1 ms: 1.13x slower                                                         |
| django_template            | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                         |
| nqueens                    | 68.7 ms                                                             | 77.8 ms: 1.13x slower                                                         |
| richards                   | 31.2 ms                                                             | 35.4 ms: 1.13x slower                                                         |
| go                         | 101 ms                                                              | 115 ms: 1.14x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 245 us: 1.15x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 48.6 ms: 1.16x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 68.7 ms: 1.16x slower                                                         |
| unpickle_pure_python       | 147 us                                                              | 171 us: 1.16x slower                                                          |
| float                      | 52.4 ms                                                             | 60.9 ms: 1.16x slower                                                         |
| mako                       | 6.94 ms                                                             | 8.10 ms: 1.17x slower                                                         |
| scimark_monte_carlo        | 45.2 ms                                                             | 53.1 ms: 1.17x slower                                                         |
| deltablue                  | 2.23 ms                                                             | 2.64 ms: 1.18x slower                                                         |
| comprehensions             | 11.9 us                                                             | 14.0 us: 1.18x slower                                                         |
| fannkuch                   | 270 ms                                                              | 320 ms: 1.19x slower                                                          |
| raytrace                   | 189 ms                                                              | 226 ms: 1.20x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 97.2 ms: 1.20x slower                                                         |
| hexiom                     | 4.23 ms                                                             | 5.09 ms: 1.20x slower                                                         |
| nbody                      | 76.9 ms                                                             | 93.6 ms: 1.22x slower                                                         |
| generators                 | 21.2 ms                                                             | 27.3 ms: 1.29x slower                                                         |
| logging_silent             | 57.9 ns                                                             | 75.1 ns: 1.30x slower                                                         |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                  |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed, bench_thread_pool, asyncio_tcp_ssl, pathlib, json_loads, gc_traversal, asyncio_tcp, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown