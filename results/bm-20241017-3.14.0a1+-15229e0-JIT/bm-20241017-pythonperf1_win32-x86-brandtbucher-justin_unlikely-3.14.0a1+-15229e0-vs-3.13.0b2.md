# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.01x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 264 ms: 1.13x slower                                                             |
| docutils       | 1.81 sec                                                            | 2.05 sec: 1.13x slower                                                           |
| html5lib       | 45.4 ms                                                             | 46.6 ms: 1.02x slower                                                            |
| tornado_http   | 94.3 ms                                                             | 110 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 462 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 462 ms: 1.03x slower                                                             |
| async_tree_io_tg           | 529 ms                                                              | 555 ms: 1.05x slower                                                             |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                     |

Benchmark hidden because not significant (4): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 57.1 ms: 1.35x faster                                                            |
| float          | 52.4 ms                                                             | 46.5 ms: 1.13x faster                                                            |
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                               | 1.15x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.80 ms: 1.05x faster                                                            |
| regex_v8       | 15.7 ms                                                             | 15.0 ms: 1.05x faster                                                            |
| regex_dna      | 118 ms                                                              | 113 ms: 1.04x faster                                                             |
| regex_compile  | 99.9 ms                                                             | 105 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.49 sec: 1.11x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 55.0 ms: 1.08x faster                                                            |
| pickle_list          | 3.57 us                                                             | 3.40 us: 1.05x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.0 ms: 1.02x faster                                                            |
| xml_etree_process    | 42.1 ms                                                             | 41.5 ms: 1.01x faster                                                            |
| unpickle_list        | 2.93 us                                                             | 2.98 us: 1.02x slower                                                            |
| pickle_dict          | 20.8 us                                                             | 21.2 us: 1.02x slower                                                            |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.04x slower                                                             |
| pickle               | 8.07 us                                                             | 8.55 us: 1.06x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 156 us: 1.06x slower                                                             |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.07x slower                                                            |
| pickle_pure_python   | 213 us                                                              | 244 us: 1.14x slower                                                             |
| json_dumps           | 6.84 ms                                                             | 7.95 ms: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                            |
| python_startup         | 22.2 ms                                                             | 26.8 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                               | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.82 ms: 1.19x faster                                                            |
| django_template | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                            |
| genshi_text     | 20.1 ms                                                             | 24.6 ms: 1.22x slower                                                            |
| genshi_xml      | 44.3 ms                                                             | 55.2 ms: 1.25x slower                                                            |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 794 us: 12.25x faster                                                            |
| coverage                   | 307 ms                                                              | 53.8 ms: 5.71x faster                                                            |
| sqlglot_normalize          | 206 ms                                                              | 103 ms: 2.00x faster                                                             |
| deepcopy_memo              | 23.5 us                                                             | 15.9 us: 1.47x faster                                                            |
| nbody                      | 76.9 ms                                                             | 57.1 ms: 1.35x faster                                                            |
| deepcopy                   | 280 us                                                              | 225 us: 1.24x faster                                                             |
| mako                       | 6.94 ms                                                             | 5.82 ms: 1.19x faster                                                            |
| scimark_sor                | 81.0 ms                                                             | 68.1 ms: 1.19x faster                                                            |
| spectral_norm              | 68.0 ms                                                             | 58.3 ms: 1.17x faster                                                            |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.6 ms: 1.14x faster                                                            |
| deepcopy_reduce            | 2.59 us                                                             | 2.28 us: 1.13x faster                                                            |
| float                      | 52.4 ms                                                             | 46.5 ms: 1.13x faster                                                            |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.55 ms: 1.13x faster                                                            |
| crypto_pyaes               | 55.8 ms                                                             | 50.0 ms: 1.12x faster                                                            |
| tomli_loads                | 1.65 sec                                                            | 1.49 sec: 1.11x faster                                                           |
| fannkuch                   | 270 ms                                                              | 244 ms: 1.11x faster                                                             |
| scimark_fft                | 198 ms                                                              | 183 ms: 1.09x faster                                                             |
| xml_etree_generate         | 59.6 ms                                                             | 55.0 ms: 1.08x faster                                                            |
| pprint_safe_repr           | 607 ms                                                              | 564 ms: 1.08x faster                                                             |
| pprint_pformat             | 1.24 sec                                                            | 1.17 sec: 1.06x faster                                                           |
| go                         | 101 ms                                                              | 94.8 ms: 1.06x faster                                                            |
| logging_silent             | 57.9 ns                                                             | 54.6 ns: 1.06x faster                                                            |
| pickle_list                | 3.57 us                                                             | 3.40 us: 1.05x faster                                                            |
| regex_effbot               | 1.88 ms                                                             | 1.80 ms: 1.05x faster                                                            |
| regex_v8                   | 15.7 ms                                                             | 15.0 ms: 1.05x faster                                                            |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                             |
| regex_dna                  | 118 ms                                                              | 113 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 462 ms: 1.02x faster                                                             |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.0 ms: 1.02x faster                                                            |
| xml_etree_process          | 42.1 ms                                                             | 41.5 ms: 1.01x faster                                                            |
| meteor_contest             | 74.1 ms                                                             | 73.1 ms: 1.01x faster                                                            |
| telco                      | 6.03 ms                                                             | 5.95 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                             |
| pyflate                    | 308 ms                                                              | 311 ms: 1.01x slower                                                             |
| unpickle_list              | 2.93 us                                                             | 2.98 us: 1.02x slower                                                            |
| scimark_lu                 | 59.4 ms                                                             | 60.6 ms: 1.02x slower                                                            |
| pickle_dict                | 20.8 us                                                             | 21.2 us: 1.02x slower                                                            |
| logging_simple             | 7.47 us                                                             | 7.65 us: 1.02x slower                                                            |
| html5lib                   | 45.4 ms                                                             | 46.6 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 136 us                                                              | 139 us: 1.03x slower                                                             |
| logging_format             | 8.13 us                                                             | 8.37 us: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 462 ms: 1.03x slower                                                             |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.5 sec: 1.04x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.04x slower                                                             |
| pathlib                    | 83.9 ms                                                             | 87.7 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 529 ms                                                              | 555 ms: 1.05x slower                                                             |
| regex_compile              | 99.9 ms                                                             | 105 ms: 1.06x slower                                                             |
| sympy_expand               | 375 ms                                                              | 397 ms: 1.06x slower                                                             |
| pickle                     | 8.07 us                                                             | 8.55 us: 1.06x slower                                                            |
| unpickle_pure_python       | 147 us                                                              | 156 us: 1.06x slower                                                             |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.07x slower                                                            |
| pycparser                  | 777 ms                                                              | 833 ms: 1.07x slower                                                             |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                                            |
| sympy_str                  | 211 ms                                                              | 231 ms: 1.09x slower                                                             |
| django_template            | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                            |
| comprehensions             | 11.9 us                                                             | 13.2 us: 1.11x slower                                                            |
| python_startup_no_site     | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                            |
| coroutines                 | 15.5 ms                                                             | 17.4 ms: 1.12x slower                                                            |
| mdp                        | 1.60 sec                                                            | 1.80 sec: 1.13x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 77.4 ms: 1.13x slower                                                            |
| sympy_sum                  | 105 ms                                                              | 119 ms: 1.13x slower                                                             |
| docutils                   | 1.81 sec                                                            | 2.05 sec: 1.13x slower                                                           |
| 2to3                       | 233 ms                                                              | 264 ms: 1.13x slower                                                             |
| pickle_pure_python         | 213 us                                                              | 244 us: 1.14x slower                                                             |
| sqlglot_transpile          | 1.19 ms                                                             | 1.37 ms: 1.15x slower                                                            |
| generators                 | 21.2 ms                                                             | 24.3 ms: 1.15x slower                                                            |
| chaos                      | 48.0 ms                                                             | 55.2 ms: 1.15x slower                                                            |
| deltablue                  | 2.23 ms                                                             | 2.57 ms: 1.15x slower                                                            |
| json_dumps                 | 6.84 ms                                                             | 7.95 ms: 1.16x slower                                                            |
| tornado_http               | 94.3 ms                                                             | 110 ms: 1.16x slower                                                             |
| async_generators           | 266 ms                                                              | 314 ms: 1.18x slower                                                             |
| sympy_integrate            | 14.6 ms                                                             | 17.4 ms: 1.19x slower                                                            |
| python_startup             | 22.2 ms                                                             | 26.8 ms: 1.21x slower                                                            |
| genshi_text                | 20.1 ms                                                             | 24.6 ms: 1.22x slower                                                            |
| json                       | 4.10 ms                                                             | 5.06 ms: 1.23x slower                                                            |
| genshi_xml                 | 44.3 ms                                                             | 55.2 ms: 1.25x slower                                                            |
| asyncio_tcp                | 662 ms                                                              | 832 ms: 1.26x slower                                                             |
| richards                   | 31.2 ms                                                             | 39.3 ms: 1.26x slower                                                            |
| sqlglot_optimize           | 39.7 ms                                                             | 50.3 ms: 1.27x slower                                                            |
| hexiom                     | 4.23 ms                                                             | 5.39 ms: 1.27x slower                                                            |
| gc_traversal               | 1.43 ms                                                             | 1.83 ms: 1.27x slower                                                            |
| richards_super             | 35.5 ms                                                             | 46.2 ms: 1.30x slower                                                            |
| pylint                     | 217 ms                                                              | 286 ms: 1.32x slower                                                             |
| bench_mp_pool              | 69.4 ms                                                             | 95.5 ms: 1.38x slower                                                            |
| raytrace                   | 189 ms                                                              | 273 ms: 1.45x slower                                                             |
| create_gc_cycles           | 756 us                                                              | 1.19 ms: 1.57x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                     |

Benchmark hidden because not significant (7): async_tree_io, json_loads, sqlite_synth, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (3) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: dulwich_log, sphinx, unpack_sequence

# HPT report

- Reliability score: 98.52% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown