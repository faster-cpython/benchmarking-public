# Results vs. 3.10.4

- fork: python
- ref: bb0268f60dfe903a9bdb
- machine: linux-x86_64
- commit hash: bb0268f
- commit date: 2025-03-17
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 644 ms: 2.48x faster                                                         |
| async_tree_none         | 692 ms                                                       | 290 ms: 2.39x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 347 ms: 2.36x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.3 ms: 1.56x faster                                                        |
| nbody          | 134 ms                                                       | 99.3 ms: 1.35x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.37x faster                                                         |
| regex_dna      | 261 ms                                                       | 229 ms: 1.14x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.07 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 228 us: 1.37x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 342 us: 1.33x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 37.7 ms: 1.33x faster                                                        |
| mako            | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.7 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.04x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 644 ms: 2.48x faster                                                         |
| async_tree_none          | 692 ms                                                       | 290 ms: 2.39x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 347 ms: 2.36x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.20x faster                                                        |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.00x faster                                                        |
| go                       | 262 ms                                                       | 131 ms: 2.00x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                         |
| logging_silent           | 167 ns                                                       | 95.7 ns: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 293 ms: 1.67x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.67x faster                                                        |
| chaos                    | 109 ms                                                       | 65.3 ms: 1.66x faster                                                        |
| scimark_lu               | 167 ms                                                       | 101 ms: 1.65x faster                                                         |
| richards_super           | 90.6 ms                                                      | 55.0 ms: 1.65x faster                                                        |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                         |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                        |
| float                    | 111 ms                                                       | 71.3 ms: 1.56x faster                                                        |
| pyflate                  | 733 ms                                                       | 474 ms: 1.55x faster                                                         |
| richards                 | 75.1 ms                                                      | 48.8 ms: 1.54x faster                                                        |
| spectral_norm            | 139 ms                                                       | 92.0 ms: 1.51x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.47x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.54 ms: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 82.9 ms: 1.44x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.37x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 228 us: 1.37x faster                                                         |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                         |
| nbody                    | 134 ms                                                       | 99.3 ms: 1.35x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                       |
| django_template          | 50.2 ms                                                      | 37.7 ms: 1.33x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 342 us: 1.33x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.70 us: 1.33x faster                                                        |
| mako                     | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.36 us: 1.31x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 809 ms: 1.30x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 62.6 ms: 1.30x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                        |
| fannkuch                 | 483 ms                                                       | 386 ms: 1.25x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                         |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                         |
| nqueens                  | 115 ms                                                       | 94.8 ms: 1.21x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 956 us: 1.19x faster                                                         |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                                        |
| regex_dna                | 261 ms                                                       | 229 ms: 1.14x faster                                                         |
| scimark_fft              | 361 ms                                                       | 318 ms: 1.14x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 56.7 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.74 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.07 ms: 1.01x faster                                                        |
| async_generators         | 421 ms                                                       | 422 ms: 1.00x slower                                                         |
| telco                    | 7.23 ms                                                      | 8.13 ms: 1.13x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.1 ms: 1.28x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.84 ms: 1.61x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.26 sec: 198.33x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250317-3.14.0a6+-bb0268f/bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.28x