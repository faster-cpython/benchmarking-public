# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 296 ms: 1.29x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 882 ms: 2.59x faster                                                     |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 659 ms: 1.93x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.7 ms: 1.54x faster                                                    |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 27.9 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.95 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.36x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 273 us: 1.34x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 174 ms: 1.21x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.60 us: 1.06x faster                                                    |
| unpickle             | 17.5 us                                                               | 17.9 us: 1.03x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.74 us: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.7 us: 1.10x slower                                                    |
| json_loads           | 30.9 us                                                               | 34.3 us: 1.11x slower                                                    |
| pickle               | 12.5 us                                                               | 16.1 us: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.08x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.2 ms: 1.34x faster                                                    |
| django_template | 53.3 ms                                                               | 40.4 ms: 1.32x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.2 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.39x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 882 ms: 2.59x faster                                                     |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.90 ms: 2.29x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 659 ms: 1.93x faster                                                     |
| go                       | 264 ms                                                                | 137 ms: 1.93x faster                                                     |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.84x faster                                                    |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.81x faster                                                    |
| raytrace                 | 573 ms                                                                | 318 ms: 1.80x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 546 ms: 1.73x faster                                                     |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                     |
| chaos                    | 121 ms                                                                | 71.0 ms: 1.70x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.0 ms: 1.70x faster                                                    |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                     |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                                    |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                                     |
| float                    | 135 ms                                                                | 87.7 ms: 1.54x faster                                                    |
| pylint                   | 485 ms                                                                | 317 ms: 1.53x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 84.1 ms: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 342 us: 1.49x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 90.0 ms: 1.49x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.41 ms: 1.47x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 51.8 ms: 1.42x faster                                                    |
| pyflate                  | 795 ms                                                                | 572 ms: 1.39x faster                                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.05 us: 1.39x faster                                                    |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.36x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 273 us: 1.34x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.34x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| django_template          | 53.3 ms                                                               | 40.4 ms: 1.32x faster                                                    |
| thrift                   | 1.26 ms                                                               | 967 us: 1.30x faster                                                     |
| 2to3                     | 381 ms                                                                | 296 ms: 1.29x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.59 us: 1.28x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                    |
| sympy_str                | 329 ms                                                                | 266 ms: 1.23x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 174 ms: 1.21x faster                                                     |
| sympy_sum                | 184 ms                                                                | 153 ms: 1.20x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.20x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 965 ms: 1.19x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| scimark_fft              | 500 ms                                                                | 429 ms: 1.17x faster                                                     |
| sympy_expand             | 543 ms                                                                | 467 ms: 1.16x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 60.2 ms: 1.16x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.9 ms: 1.15x faster                                                    |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.85 ms: 1.11x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.76 us: 1.09x faster                                                    |
| fannkuch                 | 546 ms                                                                | 507 ms: 1.08x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.95 ms: 1.07x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.60 us: 1.06x faster                                                    |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                     |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                     |
| unpickle                 | 17.5 us                                                               | 17.9 us: 1.03x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.74 us: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.7 us: 1.10x slower                                                    |
| json_loads               | 30.9 us                                                               | 34.3 us: 1.11x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.6 ms: 1.18x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.1 us: 1.29x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.68 ms: 1.61x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.82 ms: 1.69x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.75 sec: 188.96x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                             |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x