# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 315 ms: 1.21x faster                                                            |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                          |
| html5lib       | 86.5 ms                                                               | 63.6 ms: 1.36x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 899 ms: 2.54x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.41x faster                                                            |
| async_tree_none         | 950 ms                                                                | 401 ms: 2.37x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 665 ms: 1.91x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.6 ms: 1.52x faster                                                           |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 28.4 ms: 1.13x faster                                                           |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                            |
| regex_effbot   | 4.25 ms                                                               | 3.95 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 271 us: 1.35x faster                                                            |
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                          |
| pickle_pure_python   | 529 us                                                                | 402 us: 1.32x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 84.1 ms: 1.18x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                            |
| json_dumps           | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 120 ms: 1.03x faster                                                            |
| json_loads           | 30.9 us                                                               | 36.0 us: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                                           |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                           |
| django_template | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 28.9 ms: 1.22x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 64.6 ms: 1.08x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.22x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.21x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 899 ms: 2.54x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.41x faster                                                            |
| async_tree_none          | 950 ms                                                                | 401 ms: 2.37x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.71 sec: 2.17x faster                                                          |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 665 ms: 1.91x faster                                                            |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                                           |
| richards_super           | 107 ms                                                                | 58.0 ms: 1.85x faster                                                           |
| richards                 | 91.7 ms                                                               | 52.4 ms: 1.75x faster                                                           |
| logging_silent           | 222 ns                                                                | 128 ns: 1.74x faster                                                            |
| raytrace                 | 573 ms                                                                | 331 ms: 1.73x faster                                                            |
| chaos                    | 121 ms                                                                | 70.6 ms: 1.71x faster                                                           |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                            |
| deepcopy_memo            | 61.7 us                                                               | 39.4 us: 1.57x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 82.6 ms: 1.55x faster                                                           |
| pylint                   | 485 ms                                                                | 314 ms: 1.55x faster                                                            |
| hexiom                   | 10.9 ms                                                               | 7.17 ms: 1.52x faster                                                           |
| float                    | 135 ms                                                                | 88.6 ms: 1.52x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 89.3 ms: 1.50x faster                                                           |
| deepcopy                 | 511 us                                                                | 346 us: 1.47x faster                                                            |
| comprehensions           | 33.1 us                                                               | 22.9 us: 1.45x faster                                                           |
| scimark_lu               | 227 ms                                                                | 157 ms: 1.44x faster                                                            |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.42x faster                                                            |
| pyflate                  | 795 ms                                                                | 575 ms: 1.38x faster                                                            |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 53.8 ms: 1.37x faster                                                           |
| html5lib                 | 86.5 ms                                                               | 63.6 ms: 1.36x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 271 us: 1.35x faster                                                            |
| logging_simple           | 9.78 us                                                               | 7.27 us: 1.34x faster                                                           |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                           |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                            |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                          |
| pickle_pure_python       | 529 us                                                                | 402 us: 1.32x faster                                                            |
| pycparser                | 1.69 sec                                                              | 1.30 sec: 1.30x faster                                                          |
| logging_format           | 10.6 us                                                               | 8.20 us: 1.29x faster                                                           |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                           |
| thrift                   | 1.26 ms                                                               | 987 us: 1.28x faster                                                            |
| django_template          | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                           |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.70 us: 1.24x faster                                                           |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.23x faster                                                            |
| genshi_text              | 35.2 ms                                                               | 28.9 ms: 1.22x faster                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 946 ms: 1.21x faster                                                            |
| 2to3                     | 381 ms                                                                | 315 ms: 1.21x faster                                                            |
| pprint_pformat           | 2.36 sec                                                              | 1.96 sec: 1.21x faster                                                          |
| xml_etree_process        | 99.5 ms                                                               | 84.1 ms: 1.18x faster                                                           |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                          |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                           |
| sympy_str                | 329 ms                                                                | 283 ms: 1.16x faster                                                            |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 28.4 ms: 1.13x faster                                                           |
| sympy_expand             | 543 ms                                                                | 486 ms: 1.12x faster                                                            |
| scimark_fft              | 500 ms                                                                | 450 ms: 1.11x faster                                                            |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                            |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.98 ms: 1.09x faster                                                           |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                            |
| genshi_xml               | 69.8 ms                                                               | 64.6 ms: 1.08x faster                                                           |
| regex_effbot             | 4.25 ms                                                               | 3.95 ms: 1.08x faster                                                           |
| fannkuch                 | 546 ms                                                                | 509 ms: 1.07x faster                                                            |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                            |
| json_dumps               | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                            |
| xml_etree_generate       | 123 ms                                                                | 120 ms: 1.03x faster                                                            |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                            |
| async_generators         | 452 ms                                                                | 475 ms: 1.05x slower                                                            |
| json                     | 5.88 ms                                                               | 6.34 ms: 1.08x slower                                                           |
| json_loads               | 30.9 us                                                               | 36.0 us: 1.17x slower                                                           |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                                           |
| coverage                 | 83.6 ms                                                               | 110 ms: 1.31x slower                                                            |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.91 ms: 1.66x slower                                                           |
| bench_mp_pool            | 14.5 ms                                                               | 2.21 sec: 151.74x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                                    |

Benchmark hidden because not significant (2): sqlite_synth, pidigits
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.34x