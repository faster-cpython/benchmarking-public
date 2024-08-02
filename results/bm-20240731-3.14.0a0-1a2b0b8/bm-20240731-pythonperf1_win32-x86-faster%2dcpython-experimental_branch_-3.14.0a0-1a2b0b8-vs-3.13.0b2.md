# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.10x slower                                                                     |
| docutils       | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                                   |
| html5lib       | 45.4 ms                                                             | 49.5 ms: 1.09x slower                                                                    |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.11x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 517 ms: 1.02x faster                                                                     |
| async_tree_memoization     | 275 ms                                                              | 280 ms: 1.02x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 462 ms: 1.03x slower                                                                     |
| async_tree_io              | 530 ms                                                              | 559 ms: 1.05x slower                                                                     |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                             |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                                     |
| float          | 52.4 ms                                                             | 61.5 ms: 1.17x slower                                                                    |
| nbody          | 76.9 ms                                                             | 93.6 ms: 1.22x slower                                                                    |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.00x slower                                                                     |
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.02x slower                                                                    |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                                    |
| regex_compile  | 99.9 ms                                                             | 110 ms: 1.10x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.2 us: 1.02x faster                                                                    |
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.01x slower                                                                     |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.7 ms: 1.07x slower                                                                    |
| json_dumps           | 6.84 ms                                                             | 7.63 ms: 1.12x slower                                                                    |
| xml_etree_generate   | 59.6 ms                                                             | 66.8 ms: 1.12x slower                                                                    |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                                   |
| xml_etree_process    | 42.1 ms                                                             | 50.2 ms: 1.19x slower                                                                    |
| pickle_pure_python   | 213 us                                                              | 257 us: 1.21x slower                                                                     |
| unpickle_pure_python | 147 us                                                              | 181 us: 1.23x slower                                                                     |
| Geometric mean       | (ref)                                                               | 1.12x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 19.5 ms: 1.07x slower                                                                    |
| python_startup         | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                                    |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 49.3 ms: 1.11x slower                                                                    |
| django_template | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                                    |
| genshi_text     | 20.1 ms                                                             | 23.5 ms: 1.17x slower                                                                    |
| mako            | 6.94 ms                                                             | 8.15 ms: 1.17x slower                                                                    |
| Geometric mean  | (ref)                                                               | 1.15x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 769 us: 12.65x faster                                                                    |
| coverage                   | 307 ms                                                              | 52.1 ms: 5.90x faster                                                                    |
| deepcopy                   | 280 us                                                              | 256 us: 1.09x faster                                                                     |
| async_tree_io_tg           | 529 ms                                                              | 517 ms: 1.02x faster                                                                     |
| json_loads                 | 20.5 us                                                             | 20.2 us: 1.02x faster                                                                    |
| create_gc_cycles           | 756 us                                                              | 746 us: 1.01x faster                                                                     |
| deepcopy_memo              | 23.5 us                                                             | 23.4 us: 1.01x faster                                                                    |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.00x slower                                                                     |
| deepcopy_reduce            | 2.59 us                                                             | 2.60 us: 1.00x slower                                                                    |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                                     |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                                    |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.01x slower                                                                     |
| async_tree_memoization     | 275 ms                                                              | 280 ms: 1.02x slower                                                                     |
| json                       | 4.10 ms                                                             | 4.19 ms: 1.02x slower                                                                    |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.02x slower                                                                    |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                                    |
| telco                      | 6.03 ms                                                             | 6.21 ms: 1.03x slower                                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 462 ms: 1.03x slower                                                                     |
| crypto_pyaes               | 55.8 ms                                                             | 58.6 ms: 1.05x slower                                                                    |
| sympy_sum                  | 105 ms                                                              | 110 ms: 1.05x slower                                                                     |
| sympy_expand               | 375 ms                                                              | 395 ms: 1.05x slower                                                                     |
| async_tree_io              | 530 ms                                                              | 559 ms: 1.05x slower                                                                     |
| pathlib                    | 83.9 ms                                                             | 88.5 ms: 1.06x slower                                                                    |
| mdp                        | 1.60 sec                                                            | 1.69 sec: 1.06x slower                                                                   |
| asyncio_tcp                | 662 ms                                                              | 702 ms: 1.06x slower                                                                     |
| docutils                   | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                                   |
| bench_mp_pool              | 69.4 ms                                                             | 73.8 ms: 1.06x slower                                                                    |
| sympy_str                  | 211 ms                                                              | 225 ms: 1.06x slower                                                                     |
| python_startup_no_site     | 18.2 ms                                                             | 19.5 ms: 1.07x slower                                                                    |
| sympy_integrate            | 14.6 ms                                                             | 15.7 ms: 1.07x slower                                                                    |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.7 ms: 1.07x slower                                                                    |
| python_startup             | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                                    |
| logging_format             | 8.13 us                                                             | 8.72 us: 1.07x slower                                                                    |
| pylint                     | 217 ms                                                              | 236 ms: 1.09x slower                                                                     |
| chaos                      | 48.0 ms                                                             | 52.2 ms: 1.09x slower                                                                    |
| logging_simple             | 7.47 us                                                             | 8.13 us: 1.09x slower                                                                    |
| html5lib                   | 45.4 ms                                                             | 49.5 ms: 1.09x slower                                                                    |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.14 ms: 1.09x slower                                                                    |
| regex_compile              | 99.9 ms                                                             | 110 ms: 1.10x slower                                                                     |
| 2to3                       | 233 ms                                                              | 258 ms: 1.10x slower                                                                     |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.11x slower                                                                     |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                                    |
| typing_runtime_protocols   | 136 us                                                              | 151 us: 1.11x slower                                                                     |
| genshi_xml                 | 44.3 ms                                                             | 49.3 ms: 1.11x slower                                                                    |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                                    |
| json_dumps                 | 6.84 ms                                                             | 7.63 ms: 1.12x slower                                                                    |
| nqueens                    | 68.7 ms                                                             | 76.8 ms: 1.12x slower                                                                    |
| xml_etree_generate         | 59.6 ms                                                             | 66.8 ms: 1.12x slower                                                                    |
| coroutines                 | 15.5 ms                                                             | 17.4 ms: 1.12x slower                                                                    |
| meteor_contest             | 74.1 ms                                                             | 83.2 ms: 1.12x slower                                                                    |
| pycparser                  | 777 ms                                                              | 873 ms: 1.12x slower                                                                     |
| django_template            | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                                    |
| sqlglot_optimize           | 39.7 ms                                                             | 45.0 ms: 1.13x slower                                                                    |
| pprint_pformat             | 1.24 sec                                                            | 1.41 sec: 1.14x slower                                                                   |
| pprint_safe_repr           | 607 ms                                                              | 693 ms: 1.14x slower                                                                     |
| sqlglot_normalize          | 206 ms                                                              | 236 ms: 1.14x slower                                                                     |
| fannkuch                   | 270 ms                                                              | 311 ms: 1.15x slower                                                                     |
| scimark_lu                 | 59.4 ms                                                             | 68.4 ms: 1.15x slower                                                                    |
| scimark_fft                | 198 ms                                                              | 230 ms: 1.16x slower                                                                     |
| tomli_loads                | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                                   |
| genshi_text                | 20.1 ms                                                             | 23.5 ms: 1.17x slower                                                                    |
| async_generators           | 266 ms                                                              | 311 ms: 1.17x slower                                                                     |
| mako                       | 6.94 ms                                                             | 8.15 ms: 1.17x slower                                                                    |
| float                      | 52.4 ms                                                             | 61.5 ms: 1.17x slower                                                                    |
| pyflate                    | 308 ms                                                              | 364 ms: 1.18x slower                                                                     |
| xml_etree_process          | 42.1 ms                                                             | 50.2 ms: 1.19x slower                                                                    |
| raytrace                   | 189 ms                                                              | 226 ms: 1.20x slower                                                                     |
| spectral_norm              | 68.0 ms                                                             | 81.6 ms: 1.20x slower                                                                    |
| pickle_pure_python         | 213 us                                                              | 257 us: 1.21x slower                                                                     |
| comprehensions             | 11.9 us                                                             | 14.3 us: 1.21x slower                                                                    |
| scimark_sor                | 81.0 ms                                                             | 98.0 ms: 1.21x slower                                                                    |
| nbody                      | 76.9 ms                                                             | 93.6 ms: 1.22x slower                                                                    |
| richards_super             | 35.5 ms                                                             | 43.3 ms: 1.22x slower                                                                    |
| richards                   | 31.2 ms                                                             | 38.3 ms: 1.23x slower                                                                    |
| unpickle_pure_python       | 147 us                                                              | 181 us: 1.23x slower                                                                     |
| deltablue                  | 2.23 ms                                                             | 2.75 ms: 1.23x slower                                                                    |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.8 ms: 1.23x slower                                                                    |
| go                         | 101 ms                                                              | 125 ms: 1.24x slower                                                                     |
| hexiom                     | 4.23 ms                                                             | 5.36 ms: 1.27x slower                                                                    |
| generators                 | 21.2 ms                                                             | 27.7 ms: 1.31x slower                                                                    |
| logging_silent             | 57.9 ns                                                             | 76.2 ns: 1.32x slower                                                                    |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_none, bench_thread_pool
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown