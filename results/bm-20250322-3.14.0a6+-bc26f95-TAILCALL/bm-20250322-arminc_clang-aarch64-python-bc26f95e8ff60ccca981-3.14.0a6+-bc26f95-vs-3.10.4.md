# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.352x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 290 ms: 1.31x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                   |
| html5lib       | 86.5 ms                                                               | 59.3 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 884 ms: 2.58x faster                                                     |
| async_tree_none         | 950 ms                                                                | 382 ms: 2.48x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 728 ms: 1.75x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.6 ms: 1.57x faster                                                    |
| nbody          | 166 ms                                                                | 119 ms: 1.40x faster                                                     |
| pidigits       | 235 ms                                                                | 293 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.44x faster                                                     |
| regex_dna      | 257 ms                                                                | 239 ms: 1.08x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.12 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 374 us: 1.41x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 259 us: 1.41x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 74.7 ms: 1.33x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.77 us: 1.21x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 104 ms: 1.18x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 204 ms: 1.04x faster                                                     |
| pickle_dict          | 35.1 us                                                               | 35.5 us: 1.01x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                    |
| pickle               | 12.5 us                                                               | 15.6 us: 1.25x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.6 ms: 1.19x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 190 us: 3.48x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 884 ms: 2.58x faster                                                     |
| async_tree_none          | 950 ms                                                                | 382 ms: 2.48x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.94 ms: 2.27x faster                                                    |
| go                       | 264 ms                                                                | 135 ms: 1.95x faster                                                     |
| richards_super           | 107 ms                                                                | 56.0 ms: 1.91x faster                                                    |
| logging_silent           | 222 ns                                                                | 116 ns: 1.91x faster                                                     |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                                    |
| richards                 | 91.7 ms                                                               | 49.5 ms: 1.85x faster                                                    |
| raytrace                 | 573 ms                                                                | 311 ms: 1.84x faster                                                     |
| chaos                    | 121 ms                                                                | 68.8 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 728 ms: 1.75x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 35.5 us: 1.74x faster                                                    |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.72x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 557 ms: 1.69x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 77.2 ms: 1.65x faster                                                    |
| deepcopy                 | 511 us                                                                | 310 us: 1.65x faster                                                     |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                    |
| pylint                   | 485 ms                                                                | 301 ms: 1.61x faster                                                     |
| spectral_norm            | 186 ms                                                                | 117 ms: 1.59x faster                                                     |
| float                    | 135 ms                                                                | 85.6 ms: 1.57x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 88.3 ms: 1.52x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.24 ms: 1.51x faster                                                    |
| pyflate                  | 795 ms                                                                | 530 ms: 1.50x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 59.3 ms: 1.46x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 50.6 ms: 1.45x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.44x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.89 us: 1.42x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.50 us: 1.41x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 374 us: 1.41x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 259 us: 1.41x faster                                                     |
| nbody                    | 166 ms                                                                | 119 ms: 1.40x faster                                                     |
| django_template          | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| thrift                   | 1.26 ms                                                               | 910 us: 1.38x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.34 us: 1.38x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 74.7 ms: 1.33x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                                    |
| 2to3                     | 381 ms                                                                | 290 ms: 1.31x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.7 ms: 1.31x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                                   |
| scimark_fft              | 500 ms                                                                | 395 ms: 1.27x faster                                                     |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 908 ms: 1.26x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.24x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.29 ms: 1.24x faster                                                    |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 5.77 us: 1.21x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.31 ms: 1.21x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 58.6 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 458 ms: 1.18x faster                                                     |
| nqueens                  | 117 ms                                                                | 99.2 ms: 1.18x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 104 ms: 1.18x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.19 sec: 1.16x faster                                                   |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                     |
| async_generators         | 452 ms                                                                | 416 ms: 1.09x faster                                                     |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                     |
| regex_dna                | 257 ms                                                                | 239 ms: 1.08x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 204 ms: 1.04x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.12 ms: 1.03x faster                                                    |
| pickle_dict              | 35.1 us                                                               | 35.5 us: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.43 ms: 1.11x slower                                                    |
| coverage                 | 83.6 ms                                                               | 95.7 ms: 1.14x slower                                                    |
| pidigits                 | 235 ms                                                                | 293 ms: 1.25x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.6 us: 1.25x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.51 ms: 1.57x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 3.25 sec: 223.46x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (2): unpickle, json
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.352x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.36x