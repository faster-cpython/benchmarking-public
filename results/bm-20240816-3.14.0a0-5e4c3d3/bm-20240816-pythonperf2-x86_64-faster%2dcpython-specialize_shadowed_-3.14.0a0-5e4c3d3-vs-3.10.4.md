# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 5e4c3d3
- commit date: 2024-08-16
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                                |
| html5lib       | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                                 |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 338 ms: 2.05x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 409 ms: 2.00x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 816 ms: 1.96x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.9 ms: 1.56x faster                                                                 |
| float          | 111 ms                                                       | 79.9 ms: 1.39x faster                                                                 |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                                  |
| regex_dna      | 261 ms                                                       | 254 ms: 1.03x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.15x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 317 us: 1.43x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| unpickle_pure_python | 312 us                                                       | 231 us: 1.35x faster                                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.27 sec: 1.28x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 59.4 ms: 1.28x faster                                                                 |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.20x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                                                 |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.15x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.6 ms: 1.39x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                                 |
| django_template | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 53.2 ms: 1.19x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.13x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                                 |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 338 ms: 2.05x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                                 |
| async_tree_memoization   | 819 ms                                                       | 409 ms: 2.00x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 816 ms: 1.96x faster                                                                  |
| raytrace                 | 489 ms                                                       | 271 ms: 1.80x faster                                                                  |
| chaos                    | 109 ms                                                       | 61.3 ms: 1.77x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 94.4 ms: 1.77x faster                                                                 |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.71x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 64.4 ms: 1.67x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 72.9 ms: 1.64x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.63x faster                                                                  |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                                  |
| go                       | 262 ms                                                       | 161 ms: 1.62x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 55.9 ms: 1.62x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                                  |
| deepcopy                 | 468 us                                                       | 292 us: 1.60x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                                 |
| nbody                    | 134 ms                                                       | 85.9 ms: 1.56x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                                 |
| pyflate                  | 733 ms                                                       | 484 ms: 1.51x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.24 ms: 1.51x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                                 |
| richards                 | 75.1 ms                                                      | 50.1 ms: 1.50x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.43x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 97.6 ms: 1.43x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.26 us: 1.42x faster                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 4.54 ms: 1.40x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.89 us: 1.40x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.6 ms: 1.39x faster                                                                 |
| float                    | 111 ms                                                       | 79.9 ms: 1.39x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                                 |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                                 |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                                  |
| fannkuch                 | 483 ms                                                       | 357 ms: 1.35x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 231 us: 1.35x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 871 us: 1.35x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 862 us: 1.32x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.27 sec: 1.28x faster                                                                |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 59.4 ms: 1.28x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                                |
| django_template          | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 824 ms: 1.27x faster                                                                  |
| nqueens                  | 115 ms                                                       | 91.8 ms: 1.25x faster                                                                 |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                                                  |
| sympy_str                | 360 ms                                                       | 294 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.25 ms: 1.20x faster                                                                 |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.20x faster                                                                 |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 53.2 ms: 1.19x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                                  |
| async_generators         | 421 ms                                                       | 355 ms: 1.19x faster                                                                  |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 59.7 ms: 1.17x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.09x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                                                 |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| regex_dna                | 261 ms                                                       | 254 ms: 1.03x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                                  |
| telco                    | 7.23 ms                                                      | 8.00 ms: 1.11x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.15x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.15x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240816-3.14.0a0-5e4c3d3/bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x