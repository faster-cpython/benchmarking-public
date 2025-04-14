# Results vs. 3.10.4

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.368x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.3 ms: 1.37x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 609 ms: 2.62x faster                                                         |
| async_tree_none         | 692 ms                                                       | 266 ms: 2.60x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 321 ms: 2.56x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 494 ms: 1.90x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.40x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.1 ms: 1.59x faster                                                        |
| nbody          | 134 ms                                                       | 91.2 ms: 1.47x faster                                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| regex_dna      | 261 ms                                                       | 192 ms: 1.36x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 2.52 ms: 1.23x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.1 ms: 1.33x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 124 ms: 1.29x faster                                                         |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 91.8 ms: 1.20x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.6 ms: 1.14x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.16 ms: 1.25x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.33x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| django_template | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.6 ms: 1.14x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 609 ms: 2.62x faster                                                         |
| async_tree_none          | 692 ms                                                       | 266 ms: 2.60x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 321 ms: 2.56x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.33 ms: 2.25x faster                                                        |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                        |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 56.5 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 494 ms: 1.90x faster                                                         |
| chaos                    | 109 ms                                                       | 60.5 ms: 1.80x faster                                                        |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                        |
| pylint                   | 566 ms                                                       | 324 ms: 1.74x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 28.9 us: 1.72x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.7 ns: 1.71x faster                                                        |
| richards_super           | 90.6 ms                                                      | 53.2 ms: 1.70x faster                                                        |
| pyflate                  | 733 ms                                                       | 431 ms: 1.70x faster                                                         |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                         |
| spectral_norm            | 139 ms                                                       | 83.8 ms: 1.66x faster                                                        |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                         |
| richards                 | 75.1 ms                                                      | 46.3 ms: 1.62x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.8 us: 1.59x faster                                                        |
| float                    | 111 ms                                                       | 70.1 ms: 1.59x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.03 ms: 1.56x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.6 ms: 1.54x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.0 ms: 1.52x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                        |
| nbody                    | 134 ms                                                       | 91.2 ms: 1.47x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.54 sec: 1.40x faster                                                       |
| fannkuch                 | 483 ms                                                       | 346 ms: 1.40x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 757 ms: 1.39x faster                                                         |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 69.3 ms: 1.37x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| thrift                   | 1.18 ms                                                      | 865 us: 1.36x faster                                                         |
| regex_dna                | 261 ms                                                       | 192 ms: 1.36x faster                                                         |
| django_template          | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.66 us: 1.33x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.1 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.2 ms: 1.30x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.40 us: 1.30x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 124 ms: 1.29x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                                        |
| scimark_fft              | 361 ms                                                       | 284 ms: 1.27x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.43 sec: 1.24x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 2.52 ms: 1.23x faster                                                        |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| meteor_contest           | 138 ms                                                       | 114 ms: 1.21x faster                                                         |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| sympy_str                | 360 ms                                                       | 299 ms: 1.20x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 91.8 ms: 1.20x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.7 ms: 1.19x faster                                                        |
| sympy_expand             | 600 ms                                                       | 507 ms: 1.18x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 69.2 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.38 ms: 1.16x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.6 ms: 1.14x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.00 ms: 1.14x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.6 ms: 1.14x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 402 ms: 1.05x faster                                                         |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                         |
| json                     | 5.86 ms                                                      | 5.65 ms: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.59 ms: 1.05x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.16 ms: 1.25x slower                                                        |
| coverage                 | 63.3 ms                                                      | 83.3 ms: 1.32x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.46 ms: 1.60x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 853 ms: 133.88x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.368x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.27x