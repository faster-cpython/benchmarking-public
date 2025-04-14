# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.412x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 275 ms: 1.27x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                                       |
| html5lib       | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 615 ms: 2.60x faster                                                         |
| async_tree_none         | 692 ms                                                       | 272 ms: 2.54x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 539 ms: 1.74x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 66.4 ms: 1.67x faster                                                        |
| nbody          | 134 ms                                                       | 83.5 ms: 1.61x faster                                                        |
| pidigits       | 271 ms                                                       | 292 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                         |
| regex_dna      | 261 ms                                                       | 219 ms: 1.19x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 2.95 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 199 us: 1.57x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.00 sec: 1.45x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 54.2 ms: 1.40x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 77.3 ms: 1.19x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.6 us: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.50 us: 1.03x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 162 ms: 1.01x slower                                                         |
| unpickle             | 13.5 us                                                      | 13.7 us: 1.02x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 30.3 us: 1.03x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.41 us: 1.07x slower                                                        |
| pickle               | 9.89 us                                                      | 11.7 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.13 ms: 1.25x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 32.2 ms: 1.56x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 21.7 ms: 1.45x faster                                                        |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.39x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 155 us: 3.45x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 615 ms: 2.60x faster                                                         |
| async_tree_none          | 692 ms                                                       | 272 ms: 2.54x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.09 ms: 2.43x faster                                                        |
| go                       | 262 ms                                                       | 121 ms: 2.17x faster                                                         |
| logging_silent           | 167 ns                                                       | 79.6 ns: 2.10x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                         |
| scimark_sor              | 180 ms                                                       | 91.4 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                       |
| chaos                    | 109 ms                                                       | 55.8 ms: 1.95x faster                                                        |
| scimark_lu               | 167 ms                                                       | 86.3 ms: 1.93x faster                                                        |
| raytrace                 | 489 ms                                                       | 253 ms: 1.93x faster                                                         |
| richards_super           | 90.6 ms                                                      | 47.0 ms: 1.93x faster                                                        |
| generators               | 57.3 ms                                                      | 29.8 ms: 1.92x faster                                                        |
| spectral_norm            | 139 ms                                                       | 72.4 ms: 1.92x faster                                                        |
| pyflate                  | 733 ms                                                       | 395 ms: 1.86x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 26.8 us: 1.86x faster                                                        |
| pylint                   | 566 ms                                                       | 306 ms: 1.85x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 58.3 ms: 1.84x faster                                                        |
| deepcopy                 | 468 us                                                       | 258 us: 1.82x faster                                                         |
| richards                 | 75.1 ms                                                      | 41.4 ms: 1.81x faster                                                        |
| comprehensions           | 26.7 us                                                      | 15.3 us: 1.75x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 539 ms: 1.74x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.29 ms: 1.73x faster                                                        |
| float                    | 111 ms                                                       | 66.4 ms: 1.67x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.68 ms: 1.66x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.66 ms: 1.62x faster                                                        |
| nbody                    | 134 ms                                                       | 83.5 ms: 1.61x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 74.8 ms: 1.59x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 199 us: 1.57x faster                                                         |
| django_template          | 50.2 ms                                                      | 32.2 ms: 1.56x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.92 us: 1.50x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.70 us: 1.49x faster                                                        |
| thrift                   | 1.18 ms                                                      | 792 us: 1.48x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.61 us: 1.46x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.00 sec: 1.45x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                         |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 21.7 ms: 1.45x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.52 sec: 1.42x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 54.2 ms: 1.40x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 752 ms: 1.40x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                       |
| fannkuch                 | 483 ms                                                       | 351 ms: 1.37x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 139 ms: 1.36x faster                                                         |
| scimark_fft              | 361 ms                                                       | 266 ms: 1.36x faster                                                         |
| nqueens                  | 115 ms                                                       | 85.4 ms: 1.35x faster                                                        |
| sympy_sum                | 193 ms                                                       | 146 ms: 1.32x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.3 ms: 1.31x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 110 ms: 1.31x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                        |
| sympy_str                | 360 ms                                                       | 278 ms: 1.29x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 54.3 ms: 1.29x faster                                                        |
| sympy_expand             | 600 ms                                                       | 469 ms: 1.28x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 892 us: 1.28x faster                                                         |
| 2to3                     | 350 ms                                                       | 275 ms: 1.27x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.1 ms: 1.27x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.9 ms: 1.25x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.17 ms: 1.22x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 77.3 ms: 1.19x faster                                                        |
| regex_dna                | 261 ms                                                       | 219 ms: 1.19x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.61 sec: 1.15x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.6 us: 1.14x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 52.9 ns: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.29 ms: 1.11x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 2.95 ms: 1.05x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.50 us: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| async_generators         | 421 ms                                                       | 416 ms: 1.01x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 162 ms: 1.01x slower                                                         |
| unpickle                 | 13.5 us                                                      | 13.7 us: 1.02x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.3 us: 1.03x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.53 ms: 1.04x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.41 us: 1.07x slower                                                        |
| pidigits                 | 271 ms                                                       | 292 ms: 1.08x slower                                                         |
| coverage                 | 63.3 ms                                                      | 73.1 ms: 1.16x slower                                                        |
| pickle                   | 9.89 us                                                      | 11.7 us: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.13 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.47 ms: 1.60x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.85 ms: 1.62x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 961 ms: 150.87x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                 |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.412x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.32x