# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-amd64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 238 ms: 1.03x faster                                                          |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                        |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                         |
| tornado_http   | 108 ms                                                      | 84.1 ms: 1.29x faster                                                         |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 208 ms: 2.09x faster                                                          |
| async_tree_memoization  | 526 ms                                                      | 258 ms: 2.04x faster                                                          |
| async_tree_io           | 1.11 sec                                                    | 550 ms: 2.01x faster                                                          |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.67x faster                                                          |
| Geometric mean          | (ref)                                                       | 1.95x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                         |
| float          | 61.7 ms                                                     | 45.9 ms: 1.35x faster                                                         |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.4 ms: 1.19x faster                                                         |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                         |
| regex_v8       | 15.4 ms                                                     | 15.4 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 118 us: 1.56x faster                                                          |
| json_dumps           | 9.16 ms                                                     | 5.95 ms: 1.54x faster                                                         |
| pickle_pure_python   | 270 us                                                      | 183 us: 1.47x faster                                                          |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                         |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                         |
| xml_etree_parse      | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                         |
| xml_etree_generate   | 55.5 ms                                                     | 54.5 ms: 1.02x faster                                                         |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                         |
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.15 ms: 1.75x faster                                                         |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                         |
| genshi_text     | 19.8 ms                                                     | 18.6 ms: 1.06x faster                                                         |
| genshi_xml      | 41.0 ms                                                     | 43.7 ms: 1.07x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.86x faster                                                          |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.09x faster                                                          |
| async_tree_memoization   | 526 ms                                                      | 258 ms: 2.04x faster                                                          |
| async_tree_io            | 1.11 sec                                                    | 550 ms: 2.01x faster                                                          |
| deltablue                | 4.19 ms                                                     | 2.36 ms: 1.78x faster                                                         |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.77x faster                                                         |
| mako                     | 9.03 ms                                                     | 5.15 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.67x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 47.4 ms: 1.63x faster                                                         |
| logging_silent           | 94.6 ns                                                     | 58.1 ns: 1.63x faster                                                         |
| comprehensions           | 16.5 us                                                     | 10.1 us: 1.63x faster                                                         |
| richards_super           | 52.2 ms                                                     | 32.9 ms: 1.59x faster                                                         |
| unpickle_pure_python     | 183 us                                                      | 118 us: 1.56x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 5.95 ms: 1.54x faster                                                         |
| pyflate                  | 409 ms                                                      | 266 ms: 1.54x faster                                                          |
| chaos                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                         |
| crypto_pyaes             | 62.5 ms                                                     | 40.9 ms: 1.53x faster                                                         |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.41 sec: 1.50x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 489 ms: 1.50x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.3 ms: 1.50x faster                                                         |
| pickle_pure_python       | 270 us                                                      | 183 us: 1.47x faster                                                          |
| pylint                   | 350 ms                                                      | 239 ms: 1.46x faster                                                          |
| sqlglot_parse            | 1.22 ms                                                     | 830 us: 1.46x faster                                                          |
| richards                 | 42.4 ms                                                     | 29.0 ms: 1.46x faster                                                         |
| raytrace                 | 273 ms                                                      | 187 ms: 1.46x faster                                                          |
| go                       | 139 ms                                                      | 97.5 ms: 1.42x faster                                                         |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.39x faster                                                         |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                          |
| nbody                    | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                         |
| float                    | 61.7 ms                                                     | 45.9 ms: 1.35x faster                                                         |
| generators               | 32.4 ms                                                     | 24.5 ms: 1.32x faster                                                         |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                         |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.10 ms: 1.29x faster                                                         |
| tornado_http             | 108 ms                                                      | 84.1 ms: 1.29x faster                                                         |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.25x faster                                                         |
| pprint_pformat           | 1.22 sec                                                    | 978 ms: 1.25x faster                                                          |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.25x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 477 ms: 1.24x faster                                                          |
| bench_thread_pool        | 958 us                                                      | 782 us: 1.22x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                         |
| regex_compile            | 106 ms                                                      | 89.4 ms: 1.19x faster                                                         |
| scimark_lu               | 85.8 ms                                                     | 73.4 ms: 1.17x faster                                                         |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                          |
| pycparser                | 930 ms                                                      | 802 ms: 1.16x faster                                                          |
| scimark_sor              | 106 ms                                                      | 93.2 ms: 1.14x faster                                                         |
| xml_etree_process        | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                         |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                          |
| sympy_sum                | 107 ms                                                      | 95.0 ms: 1.13x faster                                                         |
| fannkuch                 | 256 ms                                                      | 227 ms: 1.13x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 60.0 ms: 1.11x faster                                                         |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                         |
| sympy_integrate          | 15.3 ms                                                     | 14.2 ms: 1.08x faster                                                         |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                         |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                         |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.6 ms: 1.06x faster                                                         |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                         |
| logging_format           | 6.76 us                                                     | 6.44 us: 1.05x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                         |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                         |
| logging_simple           | 6.22 us                                                     | 5.99 us: 1.04x faster                                                         |
| 2to3                     | 246 ms                                                      | 238 ms: 1.03x faster                                                          |
| meteor_contest           | 75.9 ms                                                     | 73.6 ms: 1.03x faster                                                         |
| xml_etree_parse          | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                         |
| xml_etree_generate       | 55.5 ms                                                     | 54.5 ms: 1.02x faster                                                         |
| regex_v8                 | 15.4 ms                                                     | 15.4 ms: 1.01x faster                                                         |
| sympy_expand             | 314 ms                                                      | 316 ms: 1.00x slower                                                          |
| python_startup           | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                         |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                         |
| genshi_xml               | 41.0 ms                                                     | 43.7 ms: 1.07x slower                                                         |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.10x slower                                                         |
| telco                    | 3.94 ms                                                     | 4.39 ms: 1.11x slower                                                         |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                         |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                         |
| create_gc_cycles         | 800 us                                                      | 910 us: 1.14x slower                                                          |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.20x slower                                                         |
| async_generators         | 222 ms                                                      | 274 ms: 1.24x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                  |

Benchmark hidden because not significant (2): pidigits, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown