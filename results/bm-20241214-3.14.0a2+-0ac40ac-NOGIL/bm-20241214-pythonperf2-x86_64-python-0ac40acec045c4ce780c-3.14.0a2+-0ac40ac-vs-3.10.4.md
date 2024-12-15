# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.005x faster
- HPT reliability: 69.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 391 ms: 1.12x slower                                                         |
| docutils       | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                       |
| html5lib       | 94.6 ms                                                      | 97.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 811 ms: 1.97x faster                                                         |
| async_tree_none         | 692 ms                                                       | 373 ms: 1.85x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 463 ms: 1.77x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 625 ms: 1.50x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| nbody          | 134 ms                                                       | 137 ms: 1.02x slower                                                         |
| float          | 111 ms                                                       | 130 ms: 1.17x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| regex_compile  | 190 ms                                                       | 182 ms: 1.04x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.32 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 95.7 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 27.5 us: 1.10x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.71 sec: 1.07x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.3 ms: 1.02x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 330 us: 1.06x slower                                                         |
| xml_etree_process    | 75.9 ms                                                      | 81.2 ms: 1.07x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 102 ms: 1.11x slower                                                         |
| pickle_pure_python   | 455 us                                                       | 525 us: 1.15x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.3 ms: 1.67x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.7 ms: 1.71x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.69x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 54.3 ms: 1.08x slower                                                        |
| genshi_text     | 31.4 ms                                                      | 34.0 ms: 1.08x slower                                                        |
| genshi_xml      | 63.3 ms                                                      | 69.3 ms: 1.10x slower                                                        |
| mako            | 14.7 ms                                                      | 19.3 ms: 1.31x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.14x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 226 us: 2.37x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 811 ms: 1.97x faster                                                         |
| async_tree_none          | 692 ms                                                       | 373 ms: 1.85x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 463 ms: 1.77x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 625 ms: 1.50x faster                                                         |
| generators               | 57.3 ms                                                      | 38.6 ms: 1.48x faster                                                        |
| pylint                   | 566 ms                                                       | 394 ms: 1.44x faster                                                         |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.37x faster                                                         |
| deepcopy                 | 468 us                                                       | 350 us: 1.34x faster                                                         |
| coroutines               | 30.3 ms                                                      | 23.2 ms: 1.31x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 40.4 us: 1.23x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.6 ms: 1.21x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 99.6 ms: 1.20x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 95.7 ms: 1.16x faster                                                        |
| json_loads               | 30.3 us                                                      | 27.5 us: 1.10x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| pyflate                  | 733 ms                                                       | 680 ms: 1.08x faster                                                         |
| richards_super           | 90.6 ms                                                      | 84.1 ms: 1.08x faster                                                        |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.71 sec: 1.07x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                       |
| chaos                    | 109 ms                                                       | 101 ms: 1.07x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.59 sec: 1.05x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.81 us: 1.05x faster                                                        |
| scimark_fft              | 361 ms                                                       | 343 ms: 1.05x faster                                                         |
| json                     | 5.86 ms                                                      | 5.59 ms: 1.05x faster                                                        |
| nqueens                  | 115 ms                                                       | 110 ms: 1.04x faster                                                         |
| regex_compile            | 190 ms                                                       | 182 ms: 1.04x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.90 sec: 1.04x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 14.3 ms: 1.02x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 81.5 ms: 1.00x slower                                                        |
| go                       | 262 ms                                                       | 266 ms: 1.02x slower                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 1.07 sec: 1.02x slower                                                       |
| nbody                    | 134 ms                                                       | 137 ms: 1.02x slower                                                         |
| comprehensions           | 26.7 us                                                      | 27.3 us: 1.02x slower                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.21 sec: 1.03x slower                                                       |
| thrift                   | 1.18 ms                                                      | 1.21 ms: 1.03x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 72.2 ms: 1.03x slower                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 23.4 ms: 1.03x slower                                                        |
| html5lib                 | 94.6 ms                                                      | 97.9 ms: 1.03x slower                                                        |
| deltablue                | 7.50 ms                                                      | 7.77 ms: 1.04x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 9.76 ms: 1.04x slower                                                        |
| logging_silent           | 167 ns                                                       | 174 ns: 1.04x slower                                                         |
| richards                 | 75.1 ms                                                      | 78.2 ms: 1.04x slower                                                        |
| raytrace                 | 489 ms                                                       | 513 ms: 1.05x slower                                                         |
| fannkuch                 | 483 ms                                                       | 509 ms: 1.05x slower                                                         |
| unpickle_pure_python     | 312 us                                                       | 330 us: 1.06x slower                                                         |
| sympy_integrate          | 28.2 ms                                                      | 30.0 ms: 1.07x slower                                                        |
| logging_simple           | 8.88 us                                                      | 9.49 us: 1.07x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 81.2 ms: 1.07x slower                                                        |
| logging_format           | 9.64 us                                                      | 10.3 us: 1.07x slower                                                        |
| scimark_lu               | 167 ms                                                       | 179 ms: 1.08x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.32 ms: 1.08x slower                                                        |
| django_template          | 50.2 ms                                                      | 54.3 ms: 1.08x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 34.0 ms: 1.08x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 69.3 ms: 1.10x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 102 ms: 1.11x slower                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 210 ms: 1.11x slower                                                         |
| 2to3                     | 350 ms                                                       | 391 ms: 1.12x slower                                                         |
| sympy_str                | 360 ms                                                       | 403 ms: 1.12x slower                                                         |
| scimark_sor              | 180 ms                                                       | 202 ms: 1.12x slower                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 121 ms: 1.13x slower                                                         |
| meteor_contest           | 138 ms                                                       | 157 ms: 1.13x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.76 ms: 1.13x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.04 ms: 1.13x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 3.88 ms: 1.13x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.58 ms: 1.15x slower                                                        |
| pickle_pure_python       | 455 us                                                       | 525 us: 1.15x slower                                                         |
| float                    | 111 ms                                                       | 130 ms: 1.17x slower                                                         |
| sympy_expand             | 600 ms                                                       | 739 ms: 1.23x slower                                                         |
| async_generators         | 421 ms                                                       | 519 ms: 1.23x slower                                                         |
| sympy_sum                | 193 ms                                                       | 239 ms: 1.24x slower                                                         |
| telco                    | 7.23 ms                                                      | 9.49 ms: 1.31x slower                                                        |
| mako                     | 14.7 ms                                                      | 19.3 ms: 1.31x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.59 ms: 1.39x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.37 sec: 1.47x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.70 ms: 1.53x slower                                                        |
| coverage                 | 63.3 ms                                                      | 105 ms: 1.66x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 12.3 ms: 1.67x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.7 ms: 1.71x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 53.8 ms: 8.45x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): sqlglot_normalize
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 69.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.52x