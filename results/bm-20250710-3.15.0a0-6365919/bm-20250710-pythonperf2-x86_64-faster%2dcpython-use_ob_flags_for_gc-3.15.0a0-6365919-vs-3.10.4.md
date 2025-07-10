# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: linux-x86_64
- commit hash: 6365919
- commit date: 2025-07-10
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                                 |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                               |
| html5lib       | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                                |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 614 ms: 2.60x faster                                                                 |
| async_tree_none         | 692 ms                                                       | 269 ms: 2.57x faster                                                                 |
| async_tree_memoization  | 819 ms                                                       | 325 ms: 2.52x faster                                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 496 ms: 1.89x faster                                                                 |
| Geometric mean          | (ref)                                                        | 2.37x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.4 ms: 1.58x faster                                                                |
| nbody          | 134 ms                                                       | 94.7 ms: 1.42x faster                                                                |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                                 |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                                 |
| regex_v8       | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                                |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 208 us: 1.50x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 58.2 ms: 1.30x faster                                                                |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.29x faster                                                                |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.22x faster                                                                |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 98.1 ms: 1.13x faster                                                                |
| xml_etree_generate   | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                                |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.77 ms: 1.20x slower                                                                |
| python_startup         | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                                |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                                |
| genshi_xml      | 63.3 ms                                                      | 52.9 ms: 1.20x faster                                                                |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.22x faster                                                                 |
| async_tree_io            | 1.60 sec                                                     | 614 ms: 2.60x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 269 ms: 2.57x faster                                                                 |
| async_tree_memoization   | 819 ms                                                       | 325 ms: 2.52x faster                                                                 |
| deltablue                | 7.50 ms                                                      | 3.15 ms: 2.38x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.34x faster                                                               |
| go                       | 262 ms                                                       | 118 ms: 2.21x faster                                                                 |
| generators               | 57.3 ms                                                      | 30.0 ms: 1.91x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 496 ms: 1.89x faster                                                                 |
| chaos                    | 109 ms                                                       | 58.2 ms: 1.87x faster                                                                |
| deepcopy_memo            | 49.8 us                                                      | 27.1 us: 1.84x faster                                                                |
| logging_silent           | 167 ns                                                       | 93.1 ns: 1.80x faster                                                                |
| pyflate                  | 733 ms                                                       | 409 ms: 1.79x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 60.2 ms: 1.78x faster                                                                |
| richards_super           | 90.6 ms                                                      | 51.1 ms: 1.77x faster                                                                |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.76x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 95.3 ms: 1.75x faster                                                                |
| deepcopy                 | 468 us                                                       | 268 us: 1.74x faster                                                                 |
| raytrace                 | 489 ms                                                       | 282 ms: 1.74x faster                                                                 |
| richards                 | 75.1 ms                                                      | 45.1 ms: 1.67x faster                                                                |
| spectral_norm            | 139 ms                                                       | 85.2 ms: 1.63x faster                                                                |
| comprehensions           | 26.7 us                                                      | 16.5 us: 1.61x faster                                                                |
| hexiom                   | 9.42 ms                                                      | 5.87 ms: 1.60x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 74.9 ms: 1.59x faster                                                                |
| float                    | 111 ms                                                       | 70.4 ms: 1.58x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 208 us: 1.50x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.03 us: 1.47x faster                                                                |
| logging_format           | 9.64 us                                                      | 6.63 us: 1.45x faster                                                                |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                                |
| nbody                    | 134 ms                                                       | 94.7 ms: 1.42x faster                                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.53 sec: 1.41x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 748 ms: 1.40x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                                                 |
| dulwich_log              | 81.1 ms                                                      | 59.2 ms: 1.37x faster                                                                |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                                |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.9 ms: 1.32x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 58.2 ms: 1.30x faster                                                                |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.29x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.0 ms: 1.28x faster                                                                |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                                 |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.26x faster                                                                |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                                 |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                                 |
| nqueens                  | 115 ms                                                       | 92.8 ms: 1.24x faster                                                                |
| sympy_expand             | 600 ms                                                       | 487 ms: 1.23x faster                                                                 |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.22x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 52.9 ms: 1.20x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                               |
| scimark_fft              | 361 ms                                                       | 307 ms: 1.18x faster                                                                 |
| regex_dna                | 261 ms                                                       | 225 ms: 1.16x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.16x faster                                                                 |
| regex_v8                 | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 98.1 ms: 1.13x faster                                                                |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.11x faster                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                                |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.87 ms: 1.04x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                                 |
| async_generators         | 421 ms                                                       | 435 ms: 1.03x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                                |
| python_startup_no_site   | 7.33 ms                                                      | 8.77 ms: 1.20x slower                                                                |
| coverage                 | 63.3 ms                                                      | 80.3 ms: 1.27x slower                                                                |
| python_startup           | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.77 ms: 1.57x slower                                                                |
| gc_traversal             | 3.42 ms                                                      | 5.88 ms: 1.72x slower                                                                |
| telco                    | 7.23 ms                                                      | 158 ms: 21.82x slower                                                                |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                         |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250710-3.15.0a0-6365919/bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.38x