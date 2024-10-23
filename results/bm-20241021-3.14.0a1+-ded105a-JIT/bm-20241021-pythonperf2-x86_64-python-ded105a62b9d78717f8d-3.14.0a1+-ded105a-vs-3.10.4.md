# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-x86_64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 315 ms: 1.11x faster                                                         |
| docutils       | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                       |
| html5lib       | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                        |
| tornado_http   | 157 ms                                                       | 124 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 340 ms: 2.03x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 411 ms: 1.99x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 831 ms: 1.92x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.7 ms: 1.58x faster                                                        |
| float          | 111 ms                                                       | 79.5 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                        |
| regex_dna      | 261 ms                                                       | 257 ms: 1.02x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.8 ms: 1.31x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 99.7 ms: 1.11x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.58 ms: 1.53x faster                                                        |
| django_template | 50.2 ms                                                      | 43.7 ms: 1.15x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.4 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.92x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                                        |
| async_tree_none          | 692 ms                                                       | 340 ms: 2.03x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 411 ms: 1.99x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 831 ms: 1.92x faster                                                         |
| logging_silent           | 167 ns                                                       | 91.6 ns: 1.83x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.3 ms: 1.75x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                         |
| go                       | 262 ms                                                       | 151 ms: 1.74x faster                                                         |
| richards_super           | 90.6 ms                                                      | 52.9 ms: 1.71x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.2 ms: 1.66x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.7 ms: 1.64x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                         |
| chaos                    | 109 ms                                                       | 68.0 ms: 1.60x faster                                                        |
| nbody                    | 134 ms                                                       | 84.7 ms: 1.58x faster                                                        |
| pyflate                  | 733 ms                                                       | 475 ms: 1.54x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.58 ms: 1.53x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 70.4 ms: 1.53x faster                                                        |
| raytrace                 | 489 ms                                                       | 321 ms: 1.52x faster                                                         |
| deepcopy                 | 468 us                                                       | 313 us: 1.50x faster                                                         |
| generators               | 57.3 ms                                                      | 38.6 ms: 1.49x faster                                                        |
| spectral_norm            | 139 ms                                                       | 93.8 ms: 1.48x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.52 ms: 1.47x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.7 us: 1.43x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 79.5 ms: 1.40x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.10 us: 1.36x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.99 ms: 1.35x faster                                                        |
| pylint                   | 566 ms                                                       | 420 ms: 1.35x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                        |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.8 ms: 1.31x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.19 ms: 1.31x faster                                                        |
| regex_compile            | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| thrift                   | 1.18 ms                                                      | 909 us: 1.29x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 62.9 ms: 1.29x faster                                                        |
| tornado_http             | 157 ms                                                       | 124 ms: 1.27x faster                                                         |
| scimark_fft              | 361 ms                                                       | 287 ms: 1.26x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.22 ms: 1.20x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 948 us: 1.20x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                       |
| django_template          | 50.2 ms                                                      | 43.7 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                        |
| sympy_expand             | 600 ms                                                       | 529 ms: 1.13x faster                                                         |
| sympy_str                | 360 ms                                                       | 318 ms: 1.13x faster                                                         |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                                        |
| nqueens                  | 115 ms                                                       | 102 ms: 1.12x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| 2to3                     | 350 ms                                                       | 315 ms: 1.11x faster                                                         |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.11x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 99.7 ms: 1.11x faster                                                        |
| async_generators         | 421 ms                                                       | 388 ms: 1.08x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                         |
| regex_dna                | 261 ms                                                       | 257 ms: 1.02x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 62.4 ms: 1.02x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 69.4 ms: 1.01x faster                                                        |
| telco                    | 7.23 ms                                                      | 7.75 ms: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                        |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.29x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.5 ms: 1.30x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.20 ms: 1.52x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.28 sec: 358.46x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                                 |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.34x