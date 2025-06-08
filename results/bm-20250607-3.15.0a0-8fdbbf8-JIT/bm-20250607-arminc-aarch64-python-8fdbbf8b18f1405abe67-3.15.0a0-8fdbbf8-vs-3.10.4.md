# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.051x slower
- HPT reliability: 96.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 369 ms: 1.03x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                                  |
| html5lib       | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.02 sec: 2.25x faster                                                  |
| async_tree_none         | 950 ms                                                                | 445 ms: 2.13x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 532 ms: 2.13x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 823 ms: 1.55x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 92.8 ms: 1.45x faster                                                   |
| nbody          | 166 ms                                                                | 143 ms: 1.16x faster                                                    |
| pidigits       | 235 ms                                                                | 279 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 227 ms: 1.13x faster                                                    |
| regex_compile  | 177 ms                                                                | 157 ms: 1.12x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                                   |
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.72 sec: 1.23x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 307 us: 1.19x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 478 us: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.72 us: 1.04x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 17.2 ms: 1.03x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 104 ms: 1.04x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 227 ms: 1.07x slower                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 170 ms: 1.09x slower                                                    |
| json_loads           | 30.9 us                                                               | 37.9 us: 1.23x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 43.2 us: 1.23x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 154 ms: 1.26x slower                                                    |
| unpickle             | 17.5 us                                                               | 22.5 us: 1.29x slower                                                   |
| pickle_list          | 5.24 us                                                               | 7.11 us: 1.36x slower                                                   |
| pickle               | 12.5 us                                                               | 20.1 us: 1.61x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.71 ms: 1.41x slower                                                   |
| python_startup         | 11.2 ms                                                               | 17.0 ms: 1.52x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 16.5 ms: 1.15x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.8 ms: 1.04x faster                                                   |
| django_template | 53.3 ms                                                               | 53.8 ms: 1.01x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 79.4 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 280 us: 2.36x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.02 sec: 2.25x faster                                                  |
| async_tree_none          | 950 ms                                                                | 445 ms: 2.13x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 532 ms: 2.13x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.44 ms: 2.02x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.99 sec: 1.86x faster                                                  |
| richards                 | 91.7 ms                                                               | 51.7 ms: 1.77x faster                                                   |
| richards_super           | 107 ms                                                                | 60.8 ms: 1.76x faster                                                   |
| generators               | 68.1 ms                                                               | 39.6 ms: 1.72x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 569 ms: 1.66x faster                                                    |
| go                       | 264 ms                                                                | 170 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 823 ms: 1.55x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.46x faster                                                  |
| float                    | 135 ms                                                                | 92.8 ms: 1.45x faster                                                   |
| raytrace                 | 573 ms                                                                | 401 ms: 1.43x faster                                                    |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.41x faster                                                    |
| chaos                    | 121 ms                                                                | 86.2 ms: 1.40x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 44.8 us: 1.38x faster                                                   |
| pyflate                  | 795 ms                                                                | 592 ms: 1.34x faster                                                    |
| comprehensions           | 33.1 us                                                               | 25.2 us: 1.31x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 98.5 ms: 1.30x faster                                                   |
| pylint                   | 485 ms                                                                | 380 ms: 1.28x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.74 ms: 1.25x faster                                                   |
| deepcopy                 | 511 us                                                                | 410 us: 1.24x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 108 ms: 1.24x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.72 sec: 1.23x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                   |
| scimark_lu               | 227 ms                                                                | 186 ms: 1.22x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 307 us: 1.19x faster                                                    |
| spectral_norm            | 186 ms                                                                | 157 ms: 1.18x faster                                                    |
| nbody                    | 166 ms                                                                | 143 ms: 1.16x faster                                                    |
| mako                     | 18.9 ms                                                               | 16.5 ms: 1.15x faster                                                   |
| regex_dna                | 257 ms                                                                | 227 ms: 1.13x faster                                                    |
| regex_compile            | 177 ms                                                                | 157 ms: 1.12x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 478 us: 1.11x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 24.2 ms: 1.10x faster                                                   |
| coroutines               | 37.2 ms                                                               | 34.0 ms: 1.09x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 67.4 ms: 1.09x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.52 ms: 1.05x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.61 sec: 1.05x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.72 us: 1.04x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 33.8 ms: 1.04x faster                                                   |
| scimark_fft              | 500 ms                                                                | 482 ms: 1.04x faster                                                    |
| 2to3                     | 381 ms                                                                | 369 ms: 1.03x faster                                                    |
| logging_simple           | 9.78 us                                                               | 9.57 us: 1.02x faster                                                   |
| logging_format           | 10.6 us                                                               | 10.4 us: 1.02x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.55 us: 1.01x faster                                                   |
| django_template          | 53.3 ms                                                               | 53.8 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.77 ms: 1.02x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 17.2 ms: 1.03x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                                  |
| xml_etree_process        | 99.5 ms                                                               | 104 ms: 1.04x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 27.8 ms: 1.06x slower                                                   |
| meteor_contest           | 126 ms                                                                | 134 ms: 1.06x slower                                                    |
| sympy_str                | 329 ms                                                                | 348 ms: 1.06x slower                                                    |
| fannkuch                 | 546 ms                                                                | 581 ms: 1.06x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 227 ms: 1.07x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 170 ms: 1.09x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 79.4 ms: 1.14x slower                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.70 us: 1.14x slower                                                   |
| sympy_expand             | 543 ms                                                                | 628 ms: 1.16x slower                                                    |
| nqueens                  | 117 ms                                                                | 136 ms: 1.16x slower                                                    |
| json                     | 5.88 ms                                                               | 6.93 ms: 1.18x slower                                                   |
| pidigits                 | 235 ms                                                                | 279 ms: 1.19x slower                                                    |
| async_generators         | 452 ms                                                                | 540 ms: 1.19x slower                                                    |
| json_loads               | 30.9 us                                                               | 37.9 us: 1.23x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 43.2 us: 1.23x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 154 ms: 1.26x slower                                                    |
| unpickle                 | 17.5 us                                                               | 22.5 us: 1.29x slower                                                   |
| pickle_list              | 5.24 us                                                               | 7.11 us: 1.36x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 3.26 sec: 1.38x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.59 sec: 1.38x slower                                                  |
| python_startup_no_site   | 6.89 ms                                                               | 9.71 ms: 1.41x slower                                                   |
| python_startup           | 11.2 ms                                                               | 17.0 ms: 1.52x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.2 ms: 1.55x slower                                                   |
| pickle                   | 12.5 us                                                               | 20.1 us: 1.61x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.39 ms: 1.78x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 4.04 ms: 1.79x slower                                                   |
| logging_silent           | 222 ns                                                                | 948 ns: 4.27x slower                                                    |
| coverage                 | 83.6 ms                                                               | 720 ms: 8.62x slower                                                    |
| thrift                   | 1.26 ms                                                               | 197 ms: 156.62x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 3.45 sec: 237.22x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (1): sympy_sum
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.051x slower

# HPT report

- Reliability score: 96.24% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.41x