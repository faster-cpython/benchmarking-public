# Results vs. 3.10.4

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: linux-x86_64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.337x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                                |
| html5lib       | 94.6 ms                                                      | 67.0 ms: 1.41x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 614 ms: 2.60x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 326 ms: 2.51x faster                                                                  |
| async_tree_none         | 692 ms                                                       | 278 ms: 2.49x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                                  |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.6 ms: 1.75x faster                                                                 |
| nbody          | 134 ms                                                       | 97.5 ms: 1.38x faster                                                                 |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                  |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.73 ms: 1.21x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 195 us: 1.60x faster                                                                  |
| tomli_loads          | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 96.8 ms: 1.14x faster                                                                 |
| json_loads           | 30.3 us                                                      | 26.8 us: 1.13x faster                                                                 |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                                 |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.95 ms: 1.48x faster                                                                 |
| django_template | 50.2 ms                                                      | 34.7 ms: 1.45x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 54.7 ms: 1.16x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 2.87 ms: 2.62x faster                                                                 |
| async_tree_io            | 1.60 sec                                                     | 614 ms: 2.60x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 326 ms: 2.51x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 278 ms: 2.49x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                                |
| richards_super           | 90.6 ms                                                      | 39.9 ms: 2.27x faster                                                                 |
| richards                 | 75.1 ms                                                      | 34.3 ms: 2.19x faster                                                                 |
| go                       | 262 ms                                                       | 125 ms: 2.09x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                                  |
| chaos                    | 109 ms                                                       | 58.9 ms: 1.84x faster                                                                 |
| pyflate                  | 733 ms                                                       | 401 ms: 1.83x faster                                                                  |
| logging_silent           | 167 ns                                                       | 92.1 ns: 1.82x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 77.6 ms: 1.79x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.78x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                                                 |
| float                    | 111 ms                                                       | 63.6 ms: 1.75x faster                                                                 |
| pylint                   | 566 ms                                                       | 324 ms: 1.74x faster                                                                  |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 62.7 ms: 1.71x faster                                                                 |
| deepcopy                 | 468 us                                                       | 277 us: 1.69x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 195 us: 1.60x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 77.5 ms: 1.54x faster                                                                 |
| hexiom                   | 9.42 ms                                                      | 6.17 ms: 1.53x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.01 us: 1.48x faster                                                                 |
| mako                     | 14.7 ms                                                      | 9.95 ms: 1.48x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.60 us: 1.46x faster                                                                 |
| django_template          | 50.2 ms                                                      | 34.7 ms: 1.45x faster                                                                 |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.51 sec: 1.42x faster                                                                |
| thrift                   | 1.18 ms                                                      | 832 us: 1.41x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 67.0 ms: 1.41x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 745 ms: 1.41x faster                                                                  |
| nbody                    | 134 ms                                                       | 97.5 ms: 1.38x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                                 |
| dulwich_log              | 81.1 ms                                                      | 59.1 ms: 1.37x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                                 |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                                 |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 22.3 ms: 1.26x faster                                                                 |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                  |
| nqueens                  | 115 ms                                                       | 93.1 ms: 1.23x faster                                                                 |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                                  |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                                  |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 54.7 ms: 1.16x faster                                                                 |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 96.8 ms: 1.14x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.13x faster                                                                  |
| json_loads               | 30.3 us                                                      | 26.8 us: 1.13x faster                                                                 |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                                 |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                  |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.96 ms: 1.02x faster                                                                 |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.73 ms: 1.21x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 82.3 ms: 1.30x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.93 ms: 1.66x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 6.74 ms: 1.97x slower                                                                 |
| telco                    | 7.23 ms                                                      | 162 ms: 22.35x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                          |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.337x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.41x