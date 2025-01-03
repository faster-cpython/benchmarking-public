# Results vs. 3.10.4

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-x86_64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.359x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.25x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                     |
| html5lib       | 94.6 ms                                                      | 67.7 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                        | 1.28x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 621 ms: 2.57x faster                                                       |
| async_tree_none         | 692 ms                                                       | 280 ms: 2.47x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 342 ms: 2.39x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                       |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.8 ms: 1.57x faster                                                      |
| nbody          | 134 ms                                                       | 88.0 ms: 1.52x faster                                                      |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.36x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                       |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.03x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.26 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                        | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.53x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                     |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                                      |
| json_loads           | 30.3 us                                                      | 23.5 us: 1.29x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 96.2 ms: 1.15x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 81.3 ms: 1.13x faster                                                      |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                      |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                                      |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                                      |
| genshi_xml      | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 165 us: 3.25x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 621 ms: 2.57x faster                                                       |
| async_tree_none          | 692 ms                                                       | 280 ms: 2.47x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 342 ms: 2.39x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.28 ms: 2.29x faster                                                      |
| go                       | 262 ms                                                       | 125 ms: 2.09x faster                                                       |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                       |
| pylint                   | 566 ms                                                       | 313 ms: 1.81x faster                                                       |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                       |
| chaos                    | 109 ms                                                       | 60.9 ms: 1.78x faster                                                      |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                                      |
| richards_super           | 90.6 ms                                                      | 52.3 ms: 1.73x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 62.8 ms: 1.71x faster                                                      |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                                      |
| sqlglot_parse            | 2.24 ms                                                      | 1.32 ms: 1.69x faster                                                      |
| deepcopy                 | 468 us                                                       | 277 us: 1.69x faster                                                       |
| pyflate                  | 733 ms                                                       | 435 ms: 1.69x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.66x faster                                                      |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.65x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.7 ms: 1.64x faster                                                      |
| richards                 | 75.1 ms                                                      | 45.9 ms: 1.64x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.70 ms: 1.58x faster                                                      |
| float                    | 111 ms                                                       | 70.8 ms: 1.57x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.01 ms: 1.57x faster                                                      |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                      |
| spectral_norm            | 139 ms                                                       | 89.2 ms: 1.56x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.53x faster                                                       |
| nbody                    | 134 ms                                                       | 88.0 ms: 1.52x faster                                                      |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                      |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.22 us: 1.43x faster                                                      |
| logging_format           | 9.64 us                                                      | 6.80 us: 1.42x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                     |
| thrift                   | 1.18 ms                                                      | 840 us: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.87 us: 1.40x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 67.7 ms: 1.40x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                     |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.39x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 763 ms: 1.38x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                      |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.34x faster                                                       |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                      |
| nqueens                  | 115 ms                                                       | 86.2 ms: 1.33x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 110 ms: 1.31x faster                                                       |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.29x faster                                                       |
| json_loads               | 30.3 us                                                      | 23.5 us: 1.29x faster                                                      |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 54.8 ms: 1.28x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                      |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                       |
| 2to3                     | 350 ms                                                       | 279 ms: 1.25x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.7 ms: 1.24x faster                                                      |
| sympy_expand             | 600 ms                                                       | 484 ms: 1.24x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 923 us: 1.24x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.45 sec: 1.23x faster                                                     |
| dulwich_log              | 81.1 ms                                                      | 66.5 ms: 1.22x faster                                                      |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                     |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                      |
| json                     | 5.86 ms                                                      | 5.08 ms: 1.15x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 96.2 ms: 1.15x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 81.3 ms: 1.13x faster                                                      |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.73 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                      |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.03x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                       |
| async_generators         | 421 ms                                                       | 433 ms: 1.03x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.26 ms: 1.06x slower                                                      |
| telco                    | 7.23 ms                                                      | 7.66 ms: 1.06x slower                                                      |
| mypy2                    | 933 ms                                                       | 1.01 sec: 1.08x slower                                                     |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                      |
| coverage                 | 63.3 ms                                                      | 81.2 ms: 1.28x slower                                                      |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 6.37 ms: 1.86x slower                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 1.48 sec: 232.88x slower                                                   |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                               |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.359x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.28x