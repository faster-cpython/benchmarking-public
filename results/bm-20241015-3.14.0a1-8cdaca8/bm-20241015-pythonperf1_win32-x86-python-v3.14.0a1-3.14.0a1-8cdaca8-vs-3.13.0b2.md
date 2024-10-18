# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 246 ms: 1.06x slower                                                |
| docutils       | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                              |
| html5lib       | 45.4 ms                                                             | 44.9 ms: 1.01x faster                                               |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                               | 1.04x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 465 ms: 1.04x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 558 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                        |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 87.2 ms: 1.13x slower                                               |
| float          | 52.4 ms                                                             | 61.9 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                               | 1.10x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.82 ms: 1.03x faster                                               |
| regex_compile  | 99.9 ms                                                             | 105 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                               | 1.00x slower                                                        |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.49 us: 1.02x faster                                               |
| unpickle_list        | 2.93 us                                                             | 2.98 us: 1.02x slower                                               |
| pickle_dict          | 20.8 us                                                             | 21.6 us: 1.04x slower                                               |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                               |
| pickle               | 8.07 us                                                             | 8.56 us: 1.06x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 113 ms: 1.08x slower                                                |
| xml_etree_iterparse  | 64.2 ms                                                             | 69.5 ms: 1.08x slower                                               |
| xml_etree_generate   | 59.6 ms                                                             | 66.5 ms: 1.12x slower                                               |
| xml_etree_process    | 42.1 ms                                                             | 47.6 ms: 1.13x slower                                               |
| tomli_loads          | 1.65 sec                                                            | 1.87 sec: 1.13x slower                                              |
| unpickle_pure_python | 147 us                                                              | 178 us: 1.21x slower                                                |
| pickle_pure_python   | 213 us                                                              | 265 us: 1.25x slower                                                |
| json_dumps           | 6.84 ms                                                             | 9.09 ms: 1.33x slower                                               |
| Geometric mean       | (ref)                                                               | 1.10x slower                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                               |
| python_startup         | 22.2 ms                                                             | 26.6 ms: 1.20x slower                                               |
| Geometric mean         | (ref)                                                               | 1.15x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 20.6 ms: 1.03x slower                                               |
| genshi_xml      | 44.3 ms                                                             | 45.9 ms: 1.04x slower                                               |
| django_template | 30.1 ms                                                             | 32.5 ms: 1.08x slower                                               |
| mako            | 6.94 ms                                                             | 7.83 ms: 1.13x slower                                               |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 762 us: 12.77x faster                                               |
| coverage                   | 307 ms                                                              | 51.9 ms: 5.92x faster                                               |
| deepcopy                   | 280 us                                                              | 242 us: 1.16x faster                                                |
| deepcopy_memo              | 23.5 us                                                             | 22.3 us: 1.05x faster                                               |
| regex_effbot               | 1.88 ms                                                             | 1.82 ms: 1.03x faster                                               |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                |
| pickle_list                | 3.57 us                                                             | 3.49 us: 1.02x faster                                               |
| deepcopy_reduce            | 2.59 us                                                             | 2.55 us: 1.01x faster                                               |
| html5lib                   | 45.4 ms                                                             | 44.9 ms: 1.01x faster                                               |
| go                         | 101 ms                                                              | 99.5 ms: 1.01x faster                                               |
| sqlite_synth               | 1.96 us                                                             | 1.99 us: 1.01x slower                                               |
| unpickle_list              | 2.93 us                                                             | 2.98 us: 1.02x slower                                               |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                |
| docutils                   | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                              |
| genshi_text                | 20.1 ms                                                             | 20.6 ms: 1.03x slower                                               |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                |
| sympy_expand               | 375 ms                                                              | 387 ms: 1.03x slower                                                |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                              |
| genshi_xml                 | 44.3 ms                                                             | 45.9 ms: 1.04x slower                                               |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 465 ms: 1.04x slower                                                |
| pickle_dict                | 20.8 us                                                             | 21.6 us: 1.04x slower                                               |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.04x slower                                               |
| pathlib                    | 83.9 ms                                                             | 88.2 ms: 1.05x slower                                               |
| regex_compile              | 99.9 ms                                                             | 105 ms: 1.05x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 558 ms: 1.05x slower                                                |
| 2to3                       | 233 ms                                                              | 246 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 136 us                                                              | 143 us: 1.06x slower                                                |
| pickle                     | 8.07 us                                                             | 8.56 us: 1.06x slower                                               |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                               |
| pycparser                  | 777 ms                                                              | 825 ms: 1.06x slower                                                |
| logging_simple             | 7.47 us                                                             | 7.95 us: 1.07x slower                                               |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                |
| logging_format             | 8.13 us                                                             | 8.70 us: 1.07x slower                                               |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                              |
| crypto_pyaes               | 55.8 ms                                                             | 60.0 ms: 1.07x slower                                               |
| xml_etree_parse            | 104 ms                                                              | 113 ms: 1.08x slower                                                |
| django_template            | 30.1 ms                                                             | 32.5 ms: 1.08x slower                                               |
| xml_etree_iterparse        | 64.2 ms                                                             | 69.5 ms: 1.08x slower                                               |
| meteor_contest             | 74.1 ms                                                             | 80.3 ms: 1.08x slower                                               |
| nqueens                    | 68.7 ms                                                             | 74.5 ms: 1.08x slower                                               |
| sqlglot_normalize          | 206 ms                                                              | 224 ms: 1.09x slower                                                |
| telco                      | 6.03 ms                                                             | 6.58 ms: 1.09x slower                                               |
| pprint_safe_repr           | 607 ms                                                              | 662 ms: 1.09x slower                                                |
| sqlglot_optimize           | 39.7 ms                                                             | 43.6 ms: 1.10x slower                                               |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.10x slower                                                |
| coroutines                 | 15.5 ms                                                             | 17.1 ms: 1.10x slower                                               |
| python_startup_no_site     | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                               |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                               |
| pprint_pformat             | 1.24 sec                                                            | 1.37 sec: 1.11x slower                                              |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.17 ms: 1.11x slower                                               |
| sqlglot_transpile          | 1.19 ms                                                             | 1.32 ms: 1.11x slower                                               |
| xml_etree_generate         | 59.6 ms                                                             | 66.5 ms: 1.12x slower                                               |
| mako                       | 6.94 ms                                                             | 7.83 ms: 1.13x slower                                               |
| comprehensions             | 11.9 us                                                             | 13.4 us: 1.13x slower                                               |
| xml_etree_process          | 42.1 ms                                                             | 47.6 ms: 1.13x slower                                               |
| nbody                      | 76.9 ms                                                             | 87.2 ms: 1.13x slower                                               |
| tomli_loads                | 1.65 sec                                                            | 1.87 sec: 1.13x slower                                              |
| spectral_norm              | 68.0 ms                                                             | 77.3 ms: 1.14x slower                                               |
| generators                 | 21.2 ms                                                             | 24.1 ms: 1.14x slower                                               |
| scimark_lu                 | 59.4 ms                                                             | 67.6 ms: 1.14x slower                                               |
| async_generators           | 266 ms                                                              | 306 ms: 1.15x slower                                                |
| chaos                      | 48.0 ms                                                             | 55.4 ms: 1.16x slower                                               |
| scimark_fft                | 198 ms                                                              | 230 ms: 1.16x slower                                                |
| float                      | 52.4 ms                                                             | 61.9 ms: 1.18x slower                                               |
| pyflate                    | 308 ms                                                              | 368 ms: 1.19x slower                                                |
| hexiom                     | 4.23 ms                                                             | 5.05 ms: 1.19x slower                                               |
| deltablue                  | 2.23 ms                                                             | 2.68 ms: 1.20x slower                                               |
| python_startup             | 22.2 ms                                                             | 26.6 ms: 1.20x slower                                               |
| logging_silent             | 57.9 ns                                                             | 69.5 ns: 1.20x slower                                               |
| fannkuch                   | 270 ms                                                              | 325 ms: 1.20x slower                                                |
| unpickle_pure_python       | 147 us                                                              | 178 us: 1.21x slower                                                |
| asyncio_tcp                | 662 ms                                                              | 819 ms: 1.24x slower                                                |
| pickle_pure_python         | 213 us                                                              | 265 us: 1.25x slower                                                |
| raytrace                   | 189 ms                                                              | 236 ms: 1.25x slower                                                |
| gc_traversal               | 1.43 ms                                                             | 1.81 ms: 1.26x slower                                               |
| scimark_sor                | 81.0 ms                                                             | 103 ms: 1.28x slower                                                |
| bench_mp_pool              | 69.4 ms                                                             | 89.0 ms: 1.28x slower                                               |
| scimark_monte_carlo        | 45.2 ms                                                             | 58.2 ms: 1.29x slower                                               |
| json_dumps                 | 6.84 ms                                                             | 9.09 ms: 1.33x slower                                               |
| richards                   | 31.2 ms                                                             | 41.5 ms: 1.33x slower                                               |
| richards_super             | 35.5 ms                                                             | 47.3 ms: 1.33x slower                                               |
| json                       | 4.10 ms                                                             | 5.97 ms: 1.46x slower                                               |
| create_gc_cycles           | 756 us                                                              | 1.19 ms: 1.58x slower                                               |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                        |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, json_loads, regex_dna, pidigits, regex_v8, async_tree_io, async_tree_memoization_tg, bench_thread_pool, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (3) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: dulwich_log, sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown