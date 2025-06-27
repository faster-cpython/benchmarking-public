# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                  |
| html5lib       | 86.5 ms                                                               | 62.3 ms: 1.39x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 665 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.1 ms: 1.56x faster                                                   |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.8 ms: 1.20x faster                                                   |
| regex_dna      | 257 ms                                                                | 227 ms: 1.13x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 384 us: 1.38x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.71 ms: 1.26x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                   |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.00 ms: 2.24x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| go                       | 264 ms                                                                | 130 ms: 2.04x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 665 ms: 1.91x faster                                                    |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                                   |
| richards_super           | 107 ms                                                                | 58.3 ms: 1.84x faster                                                   |
| raytrace                 | 573 ms                                                                | 328 ms: 1.75x faster                                                    |
| chaos                    | 121 ms                                                                | 69.6 ms: 1.74x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.1 ms: 1.73x faster                                                   |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.67x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.62x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 79.7 ms: 1.60x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 84.3 ms: 1.59x faster                                                   |
| float                    | 135 ms                                                                | 86.1 ms: 1.56x faster                                                   |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                    |
| pylint                   | 485 ms                                                                | 317 ms: 1.53x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.17 ms: 1.52x faster                                                   |
| pyflate                  | 795 ms                                                                | 533 ms: 1.49x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                    |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.44x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 62.3 ms: 1.39x faster                                                   |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 384 us: 1.38x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 54.0 ms: 1.36x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                  |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.55 us: 1.29x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.64 us: 1.28x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.39 us: 1.26x faster                                                   |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.22x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.8 ms: 1.20x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                  |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 466 ms: 1.17x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                   |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.16x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.04 sec: 1.15x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.01 sec: 1.14x faster                                                  |
| regex_dna                | 257 ms                                                                | 227 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.92 ms: 1.10x faster                                                   |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.78 us: 1.09x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.74 ms: 1.15x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.71 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.90 ms: 1.66x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.80 ms: 1.68x slower                                                   |
| logging_silent           | 222 ns                                                                | 623 ns: 2.80x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (3): json, pidigits, async_generators
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.35x