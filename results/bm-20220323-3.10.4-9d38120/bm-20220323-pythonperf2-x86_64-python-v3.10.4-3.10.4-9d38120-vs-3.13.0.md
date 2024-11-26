# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.224x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 0.82x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 350 ms: 1.20x slower                                         |
| chameleon      | 7.49 ms                                                      | 9.44 ms: 1.26x slower                                        |
| docutils       | 2.81 sec                                                     | 3.41 sec: 1.22x slower                                       |
| html5lib       | 72.9 ms                                                      | 94.6 ms: 1.30x slower                                        |
| tornado_http   | 119 ms                                                       | 157 ms: 1.32x slower                                         |
| Geometric mean | (ref)                                                        | 1.26x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_websockets      | 395 ms                                                       | 390 ms: 1.01x faster                                         |
| async_generators        | 364 ms                                                       | 421 ms: 1.16x slower                                         |
| coroutines              | 21.6 ms                                                      | 30.3 ms: 1.41x slower                                        |
| async_tree_cpu_io_mixed | 596 ms                                                       | 936 ms: 1.57x slower                                         |
| async_tree_memoization  | 447 ms                                                       | 819 ms: 1.83x slower                                         |
| async_tree_none         | 370 ms                                                       | 692 ms: 1.87x slower                                         |
| async_tree_io           | 832 ms                                                       | 1.60 sec: 1.92x slower                                       |
| Geometric mean          | (ref)                                                        | 1.49x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 271 ms: 1.07x slower                                         |
| float          | 81.6 ms                                                      | 111 ms: 1.36x slower                                         |
| nbody          | 92.1 ms                                                      | 134 ms: 1.46x slower                                         |
| Geometric mean | (ref)                                                        | 1.29x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.09 ms: 1.14x faster                                        |
| regex_v8       | 24.9 ms                                                      | 27.2 ms: 1.09x slower                                        |
| regex_dna      | 238 ms                                                       | 261 ms: 1.10x slower                                         |
| regex_compile  | 143 ms                                                       | 190 ms: 1.33x slower                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_generate   | 85.2 ms                                                      | 92.3 ms: 1.08x slower                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 110 ms: 1.11x slower                                         |
| xml_etree_parse      | 144 ms                                                       | 160 ms: 1.11x slower                                         |
| tomli_loads          | 2.43 sec                                                     | 2.92 sec: 1.20x slower                                       |
| json_loads           | 24.7 us                                                      | 30.3 us: 1.23x slower                                        |
| xml_etree_process    | 60.7 ms                                                      | 75.9 ms: 1.25x slower                                        |
| json_dumps           | 10.8 ms                                                      | 14.5 ms: 1.34x slower                                        |
| pickle_pure_python   | 322 us                                                       | 455 us: 1.41x slower                                         |
| unpickle_pure_python | 216 us                                                       | 312 us: 1.44x slower                                         |
| Geometric mean       | (ref)                                                        | 1.24x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 11.5 ms: 1.36x faster                                        |
| python_startup_no_site | 8.93 ms                                                      | 7.33 ms: 1.22x faster                                        |
| Geometric mean         | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 63.3 ms: 1.09x slower                                        |
| genshi_text     | 27.2 ms                                                      | 31.4 ms: 1.16x slower                                        |
| django_template | 38.9 ms                                                      | 50.2 ms: 1.29x slower                                        |
| mako            | 10.3 ms                                                      | 14.7 ms: 1.42x slower                                        |
| Geometric mean  | (ref)                                                        | 1.23x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles         | 2.65 ms                                                      | 1.76 ms: 1.50x faster                                        |
| python_startup           | 15.6 ms                                                      | 11.5 ms: 1.36x faster                                        |
| coverage                 | 84.5 ms                                                      | 63.3 ms: 1.34x faster                                        |
| gc_traversal             | 4.48 ms                                                      | 3.42 ms: 1.31x faster                                        |
| python_startup_no_site   | 8.93 ms                                                      | 7.33 ms: 1.22x faster                                        |
| telco                    | 8.77 ms                                                      | 7.23 ms: 1.21x faster                                        |
| regex_effbot             | 3.51 ms                                                      | 3.09 ms: 1.14x faster                                        |
| asyncio_websockets       | 395 ms                                                       | 390 ms: 1.01x faster                                         |
| json                     | 5.62 ms                                                      | 5.86 ms: 1.04x slower                                        |
| meteor_contest           | 130 ms                                                       | 138 ms: 1.06x slower                                         |
| pidigits                 | 252 ms                                                       | 271 ms: 1.07x slower                                         |
| xml_etree_generate       | 85.2 ms                                                      | 92.3 ms: 1.08x slower                                        |
| regex_v8                 | 24.9 ms                                                      | 27.2 ms: 1.09x slower                                        |
| genshi_xml               | 58.0 ms                                                      | 63.3 ms: 1.09x slower                                        |
| regex_dna                | 238 ms                                                       | 261 ms: 1.10x slower                                         |
| xml_etree_iterparse      | 99.8 ms                                                      | 110 ms: 1.11x slower                                         |
| xml_etree_parse          | 144 ms                                                       | 160 ms: 1.11x slower                                         |
| deepcopy_reduce          | 3.49 us                                                      | 4.01 us: 1.15x slower                                        |
| genshi_text              | 27.2 ms                                                      | 31.4 ms: 1.16x slower                                        |
| async_generators         | 364 ms                                                       | 421 ms: 1.16x slower                                         |
| sympy_expand             | 506 ms                                                       | 600 ms: 1.18x slower                                         |
| mdp                      | 2.53 sec                                                     | 3.01 sec: 1.19x slower                                       |
| sqlglot_optimize         | 58.7 ms                                                      | 70.1 ms: 1.20x slower                                        |
| 2to3                     | 293 ms                                                       | 350 ms: 1.20x slower                                         |
| tomli_loads              | 2.43 sec                                                     | 2.92 sec: 1.20x slower                                       |
| sympy_integrate          | 23.4 ms                                                      | 28.2 ms: 1.20x slower                                        |
| deepcopy                 | 388 us                                                       | 468 us: 1.20x slower                                         |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 5.08 ms: 1.21x slower                                        |
| sqlglot_normalize        | 119 ms                                                       | 144 ms: 1.21x slower                                         |
| scimark_fft              | 298 ms                                                       | 361 ms: 1.21x slower                                         |
| sympy_str                | 297 ms                                                       | 360 ms: 1.21x slower                                         |
| docutils                 | 2.81 sec                                                     | 3.41 sec: 1.22x slower                                       |
| pathlib                  | 17.4 ms                                                      | 21.4 ms: 1.23x slower                                        |
| json_loads               | 24.7 us                                                      | 30.3 us: 1.23x slower                                        |
| bench_thread_pool        | 929 us                                                       | 1.14 ms: 1.23x slower                                        |
| dulwich_log              | 65.5 ms                                                      | 81.1 ms: 1.24x slower                                        |
| nqueens                  | 92.3 ms                                                      | 115 ms: 1.25x slower                                         |
| xml_etree_process        | 60.7 ms                                                      | 75.9 ms: 1.25x slower                                        |
| sqlalchemy_imperative    | 18.1 ms                                                      | 22.7 ms: 1.25x slower                                        |
| sympy_sum                | 154 ms                                                       | 193 ms: 1.25x slower                                         |
| fannkuch                 | 384 ms                                                       | 483 ms: 1.26x slower                                         |
| pprint_safe_repr         | 835 ms                                                       | 1.05 sec: 1.26x slower                                       |
| chameleon                | 7.49 ms                                                      | 9.44 ms: 1.26x slower                                        |
| pprint_pformat           | 1.70 sec                                                     | 2.15 sec: 1.27x slower                                       |
| sqlalchemy_declarative   | 148 ms                                                       | 190 ms: 1.28x slower                                         |
| deepcopy_memo            | 38.9 us                                                      | 49.8 us: 1.28x slower                                        |
| thrift                   | 918 us                                                       | 1.18 ms: 1.28x slower                                        |
| django_template          | 38.9 ms                                                      | 50.2 ms: 1.29x slower                                        |
| html5lib                 | 72.9 ms                                                      | 94.6 ms: 1.30x slower                                        |
| pycparser                | 1.28 sec                                                     | 1.67 sec: 1.31x slower                                       |
| tornado_http             | 119 ms                                                       | 157 ms: 1.32x slower                                         |
| bench_mp_pool            | 4.82 ms                                                      | 6.37 ms: 1.32x slower                                        |
| regex_compile            | 143 ms                                                       | 190 ms: 1.33x slower                                         |
| json_dumps               | 10.8 ms                                                      | 14.5 ms: 1.34x slower                                        |
| float                    | 81.6 ms                                                      | 111 ms: 1.36x slower                                         |
| logging_format           | 6.95 us                                                      | 9.64 us: 1.39x slower                                        |
| coroutines               | 21.6 ms                                                      | 30.3 ms: 1.41x slower                                        |
| pickle_pure_python       | 322 us                                                       | 455 us: 1.41x slower                                         |
| logging_simple           | 6.28 us                                                      | 8.88 us: 1.41x slower                                        |
| mako                     | 10.3 ms                                                      | 14.7 ms: 1.42x slower                                        |
| spectral_norm            | 97.4 ms                                                      | 139 ms: 1.43x slower                                         |
| richards                 | 52.5 ms                                                      | 75.1 ms: 1.43x slower                                        |
| scimark_sor              | 125 ms                                                       | 180 ms: 1.44x slower                                         |
| unpickle_pure_python     | 216 us                                                       | 312 us: 1.44x slower                                         |
| hexiom                   | 6.47 ms                                                      | 9.42 ms: 1.45x slower                                        |
| nbody                    | 92.1 ms                                                      | 134 ms: 1.46x slower                                         |
| pyflate                  | 493 ms                                                       | 733 ms: 1.49x slower                                         |
| richards_super           | 60.2 ms                                                      | 90.6 ms: 1.51x slower                                        |
| sqlglot_transpile        | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                        |
| comprehensions           | 17.3 us                                                      | 26.7 us: 1.54x slower                                        |
| go                       | 167 ms                                                       | 262 ms: 1.57x slower                                         |
| async_tree_cpu_io_mixed  | 596 ms                                                       | 936 ms: 1.57x slower                                         |
| crypto_pyaes             | 73.5 ms                                                      | 119 ms: 1.62x slower                                         |
| sqlglot_parse            | 1.37 ms                                                      | 2.24 ms: 1.64x slower                                        |
| pylint                   | 345 ms                                                       | 566 ms: 1.64x slower                                         |
| scimark_monte_carlo      | 65.2 ms                                                      | 107 ms: 1.65x slower                                         |
| generators               | 33.9 ms                                                      | 57.3 ms: 1.69x slower                                        |
| scimark_lu               | 97.4 ms                                                      | 167 ms: 1.71x slower                                         |
| logging_silent           | 97.5 ns                                                      | 167 ns: 1.72x slower                                         |
| chaos                    | 60.6 ms                                                      | 109 ms: 1.79x slower                                         |
| raytrace                 | 267 ms                                                       | 489 ms: 1.83x slower                                         |
| async_tree_memoization   | 447 ms                                                       | 819 ms: 1.83x slower                                         |
| async_tree_none          | 370 ms                                                       | 692 ms: 1.87x slower                                         |
| async_tree_io            | 832 ms                                                       | 1.60 sec: 1.92x slower                                       |
| deltablue                | 3.38 ms                                                      | 7.50 ms: 2.22x slower                                        |
| typing_runtime_protocols | 176 us                                                       | 537 us: 3.06x slower                                         |
| Geometric mean           | (ref)                                                        | 1.29x slower                                                 |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.224x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 0.82x