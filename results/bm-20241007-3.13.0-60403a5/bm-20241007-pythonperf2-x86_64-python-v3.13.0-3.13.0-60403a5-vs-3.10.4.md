# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.20x faster                                         |
| chameleon      | 9.44 ms                                                      | 7.49 ms: 1.26x faster                                        |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.22x faster                                       |
| html5lib       | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                        |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                        | 1.26x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 832 ms: 1.92x faster                                         |
| async_tree_none         | 692 ms                                                       | 370 ms: 1.87x faster                                         |
| async_tree_memoization  | 819 ms                                                       | 447 ms: 1.83x faster                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 596 ms: 1.57x faster                                         |
| Geometric mean          | (ref)                                                        | 1.79x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 92.1 ms: 1.46x faster                                        |
| float          | 111 ms                                                       | 81.6 ms: 1.36x faster                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                         |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                         |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                        |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                         |
| pickle_pure_python   | 455 us                                                       | 322 us: 1.41x faster                                         |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                        |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 99.8 ms: 1.11x faster                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                        |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                        |
| python_startup         | 11.5 ms                                                      | 15.6 ms: 1.36x slower                                        |
| Geometric mean         | (ref)                                                        | 1.29x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                        |
| django_template | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                        |
| genshi_text     | 31.4 ms                                                      | 27.2 ms: 1.16x faster                                        |
| genshi_xml      | 63.3 ms                                                      | 58.0 ms: 1.09x faster                                        |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.06x faster                                         |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 832 ms: 1.92x faster                                         |
| async_tree_none          | 692 ms                                                       | 370 ms: 1.87x faster                                         |
| async_tree_memoization   | 819 ms                                                       | 447 ms: 1.83x faster                                         |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                         |
| chaos                    | 109 ms                                                       | 60.6 ms: 1.79x faster                                        |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                        |
| scimark_lu               | 167 ms                                                       | 97.4 ms: 1.71x faster                                        |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.2 ms: 1.65x faster                                        |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.37 ms: 1.64x faster                                        |
| crypto_pyaes             | 119 ms                                                       | 73.5 ms: 1.62x faster                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 596 ms: 1.57x faster                                         |
| go                       | 262 ms                                                       | 167 ms: 1.57x faster                                         |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.76 ms: 1.52x faster                                        |
| richards_super           | 90.6 ms                                                      | 60.2 ms: 1.51x faster                                        |
| pyflate                  | 733 ms                                                       | 493 ms: 1.49x faster                                         |
| nbody                    | 134 ms                                                       | 92.1 ms: 1.46x faster                                        |
| hexiom                   | 9.42 ms                                                      | 6.47 ms: 1.45x faster                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                         |
| scimark_sor              | 180 ms                                                       | 125 ms: 1.44x faster                                         |
| richards                 | 75.1 ms                                                      | 52.5 ms: 1.43x faster                                        |
| spectral_norm            | 139 ms                                                       | 97.4 ms: 1.43x faster                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                        |
| logging_simple           | 8.88 us                                                      | 6.28 us: 1.41x faster                                        |
| pickle_pure_python       | 455 us                                                       | 322 us: 1.41x faster                                         |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.41x faster                                        |
| logging_format           | 9.64 us                                                      | 6.95 us: 1.39x faster                                        |
| float                    | 111 ms                                                       | 81.6 ms: 1.36x faster                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                        |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                         |
| bench_mp_pool            | 6.37 ms                                                      | 4.82 ms: 1.32x faster                                        |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                         |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                       |
| html5lib                 | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                        |
| django_template          | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                        |
| thrift                   | 1.18 ms                                                      | 918 us: 1.28x faster                                         |
| deepcopy_memo            | 49.8 us                                                      | 38.9 us: 1.28x faster                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 148 ms: 1.28x faster                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                       |
| chameleon                | 9.44 ms                                                      | 7.49 ms: 1.26x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 835 ms: 1.26x faster                                         |
| fannkuch                 | 483 ms                                                       | 384 ms: 1.26x faster                                         |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.25x faster                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                        |
| nqueens                  | 115 ms                                                       | 92.3 ms: 1.25x faster                                        |
| dulwich_log              | 81.1 ms                                                      | 65.5 ms: 1.24x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 929 us: 1.23x faster                                         |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                        |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                        |
| docutils                 | 3.41 sec                                                     | 2.81 sec: 1.22x faster                                       |
| sympy_str                | 360 ms                                                       | 297 ms: 1.21x faster                                         |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.21 ms: 1.21x faster                                        |
| deepcopy                 | 468 us                                                       | 388 us: 1.20x faster                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                       |
| 2to3                     | 350 ms                                                       | 293 ms: 1.20x faster                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 58.7 ms: 1.20x faster                                        |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                       |
| sympy_expand             | 600 ms                                                       | 506 ms: 1.18x faster                                         |
| async_generators         | 421 ms                                                       | 364 ms: 1.16x faster                                         |
| genshi_text              | 31.4 ms                                                      | 27.2 ms: 1.16x faster                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.49 us: 1.15x faster                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 99.8 ms: 1.11x faster                                        |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                         |
| genshi_xml               | 63.3 ms                                                      | 58.0 ms: 1.09x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                         |
| json                     | 5.86 ms                                                      | 5.62 ms: 1.04x faster                                        |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                         |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                        |
| telco                    | 7.23 ms                                                      | 8.77 ms: 1.21x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                        |
| gc_traversal             | 3.42 ms                                                      | 4.48 ms: 1.31x slower                                        |
| coverage                 | 63.3 ms                                                      | 84.5 ms: 1.34x slower                                        |
| python_startup           | 11.5 ms                                                      | 15.6 ms: 1.36x slower                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.65 ms: 1.50x slower                                        |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                 |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.290x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.25x