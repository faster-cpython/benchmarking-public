# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: windows-x86
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 255 ms: 1.09x slower                                                    |
| docutils       | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                  |
| html5lib       | 45.4 ms                                                             | 46.2 ms: 1.02x slower                                                   |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                               | 1.07x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                            |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                    |
| float          | 52.4 ms                                                             | 63.6 ms: 1.21x slower                                                   |
| nbody          | 76.9 ms                                                             | 96.4 ms: 1.25x slower                                                   |
| Geometric mean | (ref)                                                               | 1.16x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 116 ms: 1.02x faster                                                    |
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                   |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                   |
| regex_compile  | 99.9 ms                                                             | 111 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                               | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.31 us: 1.08x faster                                                   |
| pickle_dict          | 20.8 us                                                             | 20.3 us: 1.02x faster                                                   |
| pickle               | 8.07 us                                                             | 7.95 us: 1.02x faster                                                   |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                   |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                    |
| unpickle_list        | 2.93 us                                                             | 3.02 us: 1.03x slower                                                   |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.8 ms: 1.06x slower                                                   |
| json_dumps           | 6.84 ms                                                             | 7.75 ms: 1.13x slower                                                   |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                  |
| xml_etree_generate   | 59.6 ms                                                             | 69.3 ms: 1.16x slower                                                   |
| xml_etree_process    | 42.1 ms                                                             | 52.5 ms: 1.25x slower                                                   |
| pickle_pure_python   | 213 us                                                              | 268 us: 1.26x slower                                                    |
| unpickle_pure_python | 147 us                                                              | 190 us: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                   |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                   |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.6 ms: 1.05x slower                                                   |
| genshi_text     | 20.1 ms                                                             | 23.0 ms: 1.14x slower                                                   |
| django_template | 30.1 ms                                                             | 35.2 ms: 1.17x slower                                                   |
| mako            | 6.94 ms                                                             | 8.22 ms: 1.18x slower                                                   |
| Geometric mean  | (ref)                                                               | 1.14x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 745 us: 13.05x faster                                                   |
| coverage                   | 307 ms                                                              | 54.0 ms: 5.69x faster                                                   |
| deepcopy                   | 280 us                                                              | 244 us: 1.15x faster                                                    |
| pickle_list                | 3.57 us                                                             | 3.31 us: 1.08x faster                                                   |
| deepcopy_memo              | 23.5 us                                                             | 22.1 us: 1.06x faster                                                   |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                    |
| pickle_dict                | 20.8 us                                                             | 20.3 us: 1.02x faster                                                   |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                    |
| pickle                     | 8.07 us                                                             | 7.95 us: 1.02x faster                                                   |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.02x faster                                                    |
| sqlite_synth               | 1.96 us                                                             | 1.95 us: 1.00x faster                                                   |
| create_gc_cycles           | 756 us                                                              | 764 us: 1.01x slower                                                    |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                   |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                  |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                   |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                   |
| html5lib                   | 45.4 ms                                                             | 46.2 ms: 1.02x slower                                                   |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                   |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                    |
| unpickle_list              | 2.93 us                                                             | 3.02 us: 1.03x slower                                                   |
| pathlib                    | 83.9 ms                                                             | 86.5 ms: 1.03x slower                                                   |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.04x slower                                                    |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.04x slower                                                   |
| docutils                   | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                  |
| sympy_expand               | 375 ms                                                              | 394 ms: 1.05x slower                                                    |
| sympy_str                  | 211 ms                                                              | 222 ms: 1.05x slower                                                    |
| genshi_xml                 | 44.3 ms                                                             | 46.6 ms: 1.05x slower                                                   |
| bench_mp_pool              | 69.4 ms                                                             | 73.1 ms: 1.05x slower                                                   |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.8 ms: 1.06x slower                                                   |
| crypto_pyaes               | 55.8 ms                                                             | 59.0 ms: 1.06x slower                                                   |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                  |
| json                       | 4.10 ms                                                             | 4.35 ms: 1.06x slower                                                   |
| python_startup             | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 136 us                                                              | 146 us: 1.08x slower                                                    |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                   |
| meteor_contest             | 74.1 ms                                                             | 80.1 ms: 1.08x slower                                                   |
| pylint                     | 217 ms                                                              | 236 ms: 1.09x slower                                                    |
| 2to3                       | 233 ms                                                              | 255 ms: 1.09x slower                                                    |
| sympy_integrate            | 14.6 ms                                                             | 16.0 ms: 1.09x slower                                                   |
| logging_format             | 8.13 us                                                             | 8.90 us: 1.09x slower                                                   |
| go                         | 101 ms                                                              | 111 ms: 1.10x slower                                                    |
| logging_simple             | 7.47 us                                                             | 8.23 us: 1.10x slower                                                   |
| regex_compile              | 99.9 ms                                                             | 111 ms: 1.11x slower                                                    |
| pprint_safe_repr           | 607 ms                                                              | 679 ms: 1.12x slower                                                    |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                    |
| pycparser                  | 777 ms                                                              | 875 ms: 1.13x slower                                                    |
| nqueens                    | 68.7 ms                                                             | 77.5 ms: 1.13x slower                                                   |
| json_dumps                 | 6.84 ms                                                             | 7.75 ms: 1.13x slower                                                   |
| telco                      | 6.03 ms                                                             | 6.85 ms: 1.14x slower                                                   |
| genshi_text                | 20.1 ms                                                             | 23.0 ms: 1.14x slower                                                   |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.29 ms: 1.15x slower                                                   |
| async_generators           | 266 ms                                                              | 305 ms: 1.15x slower                                                    |
| sqlglot_transpile          | 1.19 ms                                                             | 1.37 ms: 1.15x slower                                                   |
| tomli_loads                | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                  |
| pprint_pformat             | 1.24 sec                                                            | 1.44 sec: 1.16x slower                                                  |
| sqlglot_parse              | 964 us                                                              | 1.12 ms: 1.16x slower                                                   |
| xml_etree_generate         | 59.6 ms                                                             | 69.3 ms: 1.16x slower                                                   |
| sqlglot_normalize          | 206 ms                                                              | 240 ms: 1.16x slower                                                    |
| sqlglot_optimize           | 39.7 ms                                                             | 46.4 ms: 1.17x slower                                                   |
| django_template            | 30.1 ms                                                             | 35.2 ms: 1.17x slower                                                   |
| chaos                      | 48.0 ms                                                             | 56.1 ms: 1.17x slower                                                   |
| spectral_norm              | 68.0 ms                                                             | 80.5 ms: 1.18x slower                                                   |
| mako                       | 6.94 ms                                                             | 8.22 ms: 1.18x slower                                                   |
| coroutines                 | 15.5 ms                                                             | 18.4 ms: 1.19x slower                                                   |
| comprehensions             | 11.9 us                                                             | 14.1 us: 1.19x slower                                                   |
| scimark_fft                | 198 ms                                                              | 237 ms: 1.20x slower                                                    |
| scimark_lu                 | 59.4 ms                                                             | 71.1 ms: 1.20x slower                                                   |
| pyflate                    | 308 ms                                                              | 369 ms: 1.20x slower                                                    |
| fannkuch                   | 270 ms                                                              | 324 ms: 1.20x slower                                                    |
| float                      | 52.4 ms                                                             | 63.6 ms: 1.21x slower                                                   |
| xml_etree_process          | 42.1 ms                                                             | 52.5 ms: 1.25x slower                                                   |
| nbody                      | 76.9 ms                                                             | 96.4 ms: 1.25x slower                                                   |
| pickle_pure_python         | 213 us                                                              | 268 us: 1.26x slower                                                    |
| deltablue                  | 2.23 ms                                                             | 2.82 ms: 1.26x slower                                                   |
| hexiom                     | 4.23 ms                                                             | 5.34 ms: 1.26x slower                                                   |
| scimark_sor                | 81.0 ms                                                             | 103 ms: 1.27x slower                                                    |
| unpickle_pure_python       | 147 us                                                              | 190 us: 1.29x slower                                                    |
| scimark_monte_carlo        | 45.2 ms                                                             | 58.6 ms: 1.30x slower                                                   |
| generators                 | 21.2 ms                                                             | 27.5 ms: 1.30x slower                                                   |
| richards                   | 31.2 ms                                                             | 40.8 ms: 1.31x slower                                                   |
| logging_silent             | 57.9 ns                                                             | 75.6 ns: 1.31x slower                                                   |
| richards_super             | 35.5 ms                                                             | 47.0 ms: 1.32x slower                                                   |
| raytrace                   | 189 ms                                                              | 259 ms: 1.37x slower                                                    |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                            |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, deepcopy_reduce, async_tree_memoization_tg, async_tree_cpu_io_mixed, bench_thread_pool, async_tree_io, asyncio_tcp
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown