# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.17 sec: 1.11x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.9 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 880 ms: 2.60x faster                                                     |
| async_tree_none         | 950 ms                                                                | 387 ms: 2.45x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.41x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 663 ms: 1.92x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.3 ms: 1.58x faster                                                    |
| nbody          | 166 ms                                                                | 129 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 28.1 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                    |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 406 us: 1.30x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 288 us: 1.27x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 78.5 ms: 1.27x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.55 us: 1.07x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.65 us: 1.08x slower                                                    |
| json_loads           | 30.9 us                                                               | 34.0 us: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.11x slower                                                    |
| pickle               | 12.5 us                                                               | 15.9 us: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| django_template | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 222 us: 2.98x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 880 ms: 2.60x faster                                                     |
| async_tree_none          | 950 ms                                                                | 387 ms: 2.45x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.41x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.01 ms: 2.23x faster                                                    |
| richards_super           | 107 ms                                                                | 55.3 ms: 1.94x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 663 ms: 1.92x faster                                                     |
| generators               | 68.1 ms                                                               | 37.5 ms: 1.81x faster                                                    |
| richards                 | 91.7 ms                                                               | 51.0 ms: 1.80x faster                                                    |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 557 ms: 1.69x faster                                                     |
| chaos                    | 121 ms                                                                | 71.8 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                    |
| float                    | 135 ms                                                                | 85.3 ms: 1.58x faster                                                    |
| scimark_lu               | 227 ms                                                                | 144 ms: 1.57x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                   |
| pylint                   | 485 ms                                                                | 325 ms: 1.49x faster                                                     |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                                     |
| deepcopy                 | 511 us                                                                | 349 us: 1.46x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 87.6 ms: 1.46x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.92 us: 1.41x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.60 us: 1.39x faster                                                    |
| spectral_norm            | 186 ms                                                                | 134 ms: 1.39x faster                                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 63.9 ms: 1.35x faster                                                    |
| pyflate                  | 795 ms                                                                | 594 ms: 1.34x faster                                                     |
| thrift                   | 1.26 ms                                                               | 941 us: 1.34x faster                                                     |
| django_template          | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 102 ms: 1.32x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 151 ms: 1.31x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 406 us: 1.30x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 57.1 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| nbody                    | 166 ms                                                                | 129 ms: 1.28x faster                                                     |
| comprehensions           | 33.1 us                                                               | 26.0 us: 1.27x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.57 ms: 1.27x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 288 us: 1.27x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 78.5 ms: 1.27x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.7 ms: 1.23x faster                                                    |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.0 ms: 1.20x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.83 us: 1.20x faster                                                    |
| sympy_sum                | 184 ms                                                                | 153 ms: 1.20x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.43 sec: 1.18x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                    |
| sympy_str                | 329 ms                                                                | 283 ms: 1.16x faster                                                     |
| scimark_fft              | 500 ms                                                                | 435 ms: 1.15x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 28.1 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.17 sec: 1.11x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.74 us: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.98 ms: 1.09x faster                                                    |
| sympy_expand             | 543 ms                                                                | 498 ms: 1.09x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                    |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.55 us: 1.07x faster                                                    |
| nqueens                  | 117 ms                                                                | 112 ms: 1.05x faster                                                     |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.01x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                     |
| async_generators         | 452 ms                                                                | 478 ms: 1.06x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.65 us: 1.08x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.58 sec: 1.09x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.0 us: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.11x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.88 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.2 ms: 1.17x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.9 us: 1.27x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.58 ms: 1.58x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 814 ms: 56.01x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (4): unpickle, json, fannkuch, pidigits
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.33x