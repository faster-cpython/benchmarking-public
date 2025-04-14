# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.084x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.40 sec: 1.04x faster                                           |
| html5lib       | 86.5 ms                                                               | 80.0 ms: 1.08x faster                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                     |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 959 ms: 2.38x faster                                             |
| async_tree_none         | 950 ms                                                                | 437 ms: 2.17x faster                                             |
| async_tree_memoization  | 1.13 sec                                                              | 530 ms: 2.14x faster                                             |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 733 ms: 1.74x faster                                             |
| Geometric mean          | (ref)                                                                 | 2.09x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 135 ms                                                                | 105 ms: 1.28x faster                                             |
| nbody          | 166 ms                                                                | 184 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 162 ms: 1.09x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                             |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                             |
| pickle_pure_python   | 529 us                                                                | 494 us: 1.07x faster                                             |
| unpickle_pure_python | 366 us                                                                | 345 us: 1.06x faster                                             |
| tomli_loads          | 3.36 sec                                                              | 3.26 sec: 1.03x faster                                           |
| xml_etree_process    | 99.5 ms                                                               | 111 ms: 1.11x slower                                             |
| xml_etree_generate   | 123 ms                                                                | 141 ms: 1.15x slower                                             |
| json_loads           | 30.9 us                                                               | 37.6 us: 1.22x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.76x slower                                            |
| python_startup         | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 56.2 ms: 1.05x slower                                            |
| genshi_text     | 35.2 ms                                                               | 38.2 ms: 1.09x slower                                            |
| genshi_xml      | 69.8 ms                                                               | 79.5 ms: 1.14x slower                                            |
| mako            | 18.9 ms                                                               | 22.3 ms: 1.18x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.11x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 959 ms: 2.38x faster                                             |
| typing_runtime_protocols | 661 us                                                                | 289 us: 2.29x faster                                             |
| async_tree_none          | 950 ms                                                                | 437 ms: 2.17x faster                                             |
| async_tree_memoization   | 1.13 sec                                                              | 530 ms: 2.14x faster                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 733 ms: 1.74x faster                                             |
| generators               | 68.1 ms                                                               | 43.9 ms: 1.55x faster                                            |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                             |
| deltablue                | 8.94 ms                                                               | 6.31 ms: 1.42x faster                                            |
| logging_silent           | 222 ns                                                                | 160 ns: 1.38x faster                                             |
| scimark_sor              | 246 ms                                                                | 181 ms: 1.36x faster                                             |
| raytrace                 | 573 ms                                                                | 425 ms: 1.35x faster                                             |
| chaos                    | 121 ms                                                                | 90.7 ms: 1.34x faster                                            |
| float                    | 135 ms                                                                | 105 ms: 1.28x faster                                             |
| spectral_norm            | 186 ms                                                                | 148 ms: 1.26x faster                                             |
| richards                 | 91.7 ms                                                               | 73.4 ms: 1.25x faster                                            |
| pylint                   | 485 ms                                                                | 391 ms: 1.24x faster                                             |
| richards_super           | 107 ms                                                                | 87.4 ms: 1.23x faster                                            |
| pyflate                  | 795 ms                                                                | 654 ms: 1.22x faster                                             |
| crypto_pyaes             | 134 ms                                                                | 111 ms: 1.21x faster                                             |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                             |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                             |
| sqlglot_parse            | 2.40 ms                                                               | 2.04 ms: 1.18x faster                                            |
| scimark_lu               | 227 ms                                                                | 193 ms: 1.17x faster                                             |
| deepcopy_memo            | 61.7 us                                                               | 52.7 us: 1.17x faster                                            |
| deepcopy                 | 511 us                                                                | 439 us: 1.16x faster                                             |
| comprehensions           | 33.1 us                                                               | 28.5 us: 1.16x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.15x faster                                           |
| sqlglot_transpile        | 2.84 ms                                                               | 2.48 ms: 1.14x faster                                            |
| hexiom                   | 10.9 ms                                                               | 9.70 ms: 1.13x faster                                            |
| pathlib                  | 26.3 ms                                                               | 23.4 ms: 1.12x faster                                            |
| scimark_monte_carlo      | 128 ms                                                                | 115 ms: 1.11x faster                                             |
| coroutines               | 37.2 ms                                                               | 33.5 ms: 1.11x faster                                            |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                            |
| regex_compile            | 177 ms                                                                | 162 ms: 1.09x faster                                             |
| html5lib                 | 86.5 ms                                                               | 80.0 ms: 1.08x faster                                            |
| pickle_pure_python       | 529 us                                                                | 494 us: 1.07x faster                                             |
| unpickle_pure_python     | 366 us                                                                | 345 us: 1.06x faster                                             |
| create_gc_cycles         | 2.26 ms                                                               | 2.15 ms: 1.05x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 70.1 ms: 1.05x faster                                            |
| logging_simple           | 9.78 us                                                               | 9.40 us: 1.04x faster                                            |
| docutils                 | 3.53 sec                                                              | 3.40 sec: 1.04x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 3.26 sec: 1.03x faster                                           |
| pprint_pformat           | 2.36 sec                                                              | 2.41 sec: 1.02x slower                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.85 ms: 1.03x slower                                            |
| sqlglot_optimize         | 75.4 ms                                                               | 78.5 ms: 1.04x slower                                            |
| sympy_sum                | 184 ms                                                                | 192 ms: 1.04x slower                                             |
| asyncio_websockets       | 657 ms                                                                | 687 ms: 1.05x slower                                             |
| mdp                      | 3.70 sec                                                              | 3.87 sec: 1.05x slower                                           |
| sympy_integrate          | 26.5 ms                                                               | 27.8 ms: 1.05x slower                                            |
| django_template          | 53.3 ms                                                               | 56.2 ms: 1.05x slower                                            |
| sqlalchemy_declarative   | 197 ms                                                                | 210 ms: 1.06x slower                                             |
| json                     | 5.88 ms                                                               | 6.25 ms: 1.06x slower                                            |
| genshi_text              | 35.2 ms                                                               | 38.2 ms: 1.09x slower                                            |
| nbody                    | 166 ms                                                                | 184 ms: 1.11x slower                                             |
| xml_etree_process        | 99.5 ms                                                               | 111 ms: 1.11x slower                                             |
| sympy_str                | 329 ms                                                                | 369 ms: 1.12x slower                                             |
| genshi_xml               | 69.8 ms                                                               | 79.5 ms: 1.14x slower                                            |
| sympy_expand             | 543 ms                                                                | 620 ms: 1.14x slower                                             |
| xml_etree_generate       | 123 ms                                                                | 141 ms: 1.15x slower                                             |
| sqlalchemy_imperative    | 20.5 ms                                                               | 24.1 ms: 1.17x slower                                            |
| mako                     | 18.9 ms                                                               | 22.3 ms: 1.18x slower                                            |
| nqueens                  | 117 ms                                                                | 138 ms: 1.18x slower                                             |
| bench_thread_pool        | 1.59 ms                                                               | 1.89 ms: 1.19x slower                                            |
| json_loads               | 30.9 us                                                               | 37.6 us: 1.22x slower                                            |
| fannkuch                 | 546 ms                                                                | 675 ms: 1.24x slower                                             |
| meteor_contest           | 126 ms                                                                | 157 ms: 1.25x slower                                             |
| async_generators         | 452 ms                                                                | 566 ms: 1.25x slower                                             |
| gc_traversal             | 4.15 ms                                                               | 5.36 ms: 1.29x slower                                            |
| telco                    | 8.49 ms                                                               | 12.2 ms: 1.44x slower                                            |
| coverage                 | 83.6 ms                                                               | 132 ms: 1.58x slower                                             |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.76x slower                                            |
| python_startup           | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                            |
| bench_mp_pool            | 14.5 ms                                                               | 57.5 ms: 3.95x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.04x faster                                                     |

Benchmark hidden because not significant (12): logging_format, regex_effbot, pidigits, scimark_fft, deepcopy_reduce, thrift, 2to3, pprint_safe_repr, json_dumps, regex_dna, sqlglot_normalize, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.56x