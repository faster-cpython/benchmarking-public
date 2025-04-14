# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.137x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 363 ms: 1.05x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.25 sec: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 74.1 ms: 1.17x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 885 ms: 2.58x faster                                                     |
| async_tree_none         | 950 ms                                                                | 415 ms: 2.29x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 499 ms: 2.27x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 679 ms: 1.87x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 102 ms: 1.32x faster                                                     |
| nbody          | 166 ms                                                                | 186 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 27.6 ms: 1.16x faster                                                    |
| regex_compile  | 177 ms                                                                | 161 ms: 1.09x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.96 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 246 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 441 us: 1.20x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 308 us: 1.19x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.09 sec: 1.09x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 16.0 ms: 1.04x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 98.0 ms: 1.02x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 7.30 us: 1.04x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.72 us: 1.09x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 135 ms: 1.10x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 40.2 us: 1.14x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.3 us: 1.16x slower                                                    |
| json_loads           | 30.9 us                                                               | 38.2 us: 1.24x slower                                                    |
| pickle               | 12.5 us                                                               | 15.5 us: 1.25x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 19.5 ms: 1.74x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 14.4 ms: 2.09x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.91x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 35.2 ms                                                               | 36.1 ms: 1.03x slower                                                    |
| genshi_xml     | 69.8 ms                                                               | 76.7 ms: 1.10x slower                                                    |
| mako           | 18.9 ms                                                               | 22.1 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 885 ms: 2.58x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 262 us: 2.52x faster                                                     |
| async_tree_none          | 950 ms                                                                | 415 ms: 2.29x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 499 ms: 2.27x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 679 ms: 1.87x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.98 ms: 1.79x faster                                                    |
| generators               | 68.1 ms                                                               | 41.2 ms: 1.65x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 584 ms: 1.62x faster                                                     |
| go                       | 264 ms                                                                | 171 ms: 1.54x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 2.72 ms: 1.53x faster                                                    |
| logging_silent           | 222 ns                                                                | 146 ns: 1.52x faster                                                     |
| scimark_sor              | 246 ms                                                                | 172 ms: 1.43x faster                                                     |
| chaos                    | 121 ms                                                                | 85.1 ms: 1.42x faster                                                    |
| raytrace                 | 573 ms                                                                | 406 ms: 1.41x faster                                                     |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.34x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.46 sec: 1.33x faster                                                   |
| float                    | 135 ms                                                                | 102 ms: 1.32x faster                                                     |
| richards                 | 91.7 ms                                                               | 70.6 ms: 1.30x faster                                                    |
| richards_super           | 107 ms                                                                | 82.8 ms: 1.30x faster                                                    |
| pylint                   | 485 ms                                                                | 375 ms: 1.29x faster                                                     |
| pyflate                  | 795 ms                                                                | 622 ms: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                    |
| deepcopy                 | 511 us                                                                | 412 us: 1.24x faster                                                     |
| comprehensions           | 33.1 us                                                               | 26.9 us: 1.23x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 59.7 ms: 1.23x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 50.4 us: 1.22x faster                                                    |
| scimark_lu               | 227 ms                                                                | 187 ms: 1.22x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.21x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 111 ms: 1.21x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 441 us: 1.20x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 308 us: 1.19x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.49 us: 1.18x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.31 ms: 1.17x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 74.1 ms: 1.17x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.6 ms: 1.16x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 110 ms: 1.16x faster                                                     |
| logging_simple           | 9.78 us                                                               | 8.54 us: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.57 us: 1.11x faster                                                    |
| regex_compile            | 177 ms                                                                | 161 ms: 1.09x faster                                                     |
| thrift                   | 1.26 ms                                                               | 1.16 ms: 1.09x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.09 sec: 1.09x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.25 sec: 1.09x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.10 ms: 1.07x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.96 ms: 1.07x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.35 us: 1.06x faster                                                    |
| 2to3                     | 381 ms                                                                | 363 ms: 1.05x faster                                                     |
| regex_dna                | 257 ms                                                                | 246 ms: 1.05x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 16.0 ms: 1.04x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.10 sec: 1.04x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.26 sec: 1.04x faster                                                   |
| scimark_fft              | 500 ms                                                                | 482 ms: 1.04x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 194 ms: 1.02x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 98.0 ms: 1.02x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.74 sec: 1.01x slower                                                   |
| sympy_sum                | 184 ms                                                                | 187 ms: 1.02x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 36.1 ms: 1.03x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 21.2 ms: 1.03x slower                                                    |
| unpickle_list            | 6.99 us                                                               | 7.30 us: 1.04x slower                                                    |
| sympy_str                | 329 ms                                                                | 354 ms: 1.08x slower                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.27 ms: 1.08x slower                                                    |
| sympy_expand             | 543 ms                                                                | 592 ms: 1.09x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.72 us: 1.09x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 135 ms: 1.10x slower                                                     |
| nqueens                  | 117 ms                                                                | 129 ms: 1.10x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 76.7 ms: 1.10x slower                                                    |
| json                     | 5.88 ms                                                               | 6.58 ms: 1.12x slower                                                    |
| nbody                    | 166 ms                                                                | 186 ms: 1.12x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 40.2 us: 1.14x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.84 ms: 1.15x slower                                                    |
| async_generators         | 452 ms                                                                | 525 ms: 1.16x slower                                                     |
| unpickle                 | 17.5 us                                                               | 20.3 us: 1.16x slower                                                    |
| mako                     | 18.9 ms                                                               | 22.1 ms: 1.17x slower                                                    |
| meteor_contest           | 126 ms                                                                | 151 ms: 1.19x slower                                                     |
| fannkuch                 | 546 ms                                                                | 652 ms: 1.20x slower                                                     |
| json_loads               | 30.9 us                                                               | 38.2 us: 1.24x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.5 us: 1.25x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.7 ms: 1.38x slower                                                    |
| coverage                 | 83.6 ms                                                               | 142 ms: 1.70x slower                                                     |
| python_startup           | 11.2 ms                                                               | 19.5 ms: 1.74x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 14.4 ms: 2.09x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 57.7 ms: 3.97x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (3): pidigits, sympy_integrate, django_template
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.60x