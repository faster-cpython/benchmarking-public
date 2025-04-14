# Results vs. 3.10.4

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.323x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 639 ms: 2.50x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 341 ms: 2.40x faster                                                         |
| async_tree_none         | 692 ms                                                       | 294 ms: 2.35x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 524 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.6 ms: 1.72x faster                                                        |
| nbody          | 134 ms                                                       | 93.0 ms: 1.44x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.2 ms: 1.17x faster                                                        |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.2 ms: 1.33x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 344 us: 1.32x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 96.0 ms: 1.15x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.44x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.6 ms: 1.38x faster                                                        |
| django_template | 50.2 ms                                                      | 37.3 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.9 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.04x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 639 ms: 2.50x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.09 ms: 2.43x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 341 ms: 2.40x faster                                                         |
| async_tree_none          | 692 ms                                                       | 294 ms: 2.35x faster                                                         |
| richards_super           | 90.6 ms                                                      | 45.2 ms: 2.00x faster                                                        |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.96x faster                                                        |
| richards                 | 75.1 ms                                                      | 39.3 ms: 1.91x faster                                                        |
| go                       | 262 ms                                                       | 146 ms: 1.79x faster                                                         |
| logging_silent           | 167 ns                                                       | 93.5 ns: 1.79x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 524 ms: 1.79x faster                                                         |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                                        |
| float                    | 111 ms                                                       | 64.6 ms: 1.72x faster                                                        |
| scimark_lu               | 167 ms                                                       | 99.3 ms: 1.68x faster                                                        |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.66x faster                                                         |
| raytrace                 | 489 ms                                                       | 297 ms: 1.65x faster                                                         |
| chaos                    | 109 ms                                                       | 66.5 ms: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 451 ms: 1.62x faster                                                         |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                        |
| spectral_norm            | 139 ms                                                       | 89.5 ms: 1.55x faster                                                        |
| nbody                    | 134 ms                                                       | 93.0 ms: 1.44x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 83.6 ms: 1.43x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.80 ms: 1.39x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.42 us: 1.38x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.6 ms: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.07 us: 1.36x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                        |
| django_template          | 50.2 ms                                                      | 37.3 ms: 1.35x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.2 ms: 1.33x faster                                                        |
| thrift                   | 1.18 ms                                                      | 886 us: 1.33x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 344 us: 1.32x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                       |
| comprehensions           | 26.7 us                                                      | 20.4 us: 1.31x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 62.1 ms: 1.31x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 821 ms: 1.28x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                        |
| nqueens                  | 115 ms                                                       | 94.1 ms: 1.22x faster                                                        |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                         |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                       |
| fannkuch                 | 483 ms                                                       | 408 ms: 1.18x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.2 ms: 1.17x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| sympy_expand             | 600 ms                                                       | 515 ms: 1.17x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 980 us: 1.16x faster                                                         |
| scimark_fft              | 361 ms                                                       | 313 ms: 1.16x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 96.0 ms: 1.15x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.9 ms: 1.13x faster                                                        |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                         |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                        |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.93 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| async_generators         | 421 ms                                                       | 443 ms: 1.05x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.94 ms: 1.10x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.1 ms: 1.30x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.44x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.70 ms: 1.53x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.14 ms: 1.80x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.28 sec: 201.47x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                 |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-52b5eb9-JIT/bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.323x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x