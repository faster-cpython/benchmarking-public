# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-x86
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                              |
| html5lib       | 52.1 ms                                                         | 46.4 ms: 1.12x faster                                                             |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                              |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 471 ms: 1.96x faster                                                              |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                              |
| async_tree_io           | 940 ms                                                          | 544 ms: 1.73x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                              |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                              |
| float          | 69.6 ms                                                         | 42.9 ms: 1.62x faster                                                             |
| nbody          | 79.1 ms                                                         | 53.1 ms: 1.49x faster                                                             |
| Geometric mean | (ref)                                                           | 1.84x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.3 ms: 1.22x faster                                                             |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                              |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                             |
| regex_effbot   | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.00 ms: 1.40x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.46 sec: 1.31x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 217 us: 1.29x faster                                                              |
| unpickle_pure_python | 189 us                                                          | 149 us: 1.28x faster                                                              |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.1 ms: 1.11x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.7 ms: 1.08x faster                                                             |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.05x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 59.6 ms: 1.03x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.9 ms: 1.04x slower                                                             |
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.41 ms: 1.68x faster                                                             |
| django_template | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                             |
| genshi_xml      | 46.6 ms                                                         | 51.4 ms: 1.10x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.71x faster                                                              |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 471 ms: 1.96x faster                                                              |
| deepcopy_memo            | 29.6 us                                                         | 15.7 us: 1.88x faster                                                             |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                              |
| async_tree_io            | 940 ms                                                          | 544 ms: 1.73x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                              |
| spectral_norm            | 80.2 ms                                                         | 47.3 ms: 1.70x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.41 ms: 1.68x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 48.7 ms: 1.67x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 59.0 ns: 1.66x faster                                                             |
| float                    | 69.6 ms                                                         | 42.9 ms: 1.62x faster                                                             |
| pyflate                  | 422 ms                                                          | 264 ms: 1.60x faster                                                              |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.56x faster                                                             |
| pylint                   | 384 ms                                                          | 248 ms: 1.55x faster                                                              |
| nbody                    | 79.1 ms                                                         | 53.1 ms: 1.49x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.71 ms: 1.49x faster                                                             |
| chaos                    | 74.4 ms                                                         | 51.6 ms: 1.44x faster                                                             |
| sqlglot_parse            | 1.33 ms                                                         | 936 us: 1.42x faster                                                              |
| scimark_monte_carlo      | 61.9 ms                                                         | 44.0 ms: 1.41x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 7.00 ms: 1.40x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.37 ms: 1.37x faster                                                             |
| raytrace                 | 303 ms                                                          | 226 ms: 1.34x faster                                                              |
| fannkuch                 | 317 ms                                                          | 238 ms: 1.33x faster                                                              |
| hexiom                   | 6.13 ms                                                         | 4.62 ms: 1.33x faster                                                             |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                                             |
| pycparser                | 1.04 sec                                                        | 796 ms: 1.31x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.46 sec: 1.31x faster                                                            |
| deepcopy                 | 310 us                                                          | 237 us: 1.31x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 217 us: 1.29x faster                                                              |
| scimark_fft              | 216 ms                                                          | 167 ms: 1.29x faster                                                              |
| unpickle_pure_python     | 189 us                                                          | 149 us: 1.28x faster                                                              |
| richards_super           | 49.9 ms                                                         | 39.5 ms: 1.26x faster                                                             |
| go                       | 146 ms                                                          | 115 ms: 1.26x faster                                                              |
| thrift                   | 902 us                                                          | 725 us: 1.24x faster                                                              |
| regex_compile            | 117 ms                                                          | 95.3 ms: 1.22x faster                                                             |
| richards                 | 40.3 ms                                                         | 33.8 ms: 1.19x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 74.3 ms: 1.17x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 78.9 ms: 1.14x faster                                                             |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 582 ms: 1.13x faster                                                              |
| meteor_contest           | 80.0 ms                                                         | 70.8 ms: 1.13x faster                                                             |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                              |
| html5lib                 | 52.1 ms                                                         | 46.4 ms: 1.12x faster                                                             |
| generators               | 31.6 ms                                                         | 28.2 ms: 1.12x faster                                                             |
| django_template          | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                             |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                              |
| asyncio_tcp              | 744 ms                                                          | 671 ms: 1.11x faster                                                              |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.42 us: 1.11x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.1 ms: 1.11x faster                                                             |
| json                     | 4.76 ms                                                         | 4.31 ms: 1.10x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.66 sec: 1.10x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 44.7 ms: 1.08x faster                                                             |
| scimark_sor              | 115 ms                                                          | 107 ms: 1.08x faster                                                              |
| sympy_str                | 229 ms                                                          | 215 ms: 1.06x faster                                                              |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.05x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 16.1 ms: 1.04x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 59.6 ms: 1.03x faster                                                             |
| sympy_expand             | 391 ms                                                          | 380 ms: 1.03x faster                                                              |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                              |
| sqlglot_optimize         | 44.7 ms                                                         | 43.6 ms: 1.03x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                             |
| coroutines               | 17.9 ms                                                         | 18.0 ms: 1.01x slower                                                             |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.02x slower                                                              |
| logging_simple           | 7.29 us                                                         | 7.47 us: 1.02x slower                                                             |
| logging_format           | 7.91 us                                                         | 8.13 us: 1.03x slower                                                             |
| python_startup           | 22.9 ms                                                         | 23.9 ms: 1.04x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                             |
| pathlib                  | 81.2 ms                                                         | 88.8 ms: 1.09x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 51.4 ms: 1.10x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 769 us: 1.11x slower                                                              |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.12x slower                                                             |
| coverage                 | 46.6 ms                                                         | 52.8 ms: 1.13x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.14x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 77.4 ms: 1.17x slower                                                             |
| telco                    | 4.83 ms                                                         | 5.77 ms: 1.19x slower                                                             |
| regex_effbot             | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                             |
| async_generators         | 241 ms                                                          | 310 ms: 1.29x slower                                                              |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, docutils
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown