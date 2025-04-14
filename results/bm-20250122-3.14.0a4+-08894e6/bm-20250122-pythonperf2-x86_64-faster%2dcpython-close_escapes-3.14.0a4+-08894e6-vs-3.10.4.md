# Results vs. 3.10.4

- fork: faster-cpython
- ref: close_escapes
- machine: linux-x86_64
- commit hash: 08894e6
- commit date: 2025-01-22
- overall geometric mean: 1.348x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                            |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                          |
| html5lib       | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                           |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 624 ms: 2.56x faster                                                            |
| async_tree_none         | 692 ms                                                       | 276 ms: 2.51x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 343 ms: 2.39x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 508 ms: 1.84x faster                                                            |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.9 ms: 1.59x faster                                                           |
| nbody          | 134 ms                                                       | 90.7 ms: 1.48x faster                                                           |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                            |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                           |
| regex_effbot   | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 219 us: 1.42x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 61.8 ms: 1.23x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                            |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 95.4 ms: 1.16x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                           |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                           |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.8 ms: 1.37x faster                                                           |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 178 us: 3.02x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 624 ms: 2.56x faster                                                            |
| async_tree_none          | 692 ms                                                       | 276 ms: 2.51x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 343 ms: 2.39x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.44 ms: 2.18x faster                                                           |
| go                       | 262 ms                                                       | 128 ms: 2.05x faster                                                            |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 508 ms: 1.84x faster                                                            |
| chaos                    | 109 ms                                                       | 59.1 ms: 1.84x faster                                                           |
| pylint                   | 566 ms                                                       | 317 ms: 1.79x faster                                                            |
| raytrace                 | 489 ms                                                       | 277 ms: 1.76x faster                                                            |
| scimark_lu               | 167 ms                                                       | 95.5 ms: 1.75x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 61.7 ms: 1.74x faster                                                           |
| logging_silent           | 167 ns                                                       | 96.6 ns: 1.73x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.31 ms: 1.70x faster                                                           |
| richards_super           | 90.6 ms                                                      | 53.3 ms: 1.70x faster                                                           |
| spectral_norm            | 139 ms                                                       | 84.3 ms: 1.65x faster                                                           |
| deepcopy_memo            | 49.8 us                                                      | 30.2 us: 1.65x faster                                                           |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                            |
| richards                 | 75.1 ms                                                      | 46.1 ms: 1.63x faster                                                           |
| pyflate                  | 733 ms                                                       | 457 ms: 1.61x faster                                                            |
| crypto_pyaes             | 119 ms                                                       | 74.4 ms: 1.60x faster                                                           |
| float                    | 111 ms                                                       | 69.9 ms: 1.59x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.70 ms: 1.58x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.01 ms: 1.57x faster                                                           |
| scimark_sor              | 180 ms                                                       | 116 ms: 1.55x faster                                                            |
| comprehensions           | 26.7 us                                                      | 17.9 us: 1.49x faster                                                           |
| nbody                    | 134 ms                                                       | 90.7 ms: 1.48x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 219 us: 1.42x faster                                                            |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                          |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                           |
| django_template          | 50.2 ms                                                      | 36.8 ms: 1.37x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                            |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                           |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                            |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                           |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                                           |
| logging_simple           | 8.88 us                                                      | 6.61 us: 1.34x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                          |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 789 ms: 1.33x faster                                                            |
| logging_format           | 9.64 us                                                      | 7.27 us: 1.33x faster                                                           |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.32x faster                                                          |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.30x faster                                                            |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                           |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                            |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                           |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                            |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                            |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                            |
| bench_thread_pool        | 1.14 ms                                                      | 923 us: 1.24x faster                                                            |
| xml_etree_process        | 75.9 ms                                                      | 61.8 ms: 1.23x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 57.7 ms: 1.22x faster                                                           |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.22x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                           |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                            |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                           |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                          |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 95.4 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.44 ms: 1.14x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                           |
| async_generators         | 421 ms                                                       | 377 ms: 1.12x faster                                                            |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                            |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                           |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                            |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                           |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                            |
| regex_effbot             | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                                           |
| telco                    | 7.23 ms                                                      | 8.14 ms: 1.13x slower                                                           |
| coverage                 | 63.3 ms                                                      | 75.3 ms: 1.19x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                           |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 6.65 ms: 1.95x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 1.94 sec: 305.06x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250122-3.14.0a4+-08894e6/bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.348x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x