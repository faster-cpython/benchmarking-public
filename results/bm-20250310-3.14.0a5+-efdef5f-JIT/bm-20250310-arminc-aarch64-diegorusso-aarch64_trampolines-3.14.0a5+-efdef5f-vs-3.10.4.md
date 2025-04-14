# Results vs. 3.10.4

- fork: diegorusso
- ref: aarch64_trampolines
- machine: linux-aarch64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.301x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                        |
| docutils       | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                                      |
| html5lib       | 86.5 ms                                                               | 61.9 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 885 ms: 2.58x faster                                                        |
| async_tree_none         | 950 ms                                                                | 381 ms: 2.49x faster                                                        |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.41x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 657 ms: 1.94x faster                                                        |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.9 ms: 1.63x faster                                                       |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                        |
| regex_v8       | 32.2 ms                                                               | 28.2 ms: 1.14x faster                                                       |
| regex_effbot   | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                       |
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                      |
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                                        |
| xml_etree_process    | 99.5 ms                                                               | 76.6 ms: 1.30x faster                                                       |
| unpickle_pure_python | 366 us                                                                | 282 us: 1.30x faster                                                        |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                       |
| xml_etree_parse      | 212 ms                                                                | 177 ms: 1.20x faster                                                        |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.15x faster                                                        |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                        |
| json_loads           | 30.9 us                                                               | 34.6 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                       |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                       |
| django_template | 53.3 ms                                                               | 38.8 ms: 1.38x faster                                                       |
| genshi_text     | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                       |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.23x faster                                                        |
| async_tree_io            | 2.28 sec                                                              | 885 ms: 2.58x faster                                                        |
| async_tree_none          | 950 ms                                                                | 381 ms: 2.49x faster                                                        |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.41x faster                                                        |
| deltablue                | 8.94 ms                                                               | 3.97 ms: 2.25x faster                                                       |
| richards_super           | 107 ms                                                                | 54.0 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 657 ms: 1.94x faster                                                        |
| richards                 | 91.7 ms                                                               | 49.0 ms: 1.87x faster                                                       |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                       |
| chaos                    | 121 ms                                                                | 66.5 ms: 1.82x faster                                                       |
| raytrace                 | 573 ms                                                                | 320 ms: 1.79x faster                                                        |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                        |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                        |
| float                    | 135 ms                                                                | 82.9 ms: 1.63x faster                                                       |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 38.5 us: 1.60x faster                                                       |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                        |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                        |
| go                       | 264 ms                                                                | 174 ms: 1.52x faster                                                        |
| scimark_monte_carlo      | 128 ms                                                                | 88.8 ms: 1.44x faster                                                       |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                        |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                       |
| pyflate                  | 795 ms                                                                | 566 ms: 1.41x faster                                                        |
| html5lib                 | 86.5 ms                                                               | 61.9 ms: 1.40x faster                                                       |
| logging_format           | 10.6 us                                                               | 7.64 us: 1.39x faster                                                       |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 97.4 ms: 1.38x faster                                                       |
| django_template          | 53.3 ms                                                               | 38.8 ms: 1.38x faster                                                       |
| dulwich_log              | 73.5 ms                                                               | 53.5 ms: 1.37x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                      |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                        |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                        |
| spectral_norm            | 186 ms                                                                | 138 ms: 1.35x faster                                                        |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                       |
| thrift                   | 1.26 ms                                                               | 934 us: 1.35x faster                                                        |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                                        |
| genshi_text              | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                       |
| hexiom                   | 10.9 ms                                                               | 8.25 ms: 1.32x faster                                                       |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.30x faster                                                       |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                       |
| xml_etree_process        | 99.5 ms                                                               | 76.6 ms: 1.30x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 282 us: 1.30x faster                                                        |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                        |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                        |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                       |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.23x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                       |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                        |
| xml_etree_parse          | 212 ms                                                                | 177 ms: 1.20x faster                                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                       |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                       |
| scimark_fft              | 500 ms                                                                | 428 ms: 1.17x faster                                                        |
| sympy_expand             | 543 ms                                                                | 472 ms: 1.15x faster                                                        |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.15x faster                                                        |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.67 ms: 1.14x faster                                                       |
| regex_v8                 | 32.2 ms                                                               | 28.2 ms: 1.14x faster                                                       |
| docutils                 | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                                      |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                      |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                        |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                                       |
| regex_effbot             | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                       |
| nqueens                  | 117 ms                                                                | 108 ms: 1.09x faster                                                        |
| fannkuch                 | 546 ms                                                                | 521 ms: 1.05x faster                                                        |
| meteor_contest           | 126 ms                                                                | 121 ms: 1.04x faster                                                        |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                        |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.07x slower                                                      |
| pprint_pformat           | 2.36 sec                                                              | 2.56 sec: 1.08x slower                                                      |
| telco                    | 8.49 ms                                                               | 9.46 ms: 1.11x slower                                                       |
| json_loads               | 30.9 us                                                               | 34.6 us: 1.12x slower                                                       |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                       |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 3.57 ms: 1.58x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 6.57 ms: 1.58x slower                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 2.79 sec: 192.01x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                                |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, pidigits
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250310-3.14.0a5+-efdef5f-JIT/bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.301x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.32x