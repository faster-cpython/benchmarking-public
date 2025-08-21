# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d22a745
- commit date: 2025-08-19
- overall geometric mean: 1.151x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 320 ms: 1.09x faster                                        |
| docutils       | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                      |
| html5lib       | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                       |
| Geometric mean | (ref)                                                        | 1.17x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 656 ms: 2.44x faster                                        |
| async_tree_none         | 692 ms                                                       | 290 ms: 2.38x faster                                        |
| async_tree_memoization  | 819 ms                                                       | 352 ms: 2.33x faster                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 521 ms: 1.80x faster                                        |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 111 ms                                                       | 94.0 ms: 1.18x faster                                       |
| pidigits       | 271 ms                                                       | 257 ms: 1.06x faster                                        |
| nbody          | 134 ms                                                       | 159 ms: 1.19x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.24x faster                                        |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                        |
| regex_v8       | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                       |
| regex_effbot   | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                       |
| json_loads           | 30.3 us                                                      | 25.8 us: 1.18x faster                                       |
| pickle_pure_python   | 455 us                                                       | 400 us: 1.14x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                        |
| xml_etree_process    | 75.9 ms                                                      | 71.1 ms: 1.07x faster                                       |
| tomli_loads          | 2.92 sec                                                     | 2.81 sec: 1.04x faster                                      |
| xml_etree_iterparse  | 110 ms                                                       | 108 ms: 1.03x faster                                        |
| unpickle_pure_python | 312 us                                                       | 338 us: 1.08x slower                                        |
| xml_etree_generate   | 92.3 ms                                                      | 102 ms: 1.11x slower                                        |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                       |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                       |
| genshi_xml      | 63.3 ms                                                      | 58.0 ms: 1.09x faster                                       |
| mako            | 14.7 ms                                                      | 15.3 ms: 1.04x slower                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 193 us: 2.78x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 656 ms: 2.44x faster                                        |
| async_tree_none          | 692 ms                                                       | 290 ms: 2.38x faster                                        |
| async_tree_memoization   | 819 ms                                                       | 352 ms: 2.33x faster                                        |
| mdp                      | 3.01 sec                                                     | 1.42 sec: 2.12x faster                                      |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.97x faster                                       |
| logging_silent           | 167 ns                                                       | 92.0 ns: 1.82x faster                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 521 ms: 1.80x faster                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.77x faster                                       |
| scimark_lu               | 167 ms                                                       | 95.1 ms: 1.75x faster                                       |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                       |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.72x faster                                        |
| pylint                   | 566 ms                                                       | 335 ms: 1.69x faster                                        |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                        |
| raytrace                 | 489 ms                                                       | 323 ms: 1.52x faster                                        |
| richards_super           | 90.6 ms                                                      | 60.1 ms: 1.51x faster                                       |
| logging_simple           | 8.88 us                                                      | 5.91 us: 1.50x faster                                       |
| logging_format           | 9.64 us                                                      | 6.58 us: 1.47x faster                                       |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                       |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                       |
| thrift                   | 1.18 ms                                                      | 828 us: 1.42x faster                                        |
| deltablue                | 7.50 ms                                                      | 5.30 ms: 1.42x faster                                       |
| richards                 | 75.1 ms                                                      | 53.5 ms: 1.40x faster                                       |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                       |
| html5lib                 | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                       |
| dulwich_log              | 81.1 ms                                                      | 61.5 ms: 1.32x faster                                       |
| pyflate                  | 733 ms                                                       | 560 ms: 1.31x faster                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.07 us: 1.31x faster                                       |
| scimark_monte_carlo      | 107 ms                                                       | 82.3 ms: 1.31x faster                                       |
| go                       | 262 ms                                                       | 202 ms: 1.30x faster                                        |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                       |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                       |
| regex_compile            | 190 ms                                                       | 154 ms: 1.24x faster                                        |
| crypto_pyaes             | 119 ms                                                       | 98.4 ms: 1.21x faster                                       |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                       |
| float                    | 111 ms                                                       | 94.0 ms: 1.18x faster                                       |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                        |
| json_loads               | 30.3 us                                                      | 25.8 us: 1.18x faster                                       |
| nqueens                  | 115 ms                                                       | 99.6 ms: 1.15x faster                                       |
| sympy_str                | 360 ms                                                       | 315 ms: 1.14x faster                                        |
| pycparser                | 1.67 sec                                                     | 1.47 sec: 1.14x faster                                      |
| pickle_pure_python       | 455 us                                                       | 400 us: 1.14x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                       |
| docutils                 | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                      |
| 2to3                     | 350 ms                                                       | 320 ms: 1.09x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 58.0 ms: 1.09x faster                                       |
| sympy_expand             | 600 ms                                                       | 553 ms: 1.08x faster                                        |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.08x faster                                        |
| json                     | 5.86 ms                                                      | 5.46 ms: 1.07x faster                                       |
| xml_etree_process        | 75.9 ms                                                      | 71.1 ms: 1.07x faster                                       |
| pidigits                 | 271 ms                                                       | 257 ms: 1.06x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.81 sec: 1.04x faster                                      |
| pprint_pformat           | 2.15 sec                                                     | 2.08 sec: 1.03x faster                                      |
| xml_etree_iterparse      | 110 ms                                                       | 108 ms: 1.03x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                      |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                        |
| sqlite_synth             | 2.99 us                                                      | 2.95 us: 1.01x faster                                       |
| comprehensions           | 26.7 us                                                      | 27.4 us: 1.03x slower                                       |
| hexiom                   | 9.42 ms                                                      | 9.70 ms: 1.03x slower                                       |
| mako                     | 14.7 ms                                                      | 15.3 ms: 1.04x slower                                       |
| spectral_norm            | 139 ms                                                       | 147 ms: 1.06x slower                                        |
| async_generators         | 421 ms                                                       | 453 ms: 1.08x slower                                        |
| meteor_contest           | 138 ms                                                       | 149 ms: 1.08x slower                                        |
| unpickle_pure_python     | 312 us                                                       | 338 us: 1.08x slower                                        |
| xml_etree_generate       | 92.3 ms                                                      | 102 ms: 1.11x slower                                        |
| fannkuch                 | 483 ms                                                       | 562 ms: 1.16x slower                                        |
| scimark_fft              | 361 ms                                                       | 425 ms: 1.18x slower                                        |
| regex_effbot             | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                       |
| nbody                    | 134 ms                                                       | 159 ms: 1.19x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                       |
| coverage                 | 63.3 ms                                                      | 81.9 ms: 1.30x slower                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 7.36 ms: 1.45x slower                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                       |
| gc_traversal             | 3.42 ms                                                      | 6.73 ms: 1.97x slower                                       |
| telco                    | 7.23 ms                                                      | 161 ms: 22.24x slower                                       |
| Geometric mean           | (ref)                                                        | 1.16x faster                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250819-3.15.0a0-d22a745-PYTHON_UOPS/bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.151x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.39x