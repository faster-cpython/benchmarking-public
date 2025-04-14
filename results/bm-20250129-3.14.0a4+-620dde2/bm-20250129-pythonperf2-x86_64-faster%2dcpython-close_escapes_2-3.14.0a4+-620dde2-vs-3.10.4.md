# Results vs. 3.10.4

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                              |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                            |
| html5lib       | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                             |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 645 ms: 2.48x faster                                                              |
| async_tree_none         | 692 ms                                                       | 287 ms: 2.41x faster                                                              |
| async_tree_memoization  | 819 ms                                                       | 347 ms: 2.36x faster                                                              |
| async_tree_cpu_io_mixed | 936 ms                                                       | 515 ms: 1.82x faster                                                              |
| Geometric mean          | (ref)                                                        | 2.25x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.3 ms: 1.60x faster                                                             |
| nbody          | 134 ms                                                       | 89.3 ms: 1.50x faster                                                             |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.39x faster                                                              |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                              |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                             |
| regex_effbot   | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                              |
| tomli_loads          | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                            |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                              |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                             |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                             |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                              |
| xml_etree_iterparse  | 110 ms                                                       | 96.4 ms: 1.15x faster                                                             |
| json_loads           | 30.3 us                                                      | 26.8 us: 1.13x faster                                                             |
| xml_etree_generate   | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                             |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                             |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                             |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                             |
| genshi_text     | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                             |
| genshi_xml      | 63.3 ms                                                      | 52.6 ms: 1.20x faster                                                             |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                              |
| async_tree_io            | 1.60 sec                                                     | 645 ms: 2.48x faster                                                              |
| async_tree_none          | 692 ms                                                       | 287 ms: 2.41x faster                                                              |
| async_tree_memoization   | 819 ms                                                       | 347 ms: 2.36x faster                                                              |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.28x faster                                                             |
| go                       | 262 ms                                                       | 128 ms: 2.05x faster                                                              |
| generators               | 57.3 ms                                                      | 28.3 ms: 2.03x faster                                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 515 ms: 1.82x faster                                                              |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                              |
| chaos                    | 109 ms                                                       | 60.5 ms: 1.80x faster                                                             |
| pylint                   | 566 ms                                                       | 315 ms: 1.79x faster                                                              |
| richards_super           | 90.6 ms                                                      | 51.2 ms: 1.77x faster                                                             |
| scimark_lu               | 167 ms                                                       | 95.9 ms: 1.74x faster                                                             |
| logging_silent           | 167 ns                                                       | 96.6 ns: 1.73x faster                                                             |
| scimark_monte_carlo      | 107 ms                                                       | 63.5 ms: 1.69x faster                                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.68x faster                                                             |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.68x faster                                                              |
| spectral_norm            | 139 ms                                                       | 83.6 ms: 1.66x faster                                                             |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                              |
| richards                 | 75.1 ms                                                      | 45.7 ms: 1.64x faster                                                             |
| deepcopy_memo            | 49.8 us                                                      | 30.7 us: 1.62x faster                                                             |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                              |
| float                    | 111 ms                                                       | 69.3 ms: 1.60x faster                                                             |
| crypto_pyaes             | 119 ms                                                       | 74.4 ms: 1.60x faster                                                             |
| sqlglot_transpile        | 2.68 ms                                                      | 1.72 ms: 1.56x faster                                                             |
| hexiom                   | 9.42 ms                                                      | 6.06 ms: 1.55x faster                                                             |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                             |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                              |
| nbody                    | 134 ms                                                       | 89.3 ms: 1.50x faster                                                             |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                             |
| logging_simple           | 8.88 us                                                      | 6.17 us: 1.44x faster                                                             |
| tomli_loads              | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                             |
| logging_format           | 9.64 us                                                      | 6.89 us: 1.40x faster                                                             |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                              |
| regex_compile            | 190 ms                                                       | 136 ms: 1.39x faster                                                              |
| django_template          | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                             |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.39x faster                                                            |
| thrift                   | 1.18 ms                                                      | 848 us: 1.39x faster                                                              |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                             |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                             |
| genshi_text              | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                             |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                            |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                              |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.32x faster                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 799 ms: 1.31x faster                                                              |
| nqueens                  | 115 ms                                                       | 88.7 ms: 1.30x faster                                                             |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                             |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                             |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                              |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                             |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                              |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 923 us: 1.24x faster                                                              |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                              |
| dulwich_log              | 81.1 ms                                                      | 66.4 ms: 1.22x faster                                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                             |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.21x faster                                                              |
| genshi_xml               | 63.3 ms                                                      | 52.6 ms: 1.20x faster                                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                             |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                            |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                              |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                              |
| xml_etree_iterparse      | 110 ms                                                       | 96.4 ms: 1.15x faster                                                             |
| json_loads               | 30.3 us                                                      | 26.8 us: 1.13x faster                                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.55 ms: 1.12x faster                                                             |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                             |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                              |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                              |
| json                     | 5.86 ms                                                      | 5.53 ms: 1.06x faster                                                             |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                             |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                             |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                              |
| async_generators         | 421 ms                                                       | 418 ms: 1.01x faster                                                              |
| regex_effbot             | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                                             |
| telco                    | 7.23 ms                                                      | 7.96 ms: 1.10x slower                                                             |
| coverage                 | 63.3 ms                                                      | 76.6 ms: 1.21x slower                                                             |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                             |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                             |
| create_gc_cycles         | 1.76 ms                                                      | 2.81 ms: 1.60x slower                                                             |
| gc_traversal             | 3.42 ms                                                      | 6.59 ms: 1.93x slower                                                             |
| bench_mp_pool            | 6.37 ms                                                      | 1.27 sec: 199.57x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                      |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-620dde2/bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x