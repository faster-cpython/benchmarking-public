# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 406dc71
- commit date: 2025-08-03
- overall geometric mean: 1.114x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 325 ms: 1.08x faster                                        |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                      |
| html5lib       | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                       |
| Geometric mean | (ref)                                                        | 1.16x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 667 ms: 2.40x faster                                        |
| async_tree_memoization  | 819 ms                                                       | 362 ms: 2.27x faster                                        |
| async_tree_none         | 692 ms                                                       | 306 ms: 2.26x faster                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 531 ms: 1.76x faster                                        |
| Geometric mean          | (ref)                                                        | 2.16x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 257 ms: 1.05x faster                                        |
| float          | 111 ms                                                       | 107 ms: 1.04x faster                                        |
| nbody          | 134 ms                                                       | 184 ms: 1.37x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 159 ms: 1.20x faster                                        |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                        |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                       |
| regex_effbot   | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.21x faster                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                        |
| pickle_pure_python   | 455 us                                                       | 410 us: 1.11x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 3.08 sec: 1.06x slower                                      |
| xml_etree_generate   | 92.3 ms                                                      | 109 ms: 1.18x slower                                        |
| unpickle_pure_python | 312 us                                                       | 388 us: 1.24x slower                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                       |
| genshi_text     | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                       |
| genshi_xml      | 63.3 ms                                                      | 57.7 ms: 1.10x faster                                       |
| mako            | 14.7 ms                                                      | 16.9 ms: 1.15x slower                                       |
| Geometric mean  | (ref)                                                        | 1.16x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 201 us: 2.67x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 667 ms: 2.40x faster                                        |
| async_tree_memoization   | 819 ms                                                       | 362 ms: 2.27x faster                                        |
| async_tree_none          | 692 ms                                                       | 306 ms: 2.26x faster                                        |
| mdp                      | 3.01 sec                                                     | 1.46 sec: 2.05x faster                                      |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.92x faster                                       |
| logging_silent           | 167 ns                                                       | 91.7 ns: 1.83x faster                                       |
| scimark_lu               | 167 ms                                                       | 92.5 ms: 1.80x faster                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.6 us: 1.80x faster                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 531 ms: 1.76x faster                                        |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                        |
| chaos                    | 109 ms                                                       | 63.4 ms: 1.71x faster                                       |
| pylint                   | 566 ms                                                       | 334 ms: 1.69x faster                                        |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                        |
| richards_super           | 90.6 ms                                                      | 59.7 ms: 1.52x faster                                       |
| logging_simple           | 8.88 us                                                      | 6.10 us: 1.45x faster                                       |
| logging_format           | 9.64 us                                                      | 6.69 us: 1.44x faster                                       |
| raytrace                 | 489 ms                                                       | 341 ms: 1.43x faster                                        |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                       |
| richards                 | 75.1 ms                                                      | 53.3 ms: 1.41x faster                                       |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                        |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                       |
| html5lib                 | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                       |
| dulwich_log              | 81.1 ms                                                      | 60.9 ms: 1.33x faster                                       |
| genshi_text              | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                       |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                       |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                       |
| deltablue                | 7.50 ms                                                      | 5.97 ms: 1.26x faster                                       |
| scimark_monte_carlo      | 107 ms                                                       | 88.9 ms: 1.21x faster                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.21x faster                                       |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                        |
| regex_compile            | 190 ms                                                       | 159 ms: 1.20x faster                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.7 ms: 1.19x faster                                       |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                        |
| go                       | 262 ms                                                       | 224 ms: 1.17x faster                                        |
| pyflate                  | 733 ms                                                       | 632 ms: 1.16x faster                                        |
| sympy_str                | 360 ms                                                       | 315 ms: 1.14x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                       |
| crypto_pyaes             | 119 ms                                                       | 105 ms: 1.13x faster                                        |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                        |
| nqueens                  | 115 ms                                                       | 103 ms: 1.11x faster                                        |
| pickle_pure_python       | 455 us                                                       | 410 us: 1.11x faster                                        |
| pycparser                | 1.67 sec                                                     | 1.52 sec: 1.10x faster                                      |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                       |
| genshi_xml               | 63.3 ms                                                      | 57.7 ms: 1.10x faster                                       |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                      |
| sympy_expand             | 600 ms                                                       | 552 ms: 1.09x faster                                        |
| 2to3                     | 350 ms                                                       | 325 ms: 1.08x faster                                        |
| pidigits                 | 271 ms                                                       | 257 ms: 1.05x faster                                        |
| float                    | 111 ms                                                       | 107 ms: 1.04x faster                                        |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                        |
| sqlite_synth             | 2.99 us                                                      | 3.01 us: 1.01x slower                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.26 sec: 1.05x slower                                      |
| tomli_loads              | 2.92 sec                                                     | 3.08 sec: 1.06x slower                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.11 sec: 1.06x slower                                      |
| async_generators         | 421 ms                                                       | 456 ms: 1.08x slower                                        |
| hexiom                   | 9.42 ms                                                      | 10.6 ms: 1.13x slower                                       |
| comprehensions           | 26.7 us                                                      | 30.6 us: 1.15x slower                                       |
| mako                     | 14.7 ms                                                      | 16.9 ms: 1.15x slower                                       |
| meteor_contest           | 138 ms                                                       | 160 ms: 1.15x slower                                        |
| regex_effbot             | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                       |
| xml_etree_generate       | 92.3 ms                                                      | 109 ms: 1.18x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                       |
| spectral_norm            | 139 ms                                                       | 168 ms: 1.20x slower                                        |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                       |
| unpickle_pure_python     | 312 us                                                       | 388 us: 1.24x slower                                        |
| fannkuch                 | 483 ms                                                       | 607 ms: 1.26x slower                                        |
| scimark_fft              | 361 ms                                                       | 462 ms: 1.28x slower                                        |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                       |
| nbody                    | 134 ms                                                       | 184 ms: 1.37x slower                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 8.35 ms: 1.65x slower                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.94 ms: 1.67x slower                                       |
| gc_traversal             | 3.42 ms                                                      | 6.77 ms: 1.98x slower                                       |
| telco                    | 7.23 ms                                                      | 159 ms: 22.04x slower                                       |
| Geometric mean           | (ref)                                                        | 1.12x faster                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250803-3.15.0a0-406dc71-PYTHON_UOPS/bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.38x