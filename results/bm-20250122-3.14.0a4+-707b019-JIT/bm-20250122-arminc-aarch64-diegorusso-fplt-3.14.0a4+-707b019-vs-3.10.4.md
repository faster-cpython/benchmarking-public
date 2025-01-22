# Results vs. 3.10.4

- fork: diegorusso
- ref: fplt
- machine: linux-aarch64
- commit hash: 707b019
- commit date: 2025-01-22
- overall geometric mean: 1.204x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 325 ms: 1.17x faster                                         |
| docutils       | 3.53 sec                                                              | 3.25 sec: 1.09x faster                                       |
| html5lib       | 86.5 ms                                                               | 73.4 ms: 1.18x faster                                        |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 905 ms: 2.52x faster                                         |
| async_tree_none         | 950 ms                                                                | 397 ms: 2.39x faster                                         |
| async_tree_memoization  | 1.13 sec                                                              | 500 ms: 2.27x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 685 ms: 1.86x faster                                         |
| Geometric mean          | (ref)                                                                 | 2.25x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.6 ms: 1.50x faster                                        |
| nbody          | 166 ms                                                                | 132 ms: 1.26x faster                                         |
| pidigits       | 235 ms                                                                | 246 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 148 ms: 1.19x faster                                         |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                 |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                       |
| unpickle_pure_python | 366 us                                                                | 290 us: 1.26x faster                                         |
| pickle_pure_python   | 529 us                                                                | 430 us: 1.23x faster                                         |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                         |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 86.8 ms: 1.15x faster                                        |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.04 ms: 1.31x slower                                        |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                        |
| django_template | 53.3 ms                                                               | 49.5 ms: 1.08x faster                                        |
| genshi_text     | 35.2 ms                                                               | 33.3 ms: 1.06x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 83.7 ms: 1.20x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 225 us: 2.94x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 905 ms: 2.52x faster                                         |
| async_tree_none          | 950 ms                                                                | 397 ms: 2.39x faster                                         |
| async_tree_memoization   | 1.13 sec                                                              | 500 ms: 2.27x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.23 ms: 2.12x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 685 ms: 1.86x faster                                         |
| raytrace                 | 573 ms                                                                | 352 ms: 1.63x faster                                         |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                         |
| richards_super           | 107 ms                                                                | 70.2 ms: 1.53x faster                                        |
| float                    | 135 ms                                                                | 89.6 ms: 1.50x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.63 ms: 1.47x faster                                        |
| logging_silent           | 222 ns                                                                | 151 ns: 1.47x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.96 ms: 1.45x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 42.8 us: 1.44x faster                                        |
| go                       | 264 ms                                                                | 186 ms: 1.42x faster                                         |
| pylint                   | 485 ms                                                                | 344 ms: 1.41x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 95.5 ms: 1.40x faster                                        |
| scimark_lu               | 227 ms                                                                | 162 ms: 1.40x faster                                         |
| chaos                    | 121 ms                                                                | 88.2 ms: 1.37x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 94.8 ms: 1.35x faster                                        |
| deepcopy                 | 511 us                                                                | 388 us: 1.31x faster                                         |
| pyflate                  | 795 ms                                                                | 607 ms: 1.31x faster                                         |
| comprehensions           | 33.1 us                                                               | 25.4 us: 1.31x faster                                        |
| mako                     | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                        |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                         |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.29x faster                                         |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                       |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 290 us: 1.26x faster                                         |
| nbody                    | 166 ms                                                                | 132 ms: 1.26x faster                                         |
| pickle_pure_python       | 529 us                                                                | 430 us: 1.23x faster                                         |
| thrift                   | 1.26 ms                                                               | 1.03 ms: 1.23x faster                                        |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.0 ms: 1.21x faster                                        |
| generators               | 68.1 ms                                                               | 56.7 ms: 1.20x faster                                        |
| richards                 | 91.7 ms                                                               | 76.4 ms: 1.20x faster                                        |
| regex_compile            | 177 ms                                                                | 148 ms: 1.19x faster                                         |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                         |
| logging_simple           | 9.78 us                                                               | 8.25 us: 1.18x faster                                        |
| html5lib                 | 86.5 ms                                                               | 73.4 ms: 1.18x faster                                        |
| 2to3                     | 381 ms                                                                | 325 ms: 1.17x faster                                         |
| logging_format           | 10.6 us                                                               | 9.07 us: 1.17x faster                                        |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                        |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.15x faster                                        |
| xml_etree_process        | 99.5 ms                                                               | 86.8 ms: 1.15x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 4.05 us: 1.14x faster                                        |
| sympy_sum                | 184 ms                                                                | 163 ms: 1.13x faster                                         |
| hexiom                   | 10.9 ms                                                               | 9.92 ms: 1.10x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 24.1 ms: 1.10x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                        |
| scimark_fft              | 500 ms                                                                | 457 ms: 1.10x faster                                         |
| sqlglot_normalize        | 156 ms                                                                | 143 ms: 1.09x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                         |
| docutils                 | 3.53 sec                                                              | 3.25 sec: 1.09x faster                                       |
| pycparser                | 1.69 sec                                                              | 1.56 sec: 1.08x faster                                       |
| sympy_str                | 329 ms                                                                | 303 ms: 1.08x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| sqlglot_optimize         | 75.4 ms                                                               | 70.0 ms: 1.08x faster                                        |
| django_template          | 53.3 ms                                                               | 49.5 ms: 1.08x faster                                        |
| genshi_text              | 35.2 ms                                                               | 33.3 ms: 1.06x faster                                        |
| sympy_expand             | 543 ms                                                                | 518 ms: 1.05x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.56 sec: 1.04x faster                                       |
| dulwich_log              | 73.5 ms                                                               | 71.2 ms: 1.03x faster                                        |
| fannkuch                 | 546 ms                                                                | 532 ms: 1.03x faster                                         |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                         |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.03x slower                                         |
| pidigits                 | 235 ms                                                                | 246 ms: 1.05x slower                                         |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                        |
| async_generators         | 452 ms                                                                | 491 ms: 1.09x slower                                         |
| nqueens                  | 117 ms                                                                | 129 ms: 1.10x slower                                         |
| pprint_pformat           | 2.36 sec                                                              | 2.69 sec: 1.14x slower                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 1.35 sec: 1.18x slower                                       |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                        |
| genshi_xml               | 69.8 ms                                                               | 83.7 ms: 1.20x slower                                        |
| coverage                 | 83.6 ms                                                               | 105 ms: 1.25x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 9.04 ms: 1.31x slower                                        |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 3.69 ms: 1.63x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 6.95 ms: 1.67x slower                                        |
| bench_mp_pool            | 14.5 ms                                                               | 1.36 sec: 93.48x slower                                      |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                 |

Benchmark hidden because not significant (5): regex_effbot, sqlite_synth, regex_dna, regex_v8, json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250122-3.14.0a4+-707b019-JIT/bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.204x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.32x