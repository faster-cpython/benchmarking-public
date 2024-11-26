# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-x86
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.204x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                        |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                         |
| async_tree_io           | 940 ms                                                          | 525 ms: 1.79x faster                                                         |
| async_tree_none         | 394 ms                                                          | 222 ms: 1.77x faster                                                         |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                         |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.46x faster                                                         |
| float          | 69.6 ms                                                         | 45.8 ms: 1.52x faster                                                        |
| nbody          | 79.1 ms                                                         | 56.4 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                           | 1.74x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 98.5 ms: 1.18x faster                                                        |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                         |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                        |
| regex_effbot   | 1.66 ms                                                         | 1.79 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.52 sec: 1.26x faster                                                       |
| json_dumps           | 9.82 ms                                                         | 8.11 ms: 1.21x faster                                                        |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 41.0 ms: 1.17x faster                                                        |
| pickle_pure_python   | 280 us                                                          | 241 us: 1.16x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 55.5 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.1 ms: 1.10x faster                                                        |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                        |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                         |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                        |
| python_startup         | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.68 ms: 1.60x faster                                                        |
| django_template | 36.0 ms                                                         | 33.5 ms: 1.07x faster                                                        |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                        |
| genshi_xml      | 46.6 ms                                                         | 52.2 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                         |
| pidigits                 | 502 ms                                                          | 204 ms: 2.46x faster                                                         |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 16.3 us: 1.82x faster                                                        |
| async_tree_io            | 940 ms                                                          | 525 ms: 1.79x faster                                                         |
| async_tree_none          | 394 ms                                                          | 222 ms: 1.77x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 55.8 ns: 1.75x faster                                                        |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 49.7 ms: 1.64x faster                                                        |
| scimark_sor              | 115 ms                                                          | 70.4 ms: 1.64x faster                                                        |
| scimark_monte_carlo      | 61.9 ms                                                         | 38.3 ms: 1.62x faster                                                        |
| mako                     | 9.10 ms                                                         | 5.68 ms: 1.60x faster                                                        |
| deltablue                | 4.04 ms                                                         | 2.54 ms: 1.59x faster                                                        |
| go                       | 146 ms                                                          | 92.2 ms: 1.58x faster                                                        |
| comprehensions           | 17.7 us                                                         | 11.7 us: 1.52x faster                                                        |
| float                    | 69.6 ms                                                         | 45.8 ms: 1.52x faster                                                        |
| scimark_lu               | 89.8 ms                                                         | 59.6 ms: 1.51x faster                                                        |
| pylint                   | 384 ms                                                          | 261 ms: 1.47x faster                                                         |
| fannkuch                 | 317 ms                                                          | 219 ms: 1.45x faster                                                         |
| generators               | 31.6 ms                                                         | 21.8 ms: 1.45x faster                                                        |
| pyflate                  | 422 ms                                                          | 296 ms: 1.42x faster                                                         |
| nbody                    | 79.1 ms                                                         | 56.4 ms: 1.40x faster                                                        |
| spectral_norm            | 80.2 ms                                                         | 58.4 ms: 1.37x faster                                                        |
| deepcopy                 | 310 us                                                          | 227 us: 1.37x faster                                                         |
| chaos                    | 74.4 ms                                                         | 54.5 ms: 1.37x faster                                                        |
| sqlglot_parse            | 1.33 ms                                                         | 1.01 ms: 1.32x faster                                                        |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.46 ms: 1.32x faster                                                        |
| pycparser                | 1.04 sec                                                        | 798 ms: 1.31x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 4.75 ms: 1.29x faster                                                        |
| tomli_loads              | 1.91 sec                                                        | 1.52 sec: 1.26x faster                                                       |
| json_dumps               | 9.82 ms                                                         | 8.11 ms: 1.21x faster                                                        |
| dulwich_log              | 58.5 ms                                                         | 48.3 ms: 1.21x faster                                                        |
| sqlglot_transpile        | 1.58 ms                                                         | 1.31 ms: 1.21x faster                                                        |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                                         |
| richards_super           | 49.9 ms                                                         | 41.6 ms: 1.20x faster                                                        |
| regex_compile            | 117 ms                                                          | 98.5 ms: 1.18x faster                                                        |
| xml_etree_process        | 48.1 ms                                                         | 41.0 ms: 1.17x faster                                                        |
| scimark_fft              | 216 ms                                                          | 184 ms: 1.17x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.17 sec: 1.17x faster                                                       |
| pickle_pure_python       | 280 us                                                          | 241 us: 1.16x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 570 ms: 1.15x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                        |
| nqueens                  | 87.1 ms                                                         | 75.9 ms: 1.15x faster                                                        |
| meteor_contest           | 80.0 ms                                                         | 69.9 ms: 1.14x faster                                                        |
| thrift                   | 902 us                                                          | 789 us: 1.14x faster                                                         |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                         |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.41 us: 1.11x faster                                                        |
| xml_etree_generate       | 61.6 ms                                                         | 55.5 ms: 1.11x faster                                                        |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                        |
| raytrace                 | 303 ms                                                          | 274 ms: 1.11x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.1 ms: 1.10x faster                                                        |
| richards                 | 40.3 ms                                                         | 36.7 ms: 1.10x faster                                                        |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                       |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                         |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                        |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                         |
| django_template          | 36.0 ms                                                         | 33.5 ms: 1.07x faster                                                        |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                         |
| sympy_str                | 229 ms                                                          | 220 ms: 1.04x faster                                                         |
| coroutines               | 17.9 ms                                                         | 17.6 ms: 1.02x faster                                                        |
| sympy_expand             | 391 ms                                                          | 387 ms: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                        |
| sympy_integrate          | 16.6 ms                                                         | 16.8 ms: 1.01x slower                                                        |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.03x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.58 us: 1.04x slower                                                        |
| logging_format           | 7.91 us                                                         | 8.28 us: 1.05x slower                                                        |
| sqlglot_optimize         | 44.7 ms                                                         | 46.9 ms: 1.05x slower                                                        |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                        |
| regex_effbot             | 1.66 ms                                                         | 1.79 ms: 1.07x slower                                                        |
| pathlib                  | 81.2 ms                                                         | 88.1 ms: 1.08x slower                                                        |
| genshi_xml               | 46.6 ms                                                         | 52.2 ms: 1.12x slower                                                        |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                        |
| coverage                 | 46.6 ms                                                         | 53.1 ms: 1.14x slower                                                        |
| python_startup           | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                        |
| telco                    | 4.83 ms                                                         | 5.72 ms: 1.18x slower                                                        |
| async_generators         | 241 ms                                                          | 324 ms: 1.34x slower                                                         |
| bench_mp_pool            | 66.4 ms                                                         | 91.8 ms: 1.38x slower                                                        |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.41x slower                                                        |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.72x slower                                                        |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                 |

Benchmark hidden because not significant (2): docutils, json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.204x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown