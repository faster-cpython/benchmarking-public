# Results vs. 3.10.4

- fork: python
- ref: fecf8bc8f2fd09a9a4c5
- machine: linux-x86_64
- commit hash: fecf8bc
- commit date: 2025-02-28
- overall geometric mean: 1.336x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 68.7 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 641 ms: 2.49x faster                                                         |
| async_tree_none         | 692 ms                                                       | 286 ms: 2.42x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 348 ms: 2.35x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 519 ms: 1.81x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.25x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.9 ms: 1.59x faster                                                        |
| nbody          | 134 ms                                                       | 101 ms: 1.32x faster                                                         |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.05 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 60.0 ms: 1.26x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.3 ms: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.15 ms: 1.25x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.3 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.33x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.3 ms: 1.38x faster                                                        |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.2 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 641 ms: 2.49x faster                                                         |
| async_tree_none          | 692 ms                                                       | 286 ms: 2.42x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 348 ms: 2.35x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                        |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                         |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 519 ms: 1.81x faster                                                         |
| chaos                    | 109 ms                                                       | 60.6 ms: 1.79x faster                                                        |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                                         |
| raytrace                 | 489 ms                                                       | 280 ms: 1.75x faster                                                         |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                        |
| richards_super           | 90.6 ms                                                      | 53.2 ms: 1.70x faster                                                        |
| deepcopy                 | 468 us                                                       | 281 us: 1.67x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.66x faster                                                        |
| scimark_lu               | 167 ms                                                       | 100 ms: 1.66x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.64x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.8 ms: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 449 ms: 1.63x faster                                                         |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                         |
| richards                 | 75.1 ms                                                      | 47.0 ms: 1.60x faster                                                        |
| float                    | 111 ms                                                       | 69.9 ms: 1.59x faster                                                        |
| spectral_norm            | 139 ms                                                       | 87.6 ms: 1.59x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 76.9 ms: 1.55x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.11 ms: 1.54x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.76 ms: 1.53x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.41 us: 1.39x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                       |
| django_template          | 50.2 ms                                                      | 36.3 ms: 1.38x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 68.7 ms: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                         |
| thrift                   | 1.18 ms                                                      | 861 us: 1.37x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| nbody                    | 134 ms                                                       | 101 ms: 1.32x faster                                                         |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.32x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 797 ms: 1.32x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.29x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 60.0 ms: 1.26x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.4 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                         |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                        |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 68.1 ms: 1.19x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.3 ms: 1.14x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.2 ms: 1.13x faster                                                        |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                        |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| scimark_fft              | 361 ms                                                       | 333 ms: 1.09x faster                                                         |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                        |
| async_generators         | 421 ms                                                       | 407 ms: 1.03x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.05 ms: 1.01x faster                                                        |
| telco                    | 7.23 ms                                                      | 8.09 ms: 1.12x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.15 ms: 1.25x slower                                                        |
| coverage                 | 63.3 ms                                                      | 84.5 ms: 1.34x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.3 ms: 1.41x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.69 ms: 1.53x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.27 ms: 1.84x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.29 sec: 202.98x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                 |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250228-3.14.0a5+-fecf8bc/bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.336x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.27x