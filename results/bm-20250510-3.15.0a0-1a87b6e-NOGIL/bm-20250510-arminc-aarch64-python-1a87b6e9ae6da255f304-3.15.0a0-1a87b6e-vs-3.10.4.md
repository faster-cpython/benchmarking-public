# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.174x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                                  |
| html5lib       | 86.5 ms                                                               | 69.0 ms: 1.25x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 869 ms: 2.63x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 484 ms: 2.34x faster                                                    |
| async_tree_none         | 950 ms                                                                | 416 ms: 2.28x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 681 ms: 1.87x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.26x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.1 ms: 1.42x faster                                                   |
| pidigits       | 235 ms                                                                | 232 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 150 ms: 1.17x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                   |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 438 us: 1.21x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 302 us: 1.21x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.88 sec: 1.17x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 16.3 ms: 1.03x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 101 ms: 1.01x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.72 us: 1.09x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 40.0 us: 1.14x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 144 ms: 1.17x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.5 us: 1.17x slower                                                   |
| pickle               | 12.5 us                                                               | 15.6 us: 1.25x slower                                                   |
| json_loads           | 30.9 us                                                               | 39.0 us: 1.26x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| python_startup         | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 75.7 ms: 1.08x slower                                                   |
| mako            | 18.9 ms                                                               | 21.4 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 869 ms: 2.63x faster                                                    |
| typing_runtime_protocols | 661 us                                                                | 261 us: 2.53x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 484 ms: 2.34x faster                                                    |
| async_tree_none          | 950 ms                                                                | 416 ms: 2.28x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.96 sec: 1.89x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.78 ms: 1.87x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 681 ms: 1.87x faster                                                    |
| generators               | 68.1 ms                                                               | 39.6 ms: 1.72x faster                                                   |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 583 ms: 1.62x faster                                                    |
| scimark_sor              | 246 ms                                                                | 161 ms: 1.52x faster                                                    |
| chaos                    | 121 ms                                                                | 80.1 ms: 1.51x faster                                                   |
| raytrace                 | 573 ms                                                                | 396 ms: 1.45x faster                                                    |
| gc_traversal             | 4.15 ms                                                               | 2.93 ms: 1.42x faster                                                   |
| float                    | 135 ms                                                                | 95.1 ms: 1.42x faster                                                   |
| richards_super           | 107 ms                                                                | 78.5 ms: 1.37x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 8.03 ms: 1.36x faster                                                   |
| spectral_norm            | 186 ms                                                                | 138 ms: 1.35x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.44 sec: 1.35x faster                                                  |
| richards                 | 91.7 ms                                                               | 68.5 ms: 1.34x faster                                                   |
| pyflate                  | 795 ms                                                                | 608 ms: 1.31x faster                                                    |
| scimark_lu               | 227 ms                                                                | 174 ms: 1.30x faster                                                    |
| pylint                   | 485 ms                                                                | 374 ms: 1.30x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 47.7 us: 1.29x faster                                                   |
| comprehensions           | 33.1 us                                                               | 25.6 us: 1.29x faster                                                   |
| deepcopy                 | 511 us                                                                | 401 us: 1.27x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 69.0 ms: 1.25x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.22x faster                                                  |
| coroutines               | 37.2 ms                                                               | 30.6 ms: 1.21x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 111 ms: 1.21x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 438 us: 1.21x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 302 us: 1.21x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 61.2 ms: 1.20x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 107 ms: 1.19x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.50 us: 1.18x faster                                                   |
| regex_compile            | 177 ms                                                                | 150 ms: 1.17x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.88 sec: 1.17x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                                  |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.07 sec: 1.07x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.20 sec: 1.07x faster                                                  |
| scimark_fft              | 500 ms                                                                | 469 ms: 1.07x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.19 ms: 1.06x faster                                                   |
| 2to3                     | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.34 us: 1.06x faster                                                   |
| logging_simple           | 9.78 us                                                               | 9.29 us: 1.05x faster                                                   |
| logging_format           | 10.6 us                                                               | 10.1 us: 1.05x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                                   |
| django_template          | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 25.7 ms: 1.03x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 16.3 ms: 1.03x faster                                                   |
| pidigits                 | 235 ms                                                                | 232 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.52 ms: 1.01x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 101 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| sympy_str                | 329 ms                                                                | 338 ms: 1.03x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 75.7 ms: 1.08x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.72 us: 1.09x slower                                                   |
| sympy_expand             | 543 ms                                                                | 597 ms: 1.10x slower                                                    |
| json                     | 5.88 ms                                                               | 6.48 ms: 1.10x slower                                                   |
| async_generators         | 452 ms                                                                | 501 ms: 1.11x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.4 ms: 1.13x slower                                                   |
| fannkuch                 | 546 ms                                                                | 619 ms: 1.13x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 40.0 us: 1.14x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.84 ms: 1.15x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 144 ms: 1.17x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.5 us: 1.17x slower                                                   |
| meteor_contest           | 126 ms                                                                | 150 ms: 1.19x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.6 us: 1.25x slower                                                   |
| json_loads               | 30.9 us                                                               | 39.0 us: 1.26x slower                                                   |
| telco                    | 8.49 ms                                                               | 11.2 ms: 1.32x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| python_startup           | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| coverage                 | 83.6 ms                                                               | 150 ms: 1.79x slower                                                    |
| logging_silent           | 222 ns                                                                | 763 ns: 3.44x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 61.6 ms: 4.24x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (5): nbody, genshi_text, sympy_sum, unpickle_list, nqueens
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.174x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.64x