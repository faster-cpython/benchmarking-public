# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.338x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                            |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                          |
| html5lib       | 94.6 ms                                                      | 68.4 ms: 1.38x faster                                                           |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 651 ms: 2.46x faster                                                            |
| async_tree_none         | 692 ms                                                       | 292 ms: 2.37x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 354 ms: 2.31x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 522 ms: 1.79x faster                                                            |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.9 ms: 1.59x faster                                                           |
| nbody          | 134 ms                                                       | 101 ms: 1.32x faster                                                            |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.43x faster                                                            |
| regex_dna      | 261 ms                                                       | 250 ms: 1.05x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                           |
| regex_effbot   | 3.09 ms                                                      | 3.29 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                            |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                          |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                           |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.25x faster                                                           |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 97.9 ms: 1.13x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                           |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                           |
| python_startup         | 11.5 ms                                                      | 16.2 ms: 1.40x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.7 ms: 1.37x faster                                                           |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 55.7 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 651 ms: 2.46x faster                                                            |
| async_tree_none          | 692 ms                                                       | 292 ms: 2.37x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 354 ms: 2.31x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.24x faster                                                           |
| go                       | 262 ms                                                       | 130 ms: 2.02x faster                                                            |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.00x faster                                                           |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 522 ms: 1.79x faster                                                            |
| logging_silent           | 167 ns                                                       | 94.6 ns: 1.77x faster                                                           |
| richards_super           | 90.6 ms                                                      | 51.9 ms: 1.75x faster                                                           |
| deepcopy_memo            | 49.8 us                                                      | 28.6 us: 1.74x faster                                                           |
| chaos                    | 109 ms                                                       | 62.4 ms: 1.74x faster                                                           |
| raytrace                 | 489 ms                                                       | 282 ms: 1.73x faster                                                            |
| scimark_lu               | 167 ms                                                       | 96.4 ms: 1.73x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 63.6 ms: 1.69x faster                                                           |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.68x faster                                                            |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.34 ms: 1.66x faster                                                           |
| spectral_norm            | 139 ms                                                       | 84.8 ms: 1.64x faster                                                           |
| richards                 | 75.1 ms                                                      | 45.9 ms: 1.64x faster                                                           |
| pyflate                  | 733 ms                                                       | 451 ms: 1.63x faster                                                            |
| float                    | 111 ms                                                       | 69.9 ms: 1.59x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.00 ms: 1.57x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.73 ms: 1.55x faster                                                           |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.52x faster                                                           |
| crypto_pyaes             | 119 ms                                                       | 79.3 ms: 1.50x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                            |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                           |
| regex_compile            | 190 ms                                                       | 132 ms: 1.43x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.38 us: 1.39x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 68.4 ms: 1.38x faster                                                           |
| logging_format           | 9.64 us                                                      | 7.02 us: 1.37x faster                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                           |
| django_template          | 50.2 ms                                                      | 36.7 ms: 1.37x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                            |
| thrift                   | 1.18 ms                                                      | 860 us: 1.37x faster                                                            |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                          |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                           |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.33x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.33x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 790 ms: 1.33x faster                                                            |
| nbody                    | 134 ms                                                       | 101 ms: 1.32x faster                                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 144 ms: 1.32x faster                                                            |
| fannkuch                 | 483 ms                                                       | 370 ms: 1.30x faster                                                            |
| genshi_text              | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                           |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                           |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                            |
| sqlglot_normalize        | 144 ms                                                       | 112 ms: 1.28x faster                                                            |
| nqueens                  | 115 ms                                                       | 90.9 ms: 1.26x faster                                                           |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.25x faster                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 56.1 ms: 1.25x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.25x faster                                                           |
| sympy_str                | 360 ms                                                       | 289 ms: 1.24x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                           |
| sympy_expand             | 600 ms                                                       | 491 ms: 1.22x faster                                                            |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                            |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.22x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 66.8 ms: 1.21x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 953 us: 1.20x faster                                                            |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                          |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                                           |
| scimark_fft              | 361 ms                                                       | 311 ms: 1.16x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                            |
| genshi_xml               | 63.3 ms                                                      | 55.7 ms: 1.14x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 97.9 ms: 1.13x faster                                                           |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                            |
| xml_etree_generate       | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                           |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                                           |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.77 ms: 1.07x faster                                                           |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                           |
| regex_dna                | 261 ms                                                       | 250 ms: 1.05x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                           |
| async_generators         | 421 ms                                                       | 419 ms: 1.00x faster                                                            |
| regex_effbot             | 3.09 ms                                                      | 3.29 ms: 1.07x slower                                                           |
| telco                    | 7.23 ms                                                      | 8.17 ms: 1.13x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                           |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                           |
| python_startup           | 11.5 ms                                                      | 16.2 ms: 1.40x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 6.56 ms: 1.92x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 1.11 sec: 174.25x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250220-3.14.0a5+-d270553/bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.338x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x