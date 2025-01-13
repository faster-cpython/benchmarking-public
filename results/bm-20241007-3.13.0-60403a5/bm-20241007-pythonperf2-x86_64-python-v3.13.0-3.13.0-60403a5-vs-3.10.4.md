# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.20x faster                                         |
| chameleon      | 9.44 ms                                                      | 7.55 ms: 1.25x faster                                        |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                       |
| html5lib       | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                        |
| tornado_http   | 157 ms                                                       | 121 ms: 1.30x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 843 ms: 1.90x faster                                         |
| async_tree_none         | 692 ms                                                       | 376 ms: 1.84x faster                                         |
| async_tree_memoization  | 819 ms                                                       | 453 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 604 ms: 1.55x faster                                         |
| Geometric mean          | (ref)                                                        | 1.77x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.3 ms: 1.50x faster                                        |
| float          | 111 ms                                                       | 81.3 ms: 1.37x faster                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                         |
| regex_dna      | 261 ms                                                       | 247 ms: 1.06x faster                                         |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                        |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                         |
| pickle_pure_python   | 455 us                                                       | 323 us: 1.41x faster                                         |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                        |
| xml_etree_process    | 75.9 ms                                                      | 61.2 ms: 1.24x faster                                        |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.46 sec: 1.18x faster                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| xml_etree_generate   | 92.3 ms                                                      | 86.5 ms: 1.07x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                         |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                        |
| python_startup         | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                        |
| django_template | 50.2 ms                                                      | 36.4 ms: 1.38x faster                                        |
| genshi_text     | 31.4 ms                                                      | 26.2 ms: 1.20x faster                                        |
| genshi_xml      | 63.3 ms                                                      | 57.1 ms: 1.11x faster                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                         |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.20x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 843 ms: 1.90x faster                                         |
| async_tree_none          | 692 ms                                                       | 376 ms: 1.84x faster                                         |
| async_tree_memoization   | 819 ms                                                       | 453 ms: 1.81x faster                                         |
| chaos                    | 109 ms                                                       | 60.2 ms: 1.80x faster                                        |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                         |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                        |
| generators               | 57.3 ms                                                      | 33.6 ms: 1.70x faster                                        |
| scimark_lu               | 167 ms                                                       | 98.7 ms: 1.69x faster                                        |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                         |
| crypto_pyaes             | 119 ms                                                       | 73.3 ms: 1.63x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.1 ms: 1.62x faster                                        |
| go                       | 262 ms                                                       | 162 ms: 1.61x faster                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                        |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 604 ms: 1.55x faster                                         |
| richards_super           | 90.6 ms                                                      | 59.6 ms: 1.52x faster                                        |
| nbody                    | 134 ms                                                       | 89.3 ms: 1.50x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                        |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.46x faster                                         |
| pyflate                  | 733 ms                                                       | 503 ms: 1.46x faster                                         |
| hexiom                   | 9.42 ms                                                      | 6.55 ms: 1.44x faster                                        |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                         |
| spectral_norm            | 139 ms                                                       | 97.0 ms: 1.43x faster                                        |
| richards                 | 75.1 ms                                                      | 52.9 ms: 1.42x faster                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                        |
| pickle_pure_python       | 455 us                                                       | 323 us: 1.41x faster                                         |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                        |
| logging_format           | 9.64 us                                                      | 6.94 us: 1.39x faster                                        |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                        |
| django_template          | 50.2 ms                                                      | 36.4 ms: 1.38x faster                                        |
| float                    | 111 ms                                                       | 81.3 ms: 1.37x faster                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                       |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                         |
| fannkuch                 | 483 ms                                                       | 363 ms: 1.33x faster                                         |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                        |
| thrift                   | 1.18 ms                                                      | 901 us: 1.31x faster                                         |
| tornado_http             | 157 ms                                                       | 121 ms: 1.30x faster                                         |
| deepcopy_memo            | 49.8 us                                                      | 38.6 us: 1.29x faster                                        |
| html5lib                 | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 148 ms: 1.28x faster                                         |
| nqueens                  | 115 ms                                                       | 90.7 ms: 1.27x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.25x faster                                       |
| chameleon                | 9.44 ms                                                      | 7.55 ms: 1.25x faster                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 843 ms: 1.25x faster                                         |
| bench_mp_pool            | 6.37 ms                                                      | 5.12 ms: 1.24x faster                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                        |
| xml_etree_process        | 75.9 ms                                                      | 61.2 ms: 1.24x faster                                        |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                        |
| pathlib                  | 21.4 ms                                                      | 17.5 ms: 1.22x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 942 us: 1.21x faster                                         |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                       |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                         |
| genshi_text              | 31.4 ms                                                      | 26.2 ms: 1.20x faster                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.20x faster                                        |
| 2to3                     | 350 ms                                                       | 293 ms: 1.20x faster                                         |
| deepcopy                 | 468 us                                                       | 392 us: 1.19x faster                                         |
| dulwich_log              | 81.1 ms                                                      | 68.2 ms: 1.19x faster                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.46 sec: 1.18x faster                                       |
| mdp                      | 3.01 sec                                                     | 2.54 sec: 1.18x faster                                       |
| sympy_expand             | 600 ms                                                       | 509 ms: 1.18x faster                                         |
| gunicorn                 | 1.16 ms                                                      | 992 us: 1.17x faster                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.54 us: 1.13x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 57.1 ms: 1.11x faster                                        |
| scimark_fft              | 361 ms                                                       | 328 ms: 1.10x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                         |
| xml_etree_generate       | 92.3 ms                                                      | 86.5 ms: 1.07x faster                                        |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.77 ms: 1.06x faster                                        |
| regex_dna                | 261 ms                                                       | 247 ms: 1.06x faster                                         |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                        |
| json                     | 5.86 ms                                                      | 5.69 ms: 1.03x faster                                        |
| sqlite_synth             | 2.99 us                                                      | 2.91 us: 1.03x faster                                        |
| async_generators         | 421 ms                                                       | 457 ms: 1.08x slower                                         |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                        |
| telco                    | 7.23 ms                                                      | 8.79 ms: 1.22x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                        |
| coverage                 | 63.3 ms                                                      | 80.0 ms: 1.26x slower                                        |
| python_startup           | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                        |
| gc_traversal             | 3.42 ms                                                      | 4.74 ms: 1.39x slower                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.24x