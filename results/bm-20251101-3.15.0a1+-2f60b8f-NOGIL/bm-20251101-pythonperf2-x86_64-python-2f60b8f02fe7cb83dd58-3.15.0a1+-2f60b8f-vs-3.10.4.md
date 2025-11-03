# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.207x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 310 ms: 1.13x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 559 ms: 2.86x faster                                                         |
| async_tree_none         | 692 ms                                                       | 262 ms: 2.64x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 319 ms: 2.57x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 498 ms: 1.88x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.46x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.4 ms: 1.56x faster                                                        |
| nbody          | 134 ms                                                       | 125 ms: 1.07x faster                                                         |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.23x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                        |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 240 us: 1.30x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 88.2 ms: 1.25x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 366 us: 1.24x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.9 ms: 1.22x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 69.4 ms: 1.09x faster                                                        |
| json_loads           | 30.3 us                                                      | 27.9 us: 1.09x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 97.9 ms: 1.06x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.46 us: 1.17x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.8 us: 1.21x slower                                                        |
| unpickle             | 13.5 us                                                      | 16.4 us: 1.22x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.11 us: 1.24x slower                                                        |
| pickle               | 9.89 us                                                      | 12.4 us: 1.25x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.8 ms: 1.15x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 30.1 ms: 1.04x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 66.4 ms: 1.05x slower                                                        |
| mako            | 14.7 ms                                                      | 17.3 ms: 1.18x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 559 ms: 2.86x faster                                                         |
| async_tree_none          | 692 ms                                                       | 262 ms: 2.64x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 319 ms: 2.57x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 213 us: 2.52x faster                                                         |
| mdp                      | 3.01 sec                                                     | 1.43 sec: 2.10x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.64 ms: 2.06x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 381 ms: 2.04x faster                                                         |
| generators               | 57.3 ms                                                      | 29.8 ms: 1.92x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 498 ms: 1.88x faster                                                         |
| go                       | 262 ms                                                       | 140 ms: 1.87x faster                                                         |
| logging_silent           | 167 ns                                                       | 97.0 ns: 1.72x faster                                                        |
| pylint                   | 566 ms                                                       | 338 ms: 1.67x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                        |
| chaos                    | 109 ms                                                       | 66.5 ms: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 471 ms: 1.56x faster                                                         |
| float                    | 111 ms                                                       | 71.4 ms: 1.56x faster                                                        |
| deepcopy                 | 468 us                                                       | 301 us: 1.55x faster                                                         |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                         |
| gc_traversal             | 3.42 ms                                                      | 2.21 ms: 1.54x faster                                                        |
| raytrace                 | 489 ms                                                       | 322 ms: 1.52x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.48 ms: 1.45x faster                                                        |
| scimark_lu               | 167 ms                                                       | 118 ms: 1.42x faster                                                         |
| richards_super           | 90.6 ms                                                      | 64.5 ms: 1.41x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.3 ms: 1.40x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.39x faster                                                       |
| spectral_norm            | 139 ms                                                       | 102 ms: 1.36x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                        |
| richards                 | 75.1 ms                                                      | 56.4 ms: 1.33x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 81.5 ms: 1.32x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 61.9 ms: 1.31x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.83 us: 1.30x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 240 us: 1.30x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 93.5 ms: 1.27x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 88.2 ms: 1.25x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.75 us: 1.24x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 366 us: 1.24x faster                                                         |
| regex_compile            | 190 ms                                                       | 154 ms: 1.23x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.9 ms: 1.22x faster                                                        |
| thrift                   | 1.18 ms                                                      | 965 us: 1.22x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 883 ms: 1.19x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.38 us: 1.18x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.83 sec: 1.18x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.60 us: 1.15x faster                                                        |
| django_template          | 50.2 ms                                                      | 43.8 ms: 1.15x faster                                                        |
| sympy_sum                | 193 ms                                                       | 170 ms: 1.14x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 25.0 ms: 1.13x faster                                                        |
| 2to3                     | 350 ms                                                       | 310 ms: 1.13x faster                                                         |
| scimark_fft              | 361 ms                                                       | 322 ms: 1.12x faster                                                         |
| sympy_str                | 360 ms                                                       | 325 ms: 1.11x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 69.4 ms: 1.09x faster                                                        |
| nqueens                  | 115 ms                                                       | 105 ms: 1.09x faster                                                         |
| unpack_sequence          | 59.9 ns                                                      | 55.1 ns: 1.09x faster                                                        |
| json_loads               | 30.3 us                                                      | 27.9 us: 1.09x faster                                                        |
| sympy_expand             | 600 ms                                                       | 552 ms: 1.09x faster                                                         |
| fannkuch                 | 483 ms                                                       | 445 ms: 1.08x faster                                                         |
| nbody                    | 134 ms                                                       | 125 ms: 1.07x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| json                     | 5.86 ms                                                      | 5.53 ms: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 30.1 ms: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 375 ms: 1.04x faster                                                         |
| meteor_contest           | 138 ms                                                       | 143 ms: 1.03x slower                                                         |
| genshi_xml               | 63.3 ms                                                      | 66.4 ms: 1.05x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 97.9 ms: 1.06x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                        |
| async_generators         | 421 ms                                                       | 466 ms: 1.11x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.69 ms: 1.12x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.46 us: 1.17x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.3 ms: 1.18x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.35 ms: 1.19x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.8 us: 1.21x slower                                                        |
| unpickle                 | 13.5 us                                                      | 16.4 us: 1.22x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.11 us: 1.24x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.4 us: 1.25x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                        |
| coverage                 | 63.3 ms                                                      | 121 ms: 1.91x slower                                                         |
| telco                    | 7.23 ms                                                      | 174 ms: 24.10x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.207x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.69x