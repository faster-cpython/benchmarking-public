# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.338x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 649 ms: 2.46x faster                                                         |
| async_tree_none         | 692 ms                                                       | 292 ms: 2.37x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 357 ms: 2.29x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 519 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.0 ms: 1.52x faster                                                        |
| float          | 111 ms                                                       | 76.3 ms: 1.46x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                         |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 202 us: 1.54x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 327 us: 1.39x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 59.6 ms: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 95.6 ms: 1.16x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.3 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.2 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.5 ms: 1.41x faster                                                        |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 649 ms: 2.46x faster                                                         |
| async_tree_none          | 692 ms                                                       | 292 ms: 2.37x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 357 ms: 2.29x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                        |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                         |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 519 ms: 1.80x faster                                                         |
| chaos                    | 109 ms                                                       | 61.3 ms: 1.77x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.3 ms: 1.77x faster                                                        |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                         |
| richards_super           | 90.6 ms                                                      | 51.7 ms: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 281 ms: 1.74x faster                                                         |
| logging_silent           | 167 ns                                                       | 98.4 ns: 1.70x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.34 ms: 1.68x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.7 ms: 1.66x faster                                                        |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.9 ms: 1.64x faster                                                        |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.63x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 459 ms: 1.60x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 75.6 ms: 1.58x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.02 ms: 1.56x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.73 ms: 1.55x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 202 us: 1.54x faster                                                         |
| spectral_norm            | 139 ms                                                       | 90.4 ms: 1.54x faster                                                        |
| nbody                    | 134 ms                                                       | 88.0 ms: 1.52x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                        |
| float                    | 111 ms                                                       | 76.3 ms: 1.46x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.5 ms: 1.41x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.33 us: 1.40x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                       |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 327 us: 1.39x faster                                                         |
| logging_format           | 9.64 us                                                      | 6.96 us: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                        |
| fannkuch                 | 483 ms                                                       | 354 ms: 1.36x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                       |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 783 ms: 1.34x faster                                                         |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                        |
| nqueens                  | 115 ms                                                       | 87.9 ms: 1.31x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.6 ms: 1.28x faster                                                        |
| json_loads               | 30.3 us                                                      | 23.9 us: 1.27x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 113 ms: 1.27x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                                         |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.4 ms: 1.24x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 57.3 ms: 1.22x faster                                                        |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 957 us: 1.19x faster                                                         |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 68.5 ms: 1.18x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| scimark_fft              | 361 ms                                                       | 308 ms: 1.17x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 95.6 ms: 1.16x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                        |
| json                     | 5.86 ms                                                      | 5.14 ms: 1.14x faster                                                        |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 84.3 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.72 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| async_generators         | 421 ms                                                       | 435 ms: 1.03x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.81 ms: 1.08x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.03 sec: 1.11x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.9 ms: 1.23x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.2 ms: 1.41x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.75 ms: 1.56x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.34 ms: 1.86x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.26 sec: 197.77x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.338x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.29x