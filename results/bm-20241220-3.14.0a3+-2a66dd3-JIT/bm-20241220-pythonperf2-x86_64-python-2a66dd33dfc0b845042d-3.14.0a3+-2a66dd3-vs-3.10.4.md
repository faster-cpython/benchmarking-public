# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.3 ms: 1.37x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 657 ms: 2.43x faster                                                         |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 365 ms: 2.24x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 526 ms: 1.78x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.18x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.4 ms: 1.54x faster                                                        |
| nbody          | 134 ms                                                       | 91.3 ms: 1.47x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.35x faster                                                         |
| regex_dna      | 261 ms                                                       | 230 ms: 1.14x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 199 us: 1.57x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.2 ms: 1.33x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.19x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 94.3 ms: 1.17x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 81.3 ms: 1.14x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.53 ms: 1.54x faster                                                        |
| django_template | 50.2 ms                                                      | 39.1 ms: 1.29x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 27.8 ms: 1.13x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.03x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 657 ms: 2.43x faster                                                         |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 365 ms: 2.24x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                        |
| go                       | 262 ms                                                       | 140 ms: 1.87x faster                                                         |
| scimark_sor              | 180 ms                                                       | 98.7 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 526 ms: 1.78x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.0 ms: 1.73x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.5 ms: 1.73x faster                                                        |
| scimark_lu               | 167 ms                                                       | 97.4 ms: 1.71x faster                                                        |
| pylint                   | 566 ms                                                       | 334 ms: 1.69x faster                                                         |
| pyflate                  | 733 ms                                                       | 438 ms: 1.67x faster                                                         |
| richards                 | 75.1 ms                                                      | 46.1 ms: 1.63x faster                                                        |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 74.7 ms: 1.60x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                        |
| chaos                    | 109 ms                                                       | 69.0 ms: 1.57x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 199 us: 1.57x faster                                                         |
| deepcopy                 | 468 us                                                       | 300 us: 1.56x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.53 ms: 1.54x faster                                                        |
| spectral_norm            | 139 ms                                                       | 90.2 ms: 1.54x faster                                                        |
| float                    | 111 ms                                                       | 72.4 ms: 1.54x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                        |
| nbody                    | 134 ms                                                       | 91.3 ms: 1.47x faster                                                        |
| raytrace                 | 489 ms                                                       | 337 ms: 1.45x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                       |
| generators               | 57.3 ms                                                      | 40.7 ms: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 69.3 ms: 1.37x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.08 us: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 140 ms: 1.35x faster                                                         |
| comprehensions           | 26.7 us                                                      | 19.7 us: 1.35x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                         |
| thrift                   | 1.18 ms                                                      | 884 us: 1.33x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.2 ms: 1.33x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.32x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.16 ms: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                        |
| fannkuch                 | 483 ms                                                       | 373 ms: 1.29x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                         |
| django_template          | 50.2 ms                                                      | 39.1 ms: 1.29x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.28x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.2 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 160 ms: 1.20x faster                                                         |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.7 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.19x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 94.3 ms: 1.17x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                       |
| sympy_str                | 360 ms                                                       | 309 ms: 1.16x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 983 us: 1.16x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 24.3 ms: 1.16x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 125 ms: 1.15x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                       |
| nqueens                  | 115 ms                                                       | 101 ms: 1.14x faster                                                         |
| sympy_expand             | 600 ms                                                       | 526 ms: 1.14x faster                                                         |
| regex_dna                | 261 ms                                                       | 230 ms: 1.14x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 81.3 ms: 1.14x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 27.8 ms: 1.13x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 62.2 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.84 ms: 1.05x faster                                                        |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| async_generators         | 421 ms                                                       | 457 ms: 1.09x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.86 ms: 1.09x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.05 sec: 1.13x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 80.4 ms: 1.27x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.69 ms: 1.52x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.22 sec: 190.98x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.31x