# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.354x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 64.4 ms: 1.47x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 248 ms: 2.79x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 578 ms: 2.76x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 306 ms: 2.68x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 476 ms: 1.97x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 65.3 ms: 1.70x faster                                                        |
| nbody          | 134 ms                                                       | 92.7 ms: 1.45x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.5 ms: 1.15x faster                                                        |
| regex_dna      | 261 ms                                                       | 228 ms: 1.14x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 55.4 ms: 1.37x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 85.4 ms: 1.29x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 133 ms: 1.20x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 78.7 ms: 1.17x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 5.04 us: 1.08x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 33.6 us: 1.14x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.98 us: 1.21x slower                                                        |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.74 ms: 1.19x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.0 ms: 1.31x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.74 ms: 1.51x faster                                                        |
| django_template | 50.2 ms                                                      | 34.8 ms: 1.44x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.1 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                         |
| async_tree_none          | 692 ms                                                       | 248 ms: 2.79x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 578 ms: 2.76x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 306 ms: 2.68x faster                                                         |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.37x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.20 ms: 2.35x faster                                                        |
| go                       | 262 ms                                                       | 119 ms: 2.20x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.10x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 24.0 us: 2.07x faster                                                        |
| richards_super           | 90.6 ms                                                      | 43.8 ms: 2.07x faster                                                        |
| richards                 | 75.1 ms                                                      | 37.9 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 476 ms: 1.97x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                       |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                        |
| chaos                    | 109 ms                                                       | 57.4 ms: 1.89x faster                                                        |
| pyflate                  | 733 ms                                                       | 394 ms: 1.86x faster                                                         |
| raytrace                 | 489 ms                                                       | 272 ms: 1.80x faster                                                         |
| logging_silent           | 167 ns                                                       | 93.0 ns: 1.80x faster                                                        |
| scimark_sor              | 180 ms                                                       | 100 ms: 1.79x faster                                                         |
| deepcopy                 | 468 us                                                       | 267 us: 1.76x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 61.6 ms: 1.75x faster                                                        |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                         |
| scimark_lu               | 167 ms                                                       | 96.2 ms: 1.74x faster                                                        |
| float                    | 111 ms                                                       | 65.3 ms: 1.70x faster                                                        |
| spectral_norm            | 139 ms                                                       | 83.7 ms: 1.66x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 5.88 ms: 1.60x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 76.8 ms: 1.55x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.86 us: 1.51x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.74 ms: 1.51x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.44 us: 1.50x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.46 sec: 1.47x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 64.4 ms: 1.47x faster                                                        |
| nbody                    | 134 ms                                                       | 92.7 ms: 1.45x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.8 ms: 1.44x faster                                                        |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 730 ms: 1.44x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.1 ms: 1.41x faster                                                        |
| thrift                   | 1.18 ms                                                      | 848 us: 1.39x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 55.4 ms: 1.37x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.3 ms: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.9 ms: 1.32x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                        |
| scimark_fft              | 361 ms                                                       | 276 ms: 1.31x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 85.4 ms: 1.29x faster                                                        |
| fannkuch                 | 483 ms                                                       | 375 ms: 1.29x faster                                                         |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.3 ms: 1.26x faster                                                        |
| nqueens                  | 115 ms                                                       | 91.9 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 946 us: 1.21x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 133 ms: 1.20x faster                                                         |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 78.7 ms: 1.17x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.5 ms: 1.15x faster                                                        |
| regex_dna                | 261 ms                                                       | 228 ms: 1.14x faster                                                         |
| unpack_sequence          | 59.9 ns                                                      | 52.4 ns: 1.14x faster                                                        |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.13x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 56.1 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.74 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 411 ms: 1.05x slower                                                         |
| async_generators         | 421 ms                                                       | 444 ms: 1.05x slower                                                         |
| unpickle_list            | 4.65 us                                                      | 5.04 us: 1.08x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 33.6 us: 1.14x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.74 ms: 1.19x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.98 us: 1.21x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.5 ms: 1.24x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.0 ms: 1.31x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.94 ms: 1.67x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.88 ms: 2.01x slower                                                        |
| telco                    | 7.23 ms                                                      | 156 ms: 21.56x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.33 sec: 209.29x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                 |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.354x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.41x