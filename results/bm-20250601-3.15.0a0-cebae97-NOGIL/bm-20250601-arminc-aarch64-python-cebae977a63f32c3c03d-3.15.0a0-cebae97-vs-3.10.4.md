# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.074x slower
- HPT reliability: 97.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 443 ms: 1.16x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.90 sec: 1.11x slower                                                  |
| html5lib       | 86.5 ms                                                               | 82.9 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.01 sec: 2.25x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 560 ms: 2.03x faster                                                    |
| async_tree_none         | 950 ms                                                                | 469 ms: 2.02x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 863 ms: 1.47x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 106 ms: 1.28x faster                                                    |
| nbody          | 166 ms                                                                | 191 ms: 1.15x slower                                                    |
| pidigits       | 235 ms                                                                | 279 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 231 ms: 1.11x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                   |
| regex_compile  | 177 ms                                                                | 197 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 3.61 sec: 1.07x slower                                                  |
| pickle_pure_python   | 529 us                                                                | 569 us: 1.08x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 232 ms: 1.09x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 402 us: 1.10x slower                                                    |
| unpickle_list        | 6.99 us                                                               | 7.78 us: 1.11x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 19.8 ms: 1.18x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 129 ms: 1.30x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 45.7 us: 1.30x slower                                                   |
| pickle_list          | 5.24 us                                                               | 7.20 us: 1.37x slower                                                   |
| json_loads           | 30.9 us                                                               | 44.6 us: 1.44x slower                                                   |
| unpickle             | 17.5 us                                                               | 26.5 us: 1.52x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 193 ms: 1.57x slower                                                    |
| pickle               | 12.5 us                                                               | 20.3 us: 1.63x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.25x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 13.7 ms: 1.99x slower                                                   |
| python_startup         | 11.2 ms                                                               | 22.9 ms: 2.05x slower                                                   |
| Geometric mean         | (ref)                                                                 | 2.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 23.7 ms: 1.25x slower                                                   |
| genshi_text     | 35.2 ms                                                               | 45.5 ms: 1.29x slower                                                   |
| django_template | 53.3 ms                                                               | 74.2 ms: 1.39x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 97.2 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.33x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 1.01 sec: 2.25x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 560 ms: 2.03x faster                                                    |
| async_tree_none          | 950 ms                                                                | 469 ms: 2.02x faster                                                    |
| typing_runtime_protocols | 661 us                                                                | 354 us: 1.87x faster                                                    |
| deltablue                | 8.94 ms                                                               | 5.57 ms: 1.61x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 625 ms: 1.51x faster                                                    |
| go                       | 264 ms                                                                | 176 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 863 ms: 1.47x faster                                                    |
| mdp                      | 3.70 sec                                                              | 2.55 sec: 1.45x faster                                                  |
| generators               | 68.1 ms                                                               | 47.8 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.53 sec: 1.30x faster                                                  |
| float                    | 135 ms                                                                | 106 ms: 1.28x faster                                                    |
| scimark_sor              | 246 ms                                                                | 200 ms: 1.23x faster                                                    |
| chaos                    | 121 ms                                                                | 103 ms: 1.18x faster                                                    |
| pyflate                  | 795 ms                                                                | 682 ms: 1.17x faster                                                    |
| raytrace                 | 573 ms                                                                | 498 ms: 1.15x faster                                                    |
| gc_traversal             | 4.15 ms                                                               | 3.68 ms: 1.13x faster                                                   |
| regex_dna                | 257 ms                                                                | 231 ms: 1.11x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.83 ms: 1.11x faster                                                   |
| comprehensions           | 33.1 us                                                               | 30.2 us: 1.10x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 57.2 us: 1.08x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                   |
| richards_super           | 107 ms                                                                | 100 ms: 1.07x faster                                                    |
| pylint                   | 485 ms                                                                | 459 ms: 1.06x faster                                                    |
| richards                 | 91.7 ms                                                               | 87.3 ms: 1.05x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 82.9 ms: 1.04x faster                                                   |
| scimark_lu               | 227 ms                                                                | 225 ms: 1.01x faster                                                    |
| spectral_norm            | 186 ms                                                                | 190 ms: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                    |
| deepcopy                 | 511 us                                                                | 530 us: 1.04x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 133 ms: 1.04x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.61 sec: 1.07x slower                                                  |
| pickle_pure_python       | 529 us                                                                | 569 us: 1.08x slower                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.43 us: 1.08x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 79.3 ms: 1.08x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.45 ms: 1.08x slower                                                   |
| xml_etree_parse          | 212 ms                                                                | 232 ms: 1.09x slower                                                    |
| crypto_pyaes             | 134 ms                                                                | 147 ms: 1.10x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 402 us: 1.10x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.90 sec: 1.11x slower                                                  |
| pathlib                  | 26.3 ms                                                               | 29.2 ms: 1.11x slower                                                   |
| unpickle_list            | 6.99 us                                                               | 7.78 us: 1.11x slower                                                   |
| regex_compile            | 177 ms                                                                | 197 ms: 1.12x slower                                                    |
| nbody                    | 166 ms                                                                | 191 ms: 1.15x slower                                                    |
| 2to3                     | 381 ms                                                                | 443 ms: 1.16x slower                                                    |
| scimark_fft              | 500 ms                                                                | 590 ms: 1.18x slower                                                    |
| logging_simple           | 9.78 us                                                               | 11.5 us: 1.18x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 19.8 ms: 1.18x slower                                                   |
| pidigits                 | 235 ms                                                                | 279 ms: 1.19x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 31.6 ms: 1.19x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 9.08 ms: 1.19x slower                                                   |
| logging_format           | 10.6 us                                                               | 12.8 us: 1.21x slower                                                   |
| meteor_contest           | 126 ms                                                                | 157 ms: 1.24x slower                                                    |
| mako                     | 18.9 ms                                                               | 23.7 ms: 1.25x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 2.00 ms: 1.26x slower                                                   |
| fannkuch                 | 546 ms                                                                | 701 ms: 1.28x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 45.5 ms: 1.29x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.63 ms: 1.30x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 129 ms: 1.30x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 45.7 us: 1.30x slower                                                   |
| sympy_sum                | 184 ms                                                                | 240 ms: 1.31x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 6.01 us: 1.31x slower                                                   |
| nqueens                  | 117 ms                                                                | 155 ms: 1.32x slower                                                    |
| sympy_str                | 329 ms                                                                | 450 ms: 1.37x slower                                                    |
| pickle_list              | 5.24 us                                                               | 7.20 us: 1.37x slower                                                   |
| json                     | 5.88 ms                                                               | 8.12 ms: 1.38x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 3.27 sec: 1.39x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.59 sec: 1.39x slower                                                  |
| django_template          | 53.3 ms                                                               | 74.2 ms: 1.39x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 97.2 ms: 1.39x slower                                                   |
| async_generators         | 452 ms                                                                | 632 ms: 1.40x slower                                                    |
| json_loads               | 30.9 us                                                               | 44.6 us: 1.44x slower                                                   |
| sympy_expand             | 543 ms                                                                | 785 ms: 1.45x slower                                                    |
| unpickle                 | 17.5 us                                                               | 26.5 us: 1.52x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 193 ms: 1.57x slower                                                    |
| pickle                   | 12.5 us                                                               | 20.3 us: 1.63x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 13.7 ms: 1.99x slower                                                   |
| python_startup           | 11.2 ms                                                               | 22.9 ms: 2.05x slower                                                   |
| telco                    | 8.49 ms                                                               | 17.9 ms: 2.11x slower                                                   |
| coverage                 | 83.6 ms                                                               | 184 ms: 2.20x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 72.0 ms: 4.95x slower                                                   |
| logging_silent           | 222 ns                                                                | 1.20 us: 5.39x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.11x slower                                                            |

Benchmark hidden because not significant (4): regex_effbot, xml_etree_iterparse, pycparser, coroutines
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.074x slower

# HPT report

- Reliability score: 97.14% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.71x