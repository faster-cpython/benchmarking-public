# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-aarch64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.368x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 285 ms: 1.33x faster                                                        |
| docutils       | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                                      |
| html5lib       | 86.5 ms                                                               | 60.0 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 872 ms: 2.62x faster                                                        |
| async_tree_memoization  | 1.13 sec                                                              | 457 ms: 2.48x faster                                                        |
| async_tree_none         | 950 ms                                                                | 391 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 724 ms: 1.76x faster                                                        |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.1 ms: 1.64x faster                                                       |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                        |
| pidigits       | 235 ms                                                                | 291 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.44x faster                                                        |
| regex_v8       | 32.2 ms                                                               | 29.8 ms: 1.08x faster                                                       |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                                      |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                        |
| pickle_pure_python   | 529 us                                                                | 378 us: 1.40x faster                                                        |
| xml_etree_process    | 99.5 ms                                                               | 77.0 ms: 1.29x faster                                                       |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                       |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                        |
| xml_etree_parse      | 212 ms                                                                | 207 ms: 1.03x faster                                                        |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                       |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                       |
| genshi_text     | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                       |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                       |
| genshi_xml      | 69.8 ms                                                               | 58.7 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 189 us: 3.50x faster                                                        |
| async_tree_io            | 2.28 sec                                                              | 872 ms: 2.62x faster                                                        |
| async_tree_memoization   | 1.13 sec                                                              | 457 ms: 2.48x faster                                                        |
| async_tree_none          | 950 ms                                                                | 391 ms: 2.43x faster                                                        |
| deltablue                | 8.94 ms                                                               | 3.69 ms: 2.42x faster                                                       |
| mdp                      | 3.70 sec                                                              | 1.60 sec: 2.31x faster                                                      |
| go                       | 264 ms                                                                | 132 ms: 2.01x faster                                                        |
| generators               | 68.1 ms                                                               | 34.3 ms: 1.98x faster                                                       |
| logging_silent           | 222 ns                                                                | 118 ns: 1.89x faster                                                        |
| chaos                    | 121 ms                                                                | 65.4 ms: 1.85x faster                                                       |
| richards_super           | 107 ms                                                                | 58.2 ms: 1.84x faster                                                       |
| raytrace                 | 573 ms                                                                | 312 ms: 1.83x faster                                                        |
| scimark_sor              | 246 ms                                                                | 135 ms: 1.82x faster                                                        |
| richards                 | 91.7 ms                                                               | 51.0 ms: 1.80x faster                                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 724 ms: 1.76x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 36.6 us: 1.69x faster                                                       |
| comprehensions           | 33.1 us                                                               | 19.7 us: 1.68x faster                                                       |
| scimark_monte_carlo      | 128 ms                                                                | 76.9 ms: 1.66x faster                                                       |
| float                    | 135 ms                                                                | 82.1 ms: 1.64x faster                                                       |
| deepcopy                 | 511 us                                                                | 312 us: 1.63x faster                                                        |
| pylint                   | 485 ms                                                                | 301 ms: 1.61x faster                                                        |
| crypto_pyaes             | 134 ms                                                                | 83.1 ms: 1.61x faster                                                       |
| spectral_norm            | 186 ms                                                                | 117 ms: 1.59x faster                                                        |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                                        |
| pyflate                  | 795 ms                                                                | 515 ms: 1.54x faster                                                        |
| hexiom                   | 10.9 ms                                                               | 7.24 ms: 1.51x faster                                                       |
| regex_compile            | 177 ms                                                                | 123 ms: 1.44x faster                                                        |
| html5lib                 | 86.5 ms                                                               | 60.0 ms: 1.44x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                                      |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                        |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                       |
| dulwich_log              | 73.5 ms                                                               | 52.3 ms: 1.41x faster                                                       |
| logging_format           | 10.6 us                                                               | 7.57 us: 1.40x faster                                                       |
| pickle_pure_python       | 529 us                                                                | 378 us: 1.40x faster                                                        |
| django_template          | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                       |
| sqlalchemy_declarative   | 197 ms                                                                | 143 ms: 1.38x faster                                                        |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                      |
| sympy_integrate          | 26.5 ms                                                               | 19.5 ms: 1.36x faster                                                       |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                        |
| 2to3                     | 381 ms                                                                | 285 ms: 1.33x faster                                                        |
| deepcopy_reduce          | 4.60 us                                                               | 3.45 us: 1.33x faster                                                       |
| genshi_text              | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                       |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                       |
| scimark_fft              | 500 ms                                                                | 385 ms: 1.30x faster                                                        |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                       |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                        |
| xml_etree_process        | 99.5 ms                                                               | 77.0 ms: 1.29x faster                                                       |
| sympy_str                | 329 ms                                                                | 257 ms: 1.28x faster                                                        |
| pathlib                  | 26.3 ms                                                               | 21.0 ms: 1.25x faster                                                       |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.25x faster                                                      |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 925 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.36 ms: 1.20x faster                                                       |
| docutils                 | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                       |
| genshi_xml               | 69.8 ms                                                               | 58.7 ms: 1.19x faster                                                       |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                        |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                        |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.13x faster                                                        |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                        |
| fannkuch                 | 546 ms                                                                | 484 ms: 1.13x faster                                                        |
| async_generators         | 452 ms                                                                | 408 ms: 1.11x faster                                                        |
| regex_v8                 | 32.2 ms                                                               | 29.8 ms: 1.08x faster                                                       |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                        |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                        |
| xml_etree_parse          | 212 ms                                                                | 207 ms: 1.03x faster                                                        |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                        |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                       |
| telco                    | 8.49 ms                                                               | 9.12 ms: 1.07x slower                                                       |
| coverage                 | 83.6 ms                                                               | 94.6 ms: 1.13x slower                                                       |
| pidigits                 | 235 ms                                                                | 291 ms: 1.24x slower                                                        |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 6.53 ms: 1.57x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 3.66 ms: 1.62x slower                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 2.97 sec: 204.29x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, json
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.368x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.36x