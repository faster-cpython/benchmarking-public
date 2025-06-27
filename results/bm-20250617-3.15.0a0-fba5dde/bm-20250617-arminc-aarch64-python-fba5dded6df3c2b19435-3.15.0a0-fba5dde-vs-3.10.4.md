# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.346x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.3 ms: 1.41x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 897 ms: 2.55x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_none         | 950 ms                                                                | 395 ms: 2.41x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 662 ms: 1.92x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.7 ms: 1.57x faster                                                   |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.44x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.5 ms: 1.21x faster                                                   |
| regex_dna      | 257 ms                                                                | 223 ms: 1.16x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.39x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 385 us: 1.37x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.54 ms: 1.24x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.39x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 897 ms: 2.55x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_none          | 950 ms                                                                | 395 ms: 2.41x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.03 ms: 2.22x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 662 ms: 1.92x faster                                                    |
| generators               | 68.1 ms                                                               | 36.0 ms: 1.89x faster                                                   |
| richards_super           | 107 ms                                                                | 60.7 ms: 1.77x faster                                                   |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                                   |
| raytrace                 | 573 ms                                                                | 328 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.6 ms: 1.74x faster                                                   |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 79.2 ms: 1.61x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 84.3 ms: 1.59x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.86 ms: 1.59x faster                                                   |
| float                    | 135 ms                                                                | 85.7 ms: 1.57x faster                                                   |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                    |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                    |
| pyflate                  | 795 ms                                                                | 532 ms: 1.50x faster                                                    |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.49x faster                                                    |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.49x faster                                                    |
| regex_compile            | 177 ms                                                                | 122 ms: 1.44x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.3 ms: 1.41x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.39x faster                                                    |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 385 us: 1.37x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 54.4 ms: 1.35x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                   |
| thrift                   | 1.26 ms                                                               | 961 us: 1.31x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.33 us: 1.27x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.70 us: 1.27x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                   |
| sympy_str                | 329 ms                                                                | 263 ms: 1.25x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.75 us: 1.23x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.5 ms: 1.21x faster                                                   |
| nqueens                  | 117 ms                                                                | 97.9 ms: 1.20x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 432 ms: 1.16x faster                                                    |
| sympy_expand             | 543 ms                                                                | 469 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                   |
| regex_dna                | 257 ms                                                                | 223 ms: 1.16x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.05 sec: 1.15x faster                                                  |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.01 sec: 1.14x faster                                                  |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.13 ms: 1.07x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                   |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                   |
| async_generators         | 452 ms                                                                | 442 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.23 ms: 1.09x slower                                                   |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.24x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.54 ms: 1.24x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.00 ms: 1.68x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.84 ms: 1.70x slower                                                   |
| logging_silent           | 222 ns                                                                | 643 ns: 2.90x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.346x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x