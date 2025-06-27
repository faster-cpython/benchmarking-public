# Results vs. 3.10.4

- fork: faster-cpython
- ref: never_inline_decref
- machine: linux-x86_64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.361x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                                 |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                               |
| html5lib       | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                                |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 636 ms: 2.51x faster                                                                 |
| async_tree_memoization  | 819 ms                                                       | 331 ms: 2.47x faster                                                                 |
| async_tree_none         | 692 ms                                                       | 284 ms: 2.43x faster                                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 508 ms: 1.84x faster                                                                 |
| Geometric mean          | (ref)                                                        | 2.30x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.4 ms: 1.58x faster                                                                |
| nbody          | 134 ms                                                       | 94.5 ms: 1.42x faster                                                                |
| pidigits       | 271 ms                                                       | 258 ms: 1.05x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                 |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                                 |
| regex_v8       | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                                |
| regex_effbot   | 3.09 ms                                                      | 3.75 ms: 1.21x slower                                                                |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                                |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                                |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.20x faster                                                                |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                                                 |
| xml_etree_generate   | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                                |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                                |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                                                |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                                |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                                |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 164 us: 3.26x faster                                                                 |
| async_tree_io            | 1.60 sec                                                     | 636 ms: 2.51x faster                                                                 |
| async_tree_memoization   | 819 ms                                                       | 331 ms: 2.47x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 284 ms: 2.43x faster                                                                 |
| deltablue                | 7.50 ms                                                      | 3.20 ms: 2.34x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                               |
| go                       | 262 ms                                                       | 119 ms: 2.20x faster                                                                 |
| generators               | 57.3 ms                                                      | 29.7 ms: 1.93x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 508 ms: 1.84x faster                                                                 |
| chaos                    | 109 ms                                                       | 59.7 ms: 1.82x faster                                                                |
| logging_silent           | 167 ns                                                       | 93.3 ns: 1.79x faster                                                                |
| pyflate                  | 733 ms                                                       | 415 ms: 1.77x faster                                                                 |
| richards_super           | 90.6 ms                                                      | 51.4 ms: 1.76x faster                                                                |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                                 |
| raytrace                 | 489 ms                                                       | 280 ms: 1.75x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                                                |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 63.4 ms: 1.70x faster                                                                |
| scimark_lu               | 167 ms                                                       | 98.5 ms: 1.69x faster                                                                |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                                 |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.65x faster                                                                |
| comprehensions           | 26.7 us                                                      | 16.4 us: 1.63x faster                                                                |
| spectral_norm            | 139 ms                                                       | 85.7 ms: 1.62x faster                                                                |
| hexiom                   | 9.42 ms                                                      | 5.93 ms: 1.59x faster                                                                |
| float                    | 111 ms                                                       | 70.4 ms: 1.58x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 76.0 ms: 1.57x faster                                                                |
| logging_simple           | 8.88 us                                                      | 5.98 us: 1.48x faster                                                                |
| logging_format           | 9.64 us                                                      | 6.58 us: 1.46x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                               |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                                |
| nbody                    | 134 ms                                                       | 94.5 ms: 1.42x faster                                                                |
| thrift                   | 1.18 ms                                                      | 835 us: 1.41x faster                                                                 |
| django_template          | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                                |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                |
| dulwich_log              | 81.1 ms                                                      | 60.5 ms: 1.34x faster                                                                |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                                |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 793 ms: 1.32x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 370 ms: 1.30x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                                |
| nqueens                  | 115 ms                                                       | 90.8 ms: 1.27x faster                                                                |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                                |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                                 |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                                                 |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.20x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                                |
| regex_dna                | 261 ms                                                       | 225 ms: 1.16x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 314 ms: 1.15x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                                 |
| regex_v8                 | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                                |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                                |
| pidigits                 | 271 ms                                                       | 258 ms: 1.05x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.93 ms: 1.03x faster                                                                |
| sqlite_synth             | 2.99 us                                                      | 2.91 us: 1.03x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                                 |
| async_generators         | 421 ms                                                       | 427 ms: 1.01x slower                                                                 |
| telco                    | 7.23 ms                                                      | 8.28 ms: 1.14x slower                                                                |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.75 ms: 1.21x slower                                                                |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                                |
| coverage                 | 63.3 ms                                                      | 87.9 ms: 1.39x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.63x slower                                                                |
| gc_traversal             | 3.42 ms                                                      | 6.73 ms: 1.97x slower                                                                |
| Geometric mean           | (ref)                                                        | 1.37x faster                                                                         |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.361x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.36x