# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-x86_64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.10x faster                                                         |
| docutils       | 3.41 sec                                                     | 3.21 sec: 1.06x faster                                                       |
| html5lib       | 94.6 ms                                                      | 72.2 ms: 1.31x faster                                                        |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                         |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 343 ms: 2.01x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 417 ms: 1.96x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 846 ms: 1.89x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 581 ms: 1.61x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.86x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.2 ms: 1.57x faster                                                        |
| float          | 111 ms                                                       | 79.2 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.30x faster                                                         |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 337 us: 1.35x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 59.0 ms: 1.29x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.6 ms: 1.11x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 14.8 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.48 ms: 1.55x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                        |
| django_template | 50.2 ms                                                      | 44.8 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.92x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.33 ms: 2.25x faster                                                        |
| async_tree_none          | 692 ms                                                       | 343 ms: 2.01x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 417 ms: 1.96x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 846 ms: 1.89x faster                                                         |
| logging_silent           | 167 ns                                                       | 92.0 ns: 1.82x faster                                                        |
| scimark_lu               | 167 ms                                                       | 96.5 ms: 1.73x faster                                                        |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                         |
| go                       | 262 ms                                                       | 155 ms: 1.69x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 30.0 us: 1.66x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.8 ms: 1.64x faster                                                        |
| richards_super           | 90.6 ms                                                      | 55.4 ms: 1.63x faster                                                        |
| richards                 | 75.1 ms                                                      | 46.4 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 581 ms: 1.61x faster                                                         |
| pyflate                  | 733 ms                                                       | 456 ms: 1.61x faster                                                         |
| chaos                    | 109 ms                                                       | 68.1 ms: 1.59x faster                                                        |
| raytrace                 | 489 ms                                                       | 310 ms: 1.58x faster                                                         |
| nbody                    | 134 ms                                                       | 85.2 ms: 1.57x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.48 ms: 1.55x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 69.3 ms: 1.55x faster                                                        |
| deepcopy                 | 468 us                                                       | 307 us: 1.52x faster                                                         |
| spectral_norm            | 139 ms                                                       | 92.5 ms: 1.50x faster                                                        |
| generators               | 57.3 ms                                                      | 38.7 ms: 1.48x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.52 ms: 1.47x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.7 us: 1.43x faster                                                        |
| float                    | 111 ms                                                       | 79.2 ms: 1.40x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 337 us: 1.35x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.99 ms: 1.34x faster                                                        |
| pylint                   | 566 ms                                                       | 422 ms: 1.34x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 788 ms: 1.33x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                        |
| fannkuch                 | 483 ms                                                       | 368 ms: 1.31x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 72.2 ms: 1.31x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.19 ms: 1.31x faster                                                        |
| thrift                   | 1.18 ms                                                      | 898 us: 1.31x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.07 us: 1.31x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.84 us: 1.30x faster                                                        |
| regex_compile            | 190 ms                                                       | 147 ms: 1.30x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 59.0 ms: 1.29x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 63.1 ms: 1.29x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.53 us: 1.28x faster                                                        |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                         |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 945 us: 1.21x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.42 ms: 1.15x faster                                                        |
| json                     | 5.86 ms                                                      | 5.15 ms: 1.14x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| sympy_expand             | 600 ms                                                       | 533 ms: 1.13x faster                                                         |
| sympy_str                | 360 ms                                                       | 321 ms: 1.12x faster                                                         |
| nqueens                  | 115 ms                                                       | 102 ms: 1.12x faster                                                         |
| django_template          | 50.2 ms                                                      | 44.8 ms: 1.12x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.6 ms: 1.11x faster                                                        |
| 2to3                     | 350 ms                                                       | 317 ms: 1.10x faster                                                         |
| sympy_sum                | 193 ms                                                       | 175 ms: 1.10x faster                                                         |
| async_generators         | 421 ms                                                       | 382 ms: 1.10x faster                                                         |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.21 sec: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 27.3 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.75 ms: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.3 ms: 1.29x slower                                                        |
| python_startup           | 11.5 ms                                                      | 14.8 ms: 1.29x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.21 ms: 1.53x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.74 sec: 273.62x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (2): genshi_xml, sqlglot_optimize
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.283x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.34x