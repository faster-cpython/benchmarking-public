# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.042x faster
- HPT reliability: 99.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 357 ms: 1.07x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.44 sec: 1.03x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.3 ms: 1.28x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 532 ms: 2.13x faster                                                    |
| async_tree_none         | 950 ms                                                                | 449 ms: 2.11x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 823 ms: 1.55x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 96.7 ms: 1.39x faster                                                   |
| nbody          | 166 ms                                                                | 141 ms: 1.17x faster                                                    |
| pidigits       | 235 ms                                                                | 282 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 225 ms: 1.14x faster                                                    |
| regex_compile  | 177 ms                                                                | 155 ms: 1.14x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.93 sec: 1.15x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 468 us: 1.13x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 329 us: 1.11x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                   |
| xml_etree_parse      | 212 ms                                                                | 227 ms: 1.07x slower                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 170 ms: 1.09x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 110 ms: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 43.4 us: 1.23x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.5 us: 1.24x slower                                                   |
| unpickle             | 17.5 us                                                               | 22.6 us: 1.29x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| pickle_list          | 5.24 us                                                               | 7.08 us: 1.35x slower                                                   |
| pickle               | 12.5 us                                                               | 20.5 us: 1.64x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.73 ms: 1.41x slower                                                   |
| python_startup         | 11.2 ms                                                               | 17.1 ms: 1.53x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.0 ms: 1.11x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.3 ms: 1.06x faster                                                   |
| django_template | 53.3 ms                                                               | 53.6 ms: 1.01x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 75.1 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 259 us: 2.55x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 532 ms: 2.13x faster                                                    |
| async_tree_none          | 950 ms                                                                | 449 ms: 2.11x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.54 ms: 1.97x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.97 sec: 1.88x faster                                                  |
| go                       | 264 ms                                                                | 141 ms: 1.88x faster                                                    |
| generators               | 68.1 ms                                                               | 39.7 ms: 1.71x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 570 ms: 1.66x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 823 ms: 1.55x faster                                                    |
| richards_super           | 107 ms                                                                | 72.2 ms: 1.49x faster                                                   |
| raytrace                 | 573 ms                                                                | 390 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.46x faster                                                  |
| chaos                    | 121 ms                                                                | 82.7 ms: 1.46x faster                                                   |
| scimark_sor              | 246 ms                                                                | 169 ms: 1.45x faster                                                    |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.43x faster                                                   |
| richards                 | 91.7 ms                                                               | 64.0 ms: 1.43x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 43.3 us: 1.42x faster                                                   |
| float                    | 135 ms                                                                | 96.7 ms: 1.39x faster                                                   |
| pyflate                  | 795 ms                                                                | 581 ms: 1.37x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 95.9 ms: 1.33x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 8.23 ms: 1.33x faster                                                   |
| pylint                   | 485 ms                                                                | 367 ms: 1.32x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 67.3 ms: 1.28x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 105 ms: 1.28x faster                                                    |
| deepcopy                 | 511 us                                                                | 406 us: 1.26x faster                                                    |
| scimark_lu               | 227 ms                                                                | 186 ms: 1.22x faster                                                    |
| spectral_norm            | 186 ms                                                                | 156 ms: 1.19x faster                                                    |
| nbody                    | 166 ms                                                                | 141 ms: 1.17x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.93 sec: 1.15x faster                                                  |
| regex_dna                | 257 ms                                                                | 225 ms: 1.14x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.14x faster                                                  |
| regex_compile            | 177 ms                                                                | 155 ms: 1.14x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 468 us: 1.13x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.5 ms: 1.13x faster                                                   |
| coroutines               | 37.2 ms                                                               | 33.0 ms: 1.13x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 66.0 ms: 1.11x faster                                                   |
| mako                     | 18.9 ms                                                               | 17.0 ms: 1.11x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 329 us: 1.11x faster                                                    |
| 2to3                     | 381 ms                                                                | 357 ms: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 33.3 ms: 1.06x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.52 ms: 1.05x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                   |
| logging_simple           | 9.78 us                                                               | 9.40 us: 1.04x faster                                                   |
| logging_format           | 10.6 us                                                               | 10.3 us: 1.03x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.44 sec: 1.03x faster                                                  |
| thrift                   | 1.26 ms                                                               | 1.25 ms: 1.01x faster                                                   |
| django_template          | 53.3 ms                                                               | 53.6 ms: 1.01x slower                                                   |
| meteor_contest           | 126 ms                                                                | 128 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.76 ms: 1.02x slower                                                   |
| pathlib                  | 26.3 ms                                                               | 26.8 ms: 1.02x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                    |
| sympy_str                | 329 ms                                                                | 339 ms: 1.03x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                   |
| nqueens                  | 117 ms                                                                | 125 ms: 1.06x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 227 ms: 1.07x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 75.1 ms: 1.08x slower                                                   |
| fannkuch                 | 546 ms                                                                | 590 ms: 1.08x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 170 ms: 1.09x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 110 ms: 1.10x slower                                                    |
| sympy_expand             | 543 ms                                                                | 606 ms: 1.12x slower                                                    |
| async_generators         | 452 ms                                                                | 515 ms: 1.14x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.70 sec: 1.14x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.34 sec: 1.17x slower                                                  |
| json                     | 5.88 ms                                                               | 6.86 ms: 1.17x slower                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.82 us: 1.17x slower                                                   |
| pidigits                 | 235 ms                                                                | 282 ms: 1.20x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 43.4 us: 1.23x slower                                                   |
| json_loads               | 30.9 us                                                               | 38.5 us: 1.24x slower                                                   |
| unpickle                 | 17.5 us                                                               | 22.6 us: 1.29x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| pickle_list              | 5.24 us                                                               | 7.08 us: 1.35x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 9.73 ms: 1.41x slower                                                   |
| python_startup           | 11.2 ms                                                               | 17.1 ms: 1.53x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.6 ms: 1.60x slower                                                   |
| pickle                   | 12.5 us                                                               | 20.5 us: 1.64x slower                                                   |
| coverage                 | 83.6 ms                                                               | 141 ms: 1.68x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.86 ms: 1.71x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.30 ms: 1.76x slower                                                   |
| logging_silent           | 222 ns                                                                | 946 ns: 4.26x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.40 sec: 371.85x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (4): unpickle_list, sympy_sum, scimark_fft, deepcopy_reduce
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.29% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.38x