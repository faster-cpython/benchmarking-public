# Results vs. 3.10.4

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-aarch64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.356x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 58.7 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 362 ms: 2.62x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 887 ms: 2.58x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 461 ms: 2.46x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 656 ms: 1.94x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.38x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.3 ms: 1.56x faster                                                    |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.37x faster                                                     |
| regex_dna      | 257 ms                                                                | 197 ms: 1.31x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.30 ms: 1.29x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 29.2 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 165 ms: 1.28x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 287 us: 1.27x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 78.7 ms: 1.26x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 138 ms: 1.13x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                     |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.33 ms: 1.36x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.7 ms: 1.50x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.42x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| django_template | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.7 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                                     |
| async_tree_none          | 950 ms                                                                | 362 ms: 2.62x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 887 ms: 2.58x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 461 ms: 2.46x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.95 ms: 2.27x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 656 ms: 1.94x faster                                                     |
| go                       | 264 ms                                                                | 141 ms: 1.88x faster                                                     |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                                    |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                                    |
| raytrace                 | 573 ms                                                                | 317 ms: 1.81x faster                                                     |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.6 ms: 1.74x faster                                                    |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.64x faster                                                    |
| spectral_norm            | 186 ms                                                                | 116 ms: 1.61x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                    |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.59x faster                                                     |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.1 us: 1.58x faster                                                    |
| logging_silent           | 222 ns                                                                | 141 ns: 1.58x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 81.2 ms: 1.57x faster                                                    |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                     |
| float                    | 135 ms                                                                | 86.3 ms: 1.56x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.87 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 90.7 ms: 1.48x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.40 ms: 1.47x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 58.7 ms: 1.47x faster                                                    |
| pyflate                  | 795 ms                                                                | 553 ms: 1.44x faster                                                     |
| regex_compile            | 177 ms                                                                | 128 ms: 1.37x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.14 us: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.92 us: 1.34x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.47 us: 1.32x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.32x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                    |
| regex_dna                | 257 ms                                                                | 197 ms: 1.31x faster                                                     |
| scimark_fft              | 500 ms                                                                | 384 ms: 1.30x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.30 ms: 1.29x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 165 ms: 1.28x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 287 us: 1.27x faster                                                     |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 78.7 ms: 1.26x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 912 ms: 1.26x faster                                                     |
| thrift                   | 1.26 ms                                                               | 1.00 ms: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.11 ms: 1.25x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                                     |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                     |
| meteor_contest           | 126 ms                                                                | 103 ms: 1.22x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.9 ms: 1.21x faster                                                    |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                     |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 64.5 ms: 1.17x faster                                                    |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 64.6 ms: 1.14x faster                                                    |
| sympy_expand             | 543 ms                                                                | 480 ms: 1.13x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 138 ms: 1.13x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 62.7 ms: 1.11x faster                                                    |
| async_generators         | 452 ms                                                                | 411 ms: 1.10x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 29.2 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.95 us: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 6.20 ms: 1.05x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.03 ms: 1.06x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                    |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.33 ms: 1.36x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.7 ms: 1.50x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.64 ms: 1.60x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.74 ms: 1.66x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.37 sec: 369.65x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                             |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.356x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.29x