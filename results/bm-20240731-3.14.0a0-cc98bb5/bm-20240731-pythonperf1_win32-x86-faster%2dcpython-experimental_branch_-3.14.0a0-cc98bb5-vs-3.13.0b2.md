# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 262 ms: 1.12x slower                                                                     |
| docutils       | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                                   |
| html5lib       | 45.4 ms                                                             | 49.1 ms: 1.08x slower                                                                    |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 523 ms: 1.01x faster                                                                     |
| async_tree_none            | 228 ms                                                              | 232 ms: 1.02x slower                                                                     |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 486 ms: 1.03x slower                                                                     |
| async_tree_memoization     | 275 ms                                                              | 285 ms: 1.04x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 474 ms: 1.06x slower                                                                     |
| async_tree_io              | 530 ms                                                              | 564 ms: 1.06x slower                                                                     |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                             |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                                     |
| float          | 52.4 ms                                                             | 60.0 ms: 1.15x slower                                                                    |
| nbody          | 76.9 ms                                                             | 99.2 ms: 1.29x slower                                                                    |
| Geometric mean | (ref)                                                               | 1.14x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                                     |
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                                    |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                                    |
| regex_compile  | 99.9 ms                                                             | 109 ms: 1.09x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.4 us: 1.00x faster                                                                    |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.9 ms: 1.06x slower                                                                    |
| json_dumps           | 6.84 ms                                                             | 7.35 ms: 1.07x slower                                                                    |
| tomli_loads          | 1.65 sec                                                            | 1.79 sec: 1.09x slower                                                                   |
| xml_etree_generate   | 59.6 ms                                                             | 66.2 ms: 1.11x slower                                                                    |
| xml_etree_process    | 42.1 ms                                                             | 48.6 ms: 1.15x slower                                                                    |
| unpickle_pure_python | 147 us                                                              | 173 us: 1.17x slower                                                                     |
| pickle_pure_python   | 213 us                                                              | 257 us: 1.21x slower                                                                     |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.3 ms: 1.09x slower                                                                    |
| python_startup_no_site | 18.2 ms                                                             | 20.4 ms: 1.12x slower                                                                    |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.4 ms: 1.09x slower                                                                    |
| genshi_text     | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                                    |
| django_template | 30.1 ms                                                             | 33.9 ms: 1.13x slower                                                                    |
| mako            | 6.94 ms                                                             | 8.24 ms: 1.19x slower                                                                    |
| Geometric mean  | (ref)                                                               | 1.13x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 769 us: 12.64x faster                                                                    |
| coverage                   | 307 ms                                                              | 51.9 ms: 5.92x faster                                                                    |
| deepcopy                   | 280 us                                                              | 259 us: 1.08x faster                                                                     |
| async_tree_io_tg           | 529 ms                                                              | 523 ms: 1.01x faster                                                                     |
| deepcopy_memo              | 23.5 us                                                             | 23.3 us: 1.01x faster                                                                    |
| create_gc_cycles           | 756 us                                                              | 749 us: 1.01x faster                                                                     |
| json_loads                 | 20.5 us                                                             | 20.4 us: 1.00x faster                                                                    |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                                   |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                                     |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                                     |
| async_tree_none            | 228 ms                                                              | 232 ms: 1.02x slower                                                                     |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                                    |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 486 ms: 1.03x slower                                                                     |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                                    |
| telco                      | 6.03 ms                                                             | 6.24 ms: 1.03x slower                                                                    |
| async_tree_memoization     | 275 ms                                                              | 285 ms: 1.04x slower                                                                     |
| json                       | 4.10 ms                                                             | 4.29 ms: 1.05x slower                                                                    |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.9 ms: 1.06x slower                                                                    |
| crypto_pyaes               | 55.8 ms                                                             | 59.1 ms: 1.06x slower                                                                    |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 474 ms: 1.06x slower                                                                     |
| bench_mp_pool              | 69.4 ms                                                             | 73.7 ms: 1.06x slower                                                                    |
| async_tree_io              | 530 ms                                                              | 564 ms: 1.06x slower                                                                     |
| mdp                        | 1.60 sec                                                            | 1.71 sec: 1.07x slower                                                                   |
| pathlib                    | 83.9 ms                                                             | 89.6 ms: 1.07x slower                                                                    |
| docutils                   | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                                   |
| sympy_sum                  | 105 ms                                                              | 112 ms: 1.07x slower                                                                     |
| asyncio_tcp                | 662 ms                                                              | 708 ms: 1.07x slower                                                                     |
| json_dumps                 | 6.84 ms                                                             | 7.35 ms: 1.07x slower                                                                    |
| sympy_expand               | 375 ms                                                              | 404 ms: 1.08x slower                                                                     |
| html5lib                   | 45.4 ms                                                             | 49.1 ms: 1.08x slower                                                                    |
| sympy_str                  | 211 ms                                                              | 229 ms: 1.08x slower                                                                     |
| tomli_loads                | 1.65 sec                                                            | 1.79 sec: 1.09x slower                                                                   |
| sympy_integrate            | 14.6 ms                                                             | 15.9 ms: 1.09x slower                                                                    |
| regex_compile              | 99.9 ms                                                             | 109 ms: 1.09x slower                                                                     |
| genshi_xml                 | 44.3 ms                                                             | 48.4 ms: 1.09x slower                                                                    |
| python_startup             | 22.2 ms                                                             | 24.3 ms: 1.09x slower                                                                    |
| pylint                     | 217 ms                                                              | 238 ms: 1.10x slower                                                                     |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.16 ms: 1.10x slower                                                                    |
| logging_format             | 8.13 us                                                             | 8.98 us: 1.10x slower                                                                    |
| logging_simple             | 7.47 us                                                             | 8.26 us: 1.11x slower                                                                    |
| async_generators           | 266 ms                                                              | 294 ms: 1.11x slower                                                                     |
| genshi_text                | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                                    |
| xml_etree_generate         | 59.6 ms                                                             | 66.2 ms: 1.11x slower                                                                    |
| pprint_pformat             | 1.24 sec                                                            | 1.39 sec: 1.12x slower                                                                   |
| python_startup_no_site     | 18.2 ms                                                             | 20.4 ms: 1.12x slower                                                                    |
| pprint_safe_repr           | 607 ms                                                              | 680 ms: 1.12x slower                                                                     |
| sqlglot_normalize          | 206 ms                                                              | 231 ms: 1.12x slower                                                                     |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                                     |
| 2to3                       | 233 ms                                                              | 262 ms: 1.12x slower                                                                     |
| sqlglot_optimize           | 39.7 ms                                                             | 44.6 ms: 1.12x slower                                                                    |
| coroutines                 | 15.5 ms                                                             | 17.4 ms: 1.13x slower                                                                    |
| chaos                      | 48.0 ms                                                             | 54.0 ms: 1.13x slower                                                                    |
| django_template            | 30.1 ms                                                             | 33.9 ms: 1.13x slower                                                                    |
| sqlglot_parse              | 964 us                                                              | 1.09 ms: 1.14x slower                                                                    |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.14x slower                                                                    |
| meteor_contest             | 74.1 ms                                                             | 84.3 ms: 1.14x slower                                                                    |
| float                      | 52.4 ms                                                             | 60.0 ms: 1.15x slower                                                                    |
| pycparser                  | 777 ms                                                              | 893 ms: 1.15x slower                                                                     |
| pyflate                    | 308 ms                                                              | 355 ms: 1.15x slower                                                                     |
| nqueens                    | 68.7 ms                                                             | 79.1 ms: 1.15x slower                                                                    |
| xml_etree_process          | 42.1 ms                                                             | 48.6 ms: 1.15x slower                                                                    |
| typing_runtime_protocols   | 136 us                                                              | 158 us: 1.16x slower                                                                     |
| spectral_norm              | 68.0 ms                                                             | 79.2 ms: 1.16x slower                                                                    |
| unpickle_pure_python       | 147 us                                                              | 173 us: 1.17x slower                                                                     |
| scimark_lu                 | 59.4 ms                                                             | 70.0 ms: 1.18x slower                                                                    |
| go                         | 101 ms                                                              | 119 ms: 1.18x slower                                                                     |
| mako                       | 6.94 ms                                                             | 8.24 ms: 1.19x slower                                                                    |
| raytrace                   | 189 ms                                                              | 226 ms: 1.20x slower                                                                     |
| scimark_fft                | 198 ms                                                              | 237 ms: 1.20x slower                                                                     |
| comprehensions             | 11.9 us                                                             | 14.3 us: 1.20x slower                                                                    |
| pickle_pure_python         | 213 us                                                              | 257 us: 1.21x slower                                                                     |
| scimark_sor                | 81.0 ms                                                             | 98.5 ms: 1.22x slower                                                                    |
| fannkuch                   | 270 ms                                                              | 330 ms: 1.22x slower                                                                     |
| deltablue                  | 2.23 ms                                                             | 2.74 ms: 1.22x slower                                                                    |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.6 ms: 1.23x slower                                                                    |
| richards_super             | 35.5 ms                                                             | 44.2 ms: 1.24x slower                                                                    |
| richards                   | 31.2 ms                                                             | 39.1 ms: 1.25x slower                                                                    |
| hexiom                     | 4.23 ms                                                             | 5.31 ms: 1.25x slower                                                                    |
| nbody                      | 76.9 ms                                                             | 99.2 ms: 1.29x slower                                                                    |
| logging_silent             | 57.9 ns                                                             | 74.9 ns: 1.29x slower                                                                    |
| generators                 | 21.2 ms                                                             | 27.6 ms: 1.30x slower                                                                    |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, xml_etree_parse, async_tree_memoization_tg, gc_traversal, deepcopy_reduce, bench_thread_pool
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown