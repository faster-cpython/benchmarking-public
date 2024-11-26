# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-aarch64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.219x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 315 ms: 1.21x faster                                                       |
| docutils       | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                     |
| html5lib       | 86.5 ms                                                               | 72.3 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 469 ms: 2.02x faster                                                       |
| async_tree_memoization  | 1.13 sec                                                              | 598 ms: 1.90x faster                                                       |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 766 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                                 | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 117 ms: 1.41x faster                                                       |
| float          | 135 ms                                                                | 98.4 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 141 ms: 1.26x faster                                                       |
| regex_dna      | 257 ms                                                                | 270 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 271 us: 1.35x faster                                                       |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                       |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                      |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                      |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                       |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.89 ms: 1.29x slower                                                      |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                      |
| django_template | 53.3 ms                                                               | 48.7 ms: 1.09x faster                                                      |
| genshi_text     | 35.2 ms                                                               | 32.7 ms: 1.08x faster                                                      |
| genshi_xml      | 69.8 ms                                                               | 81.0 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.09x faster                                                       |
| deltablue                | 8.94 ms                                                               | 4.11 ms: 2.17x faster                                                      |
| async_tree_none          | 950 ms                                                                | 469 ms: 2.02x faster                                                       |
| async_tree_memoization   | 1.13 sec                                                              | 598 ms: 1.90x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                     |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 766 ms: 1.66x faster                                                       |
| richards                 | 91.7 ms                                                               | 56.4 ms: 1.62x faster                                                      |
| raytrace                 | 573 ms                                                                | 361 ms: 1.59x faster                                                       |
| logging_silent           | 222 ns                                                                | 141 ns: 1.58x faster                                                       |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                       |
| pylint                   | 485 ms                                                                | 318 ms: 1.53x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 88.7 ms: 1.51x faster                                                      |
| deepcopy_memo            | 61.7 us                                                               | 41.0 us: 1.50x faster                                                      |
| sqlglot_parse            | 2.40 ms                                                               | 1.61 ms: 1.49x faster                                                      |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.49x faster                                                       |
| scimark_monte_carlo      | 128 ms                                                                | 87.9 ms: 1.45x faster                                                      |
| go                       | 264 ms                                                                | 183 ms: 1.45x faster                                                       |
| sqlglot_transpile        | 2.84 ms                                                               | 1.98 ms: 1.43x faster                                                      |
| chaos                    | 121 ms                                                                | 85.2 ms: 1.42x faster                                                      |
| nbody                    | 166 ms                                                                | 117 ms: 1.41x faster                                                       |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                      |
| float                    | 135 ms                                                                | 98.4 ms: 1.37x faster                                                      |
| generators               | 68.1 ms                                                               | 50.4 ms: 1.35x faster                                                      |
| unpickle_pure_python     | 366 us                                                                | 271 us: 1.35x faster                                                       |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                       |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                       |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.32x faster                                                      |
| pyflate                  | 795 ms                                                                | 603 ms: 1.32x faster                                                       |
| deepcopy                 | 511 us                                                                | 397 us: 1.29x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                     |
| thrift                   | 1.26 ms                                                               | 994 us: 1.27x faster                                                       |
| xml_etree_process        | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                      |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                      |
| regex_compile            | 177 ms                                                                | 141 ms: 1.26x faster                                                       |
| logging_format           | 10.6 us                                                               | 8.52 us: 1.24x faster                                                      |
| logging_simple           | 9.78 us                                                               | 7.97 us: 1.23x faster                                                      |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.9 ms: 1.22x faster                                                      |
| 2to3                     | 381 ms                                                                | 315 ms: 1.21x faster                                                       |
| spectral_norm            | 186 ms                                                                | 154 ms: 1.21x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 72.3 ms: 1.20x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 9.22 ms: 1.18x faster                                                      |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                      |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                      |
| sympy_sum                | 184 ms                                                                | 159 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 4.03 us: 1.14x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                      |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                       |
| sympy_integrate          | 26.5 ms                                                               | 24.0 ms: 1.11x faster                                                      |
| fannkuch                 | 546 ms                                                                | 494 ms: 1.11x faster                                                       |
| sqlglot_normalize        | 156 ms                                                                | 141 ms: 1.10x faster                                                       |
| scimark_fft              | 500 ms                                                                | 454 ms: 1.10x faster                                                       |
| sympy_str                | 329 ms                                                                | 300 ms: 1.10x faster                                                       |
| django_template          | 53.3 ms                                                               | 48.7 ms: 1.09x faster                                                      |
| docutils                 | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 69.3 ms: 1.09x faster                                                      |
| genshi_text              | 35.2 ms                                                               | 32.7 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.11 ms: 1.07x faster                                                      |
| sympy_expand             | 543 ms                                                                | 516 ms: 1.05x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.56 sec: 1.04x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                       |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                      |
| regex_dna                | 257 ms                                                                | 270 ms: 1.05x slower                                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 1.27 sec: 1.11x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.64 sec: 1.12x slower                                                     |
| nqueens                  | 117 ms                                                                | 132 ms: 1.12x slower                                                       |
| telco                    | 8.49 ms                                                               | 9.64 ms: 1.14x slower                                                      |
| genshi_xml               | 69.8 ms                                                               | 81.0 ms: 1.16x slower                                                      |
| async_generators         | 452 ms                                                                | 539 ms: 1.19x slower                                                       |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 8.89 ms: 1.29x slower                                                      |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                      |
| gc_traversal             | 4.15 ms                                                               | 6.42 ms: 1.55x slower                                                      |
| create_gc_cycles         | 2.26 ms                                                               | 3.74 ms: 1.66x slower                                                      |
| bench_mp_pool            | 14.5 ms                                                               | 2.26 sec: 155.50x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                               |

Benchmark hidden because not significant (9): xml_etree_parse, json, regex_effbot, meteor_contest, dulwich_log, sqlite_synth, asyncio_websockets, pidigits, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.219x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.31x