# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: clang_hot
- machine: linux-aarch64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.356x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 296 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                  |
| html5lib       | 86.5 ms                                                               | 60.4 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 374 ms: 2.54x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 902 ms: 2.53x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 479 ms: 2.36x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 744 ms: 1.71x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.26x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.2 ms: 1.53x faster                                                   |
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                                    |
| pidigits       | 235 ms                                                                | 305 ms: 1.30x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 34.4 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 378 us: 1.40x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 77.0 ms: 1.29x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.15x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 224 ms: 1.06x slower                                                    |
| json_loads           | 30.9 us                                                               | 35.0 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.33 ms: 1.35x slower                                                   |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.41x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.2 ms: 1.40x faster                                                   |
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 184 us: 3.60x faster                                                    |
| async_tree_none          | 950 ms                                                                | 374 ms: 2.54x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 902 ms: 2.53x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 479 ms: 2.36x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| go                       | 264 ms                                                                | 133 ms: 1.99x faster                                                    |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.91x faster                                                   |
| richards_super           | 107 ms                                                                | 58.0 ms: 1.85x faster                                                   |
| richards                 | 91.7 ms                                                               | 49.8 ms: 1.84x faster                                                   |
| raytrace                 | 573 ms                                                                | 312 ms: 1.84x faster                                                    |
| logging_silent           | 222 ns                                                                | 122 ns: 1.82x faster                                                    |
| chaos                    | 121 ms                                                                | 67.2 ms: 1.80x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 744 ms: 1.71x faster                                                    |
| spectral_norm            | 186 ms                                                                | 109 ms: 1.71x faster                                                    |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 36.4 us: 1.70x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.69 ms: 1.69x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.0 us: 1.66x faster                                                   |
| deepcopy                 | 511 us                                                                | 315 us: 1.62x faster                                                    |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                    |
| pylint                   | 485 ms                                                                | 302 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 81.2 ms: 1.57x faster                                                   |
| float                    | 135 ms                                                                | 88.2 ms: 1.53x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.21 ms: 1.51x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 89.0 ms: 1.51x faster                                                   |
| pyflate                  | 795 ms                                                                | 542 ms: 1.47x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.37 us: 1.44x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 60.4 ms: 1.43x faster                                                   |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.93 us: 1.41x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 378 us: 1.40x faster                                                    |
| django_template          | 53.3 ms                                                               | 38.2 ms: 1.40x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.31 us: 1.39x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.35x faster                                                  |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.3 ms: 1.34x faster                                                   |
| thrift                   | 1.26 ms                                                               | 961 us: 1.31x faster                                                    |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.31x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.0 ms: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 296 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                   |
| scimark_fft              | 500 ms                                                                | 391 ms: 1.28x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 124 ms: 1.26x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 60.5 ms: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.24x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 60.0 ms: 1.23x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.23 ms: 1.22x faster                                                   |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 944 ms: 1.22x faster                                                    |
| sympy_expand             | 543 ms                                                                | 453 ms: 1.20x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                  |
| nqueens                  | 117 ms                                                                | 99.9 ms: 1.18x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.15x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                  |
| fannkuch                 | 546 ms                                                                | 498 ms: 1.10x faster                                                    |
| async_generators         | 452 ms                                                                | 418 ms: 1.08x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 224 ms: 1.06x slower                                                    |
| regex_v8                 | 32.2 ms                                                               | 34.4 ms: 1.07x slower                                                   |
| coverage                 | 83.6 ms                                                               | 93.9 ms: 1.12x slower                                                   |
| json_loads               | 30.9 us                                                               | 35.0 us: 1.13x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.73 ms: 1.15x slower                                                   |
| pidigits                 | 235 ms                                                                | 305 ms: 1.30x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.33 ms: 1.35x slower                                                   |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.73 ms: 1.62x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.27 sec: 500.13x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (6): meteor_contest, sqlite_synth, regex_dna, json, xml_etree_iterparse, regex_effbot
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.356x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.35x