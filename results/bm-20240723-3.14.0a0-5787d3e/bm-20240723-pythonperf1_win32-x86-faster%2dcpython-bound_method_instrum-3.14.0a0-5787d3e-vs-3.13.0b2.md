# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-x86
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                                     |
| docutils       | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                                   |
| html5lib       | 45.4 ms                                                             | 48.2 ms: 1.06x slower                                                                    |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.11x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 203 ms                                                              | 190 ms: 1.07x faster                                                                     |
| async_tree_io_tg           | 529 ms                                                              | 501 ms: 1.06x faster                                                                     |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                                     |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                                     |
| async_tree_io              | 530 ms                                                              | 547 ms: 1.03x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                                     |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                             |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                                     |
| float          | 52.4 ms                                                             | 58.9 ms: 1.13x slower                                                                    |
| nbody          | 76.9 ms                                                             | 90.3 ms: 1.17x slower                                                                    |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.03x slower                                                                    |
| regex_effbot   | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                                    |
| regex_compile  | 99.9 ms                                                             | 105 ms: 1.05x slower                                                                     |
| regex_dna      | 118 ms                                                              | 128 ms: 1.08x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.3 us: 1.01x faster                                                                    |
| xml_etree_parse      | 104 ms                                                              | 105 ms: 1.01x slower                                                                     |
| json_dumps           | 6.84 ms                                                             | 7.12 ms: 1.04x slower                                                                    |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.6 ms: 1.05x slower                                                                    |
| xml_etree_generate   | 59.6 ms                                                             | 64.4 ms: 1.08x slower                                                                    |
| tomli_loads          | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                                   |
| xml_etree_process    | 42.1 ms                                                             | 47.2 ms: 1.12x slower                                                                    |
| unpickle_pure_python | 147 us                                                              | 166 us: 1.13x slower                                                                     |
| pickle_pure_python   | 213 us                                                              | 242 us: 1.14x slower                                                                     |
| Geometric mean       | (ref)                                                               | 1.07x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.6 ms: 1.06x slower                                                                    |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                                    |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.2 ms: 1.09x slower                                                                    |
| genshi_text     | 20.1 ms                                                             | 22.2 ms: 1.11x slower                                                                    |
| mako            | 6.94 ms                                                             | 7.96 ms: 1.15x slower                                                                    |
| django_template | 30.1 ms                                                             | 35.0 ms: 1.16x slower                                                                    |
| Geometric mean  | (ref)                                                               | 1.13x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 758 us: 12.84x faster                                                                    |
| coverage                   | 307 ms                                                              | 51.5 ms: 5.96x faster                                                                    |
| deepcopy                   | 280 us                                                              | 249 us: 1.12x faster                                                                     |
| deepcopy_memo              | 23.5 us                                                             | 21.3 us: 1.10x faster                                                                    |
| async_tree_none_tg         | 203 ms                                                              | 190 ms: 1.07x faster                                                                     |
| async_tree_io_tg           | 529 ms                                                              | 501 ms: 1.06x faster                                                                     |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                                     |
| deepcopy_reduce            | 2.59 us                                                             | 2.53 us: 1.02x faster                                                                    |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                                     |
| create_gc_cycles           | 756 us                                                              | 741 us: 1.02x faster                                                                     |
| json_loads                 | 20.5 us                                                             | 20.3 us: 1.01x faster                                                                    |
| xml_etree_parse            | 104 ms                                                              | 105 ms: 1.01x slower                                                                     |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                                   |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                                     |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.03x slower                                                                    |
| async_tree_io              | 530 ms                                                              | 547 ms: 1.03x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                                     |
| bench_mp_pool              | 69.4 ms                                                             | 72.0 ms: 1.04x slower                                                                    |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.04x slower                                                                     |
| json_dumps                 | 6.84 ms                                                             | 7.12 ms: 1.04x slower                                                                    |
| json                       | 4.10 ms                                                             | 4.28 ms: 1.04x slower                                                                    |
| sympy_expand               | 375 ms                                                              | 392 ms: 1.04x slower                                                                     |
| meteor_contest             | 74.1 ms                                                             | 77.5 ms: 1.05x slower                                                                    |
| sympy_str                  | 211 ms                                                              | 221 ms: 1.05x slower                                                                     |
| docutils                   | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                                   |
| regex_effbot               | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                                    |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.6 ms: 1.05x slower                                                                    |
| mdp                        | 1.60 sec                                                            | 1.69 sec: 1.05x slower                                                                   |
| regex_compile              | 99.9 ms                                                             | 105 ms: 1.05x slower                                                                     |
| crypto_pyaes               | 55.8 ms                                                             | 58.9 ms: 1.06x slower                                                                    |
| pathlib                    | 83.9 ms                                                             | 88.6 ms: 1.06x slower                                                                    |
| telco                      | 6.03 ms                                                             | 6.37 ms: 1.06x slower                                                                    |
| html5lib                   | 45.4 ms                                                             | 48.2 ms: 1.06x slower                                                                    |
| sympy_integrate            | 14.6 ms                                                             | 15.6 ms: 1.06x slower                                                                    |
| python_startup             | 22.2 ms                                                             | 23.6 ms: 1.06x slower                                                                    |
| pprint_safe_repr           | 607 ms                                                              | 648 ms: 1.07x slower                                                                     |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                                   |
| async_generators           | 266 ms                                                              | 284 ms: 1.07x slower                                                                     |
| logging_simple             | 7.47 us                                                             | 7.99 us: 1.07x slower                                                                    |
| logging_format             | 8.13 us                                                             | 8.72 us: 1.07x slower                                                                    |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                                    |
| xml_etree_generate         | 59.6 ms                                                             | 64.4 ms: 1.08x slower                                                                    |
| regex_dna                  | 118 ms                                                              | 128 ms: 1.08x slower                                                                     |
| pylint                     | 217 ms                                                              | 235 ms: 1.08x slower                                                                     |
| asyncio_tcp                | 662 ms                                                              | 719 ms: 1.09x slower                                                                     |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                                     |
| genshi_xml                 | 44.3 ms                                                             | 48.2 ms: 1.09x slower                                                                    |
| pyflate                    | 308 ms                                                              | 337 ms: 1.09x slower                                                                     |
| typing_runtime_protocols   | 136 us                                                              | 149 us: 1.10x slower                                                                     |
| coroutines                 | 15.5 ms                                                             | 17.1 ms: 1.10x slower                                                                    |
| genshi_text                | 20.1 ms                                                             | 22.2 ms: 1.11x slower                                                                    |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.11x slower                                                                     |
| spectral_norm              | 68.0 ms                                                             | 75.4 ms: 1.11x slower                                                                    |
| pycparser                  | 777 ms                                                              | 863 ms: 1.11x slower                                                                     |
| tomli_loads                | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                                   |
| chaos                      | 48.0 ms                                                             | 53.7 ms: 1.12x slower                                                                    |
| xml_etree_process          | 42.1 ms                                                             | 47.2 ms: 1.12x slower                                                                    |
| fannkuch                   | 270 ms                                                              | 303 ms: 1.12x slower                                                                     |
| scimark_fft                | 198 ms                                                              | 223 ms: 1.12x slower                                                                     |
| sqlglot_parse              | 964 us                                                              | 1.08 ms: 1.12x slower                                                                    |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.12x slower                                                                    |
| float                      | 52.4 ms                                                             | 58.9 ms: 1.13x slower                                                                    |
| unpickle_pure_python       | 147 us                                                              | 166 us: 1.13x slower                                                                     |
| go                         | 101 ms                                                              | 114 ms: 1.14x slower                                                                     |
| pickle_pure_python         | 213 us                                                              | 242 us: 1.14x slower                                                                     |
| sqlglot_normalize          | 206 ms                                                              | 235 ms: 1.14x slower                                                                     |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.29 ms: 1.14x slower                                                                    |
| mako                       | 6.94 ms                                                             | 7.96 ms: 1.15x slower                                                                    |
| sqlglot_optimize           | 39.7 ms                                                             | 45.7 ms: 1.15x slower                                                                    |
| deltablue                  | 2.23 ms                                                             | 2.58 ms: 1.15x slower                                                                    |
| comprehensions             | 11.9 us                                                             | 13.7 us: 1.15x slower                                                                    |
| scimark_sor                | 81.0 ms                                                             | 93.9 ms: 1.16x slower                                                                    |
| django_template            | 30.1 ms                                                             | 35.0 ms: 1.16x slower                                                                    |
| scimark_monte_carlo        | 45.2 ms                                                             | 52.7 ms: 1.17x slower                                                                    |
| scimark_lu                 | 59.4 ms                                                             | 69.4 ms: 1.17x slower                                                                    |
| raytrace                   | 189 ms                                                              | 221 ms: 1.17x slower                                                                     |
| nbody                      | 76.9 ms                                                             | 90.3 ms: 1.17x slower                                                                    |
| richards_super             | 35.5 ms                                                             | 41.8 ms: 1.18x slower                                                                    |
| nqueens                    | 68.7 ms                                                             | 80.9 ms: 1.18x slower                                                                    |
| richards                   | 31.2 ms                                                             | 37.3 ms: 1.19x slower                                                                    |
| hexiom                     | 4.23 ms                                                             | 5.06 ms: 1.20x slower                                                                    |
| generators                 | 21.2 ms                                                             | 26.3 ms: 1.24x slower                                                                    |
| logging_silent             | 57.9 ns                                                             | 72.7 ns: 1.26x slower                                                                    |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                             |

Benchmark hidden because not significant (4): async_tree_memoization, gc_traversal, async_tree_cpu_io_mixed, bench_thread_pool
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown