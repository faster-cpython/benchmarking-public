# Results vs. 3.10.4

- fork: python
- ref: 6226edc48baa888b413f
- machine: linux-x86_64
- commit hash: 6226edc
- commit date: 2025-03-24
- overall geometric mean: 1.203x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 326 ms: 1.08x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 579 ms: 2.76x faster                                                         |
| async_tree_none         | 692 ms                                                       | 278 ms: 2.49x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 337 ms: 2.43x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 510 ms: 1.84x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 77.0 ms: 1.44x faster                                                        |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 161 ms: 1.18x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 244 us: 1.28x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 367 us: 1.24x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 89.7 ms: 1.23x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 13.3 ms: 1.09x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 70.0 ms: 1.08x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.2 us: 1.04x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 97.5 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 19.4 ms: 1.69x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 13.8 ms: 1.88x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.78x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.7 ms: 1.10x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.8 ms: 1.01x faster                                                        |
| mako            | 14.7 ms                                                      | 17.7 ms: 1.20x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 579 ms: 2.76x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 214 us: 2.50x faster                                                         |
| async_tree_none          | 692 ms                                                       | 278 ms: 2.49x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 337 ms: 2.43x faster                                                         |
| generators               | 57.3 ms                                                      | 30.6 ms: 1.87x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.05 ms: 1.85x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 510 ms: 1.84x faster                                                         |
| go                       | 262 ms                                                       | 153 ms: 1.71x faster                                                         |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                         |
| gc_traversal             | 3.42 ms                                                      | 2.10 ms: 1.62x faster                                                        |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                         |
| chaos                    | 109 ms                                                       | 69.2 ms: 1.57x faster                                                        |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.50x faster                                                         |
| raytrace                 | 489 ms                                                       | 328 ms: 1.49x faster                                                         |
| pyflate                  | 733 ms                                                       | 495 ms: 1.48x faster                                                         |
| float                    | 111 ms                                                       | 77.0 ms: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 97.3 ms: 1.43x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| deepcopy                 | 468 us                                                       | 333 us: 1.41x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 36.2 us: 1.37x faster                                                        |
| richards_super           | 90.6 ms                                                      | 66.8 ms: 1.36x faster                                                        |
| scimark_lu               | 167 ms                                                       | 124 ms: 1.35x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.33x faster                                                       |
| comprehensions           | 26.7 us                                                      | 20.2 us: 1.32x faster                                                        |
| richards                 | 75.1 ms                                                      | 57.3 ms: 1.31x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 91.9 ms: 1.30x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 244 us: 1.28x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.44 ms: 1.27x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.26x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 86.7 ms: 1.24x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 367 us: 1.24x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 89.7 ms: 1.23x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.24 us: 1.23x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.5 ms: 1.22x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| thrift                   | 1.18 ms                                                      | 966 us: 1.22x faster                                                         |
| logging_format           | 9.64 us                                                      | 8.07 us: 1.19x faster                                                        |
| regex_compile            | 190 ms                                                       | 161 ms: 1.18x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 904 ms: 1.16x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.86 sec: 1.16x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.60 us: 1.15x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.51 us: 1.14x faster                                                        |
| sympy_sum                | 193 ms                                                       | 175 ms: 1.10x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.7 ms: 1.10x faster                                                        |
| django_template          | 50.2 ms                                                      | 45.7 ms: 1.10x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 173 ms: 1.10x faster                                                         |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 13.3 ms: 1.09x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 70.0 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| sympy_str                | 360 ms                                                       | 334 ms: 1.08x faster                                                         |
| 2to3                     | 350 ms                                                       | 326 ms: 1.08x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.80 sec: 1.07x faster                                                       |
| sympy_expand             | 600 ms                                                       | 564 ms: 1.06x faster                                                         |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 26.6 ms: 1.06x faster                                                        |
| nqueens                  | 115 ms                                                       | 110 ms: 1.05x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                        |
| scimark_fft              | 361 ms                                                       | 347 ms: 1.04x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 375 ms: 1.04x faster                                                         |
| json_loads               | 30.3 us                                                      | 29.2 us: 1.04x faster                                                        |
| json                     | 5.86 ms                                                      | 5.66 ms: 1.04x faster                                                        |
| fannkuch                 | 483 ms                                                       | 473 ms: 1.02x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 62.8 ms: 1.01x faster                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 97.5 ms: 1.06x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                        |
| meteor_contest           | 138 ms                                                       | 154 ms: 1.11x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.73 ms: 1.13x slower                                                        |
| async_generators         | 421 ms                                                       | 495 ms: 1.18x slower                                                         |
| mako                     | 14.7 ms                                                      | 17.7 ms: 1.20x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.44 ms: 1.26x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.51 ms: 1.32x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.4 ms: 1.69x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 13.8 ms: 1.88x slower                                                        |
| coverage                 | 63.3 ms                                                      | 121 ms: 1.91x slower                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 50.4 ms: 7.91x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250324-3.14.0a6+-6226edc-NOGIL/bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.203x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.55x