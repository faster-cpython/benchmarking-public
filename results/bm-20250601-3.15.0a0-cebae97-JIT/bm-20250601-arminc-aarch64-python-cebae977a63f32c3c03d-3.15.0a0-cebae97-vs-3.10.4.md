# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.375x faster
- HPT reliability: 99.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 366 ms: 1.04x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                                  |
| html5lib       | 86.5 ms                                                               | 69.6 ms: 1.24x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 528 ms: 2.15x faster                                                    |
| async_tree_none         | 950 ms                                                                | 449 ms: 2.11x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 825 ms: 1.54x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.6 ms: 1.47x faster                                                   |
| nbody          | 166 ms                                                                | 138 ms: 1.20x faster                                                    |
| pidigits       | 235 ms                                                                | 276 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 226 ms: 1.14x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.69 sec: 1.25x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 311 us: 1.18x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 488 us: 1.08x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 105 ms: 1.05x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 227 ms: 1.07x slower                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 171 ms: 1.09x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 149 ms: 1.21x slower                                                    |
| json_loads           | 30.9 us                                                               | 38.0 us: 1.23x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 43.5 us: 1.24x slower                                                   |
| unpickle             | 17.5 us                                                               | 22.7 us: 1.30x slower                                                   |
| pickle_list          | 5.24 us                                                               | 7.08 us: 1.35x slower                                                   |
| pickle               | 12.5 us                                                               | 19.9 us: 1.59x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (2): unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.68 ms: 1.40x slower                                                   |
| python_startup         | 11.2 ms                                                               | 17.0 ms: 1.52x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 17.5 ms: 1.08x faster                                                   |
| genshi_text    | 35.2 ms                                                               | 32.9 ms: 1.07x faster                                                   |
| genshi_xml     | 69.8 ms                                                               | 75.9 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat           | 2.36 sec                                                              | 2.43 us: 970112.85x faster                                              |
| pprint_safe_repr         | 1.15 sec                                                              | 1.50 us: 763963.80x faster                                              |
| typing_runtime_protocols | 661 us                                                                | 262 us: 2.52x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 528 ms: 2.15x faster                                                    |
| async_tree_none          | 950 ms                                                                | 449 ms: 2.11x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.28 ms: 2.09x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.98 sec: 1.87x faster                                                  |
| richards                 | 91.7 ms                                                               | 51.6 ms: 1.78x faster                                                   |
| richards_super           | 107 ms                                                                | 61.4 ms: 1.75x faster                                                   |
| generators               | 68.1 ms                                                               | 40.0 ms: 1.70x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 566 ms: 1.67x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 825 ms: 1.54x faster                                                    |
| go                       | 264 ms                                                                | 172 ms: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 91.6 ms: 1.47x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| chaos                    | 121 ms                                                                | 83.9 ms: 1.44x faster                                                   |
| raytrace                 | 573 ms                                                                | 399 ms: 1.44x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 43.1 us: 1.43x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| pyflate                  | 795 ms                                                                | 598 ms: 1.33x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 97.3 ms: 1.31x faster                                                   |
| pylint                   | 485 ms                                                                | 375 ms: 1.30x faster                                                    |
| deepcopy                 | 511 us                                                                | 400 us: 1.28x faster                                                    |
| comprehensions           | 33.1 us                                                               | 26.5 us: 1.25x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.69 sec: 1.25x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 8.76 ms: 1.25x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 69.6 ms: 1.24x faster                                                   |
| spectral_norm            | 186 ms                                                                | 150 ms: 1.24x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 108 ms: 1.24x faster                                                    |
| scimark_lu               | 227 ms                                                                | 187 ms: 1.21x faster                                                    |
| nbody                    | 166 ms                                                                | 138 ms: 1.20x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 311 us: 1.18x faster                                                    |
| regex_dna                | 257 ms                                                                | 226 ms: 1.14x faster                                                    |
| coroutines               | 37.2 ms                                                               | 33.9 ms: 1.10x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 24.2 ms: 1.10x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 488 us: 1.08x faster                                                    |
| mako                     | 18.9 ms                                                               | 17.5 ms: 1.08x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 68.2 ms: 1.08x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 32.9 ms: 1.07x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                   |
| 2to3                     | 381 ms                                                                | 366 ms: 1.04x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.53 ms: 1.04x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.63 sec: 1.04x faster                                                  |
| logging_format           | 10.6 us                                                               | 10.2 us: 1.04x faster                                                   |
| logging_simple           | 9.78 us                                                               | 9.46 us: 1.03x faster                                                   |
| scimark_fft              | 500 ms                                                                | 489 ms: 1.02x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.51 us: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                                  |
| meteor_contest           | 126 ms                                                                | 130 ms: 1.03x slower                                                    |
| sympy_str                | 329 ms                                                                | 340 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.98 ms: 1.05x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 105 ms: 1.05x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 227 ms: 1.07x slower                                                    |
| fannkuch                 | 546 ms                                                                | 588 ms: 1.08x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 75.9 ms: 1.09x slower                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 171 ms: 1.09x slower                                                    |
| sympy_expand             | 543 ms                                                                | 622 ms: 1.15x slower                                                    |
| nqueens                  | 117 ms                                                                | 135 ms: 1.15x slower                                                    |
| json                     | 5.88 ms                                                               | 6.84 ms: 1.16x slower                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.81 us: 1.17x slower                                                   |
| pidigits                 | 235 ms                                                                | 276 ms: 1.18x slower                                                    |
| async_generators         | 452 ms                                                                | 542 ms: 1.20x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 149 ms: 1.21x slower                                                    |
| json_loads               | 30.9 us                                                               | 38.0 us: 1.23x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 43.5 us: 1.24x slower                                                   |
| unpickle                 | 17.5 us                                                               | 22.7 us: 1.30x slower                                                   |
| pickle_list              | 5.24 us                                                               | 7.08 us: 1.35x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 9.68 ms: 1.40x slower                                                   |
| python_startup           | 11.2 ms                                                               | 17.0 ms: 1.52x slower                                                   |
| pickle                   | 12.5 us                                                               | 19.9 us: 1.59x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.5 ms: 1.60x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.88 ms: 1.72x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.50 ms: 1.80x slower                                                   |
| logging_silent           | 222 ns                                                                | 898 ns: 4.04x slower                                                    |
| coverage                 | 83.6 ms                                                               | 729 ms: 8.72x slower                                                    |
| thrift                   | 1.26 ms                                                               | 200 ms: 158.80x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 2.87 sec: 197.30x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (5): sympy_sum, unpickle_list, json_dumps, django_template, pathlib
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.375x faster

# HPT report

- Reliability score: 99.41% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.40x