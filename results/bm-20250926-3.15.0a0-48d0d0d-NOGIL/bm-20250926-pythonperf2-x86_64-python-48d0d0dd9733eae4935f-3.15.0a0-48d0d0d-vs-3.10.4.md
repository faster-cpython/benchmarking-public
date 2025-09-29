# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.205x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 312 ms: 1.12x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 555 ms: 2.88x faster                                                        |
| async_tree_none         | 692 ms                                                       | 261 ms: 2.65x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 320 ms: 2.56x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 494 ms: 1.90x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.47x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.8 ms: 1.55x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| nbody          | 134 ms                                                       | 126 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.23x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                       |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| unpickle_pure_python | 312 us                                                       | 241 us: 1.29x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 88.3 ms: 1.25x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 364 us: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| json_loads           | 30.3 us                                                      | 27.6 us: 1.10x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 70.8 ms: 1.07x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 99.0 ms: 1.07x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.9 us: 1.08x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.54 us: 1.19x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.00 us: 1.21x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.5 us: 1.22x slower                                                       |
| pickle               | 9.89 us                                                      | 12.1 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| python_startup         | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.2 ms: 1.16x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.5 ms: 1.05x slower                                                       |
| mako            | 14.7 ms                                                      | 17.3 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 555 ms: 2.88x faster                                                        |
| async_tree_none          | 692 ms                                                       | 261 ms: 2.65x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 209 us: 2.57x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 320 ms: 2.56x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.60 ms: 2.08x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.45 sec: 2.07x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 494 ms: 1.90x faster                                                        |
| go                       | 262 ms                                                       | 139 ms: 1.89x faster                                                        |
| generators               | 57.3 ms                                                      | 31.8 ms: 1.81x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                       |
| pylint                   | 566 ms                                                       | 339 ms: 1.67x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.89 sec: 1.64x faster                                                      |
| chaos                    | 109 ms                                                       | 66.4 ms: 1.64x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.6 us: 1.63x faster                                                       |
| deepcopy                 | 468 us                                                       | 300 us: 1.56x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.19 ms: 1.56x faster                                                       |
| scimark_sor              | 180 ms                                                       | 116 ms: 1.56x faster                                                        |
| float                    | 111 ms                                                       | 71.8 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 474 ms: 1.55x faster                                                        |
| raytrace                 | 489 ms                                                       | 319 ms: 1.53x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.52 ms: 1.44x faster                                                       |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.43x faster                                                        |
| richards_super           | 90.6 ms                                                      | 64.3 ms: 1.41x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.5 ms: 1.38x faster                                                       |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.37x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| richards                 | 75.1 ms                                                      | 55.8 ms: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 61.3 ms: 1.32x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 81.7 ms: 1.31x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 91.7 ms: 1.30x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 241 us: 1.29x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.97 us: 1.27x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 88.3 ms: 1.25x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 364 us: 1.25x faster                                                        |
| regex_compile            | 190 ms                                                       | 154 ms: 1.23x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.82 us: 1.23x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.37 us: 1.19x faster                                                       |
| thrift                   | 1.18 ms                                                      | 990 us: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 894 ms: 1.17x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.85 sec: 1.16x faster                                                      |
| django_template          | 50.2 ms                                                      | 43.2 ms: 1.16x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.62 us: 1.14x faster                                                       |
| sympy_sum                | 193 ms                                                       | 170 ms: 1.13x faster                                                        |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.0 ms: 1.13x faster                                                       |
| 2to3                     | 350 ms                                                       | 312 ms: 1.12x faster                                                        |
| sympy_str                | 360 ms                                                       | 325 ms: 1.11x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 54.2 ns: 1.11x faster                                                       |
| scimark_fft              | 361 ms                                                       | 328 ms: 1.10x faster                                                        |
| json_loads               | 30.3 us                                                      | 27.6 us: 1.10x faster                                                       |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                       |
| nqueens                  | 115 ms                                                       | 105 ms: 1.09x faster                                                        |
| sympy_expand             | 600 ms                                                       | 552 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 70.8 ms: 1.07x faster                                                       |
| nbody                    | 134 ms                                                       | 126 ms: 1.06x faster                                                        |
| fannkuch                 | 483 ms                                                       | 456 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 371 ms: 1.05x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                       |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 66.5 ms: 1.05x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 99.0 ms: 1.07x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 31.9 us: 1.08x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.72 ms: 1.13x slower                                                       |
| async_generators         | 421 ms                                                       | 480 ms: 1.14x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| mako                     | 14.7 ms                                                      | 17.3 ms: 1.18x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.54 us: 1.19x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.37 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.00 us: 1.21x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.5 us: 1.22x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.23x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| python_startup           | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                       |
| coverage                 | 63.3 ms                                                      | 120 ms: 1.89x slower                                                        |
| telco                    | 7.23 ms                                                      | 172 ms: 23.83x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.205x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.67x