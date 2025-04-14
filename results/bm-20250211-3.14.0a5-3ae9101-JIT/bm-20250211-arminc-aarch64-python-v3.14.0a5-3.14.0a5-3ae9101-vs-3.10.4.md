# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a5
- machine: linux-aarch64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.275x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.19x faster                                         |
| docutils       | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                       |
| html5lib       | 86.5 ms                                                               | 64.4 ms: 1.34x faster                                        |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 936 ms: 2.44x faster                                         |
| async_tree_none         | 950 ms                                                                | 401 ms: 2.37x faster                                         |
| async_tree_memoization  | 1.13 sec                                                              | 513 ms: 2.21x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 701 ms: 1.82x faster                                         |
| Geometric mean          | (ref)                                                                 | 2.20x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.9 ms: 1.55x faster                                        |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                 |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.48 sec: 1.35x faster                                       |
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                         |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                        |
| pickle_pure_python   | 529 us                                                                | 426 us: 1.24x faster                                         |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                         |
| json_loads           | 30.9 us                                                               | 34.5 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.04 ms: 1.31x slower                                        |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                        |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                        |
| genshi_text     | 35.2 ms                                                               | 30.0 ms: 1.17x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.23x faster                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 218 us: 3.03x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 936 ms: 2.44x faster                                         |
| async_tree_none          | 950 ms                                                                | 401 ms: 2.37x faster                                         |
| async_tree_memoization   | 1.13 sec                                                              | 513 ms: 2.21x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.22 ms: 2.12x faster                                        |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.84x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 701 ms: 1.82x faster                                         |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                        |
| chaos                    | 121 ms                                                                | 68.5 ms: 1.77x faster                                        |
| richards                 | 91.7 ms                                                               | 53.3 ms: 1.72x faster                                        |
| raytrace                 | 573 ms                                                                | 338 ms: 1.69x faster                                         |
| go                       | 264 ms                                                                | 165 ms: 1.60x faster                                         |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                         |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.58x faster                                         |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                         |
| scimark_lu               | 227 ms                                                                | 144 ms: 1.58x faster                                         |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                        |
| float                    | 135 ms                                                                | 86.9 ms: 1.55x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.56 ms: 1.54x faster                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 1.89 ms: 1.51x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 85.0 ms: 1.50x faster                                        |
| deepcopy                 | 511 us                                                                | 341 us: 1.50x faster                                         |
| pylint                   | 485 ms                                                                | 327 ms: 1.49x faster                                         |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 96.3 ms: 1.39x faster                                        |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                        |
| logging_simple           | 9.78 us                                                               | 7.08 us: 1.38x faster                                        |
| pyflate                  | 795 ms                                                                | 580 ms: 1.37x faster                                         |
| logging_format           | 10.6 us                                                               | 7.77 us: 1.37x faster                                        |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.48 sec: 1.35x faster                                       |
| comprehensions           | 33.1 us                                                               | 24.5 us: 1.35x faster                                        |
| html5lib                 | 86.5 ms                                                               | 64.4 ms: 1.34x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                         |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                         |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.31x faster                                         |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.31x faster                                        |
| thrift                   | 1.26 ms                                                               | 978 us: 1.29x faster                                         |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.29x faster                                        |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                        |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                        |
| pickle_pure_python       | 529 us                                                                | 426 us: 1.24x faster                                         |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.23x faster                                         |
| hexiom                   | 10.9 ms                                                               | 8.94 ms: 1.22x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                         |
| 2to3                     | 381 ms                                                                | 319 ms: 1.19x faster                                         |
| scimark_fft              | 500 ms                                                                | 419 ms: 1.19x faster                                         |
| sympy_integrate          | 26.5 ms                                                               | 22.3 ms: 1.19x faster                                        |
| pycparser                | 1.69 sec                                                              | 1.43 sec: 1.18x faster                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                        |
| genshi_text              | 35.2 ms                                                               | 30.0 ms: 1.17x faster                                        |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                        |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                        |
| sympy_str                | 329 ms                                                                | 288 ms: 1.14x faster                                         |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                         |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.77 ms: 1.13x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 68.6 ms: 1.10x faster                                        |
| sympy_expand             | 543 ms                                                                | 497 ms: 1.09x faster                                         |
| docutils                 | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                       |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                         |
| dulwich_log              | 73.5 ms                                                               | 69.2 ms: 1.06x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.57 sec: 1.04x faster                                       |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.03x slower                                         |
| nqueens                  | 117 ms                                                                | 122 ms: 1.04x slower                                         |
| async_generators         | 452 ms                                                                | 486 ms: 1.07x slower                                         |
| json_loads               | 30.9 us                                                               | 34.5 us: 1.11x slower                                        |
| telco                    | 8.49 ms                                                               | 9.68 ms: 1.14x slower                                        |
| pprint_pformat           | 2.36 sec                                                              | 2.72 sec: 1.15x slower                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 1.32 sec: 1.15x slower                                       |
| coverage                 | 83.6 ms                                                               | 98.2 ms: 1.18x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 9.04 ms: 1.31x slower                                        |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 3.64 ms: 1.61x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 6.85 ms: 1.65x slower                                        |
| bench_mp_pool            | 14.5 ms                                                               | 3.45 sec: 237.19x slower                                     |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                                 |

Benchmark hidden because not significant (9): genshi_xml, regex_effbot, sqlite_synth, fannkuch, regex_dna, meteor_contest, pidigits, json, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.275x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.32x