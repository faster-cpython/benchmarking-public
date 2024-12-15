# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 648 ms: 2.47x faster                                                         |
| async_tree_none         | 692 ms                                                       | 293 ms: 2.36x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 359 ms: 2.28x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 519 ms: 1.81x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.9 ms: 1.52x faster                                                        |
| nbody          | 134 ms                                                       | 92.2 ms: 1.45x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                         |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.31 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 200 us: 1.56x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 338 us: 1.35x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 56.5 ms: 1.34x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 94.0 ms: 1.18x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.38 ms: 1.57x faster                                                        |
| django_template | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 28.0 ms: 1.12x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.92x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 648 ms: 2.47x faster                                                         |
| async_tree_none          | 692 ms                                                       | 293 ms: 2.36x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 359 ms: 2.28x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 519 ms: 1.81x faster                                                         |
| go                       | 262 ms                                                       | 147 ms: 1.78x faster                                                         |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 63.1 ms: 1.70x faster                                                        |
| scimark_lu               | 167 ms                                                       | 98.2 ms: 1.70x faster                                                        |
| pylint                   | 566 ms                                                       | 334 ms: 1.70x faster                                                         |
| pyflate                  | 733 ms                                                       | 438 ms: 1.67x faster                                                         |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                         |
| chaos                    | 109 ms                                                       | 66.8 ms: 1.63x faster                                                        |
| richards_super           | 90.6 ms                                                      | 55.8 ms: 1.62x faster                                                        |
| deepcopy                 | 468 us                                                       | 295 us: 1.58x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 75.4 ms: 1.58x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.38 ms: 1.57x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 200 us: 1.56x faster                                                         |
| richards                 | 75.1 ms                                                      | 48.4 ms: 1.55x faster                                                        |
| float                    | 111 ms                                                       | 72.9 ms: 1.52x faster                                                        |
| spectral_norm            | 139 ms                                                       | 91.9 ms: 1.51x faster                                                        |
| raytrace                 | 489 ms                                                       | 330 ms: 1.48x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.46x faster                                                        |
| generators               | 57.3 ms                                                      | 39.3 ms: 1.46x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.45x faster                                                        |
| nbody                    | 134 ms                                                       | 92.2 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.9 us: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.15 us: 1.35x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 338 us: 1.35x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.35x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 56.5 ms: 1.34x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                         |
| thrift                   | 1.18 ms                                                      | 889 us: 1.32x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.13 ms: 1.32x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 811 ms: 1.29x faster                                                         |
| fannkuch                 | 483 ms                                                       | 374 ms: 1.29x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                                         |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.9 ms: 1.19x faster                                                        |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| sympy_str                | 360 ms                                                       | 305 ms: 1.18x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 94.0 ms: 1.18x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 24.1 ms: 1.17x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 124 ms: 1.16x faster                                                         |
| sympy_expand             | 600 ms                                                       | 519 ms: 1.16x faster                                                         |
| nqueens                  | 115 ms                                                       | 99.4 ms: 1.16x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.16 ms: 1.14x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 61.9 ms: 1.13x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.0 ms: 1.12x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.02 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                         |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                        |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.13 ms: 1.01x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.53 ms: 1.04x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.31 ms: 1.07x slower                                                        |
| async_generators         | 421 ms                                                       | 465 ms: 1.10x slower                                                         |
| mypy2                    | 933 ms                                                       | 1.04 sec: 1.12x slower                                                       |
| coverage                 | 63.3 ms                                                      | 76.8 ms: 1.21x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.69 ms: 1.53x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.53 ms: 1.91x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.01 sec: 157.93x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.30x