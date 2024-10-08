# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 253 ms: 1.08x slower                                                  |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                |
| html5lib       | 45.4 ms                                                             | 46.9 ms: 1.03x slower                                                 |
| tornado_http   | 94.3 ms                                                             | 95.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 217 ms: 1.05x faster                                                  |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 529 ms                                                              | 520 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                          |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                  |
| nbody          | 76.9 ms                                                             | 90.2 ms: 1.17x slower                                                 |
| float          | 52.4 ms                                                             | 63.2 ms: 1.21x slower                                                 |
| Geometric mean | (ref)                                                               | 1.12x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                  |
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                 |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                 |
| regex_compile  | 99.9 ms                                                             | 108 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.42 us: 1.04x faster                                                 |
| unpickle_list        | 2.93 us                                                             | 2.85 us: 1.03x faster                                                 |
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                 |
| json_loads           | 20.5 us                                                             | 20.6 us: 1.00x slower                                                 |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.03x slower                                                  |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                 |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.9 ms: 1.07x slower                                                 |
| json_dumps           | 6.84 ms                                                             | 7.57 ms: 1.11x slower                                                 |
| tomli_loads          | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                |
| xml_etree_generate   | 59.6 ms                                                             | 67.0 ms: 1.12x slower                                                 |
| xml_etree_process    | 42.1 ms                                                             | 48.6 ms: 1.16x slower                                                 |
| pickle_pure_python   | 213 us                                                              | 260 us: 1.22x slower                                                  |
| unpickle_pure_python | 147 us                                                              | 182 us: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.07x slower                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.06x slower                                                 |
| python_startup_no_site | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 32.1 ms: 1.07x slower                                                 |
| genshi_xml      | 44.3 ms                                                             | 47.6 ms: 1.08x slower                                                 |
| genshi_text     | 20.1 ms                                                             | 22.2 ms: 1.11x slower                                                 |
| mako            | 6.94 ms                                                             | 8.30 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 766 us: 12.70x faster                                                 |
| coverage                   | 307 ms                                                              | 53.2 ms: 5.77x faster                                                 |
| deepcopy                   | 280 us                                                              | 249 us: 1.12x faster                                                  |
| deepcopy_reduce            | 2.59 us                                                             | 2.42 us: 1.07x faster                                                 |
| async_tree_none            | 228 ms                                                              | 217 ms: 1.05x faster                                                  |
| pickle_list                | 3.57 us                                                             | 3.42 us: 1.04x faster                                                 |
| create_gc_cycles           | 756 us                                                              | 735 us: 1.03x faster                                                  |
| unpickle_list              | 2.93 us                                                             | 2.85 us: 1.03x faster                                                 |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 529 ms                                                              | 520 ms: 1.02x faster                                                  |
| deepcopy_memo              | 23.5 us                                                             | 23.1 us: 1.02x faster                                                 |
| gc_traversal               | 1.43 ms                                                             | 1.41 ms: 1.02x faster                                                 |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                  |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                 |
| sqlite_synth               | 1.96 us                                                             | 1.95 us: 1.00x faster                                                 |
| json_loads                 | 20.5 us                                                             | 20.6 us: 1.00x slower                                                 |
| tornado_http               | 94.3 ms                                                             | 95.1 ms: 1.01x slower                                                 |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                 |
| sympy_expand               | 375 ms                                                              | 380 ms: 1.01x slower                                                  |
| json                       | 4.10 ms                                                             | 4.16 ms: 1.02x slower                                                 |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                                  |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                  |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                 |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.03x slower                                                  |
| html5lib                   | 45.4 ms                                                             | 46.9 ms: 1.03x slower                                                 |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                  |
| crypto_pyaes               | 55.8 ms                                                             | 57.9 ms: 1.04x slower                                                 |
| bench_mp_pool              | 69.4 ms                                                             | 72.2 ms: 1.04x slower                                                 |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.04x slower                                                 |
| typing_runtime_protocols   | 136 us                                                              | 142 us: 1.05x slower                                                  |
| pprint_safe_repr           | 607 ms                                                              | 636 ms: 1.05x slower                                                  |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                 |
| pprint_pformat             | 1.24 sec                                                            | 1.32 sec: 1.06x slower                                                |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.06x slower                                                 |
| django_template            | 30.1 ms                                                             | 32.1 ms: 1.07x slower                                                 |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                  |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.9 ms: 1.07x slower                                                 |
| genshi_xml                 | 44.3 ms                                                             | 47.6 ms: 1.08x slower                                                 |
| logging_format             | 8.13 us                                                             | 8.76 us: 1.08x slower                                                 |
| python_startup_no_site     | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                 |
| go                         | 101 ms                                                              | 109 ms: 1.08x slower                                                  |
| regex_compile              | 99.9 ms                                                             | 108 ms: 1.08x slower                                                  |
| logging_simple             | 7.47 us                                                             | 8.09 us: 1.08x slower                                                 |
| 2to3                       | 233 ms                                                              | 253 ms: 1.08x slower                                                  |
| telco                      | 6.03 ms                                                             | 6.54 ms: 1.09x slower                                                 |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.13 ms: 1.09x slower                                                 |
| sqlglot_optimize           | 39.7 ms                                                             | 43.4 ms: 1.09x slower                                                 |
| pycparser                  | 777 ms                                                              | 854 ms: 1.10x slower                                                  |
| meteor_contest             | 74.1 ms                                                             | 81.8 ms: 1.10x slower                                                 |
| genshi_text                | 20.1 ms                                                             | 22.2 ms: 1.11x slower                                                 |
| mdp                        | 1.60 sec                                                            | 1.77 sec: 1.11x slower                                                |
| json_dumps                 | 6.84 ms                                                             | 7.57 ms: 1.11x slower                                                 |
| sqlglot_normalize          | 206 ms                                                              | 230 ms: 1.11x slower                                                  |
| tomli_loads                | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                |
| xml_etree_generate         | 59.6 ms                                                             | 67.0 ms: 1.12x slower                                                 |
| nqueens                    | 68.7 ms                                                             | 78.2 ms: 1.14x slower                                                 |
| chaos                      | 48.0 ms                                                             | 54.6 ms: 1.14x slower                                                 |
| sqlglot_transpile          | 1.19 ms                                                             | 1.36 ms: 1.14x slower                                                 |
| sqlglot_parse              | 964 us                                                              | 1.10 ms: 1.14x slower                                                 |
| xml_etree_process          | 42.1 ms                                                             | 48.6 ms: 1.16x slower                                                 |
| async_generators           | 266 ms                                                              | 307 ms: 1.16x slower                                                  |
| nbody                      | 76.9 ms                                                             | 90.2 ms: 1.17x slower                                                 |
| pyflate                    | 308 ms                                                              | 364 ms: 1.18x slower                                                  |
| scimark_fft                | 198 ms                                                              | 236 ms: 1.19x slower                                                  |
| mako                       | 6.94 ms                                                             | 8.30 ms: 1.20x slower                                                 |
| coroutines                 | 15.5 ms                                                             | 18.7 ms: 1.21x slower                                                 |
| float                      | 52.4 ms                                                             | 63.2 ms: 1.21x slower                                                 |
| scimark_lu                 | 59.4 ms                                                             | 71.7 ms: 1.21x slower                                                 |
| spectral_norm              | 68.0 ms                                                             | 82.1 ms: 1.21x slower                                                 |
| pickle_pure_python         | 213 us                                                              | 260 us: 1.22x slower                                                  |
| comprehensions             | 11.9 us                                                             | 14.6 us: 1.23x slower                                                 |
| unpickle_pure_python       | 147 us                                                              | 182 us: 1.24x slower                                                  |
| raytrace                   | 189 ms                                                              | 237 ms: 1.26x slower                                                  |
| hexiom                     | 4.23 ms                                                             | 5.33 ms: 1.26x slower                                                 |
| deltablue                  | 2.23 ms                                                             | 2.82 ms: 1.26x slower                                                 |
| fannkuch                   | 270 ms                                                              | 341 ms: 1.26x slower                                                  |
| richards_super             | 35.5 ms                                                             | 45.6 ms: 1.28x slower                                                 |
| generators                 | 21.2 ms                                                             | 27.2 ms: 1.28x slower                                                 |
| scimark_sor                | 81.0 ms                                                             | 105 ms: 1.29x slower                                                  |
| scimark_monte_carlo        | 45.2 ms                                                             | 58.6 ms: 1.30x slower                                                 |
| richards                   | 31.2 ms                                                             | 40.5 ms: 1.30x slower                                                 |
| logging_silent             | 57.9 ns                                                             | 75.2 ns: 1.30x slower                                                 |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, pickle, async_tree_cpu_io_mixed, pathlib, async_tree_io, asyncio_tcp
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown