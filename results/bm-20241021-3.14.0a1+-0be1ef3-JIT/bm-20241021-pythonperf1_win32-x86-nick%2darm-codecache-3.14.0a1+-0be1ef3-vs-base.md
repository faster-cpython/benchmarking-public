# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: windows-x86
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                          | 255 ms: 1.04x faster                                                     |
| docutils       | 2.06 sec                                                                        | 1.97 sec: 1.04x faster                                                   |
| sphinx         | 851 ms                                                                          | 819 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 269 ms                                                                          | 252 ms: 1.07x faster                                                     |
| async_tree_none_tg         | 206 ms                                                                          | 200 ms: 1.03x faster                                                     |
| async_tree_none            | 222 ms                                                                          | 217 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                          | 463 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 476 ms                                                                          | 470 ms: 1.01x faster                                                     |
| coroutines                 | 17.3 ms                                                                         | 17.4 ms: 1.01x slower                                                    |
| async_generators           | 314 ms                                                                          | 319 ms: 1.01x slower                                                     |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                             |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 64.6 ms                                                                         | 57.9 ms: 1.12x faster                                                    |
| float          | 46.6 ms                                                                         | 45.9 ms: 1.01x faster                                                    |
| pidigits       | 204 ms                                                                          | 203 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                          | 113 ms: 1.09x faster                                                     |
| regex_compile  | 105 ms                                                                          | 97.7 ms: 1.08x faster                                                    |
| regex_effbot   | 1.89 ms                                                                         | 1.76 ms: 1.07x faster                                                    |
| regex_v8       | 15.4 ms                                                                         | 15.2 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                           | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 246 us                                                                          | 237 us: 1.04x faster                                                     |
| xml_etree_process    | 42.1 ms                                                                         | 40.8 ms: 1.03x faster                                                    |
| unpickle_pure_python | 160 us                                                                          | 156 us: 1.03x faster                                                     |
| xml_etree_parse      | 112 ms                                                                          | 109 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 65.1 ms                                                                         | 63.5 ms: 1.02x faster                                                    |
| json_dumps           | 8.14 ms                                                                         | 8.03 ms: 1.01x faster                                                    |
| tomli_loads          | 1.53 sec                                                                        | 1.51 sec: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                                           | 1.02x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 20.4 ms                                                                         | 20.6 ms: 1.01x slower                                                    |
| python_startup         | 26.7 ms                                                                         | 27.0 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                           | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 54.3 ms                                                                         | 48.9 ms: 1.11x faster                                                    |
| genshi_text     | 23.4 ms                                                                         | 22.5 ms: 1.04x faster                                                    |
| django_template | 32.7 ms                                                                         | 32.4 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                           | 1.04x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| hexiom                     | 5.32 ms                                                                         | 4.70 ms: 1.13x faster                                                    |
| richards                   | 39.2 ms                                                                         | 34.9 ms: 1.12x faster                                                    |
| nbody                      | 64.6 ms                                                                         | 57.9 ms: 1.12x faster                                                    |
| richards_super             | 45.3 ms                                                                         | 40.7 ms: 1.11x faster                                                    |
| genshi_xml                 | 54.3 ms                                                                         | 48.9 ms: 1.11x faster                                                    |
| regex_dna                  | 124 ms                                                                          | 113 ms: 1.09x faster                                                     |
| go                         | 96.7 ms                                                                         | 89.2 ms: 1.08x faster                                                    |
| regex_compile              | 105 ms                                                                          | 97.7 ms: 1.08x faster                                                    |
| regex_effbot               | 1.89 ms                                                                         | 1.76 ms: 1.07x faster                                                    |
| scimark_lu                 | 61.8 ms                                                                         | 57.7 ms: 1.07x faster                                                    |
| generators                 | 23.9 ms                                                                         | 22.4 ms: 1.07x faster                                                    |
| async_tree_memoization_tg  | 269 ms                                                                          | 252 ms: 1.07x faster                                                     |
| scimark_monte_carlo        | 40.0 ms                                                                         | 37.9 ms: 1.05x faster                                                    |
| deepcopy_memo              | 16.6 us                                                                         | 15.8 us: 1.05x faster                                                    |
| scimark_sor                | 70.2 ms                                                                         | 67.0 ms: 1.05x faster                                                    |
| sympy_str                  | 230 ms                                                                          | 219 ms: 1.05x faster                                                     |
| raytrace                   | 275 ms                                                                          | 263 ms: 1.05x faster                                                     |
| sqlglot_parse              | 1.05 ms                                                                         | 1.01 ms: 1.05x faster                                                    |
| sqlglot_optimize           | 49.9 ms                                                                         | 47.8 ms: 1.05x faster                                                    |
| scimark_fft                | 183 ms                                                                          | 175 ms: 1.05x faster                                                     |
| sympy_expand               | 399 ms                                                                          | 382 ms: 1.04x faster                                                     |
| docutils                   | 2.06 sec                                                                        | 1.97 sec: 1.04x faster                                                   |
| pyflate                    | 312 ms                                                                          | 300 ms: 1.04x faster                                                     |
| sphinx                     | 851 ms                                                                          | 819 ms: 1.04x faster                                                     |
| nqueens                    | 76.3 ms                                                                         | 73.4 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.35 ms                                                                         | 1.30 ms: 1.04x faster                                                    |
| comprehensions             | 13.0 us                                                                         | 12.5 us: 1.04x faster                                                    |
| pickle_pure_python         | 246 us                                                                          | 237 us: 1.04x faster                                                     |
| 2to3                       | 264 ms                                                                          | 255 ms: 1.04x faster                                                     |
| genshi_text                | 23.4 ms                                                                         | 22.5 ms: 1.04x faster                                                    |
| pycparser                  | 809 ms                                                                          | 781 ms: 1.04x faster                                                     |
| deepcopy_reduce            | 2.44 us                                                                         | 2.36 us: 1.03x faster                                                    |
| xml_etree_process          | 42.1 ms                                                                         | 40.8 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 160 us                                                                          | 156 us: 1.03x faster                                                     |
| async_tree_none_tg         | 206 ms                                                                          | 200 ms: 1.03x faster                                                     |
| chaos                      | 54.5 ms                                                                         | 53.0 ms: 1.03x faster                                                    |
| xml_etree_parse            | 112 ms                                                                          | 109 ms: 1.03x faster                                                     |
| telco                      | 6.33 ms                                                                         | 6.16 ms: 1.03x faster                                                    |
| async_tree_none            | 222 ms                                                                          | 217 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 65.1 ms                                                                         | 63.5 ms: 1.02x faster                                                    |
| fannkuch                   | 237 ms                                                                          | 232 ms: 1.02x faster                                                     |
| meteor_contest             | 72.3 ms                                                                         | 70.7 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.16 sec                                                                        | 1.13 sec: 1.02x faster                                                   |
| pprint_safe_repr           | 567 ms                                                                          | 556 ms: 1.02x faster                                                     |
| mdp                        | 1.70 sec                                                                        | 1.67 sec: 1.02x faster                                                   |
| sqlglot_normalize          | 101 ms                                                                          | 99.3 ms: 1.02x faster                                                    |
| crypto_pyaes               | 49.8 ms                                                                         | 48.9 ms: 1.02x faster                                                    |
| sympy_integrate            | 17.3 ms                                                                         | 17.0 ms: 1.02x faster                                                    |
| sympy_sum                  | 116 ms                                                                          | 114 ms: 1.02x faster                                                     |
| dulwich_log                | 49.5 ms                                                                         | 48.7 ms: 1.02x faster                                                    |
| typing_runtime_protocols   | 141 us                                                                          | 139 us: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                          | 463 ms: 1.02x faster                                                     |
| float                      | 46.6 ms                                                                         | 45.9 ms: 1.01x faster                                                    |
| json_dumps                 | 8.14 ms                                                                         | 8.03 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 476 ms                                                                          | 470 ms: 1.01x faster                                                     |
| deepcopy                   | 236 us                                                                          | 233 us: 1.01x faster                                                     |
| django_template            | 32.7 ms                                                                         | 32.4 ms: 1.01x faster                                                    |
| logging_silent             | 55.6 ns                                                                         | 55.1 ns: 1.01x faster                                                    |
| logging_simple             | 7.58 us                                                                         | 7.50 us: 1.01x faster                                                    |
| regex_v8                   | 15.4 ms                                                                         | 15.2 ms: 1.01x faster                                                    |
| tomli_loads                | 1.53 sec                                                                        | 1.51 sec: 1.01x faster                                                   |
| create_gc_cycles           | 1.19 ms                                                                         | 1.18 ms: 1.01x faster                                                    |
| bench_mp_pool              | 94.1 ms                                                                         | 93.6 ms: 1.00x faster                                                    |
| pidigits                   | 204 ms                                                                          | 203 ms: 1.00x faster                                                     |
| coroutines                 | 17.3 ms                                                                         | 17.4 ms: 1.01x slower                                                    |
| python_startup_no_site     | 20.4 ms                                                                         | 20.6 ms: 1.01x slower                                                    |
| python_startup             | 26.7 ms                                                                         | 27.0 ms: 1.01x slower                                                    |
| async_generators           | 314 ms                                                                          | 319 ms: 1.01x slower                                                     |
| spectral_norm              | 57.8 ms                                                                         | 58.7 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                                           | 1.03x faster                                                             |

Benchmark hidden because not significant (18): pylint, async_tree_memoization, xml_etree_generate, async_tree_io_tg, async_tree_io, coverage, scimark_sparse_mat_mult, mako, gc_traversal, logging_format, html5lib, json_loads, deltablue, pathlib, tornado_http, thrift, bench_thread_pool, json

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown