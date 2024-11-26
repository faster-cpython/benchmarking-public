# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.180x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 253 ms: 1.03x slower                                                           |
| docutils       | 1.92 sec                                                    | 1.94 sec: 1.01x slower                                                         |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                          |
| tornado_http   | 108 ms                                                      | 98.6 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 550 ms: 2.01x faster                                                           |
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.64x faster                                                           |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.9 ms: 1.37x faster                                                          |
| float          | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                                          |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 92.7 ms: 1.14x faster                                                          |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                           |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.47 ms: 1.42x faster                                                          |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.36x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 1.31 sec: 1.27x faster                                                         |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.26x faster                                                           |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                          |
| xml_etree_parse      | 96.8 ms                                                     | 95.7 ms: 1.01x faster                                                          |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.20 ms: 1.74x faster                                                          |
| django_template | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 49.1 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.86x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 550 ms: 2.01x faster                                                           |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.38 ms: 1.76x faster                                                          |
| mako                     | 9.03 ms                                                     | 5.20 ms: 1.74x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 16.9 us: 1.71x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 56.4 ns: 1.68x faster                                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.64x faster                                                           |
| scimark_sor              | 106 ms                                                      | 67.0 ms: 1.59x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.0 ms: 1.51x faster                                                          |
| go                       | 139 ms                                                      | 94.0 ms: 1.48x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 42.5 ms: 1.47x faster                                                          |
| scimark_lu               | 85.8 ms                                                     | 59.0 ms: 1.45x faster                                                          |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 53.9 ms: 1.43x faster                                                          |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 6.47 ms: 1.42x faster                                                          |
| nbody                    | 71.3 ms                                                     | 51.9 ms: 1.37x faster                                                          |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                          |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.36x faster                                                           |
| pyflate                  | 409 ms                                                      | 303 ms: 1.35x faster                                                           |
| richards_super           | 52.2 ms                                                     | 39.5 ms: 1.32x faster                                                          |
| raytrace                 | 273 ms                                                      | 208 ms: 1.31x faster                                                           |
| deepcopy                 | 255 us                                                      | 195 us: 1.31x faster                                                           |
| sqlglot_parse            | 1.22 ms                                                     | 931 us: 1.31x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 941 ms: 1.30x faster                                                           |
| float                    | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.31 sec: 1.27x faster                                                         |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.26x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 470 ms: 1.26x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                          |
| pycparser                | 930 ms                                                      | 744 ms: 1.25x faster                                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.20 ms: 1.24x faster                                                          |
| pylint                   | 350 ms                                                      | 284 ms: 1.23x faster                                                           |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                          |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                          |
| sqlglot_transpile        | 1.48 ms                                                     | 1.21 ms: 1.22x faster                                                          |
| richards                 | 42.4 ms                                                     | 35.5 ms: 1.20x faster                                                          |
| thrift                   | 617 us                                                      | 521 us: 1.18x faster                                                           |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                          |
| scimark_fft              | 187 ms                                                      | 161 ms: 1.16x faster                                                           |
| mdp                      | 1.78 sec                                                    | 1.54 sec: 1.16x faster                                                         |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.15x faster                                                           |
| regex_compile            | 106 ms                                                      | 92.7 ms: 1.14x faster                                                          |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                           |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                          |
| tornado_http             | 108 ms                                                      | 98.6 ms: 1.10x faster                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                          |
| django_template          | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 5.43 ms: 1.06x faster                                                          |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                          |
| fannkuch                 | 256 ms                                                      | 248 ms: 1.03x faster                                                           |
| nqueens                  | 66.6 ms                                                     | 64.7 ms: 1.03x faster                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                          |
| logging_format           | 6.76 us                                                     | 6.59 us: 1.03x faster                                                          |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                          |
| logging_simple           | 6.22 us                                                     | 6.12 us: 1.02x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 95.7 ms: 1.01x faster                                                          |
| sympy_sum                | 107 ms                                                      | 106 ms: 1.01x faster                                                           |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| docutils                 | 1.92 sec                                                    | 1.94 sec: 1.01x slower                                                         |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                          |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                          |
| sqlglot_normalize        | 205 ms                                                      | 210 ms: 1.02x slower                                                           |
| 2to3                     | 246 ms                                                      | 253 ms: 1.03x slower                                                           |
| sympy_integrate          | 15.3 ms                                                     | 15.8 ms: 1.04x slower                                                          |
| sympy_expand             | 314 ms                                                      | 330 ms: 1.05x slower                                                           |
| pathlib                  | 75.7 ms                                                     | 81.1 ms: 1.07x slower                                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 43.9 ms: 1.10x slower                                                          |
| python_startup           | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                          |
| genshi_xml               | 41.0 ms                                                     | 49.1 ms: 1.20x slower                                                          |
| telco                    | 3.94 ms                                                     | 4.72 ms: 1.20x slower                                                          |
| async_generators         | 222 ms                                                      | 267 ms: 1.21x slower                                                           |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 89.9 ms: 1.45x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.40 ms: 1.75x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                   |

Benchmark hidden because not significant (3): regex_v8, sympy_str, genshi_text
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.180x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown