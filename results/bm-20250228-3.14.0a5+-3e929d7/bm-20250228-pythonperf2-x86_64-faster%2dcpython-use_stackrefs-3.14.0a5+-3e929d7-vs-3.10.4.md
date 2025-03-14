# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                                            |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                          |
| html5lib       | 94.6 ms                                                      | 69.3 ms: 1.37x faster                                                           |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 646 ms: 2.47x faster                                                            |
| async_tree_none         | 692 ms                                                       | 291 ms: 2.38x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 351 ms: 2.34x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.9 ms: 1.57x faster                                                           |
| nbody          | 134 ms                                                       | 105 ms: 1.27x faster                                                            |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                           |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                            |
| regex_effbot   | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 221 us: 1.41x faster                                                            |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                                          |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                           |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                           |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 99.7 ms: 1.11x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                           |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.14 ms: 1.25x slower                                                           |
| python_startup         | 11.5 ms                                                      | 16.3 ms: 1.41x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.33x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.0 ms: 1.39x faster                                                           |
| mako            | 14.7 ms                                                      | 11.3 ms: 1.31x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 56.3 ms: 1.12x faster                                                           |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 646 ms: 2.47x faster                                                            |
| async_tree_none          | 692 ms                                                       | 291 ms: 2.38x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 351 ms: 2.34x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                           |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.96x faster                                                           |
| go                       | 262 ms                                                       | 134 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                            |
| logging_silent           | 167 ns                                                       | 94.1 ns: 1.78x faster                                                           |
| pylint                   | 566 ms                                                       | 319 ms: 1.78x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                           |
| raytrace                 | 489 ms                                                       | 289 ms: 1.69x faster                                                            |
| chaos                    | 109 ms                                                       | 65.2 ms: 1.67x faster                                                           |
| pyflate                  | 733 ms                                                       | 441 ms: 1.66x faster                                                            |
| richards_super           | 90.6 ms                                                      | 54.8 ms: 1.65x faster                                                           |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                            |
| scimark_lu               | 167 ms                                                       | 102 ms: 1.64x faster                                                            |
| scimark_monte_carlo      | 107 ms                                                       | 65.8 ms: 1.63x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                                           |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                            |
| float                    | 111 ms                                                       | 70.9 ms: 1.57x faster                                                           |
| richards                 | 75.1 ms                                                      | 47.9 ms: 1.57x faster                                                           |
| spectral_norm            | 139 ms                                                       | 90.5 ms: 1.54x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.27 ms: 1.50x faster                                                           |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                           |
| crypto_pyaes             | 119 ms                                                       | 84.2 ms: 1.41x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 221 us: 1.41x faster                                                            |
| django_template          | 50.2 ms                                                      | 36.0 ms: 1.39x faster                                                           |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                            |
| thrift                   | 1.18 ms                                                      | 860 us: 1.37x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 69.3 ms: 1.37x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                                          |
| logging_format           | 9.64 us                                                      | 7.17 us: 1.35x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.33x faster                                                          |
| deepcopy_reduce          | 4.01 us                                                      | 3.01 us: 1.33x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 797 ms: 1.32x faster                                                            |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                          |
| mako                     | 14.7 ms                                                      | 11.3 ms: 1.31x faster                                                           |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                            |
| genshi_text              | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                           |
| fannkuch                 | 483 ms                                                       | 377 ms: 1.28x faster                                                            |
| nbody                    | 134 ms                                                       | 105 ms: 1.27x faster                                                            |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.2 ms: 1.25x faster                                                           |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                            |
| sympy_str                | 360 ms                                                       | 294 ms: 1.22x faster                                                            |
| nqueens                  | 115 ms                                                       | 94.3 ms: 1.22x faster                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 58.0 ms: 1.21x faster                                                           |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                           |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                            |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                                          |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 68.6 ms: 1.18x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 970 us: 1.18x faster                                                            |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                          |
| genshi_xml               | 63.3 ms                                                      | 56.3 ms: 1.12x faster                                                           |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 99.7 ms: 1.11x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                           |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                                           |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                           |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                           |
| scimark_fft              | 361 ms                                                       | 339 ms: 1.07x faster                                                            |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                            |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.80 ms: 1.06x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                            |
| async_generators         | 421 ms                                                       | 419 ms: 1.00x faster                                                            |
| regex_effbot             | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                                           |
| telco                    | 7.23 ms                                                      | 8.21 ms: 1.14x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 9.14 ms: 1.25x slower                                                           |
| coverage                 | 63.3 ms                                                      | 83.9 ms: 1.33x slower                                                           |
| python_startup           | 11.5 ms                                                      | 16.3 ms: 1.41x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 6.54 ms: 1.92x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 907 ms: 142.33x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250228-3.14.0a5+-3e929d7/bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.27x