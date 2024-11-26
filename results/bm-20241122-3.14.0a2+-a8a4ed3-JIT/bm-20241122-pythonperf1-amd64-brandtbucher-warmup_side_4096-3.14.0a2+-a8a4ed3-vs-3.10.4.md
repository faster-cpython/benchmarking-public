# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-amd64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.229x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                          |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                        |
| html5lib       | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                         |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 214 ms: 2.04x faster                                                          |
| async_tree_io           | 1.11 sec                                                    | 575 ms: 1.93x faster                                                          |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                          |
| async_tree_cpu_io_mixed | 638 ms                                                      | 399 ms: 1.60x faster                                                          |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                         |
| nbody          | 71.3 ms                                                     | 56.4 ms: 1.27x faster                                                         |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.2 ms: 1.29x faster                                                         |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                         |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 111 us: 1.65x faster                                                          |
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                         |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                          |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                         |
| xml_etree_generate   | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                                         |
| xml_etree_parse      | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                         |
| json_loads           | 14.0 us                                                     | 14.0 us: 1.00x faster                                                         |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                         |
| python_startup         | 20.6 ms                                                     | 23.7 ms: 1.15x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                         |
| django_template | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                         |
| genshi_xml      | 41.0 ms                                                     | 48.0 ms: 1.17x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                          |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.04x faster                                                          |
| async_tree_io            | 1.11 sec                                                    | 575 ms: 1.93x faster                                                          |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                          |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                         |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                          |
| mako                     | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                         |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.71x faster                                                         |
| scimark_sor              | 106 ms                                                      | 62.1 ms: 1.71x faster                                                         |
| logging_silent           | 94.6 ns                                                     | 56.7 ns: 1.67x faster                                                         |
| unpickle_pure_python     | 183 us                                                      | 111 us: 1.65x faster                                                          |
| scimark_lu               | 85.8 ms                                                     | 53.0 ms: 1.62x faster                                                         |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 399 ms: 1.60x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                         |
| go                       | 139 ms                                                      | 89.7 ms: 1.55x faster                                                         |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.1 ms: 1.54x faster                                                         |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                         |
| spectral_norm            | 77.3 ms                                                     | 52.6 ms: 1.47x faster                                                         |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                         |
| pyflate                  | 409 ms                                                      | 290 ms: 1.41x faster                                                          |
| sqlglot_parse            | 1.22 ms                                                     | 863 us: 1.41x faster                                                          |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                         |
| generators               | 32.4 ms                                                     | 23.4 ms: 1.39x faster                                                         |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                         |
| deepcopy                 | 255 us                                                      | 193 us: 1.32x faster                                                          |
| richards_super           | 52.2 ms                                                     | 39.7 ms: 1.31x faster                                                         |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.08 ms: 1.31x faster                                                         |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                          |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                         |
| regex_compile            | 106 ms                                                      | 82.2 ms: 1.29x faster                                                         |
| raytrace                 | 273 ms                                                      | 212 ms: 1.29x faster                                                          |
| float                    | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                         |
| nbody                    | 71.3 ms                                                     | 56.4 ms: 1.27x faster                                                         |
| dulwich_log              | 50.5 ms                                                     | 40.0 ms: 1.26x faster                                                         |
| xml_etree_process        | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                         |
| pprint_pformat           | 1.22 sec                                                    | 988 ms: 1.23x faster                                                          |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.22x faster                                                          |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                         |
| richards                 | 42.4 ms                                                     | 35.1 ms: 1.21x faster                                                         |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                          |
| pprint_safe_repr         | 592 ms                                                      | 497 ms: 1.19x faster                                                          |
| bench_thread_pool        | 958 us                                                      | 806 us: 1.19x faster                                                          |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                         |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.17x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                         |
| sympy_sum                | 107 ms                                                      | 91.5 ms: 1.17x faster                                                         |
| hexiom                   | 5.74 ms                                                     | 4.98 ms: 1.15x faster                                                         |
| thrift                   | 617 us                                                      | 543 us: 1.14x faster                                                          |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                         |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                          |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                        |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                         |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                         |
| fannkuch                 | 256 ms                                                      | 240 ms: 1.07x faster                                                          |
| django_template          | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                         |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                         |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                                         |
| nqueens                  | 66.6 ms                                                     | 64.2 ms: 1.04x faster                                                         |
| xml_etree_parse          | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                         |
| meteor_contest           | 75.9 ms                                                     | 73.8 ms: 1.03x faster                                                         |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 38.9 ms: 1.02x faster                                                         |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                          |
| json_loads               | 14.0 us                                                     | 14.0 us: 1.00x faster                                                         |
| pathlib                  | 75.7 ms                                                     | 76.1 ms: 1.01x slower                                                         |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                         |
| sqlglot_normalize        | 205 ms                                                      | 208 ms: 1.01x slower                                                          |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                         |
| telco                    | 3.94 ms                                                     | 4.28 ms: 1.09x slower                                                         |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                         |
| python_startup           | 20.6 ms                                                     | 23.7 ms: 1.15x slower                                                         |
| genshi_xml               | 41.0 ms                                                     | 48.0 ms: 1.17x slower                                                         |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                         |
| async_generators         | 222 ms                                                      | 270 ms: 1.22x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 1.86 ms: 1.32x slower                                                         |
| bench_mp_pool            | 62.0 ms                                                     | 82.1 ms: 1.32x slower                                                         |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.67x slower                                                         |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.229x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown