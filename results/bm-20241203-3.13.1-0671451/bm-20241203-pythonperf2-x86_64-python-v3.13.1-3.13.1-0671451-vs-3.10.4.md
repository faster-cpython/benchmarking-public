# Results vs. 3.10.4

- fork: python
- ref: v3.13.1
- machine: linux-x86_64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.19x faster                                         |
| chameleon      | 9.44 ms                                                      | 7.48 ms: 1.26x faster                                        |
| docutils       | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                       |
| html5lib       | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                        |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 836 ms: 1.91x faster                                         |
| async_tree_none         | 692 ms                                                       | 374 ms: 1.85x faster                                         |
| async_tree_memoization  | 819 ms                                                       | 454 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 604 ms: 1.55x faster                                         |
| Geometric mean          | (ref)                                                        | 1.77x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.6 ms: 1.51x faster                                        |
| float          | 111 ms                                                       | 79.7 ms: 1.39x faster                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                         |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                        |
| regex_dna      | 261 ms                                                       | 250 ms: 1.04x faster                                         |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                         |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.39x faster                                         |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.25 sec: 1.30x faster                                       |
| xml_etree_process    | 75.9 ms                                                      | 61.5 ms: 1.24x faster                                        |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                         |
| xml_etree_parse      | 160 ms                                                       | 149 ms: 1.07x faster                                         |
| xml_etree_generate   | 92.3 ms                                                      | 87.5 ms: 1.05x faster                                        |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                        |
| django_template | 50.2 ms                                                      | 36.3 ms: 1.38x faster                                        |
| genshi_text     | 31.4 ms                                                      | 27.3 ms: 1.15x faster                                        |
| genshi_xml      | 63.3 ms                                                      | 59.5 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                         |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 836 ms: 1.91x faster                                         |
| async_tree_none          | 692 ms                                                       | 374 ms: 1.85x faster                                         |
| chaos                    | 109 ms                                                       | 59.2 ms: 1.83x faster                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.83x faster                                         |
| async_tree_memoization   | 819 ms                                                       | 454 ms: 1.81x faster                                         |
| generators               | 57.3 ms                                                      | 32.8 ms: 1.75x faster                                        |
| logging_silent           | 167 ns                                                       | 96.2 ns: 1.74x faster                                        |
| scimark_lu               | 167 ms                                                       | 99.8 ms: 1.67x faster                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.37 ms: 1.64x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.8 ms: 1.63x faster                                        |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                         |
| crypto_pyaes             | 119 ms                                                       | 73.5 ms: 1.62x faster                                        |
| go                       | 262 ms                                                       | 162 ms: 1.61x faster                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 604 ms: 1.55x faster                                         |
| richards_super           | 90.6 ms                                                      | 58.9 ms: 1.54x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.52x faster                                        |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.51x faster                                        |
| nbody                    | 134 ms                                                       | 88.6 ms: 1.51x faster                                        |
| pyflate                  | 733 ms                                                       | 495 ms: 1.48x faster                                         |
| hexiom                   | 9.42 ms                                                      | 6.38 ms: 1.48x faster                                        |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                         |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                        |
| spectral_norm            | 139 ms                                                       | 96.2 ms: 1.45x faster                                        |
| richards                 | 75.1 ms                                                      | 52.0 ms: 1.44x faster                                        |
| scimark_sor              | 180 ms                                                       | 125 ms: 1.44x faster                                         |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                        |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.39x faster                                         |
| float                    | 111 ms                                                       | 79.7 ms: 1.39x faster                                        |
| django_template          | 50.2 ms                                                      | 36.3 ms: 1.38x faster                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                       |
| logging_format           | 9.64 us                                                      | 7.22 us: 1.34x faster                                        |
| logging_simple           | 8.88 us                                                      | 6.65 us: 1.33x faster                                        |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                         |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                        |
| nqueens                  | 115 ms                                                       | 87.4 ms: 1.31x faster                                        |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                         |
| fannkuch                 | 483 ms                                                       | 370 ms: 1.30x faster                                         |
| tomli_loads              | 2.92 sec                                                     | 2.25 sec: 1.30x faster                                       |
| thrift                   | 1.18 ms                                                      | 908 us: 1.29x faster                                         |
| html5lib                 | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                         |
| chameleon                | 9.44 ms                                                      | 7.48 ms: 1.26x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 835 ms: 1.26x faster                                         |
| bench_mp_pool            | 6.37 ms                                                      | 5.08 ms: 1.25x faster                                        |
| deepcopy_memo            | 49.8 us                                                      | 39.8 us: 1.25x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.25x faster                                       |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                        |
| xml_etree_process        | 75.9 ms                                                      | 61.5 ms: 1.24x faster                                        |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.24x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 930 us: 1.23x faster                                         |
| pathlib                  | 21.4 ms                                                      | 17.6 ms: 1.22x faster                                        |
| dulwich_log              | 81.1 ms                                                      | 66.8 ms: 1.21x faster                                        |
| docutils                 | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                         |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                       |
| sympy_str                | 360 ms                                                       | 299 ms: 1.20x faster                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                        |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                        |
| 2to3                     | 350 ms                                                       | 293 ms: 1.19x faster                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 59.4 ms: 1.18x faster                                        |
| sympy_expand             | 600 ms                                                       | 512 ms: 1.17x faster                                         |
| gunicorn                 | 1.16 ms                                                      | 990 us: 1.17x faster                                         |
| deepcopy                 | 468 us                                                       | 401 us: 1.17x faster                                         |
| genshi_text              | 31.4 ms                                                      | 27.3 ms: 1.15x faster                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.58 us: 1.12x faster                                        |
| scimark_fft              | 361 ms                                                       | 326 ms: 1.11x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                         |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| xml_etree_parse          | 160 ms                                                       | 149 ms: 1.07x faster                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.76 ms: 1.07x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 59.5 ms: 1.06x faster                                        |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                         |
| json                     | 5.86 ms                                                      | 5.54 ms: 1.06x faster                                        |
| xml_etree_generate       | 92.3 ms                                                      | 87.5 ms: 1.05x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                        |
| regex_dna                | 261 ms                                                       | 250 ms: 1.04x faster                                         |
| sqlite_synth             | 2.99 us                                                      | 2.93 us: 1.02x faster                                        |
| async_generators         | 421 ms                                                       | 445 ms: 1.06x slower                                         |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                        |
| telco                    | 7.23 ms                                                      | 8.93 ms: 1.23x slower                                        |
| coverage                 | 63.3 ms                                                      | 82.7 ms: 1.31x slower                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                        |
| gc_traversal             | 3.42 ms                                                      | 4.94 ms: 1.45x slower                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.24x