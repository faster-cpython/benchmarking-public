# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-aarch64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.266x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.20x faster                                                           |
| docutils       | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                         |
| html5lib       | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 958 ms: 2.38x faster                                                           |
| async_tree_none         | 950 ms                                                                | 414 ms: 2.29x faster                                                           |
| async_tree_memoization  | 1.13 sec                                                              | 518 ms: 2.19x faster                                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 701 ms: 1.81x faster                                                           |
| Geometric mean          | (ref)                                                                 | 2.16x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.0 ms: 1.59x faster                                                          |
| nbody          | 166 ms                                                                | 132 ms: 1.26x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 130 ms: 1.36x faster                                                           |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.31x faster                                                         |
| unpickle_pure_python | 366 us                                                                | 284 us: 1.29x faster                                                           |
| pickle_pure_python   | 529 us                                                                | 411 us: 1.29x faster                                                           |
| xml_etree_process    | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                          |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                           |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                          |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                           |
| json_loads           | 30.9 us                                                               | 35.9 us: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.15 ms: 1.33x slower                                                          |
| python_startup         | 11.2 ms                                                               | 16.6 ms: 1.49x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.41x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                          |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                          |
| genshi_text     | 35.2 ms                                                               | 29.5 ms: 1.19x faster                                                          |
| genshi_xml      | 69.8 ms                                                               | 65.9 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                                 | 1.21x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 220 us: 3.00x faster                                                           |
| async_tree_io            | 2.28 sec                                                              | 958 ms: 2.38x faster                                                           |
| async_tree_none          | 950 ms                                                                | 414 ms: 2.29x faster                                                           |
| async_tree_memoization   | 1.13 sec                                                              | 518 ms: 2.19x faster                                                           |
| deltablue                | 8.94 ms                                                               | 4.15 ms: 2.16x faster                                                          |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.84x faster                                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 701 ms: 1.81x faster                                                           |
| richards_super           | 107 ms                                                                | 60.9 ms: 1.76x faster                                                          |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                                          |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                          |
| raytrace                 | 573 ms                                                                | 335 ms: 1.71x faster                                                           |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                           |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                           |
| float                    | 135 ms                                                                | 85.0 ms: 1.59x faster                                                          |
| deepcopy_memo            | 61.7 us                                                               | 40.0 us: 1.54x faster                                                          |
| go                       | 264 ms                                                                | 173 ms: 1.53x faster                                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.58 ms: 1.52x faster                                                          |
| spectral_norm            | 186 ms                                                                | 123 ms: 1.52x faster                                                           |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                                           |
| deepcopy                 | 511 us                                                                | 339 us: 1.51x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 85.3 ms: 1.50x faster                                                          |
| pylint                   | 485 ms                                                                | 325 ms: 1.49x faster                                                           |
| sqlglot_transpile        | 2.84 ms                                                               | 1.90 ms: 1.49x faster                                                          |
| thrift                   | 1.26 ms                                                               | 919 us: 1.37x faster                                                           |
| pyflate                  | 795 ms                                                                | 580 ms: 1.37x faster                                                           |
| comprehensions           | 33.1 us                                                               | 24.4 us: 1.36x faster                                                          |
| crypto_pyaes             | 134 ms                                                                | 98.7 ms: 1.36x faster                                                          |
| regex_compile            | 177 ms                                                                | 130 ms: 1.36x faster                                                           |
| html5lib                 | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                          |
| logging_simple           | 9.78 us                                                               | 7.27 us: 1.35x faster                                                          |
| logging_format           | 10.6 us                                                               | 7.92 us: 1.34x faster                                                          |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                          |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.31x faster                                                         |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 284 us: 1.29x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 411 us: 1.29x faster                                                           |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                          |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                          |
| deepcopy_reduce          | 4.60 us                                                               | 3.64 us: 1.26x faster                                                          |
| nbody                    | 166 ms                                                                | 132 ms: 1.26x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                          |
| sympy_integrate          | 26.5 ms                                                               | 22.1 ms: 1.20x faster                                                          |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.2 ms: 1.20x faster                                                          |
| 2to3                     | 381 ms                                                                | 319 ms: 1.20x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 29.5 ms: 1.19x faster                                                          |
| hexiom                   | 10.9 ms                                                               | 9.15 ms: 1.19x faster                                                          |
| pycparser                | 1.69 sec                                                              | 1.43 sec: 1.19x faster                                                         |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                           |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                          |
| scimark_fft              | 500 ms                                                                | 429 ms: 1.17x faster                                                           |
| sympy_sum                | 184 ms                                                                | 158 ms: 1.16x faster                                                           |
| sqlglot_normalize        | 156 ms                                                                | 134 ms: 1.16x faster                                                           |
| dulwich_log              | 73.5 ms                                                               | 64.1 ms: 1.15x faster                                                          |
| sympy_str                | 329 ms                                                                | 288 ms: 1.14x faster                                                           |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                          |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                          |
| sqlglot_optimize         | 75.4 ms                                                               | 66.9 ms: 1.13x faster                                                          |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                          |
| docutils                 | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                         |
| sympy_expand             | 543 ms                                                                | 503 ms: 1.08x faster                                                           |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                           |
| genshi_xml               | 69.8 ms                                                               | 65.9 ms: 1.06x faster                                                          |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                          |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                           |
| mdp                      | 3.70 sec                                                              | 3.56 sec: 1.04x faster                                                         |
| sqlite_synth             | 4.12 us                                                               | 3.99 us: 1.03x faster                                                          |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.03x slower                                                           |
| json                     | 5.88 ms                                                               | 6.13 ms: 1.04x slower                                                          |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                                           |
| async_generators         | 452 ms                                                                | 492 ms: 1.09x slower                                                           |
| json_loads               | 30.9 us                                                               | 35.9 us: 1.16x slower                                                          |
| pprint_pformat           | 2.36 sec                                                              | 2.77 sec: 1.17x slower                                                         |
| telco                    | 8.49 ms                                                               | 9.96 ms: 1.17x slower                                                          |
| pprint_safe_repr         | 1.15 sec                                                              | 1.35 sec: 1.18x slower                                                         |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 9.15 ms: 1.33x slower                                                          |
| python_startup           | 11.2 ms                                                               | 16.6 ms: 1.49x slower                                                          |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.65x slower                                                          |
| gc_traversal             | 4.15 ms                                                               | 6.93 ms: 1.67x slower                                                          |
| bench_mp_pool            | 14.5 ms                                                               | 2.14 sec: 147.10x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                                                   |

Benchmark hidden because not significant (5): regex_dna, regex_v8, fannkuch, meteor_contest, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.266x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.32x