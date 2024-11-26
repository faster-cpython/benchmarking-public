# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: windows-x86
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                          | 255 ms: 1.03x faster                                                     |
| docutils       | 2.06 sec                                                                        | 1.97 sec: 1.04x faster                                                   |
| sphinx         | 849 ms                                                                          | 819 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg   | 562 ms                                                                          | 549 ms: 1.02x faster                                                     |
| async_tree_none_tg | 204 ms                                                                          | 200 ms: 1.02x faster                                                     |
| coroutines         | 17.7 ms                                                                         | 17.4 ms: 1.02x faster                                                    |
| async_tree_none    | 220 ms                                                                          | 217 ms: 1.02x faster                                                     |
| async_generators   | 315 ms                                                                          | 319 ms: 1.01x slower                                                     |
| Geometric mean     | (ref)                                                                           | 1.01x faster                                                             |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 65.9 ms                                                                         | 57.9 ms: 1.14x faster                                                    |
| float          | 46.7 ms                                                                         | 45.9 ms: 1.02x faster                                                    |
| pidigits       | 205 ms                                                                          | 203 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                           | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                          | 113 ms: 1.09x faster                                                     |
| regex_effbot   | 1.90 ms                                                                         | 1.76 ms: 1.08x faster                                                    |
| regex_compile  | 104 ms                                                                          | 97.7 ms: 1.07x faster                                                    |
| regex_v8       | 15.6 ms                                                                         | 15.2 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                           | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                                         | 63.5 ms: 1.03x faster                                                    |
| json_loads           | 21.3 us                                                                         | 20.8 us: 1.02x faster                                                    |
| unpickle_pure_python | 159 us                                                                          | 156 us: 1.02x faster                                                     |
| xml_etree_parse      | 111 ms                                                                          | 109 ms: 1.02x faster                                                     |
| json_dumps           | 8.14 ms                                                                         | 8.03 ms: 1.01x faster                                                    |
| xml_etree_process    | 41.4 ms                                                                         | 40.8 ms: 1.01x faster                                                    |
| xml_etree_generate   | 55.6 ms                                                                         | 54.9 ms: 1.01x faster                                                    |
| pickle_pure_python   | 239 us                                                                          | 237 us: 1.01x faster                                                     |
| tomli_loads          | 1.49 sec                                                                        | 1.51 sec: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                           | 1.01x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 20.2 ms                                                                         | 20.6 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                                           | 1.01x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 52.7 ms                                                                         | 48.9 ms: 1.08x faster                                                    |
| django_template | 33.4 ms                                                                         | 32.4 ms: 1.03x faster                                                    |
| genshi_text     | 23.1 ms                                                                         | 22.5 ms: 1.03x faster                                                    |
| Geometric mean  | (ref)                                                                           | 1.03x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| sqlglot_normalize        | 240 ms                                                                          | 99.3 ms: 2.42x faster                                                    |
| nbody                    | 65.9 ms                                                                         | 57.9 ms: 1.14x faster                                                    |
| richards                 | 39.3 ms                                                                         | 34.9 ms: 1.13x faster                                                    |
| hexiom                   | 5.27 ms                                                                         | 4.70 ms: 1.12x faster                                                    |
| generators               | 24.7 ms                                                                         | 22.4 ms: 1.10x faster                                                    |
| mdp                      | 1.84 sec                                                                        | 1.67 sec: 1.10x faster                                                   |
| richards_super           | 44.5 ms                                                                         | 40.7 ms: 1.09x faster                                                    |
| regex_dna                | 123 ms                                                                          | 113 ms: 1.09x faster                                                     |
| go                       | 96.7 ms                                                                         | 89.2 ms: 1.08x faster                                                    |
| genshi_xml               | 52.7 ms                                                                         | 48.9 ms: 1.08x faster                                                    |
| regex_effbot             | 1.90 ms                                                                         | 1.76 ms: 1.08x faster                                                    |
| fannkuch                 | 248 ms                                                                          | 232 ms: 1.07x faster                                                     |
| regex_compile            | 104 ms                                                                          | 97.7 ms: 1.07x faster                                                    |
| pyflate                  | 319 ms                                                                          | 300 ms: 1.06x faster                                                     |
| typing_runtime_protocols | 147 us                                                                          | 139 us: 1.06x faster                                                     |
| sqlglot_parse            | 1.06 ms                                                                         | 1.01 ms: 1.06x faster                                                    |
| pycparser                | 824 ms                                                                          | 781 ms: 1.05x faster                                                     |
| comprehensions           | 13.2 us                                                                         | 12.5 us: 1.05x faster                                                    |
| sqlglot_transpile        | 1.37 ms                                                                         | 1.30 ms: 1.05x faster                                                    |
| sympy_expand             | 400 ms                                                                          | 382 ms: 1.05x faster                                                     |
| sympy_str                | 229 ms                                                                          | 219 ms: 1.05x faster                                                     |
| docutils                 | 2.06 sec                                                                        | 1.97 sec: 1.04x faster                                                   |
| sqlglot_optimize         | 49.8 ms                                                                         | 47.8 ms: 1.04x faster                                                    |
| scimark_fft              | 182 ms                                                                          | 175 ms: 1.04x faster                                                     |
| sphinx                   | 849 ms                                                                          | 819 ms: 1.04x faster                                                     |
| 2to3                     | 263 ms                                                                          | 255 ms: 1.03x faster                                                     |
| meteor_contest           | 73.1 ms                                                                         | 70.7 ms: 1.03x faster                                                    |
| raytrace                 | 271 ms                                                                          | 263 ms: 1.03x faster                                                     |
| django_template          | 33.4 ms                                                                         | 32.4 ms: 1.03x faster                                                    |
| scimark_lu               | 59.5 ms                                                                         | 57.7 ms: 1.03x faster                                                    |
| sympy_sum                | 117 ms                                                                          | 114 ms: 1.03x faster                                                     |
| scimark_monte_carlo      | 39.0 ms                                                                         | 37.9 ms: 1.03x faster                                                    |
| xml_etree_iterparse      | 65.2 ms                                                                         | 63.5 ms: 1.03x faster                                                    |
| genshi_text              | 23.1 ms                                                                         | 22.5 ms: 1.03x faster                                                    |
| async_tree_io_tg         | 562 ms                                                                          | 549 ms: 1.02x faster                                                     |
| regex_v8                 | 15.6 ms                                                                         | 15.2 ms: 1.02x faster                                                    |
| json_loads               | 21.3 us                                                                         | 20.8 us: 1.02x faster                                                    |
| async_tree_none_tg       | 204 ms                                                                          | 200 ms: 1.02x faster                                                     |
| deepcopy_memo            | 16.2 us                                                                         | 15.8 us: 1.02x faster                                                    |
| unpickle_pure_python     | 159 us                                                                          | 156 us: 1.02x faster                                                     |
| create_gc_cycles         | 1.20 ms                                                                         | 1.18 ms: 1.02x faster                                                    |
| coroutines               | 17.7 ms                                                                         | 17.4 ms: 1.02x faster                                                    |
| xml_etree_parse          | 111 ms                                                                          | 109 ms: 1.02x faster                                                     |
| logging_simple           | 7.63 us                                                                         | 7.50 us: 1.02x faster                                                    |
| deepcopy_reduce          | 2.40 us                                                                         | 2.36 us: 1.02x faster                                                    |
| float                    | 46.7 ms                                                                         | 45.9 ms: 1.02x faster                                                    |
| coverage                 | 54.1 ms                                                                         | 53.3 ms: 1.02x faster                                                    |
| async_tree_none          | 220 ms                                                                          | 217 ms: 1.02x faster                                                     |
| crypto_pyaes             | 49.6 ms                                                                         | 48.9 ms: 1.01x faster                                                    |
| json_dumps               | 8.14 ms                                                                         | 8.03 ms: 1.01x faster                                                    |
| xml_etree_process        | 41.4 ms                                                                         | 40.8 ms: 1.01x faster                                                    |
| sympy_integrate          | 17.3 ms                                                                         | 17.0 ms: 1.01x faster                                                    |
| xml_etree_generate       | 55.6 ms                                                                         | 54.9 ms: 1.01x faster                                                    |
| dulwich_log              | 49.3 ms                                                                         | 48.7 ms: 1.01x faster                                                    |
| pidigits                 | 205 ms                                                                          | 203 ms: 1.01x faster                                                     |
| pprint_pformat           | 1.14 sec                                                                        | 1.13 sec: 1.01x faster                                                   |
| deltablue                | 2.55 ms                                                                         | 2.52 ms: 1.01x faster                                                    |
| pickle_pure_python       | 239 us                                                                          | 237 us: 1.01x faster                                                     |
| nqueens                  | 73.9 ms                                                                         | 73.4 ms: 1.01x faster                                                    |
| pprint_safe_repr         | 560 ms                                                                          | 556 ms: 1.01x faster                                                     |
| logging_format           | 8.28 us                                                                         | 8.23 us: 1.01x faster                                                    |
| bench_mp_pool            | 94.1 ms                                                                         | 93.6 ms: 1.01x faster                                                    |
| scimark_sor              | 66.5 ms                                                                         | 67.0 ms: 1.01x slower                                                    |
| deepcopy                 | 231 us                                                                          | 233 us: 1.01x slower                                                     |
| spectral_norm            | 58.3 ms                                                                         | 58.7 ms: 1.01x slower                                                    |
| async_generators         | 315 ms                                                                          | 319 ms: 1.01x slower                                                     |
| tomli_loads              | 1.49 sec                                                                        | 1.51 sec: 1.01x slower                                                   |
| telco                    | 6.06 ms                                                                         | 6.16 ms: 1.02x slower                                                    |
| thrift                   | 770 us                                                                          | 784 us: 1.02x slower                                                     |
| python_startup_no_site   | 20.2 ms                                                                         | 20.6 ms: 1.02x slower                                                    |
| logging_silent           | 53.8 ns                                                                         | 55.1 ns: 1.02x slower                                                    |
| Geometric mean           | (ref)                                                                           | 1.04x faster                                                             |

Benchmark hidden because not significant (16): pylint, async_tree_memoization_tg, async_tree_memoization, scimark_sparse_mat_mult, tornado_http, async_tree_cpu_io_mixed_tg, html5lib, gc_traversal, async_tree_io, mako, python_startup, chaos, pathlib, async_tree_cpu_io_mixed, bench_thread_pool, json

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown