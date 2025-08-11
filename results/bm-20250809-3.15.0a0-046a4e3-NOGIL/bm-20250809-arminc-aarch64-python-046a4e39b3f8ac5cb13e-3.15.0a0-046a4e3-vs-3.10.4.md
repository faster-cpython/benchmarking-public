# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.140x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 352 ms: 1.08x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                                  |
| html5lib       | 86.5 ms                                                               | 69.9 ms: 1.24x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 867 ms: 2.64x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 475 ms: 2.39x faster                                                    |
| async_tree_none         | 950 ms                                                                | 400 ms: 2.38x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 668 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.0 ms: 1.42x faster                                                   |
| nbody          | 166 ms                                                                | 181 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 26.9 ms: 1.19x faster                                                   |
| regex_compile  | 177 ms                                                                | 148 ms: 1.19x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                                   |
| regex_dna      | 257 ms                                                                | 241 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 299 us: 1.22x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 437 us: 1.21x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 131 ms: 1.19x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.87 sec: 1.17x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.74 us: 1.09x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.7 us: 1.10x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 142 ms: 1.15x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.2 us: 1.16x slower                                                   |
| json_loads           | 30.9 us                                                               | 36.4 us: 1.18x slower                                                   |
| pickle               | 12.5 us                                                               | 15.7 us: 1.25x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| python_startup         | 11.2 ms                                                               | 19.9 ms: 1.78x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.76x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 35.2 ms                                                               | 35.8 ms: 1.02x slower                                                   |
| genshi_xml     | 69.8 ms                                                               | 76.4 ms: 1.09x slower                                                   |
| mako           | 18.9 ms                                                               | 21.0 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 250 us: 2.65x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 867 ms: 2.64x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 475 ms: 2.39x faster                                                    |
| async_tree_none          | 950 ms                                                                | 400 ms: 2.38x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.94 sec: 1.91x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 668 ms: 1.91x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.85 ms: 1.84x faster                                                   |
| go                       | 264 ms                                                                | 153 ms: 1.73x faster                                                    |
| generators               | 68.1 ms                                                               | 40.9 ms: 1.67x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 568 ms: 1.66x faster                                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                    |
| chaos                    | 121 ms                                                                | 80.0 ms: 1.51x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 2.85 ms: 1.46x faster                                                   |
| raytrace                 | 573 ms                                                                | 396 ms: 1.45x faster                                                    |
| float                    | 135 ms                                                                | 95.0 ms: 1.42x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.2 us: 1.37x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.98 ms: 1.37x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.41 sec: 1.36x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 45.5 us: 1.36x faster                                                   |
| pyflate                  | 795 ms                                                                | 595 ms: 1.34x faster                                                    |
| deepcopy                 | 511 us                                                                | 386 us: 1.32x faster                                                    |
| richards_super           | 107 ms                                                                | 81.2 ms: 1.32x faster                                                   |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                    |
| richards                 | 91.7 ms                                                               | 70.6 ms: 1.30x faster                                                   |
| pylint                   | 485 ms                                                                | 381 ms: 1.27x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 69.9 ms: 1.24x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 104 ms: 1.23x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 59.7 ms: 1.23x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 109 ms: 1.23x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 299 us: 1.22x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 437 us: 1.21x faster                                                    |
| scimark_lu               | 227 ms                                                                | 188 ms: 1.21x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.17 us: 1.20x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.9 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 131 ms: 1.19x faster                                                    |
| regex_compile            | 177 ms                                                                | 148 ms: 1.19x faster                                                    |
| coroutines               | 37.2 ms                                                               | 31.4 ms: 1.18x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.87 sec: 1.17x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.52 us: 1.17x faster                                                   |
| logging_format           | 10.6 us                                                               | 9.14 us: 1.16x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.16 sec: 1.09x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.05 sec: 1.09x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 4.21 us: 1.09x faster                                                   |
| 2to3                     | 381 ms                                                                | 352 ms: 1.08x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                                   |
| thrift                   | 1.26 ms                                                               | 1.18 ms: 1.07x faster                                                   |
| regex_dna                | 257 ms                                                                | 241 ms: 1.07x faster                                                    |
| scimark_fft              | 500 ms                                                                | 471 ms: 1.06x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 25.6 ms: 1.04x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 35.8 ms: 1.02x slower                                                   |
| sympy_str                | 329 ms                                                                | 342 ms: 1.04x slower                                                    |
| json                     | 5.88 ms                                                               | 6.30 ms: 1.07x slower                                                   |
| fannkuch                 | 546 ms                                                                | 593 ms: 1.09x slower                                                    |
| sympy_expand             | 543 ms                                                                | 591 ms: 1.09x slower                                                    |
| nbody                    | 166 ms                                                                | 181 ms: 1.09x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 76.4 ms: 1.09x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.74 us: 1.09x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.7 us: 1.10x slower                                                   |
| meteor_contest           | 126 ms                                                                | 140 ms: 1.11x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.0 ms: 1.11x slower                                                   |
| async_generators         | 452 ms                                                                | 515 ms: 1.14x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 142 ms: 1.15x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.2 us: 1.16x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.86 ms: 1.17x slower                                                   |
| json_loads               | 30.9 us                                                               | 36.4 us: 1.18x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.25x slower                                                   |
| coverage                 | 83.6 ms                                                               | 144 ms: 1.73x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| python_startup           | 11.2 ms                                                               | 19.9 ms: 1.78x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 66.8 ms: 4.59x slower                                                   |
| telco                    | 8.49 ms                                                               | 187 ms: 22.04x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (8): django_template, unpickle_list, pidigits, create_gc_cycles, nqueens, xml_etree_process, sympy_sum, scimark_sparse_mat_mult
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.140x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.67x