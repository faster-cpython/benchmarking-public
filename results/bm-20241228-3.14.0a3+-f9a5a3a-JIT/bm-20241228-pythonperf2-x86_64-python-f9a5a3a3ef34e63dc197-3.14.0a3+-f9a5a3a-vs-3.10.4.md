# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.20x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.5 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 661 ms: 2.42x faster                                                         |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 366 ms: 2.24x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 527 ms: 1.78x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.18x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 73.0 ms: 1.52x faster                                                        |
| nbody          | 134 ms                                                       | 92.6 ms: 1.45x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                        |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.23 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 198 us: 1.57x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.21x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 93.7 ms: 1.18x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.61 ms: 1.53x faster                                                        |
| django_template | 50.2 ms                                                      | 38.5 ms: 1.31x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 178 us: 3.01x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 661 ms: 2.42x faster                                                         |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 366 ms: 2.24x faster                                                         |
| go                       | 262 ms                                                       | 139 ms: 1.88x faster                                                         |
| scimark_sor              | 180 ms                                                       | 98.6 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 527 ms: 1.78x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.8 ms: 1.72x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.5 ms: 1.72x faster                                                        |
| pyflate                  | 733 ms                                                       | 432 ms: 1.70x faster                                                         |
| pylint                   | 566 ms                                                       | 338 ms: 1.68x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 30.1 us: 1.65x faster                                                        |
| logging_silent           | 167 ns                                                       | 101 ns: 1.65x faster                                                         |
| richards                 | 75.1 ms                                                      | 46.0 ms: 1.63x faster                                                        |
| chaos                    | 109 ms                                                       | 67.5 ms: 1.61x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 75.0 ms: 1.59x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.58x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 198 us: 1.57x faster                                                         |
| deepcopy                 | 468 us                                                       | 306 us: 1.53x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.61 ms: 1.53x faster                                                        |
| float                    | 111 ms                                                       | 73.0 ms: 1.52x faster                                                        |
| spectral_norm            | 139 ms                                                       | 92.5 ms: 1.50x faster                                                        |
| raytrace                 | 489 ms                                                       | 329 ms: 1.49x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.48x faster                                                        |
| nbody                    | 134 ms                                                       | 92.6 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| generators               | 57.3 ms                                                      | 40.6 ms: 1.41x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.4 us: 1.38x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                                        |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 69.5 ms: 1.36x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 778 ms: 1.35x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.33x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.24 us: 1.33x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                        |
| thrift                   | 1.18 ms                                                      | 896 us: 1.31x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                       |
| django_template          | 50.2 ms                                                      | 38.5 ms: 1.31x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.25 ms: 1.30x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                         |
| fannkuch                 | 483 ms                                                       | 379 ms: 1.27x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.2 ms: 1.25x faster                                                        |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.21x faster                                                        |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                                         |
| 2to3                     | 350 ms                                                       | 293 ms: 1.20x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 68.3 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 93.7 ms: 1.18x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| sympy_str                | 360 ms                                                       | 308 ms: 1.17x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 24.2 ms: 1.16x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.15x faster                                                       |
| nqueens                  | 115 ms                                                       | 100.0 ms: 1.15x faster                                                       |
| json                     | 5.86 ms                                                      | 5.11 ms: 1.15x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 126 ms: 1.15x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| sympy_expand             | 600 ms                                                       | 526 ms: 1.14x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 1.01 ms: 1.13x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 62.5 ms: 1.12x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.83 ms: 1.05x faster                                                        |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.04x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.23 ms: 1.05x slower                                                        |
| async_generators         | 421 ms                                                       | 457 ms: 1.09x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.90 ms: 1.09x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.04 sec: 1.12x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.64 ms: 1.50x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.30 ms: 1.85x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.15 sec: 180.21x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.31x