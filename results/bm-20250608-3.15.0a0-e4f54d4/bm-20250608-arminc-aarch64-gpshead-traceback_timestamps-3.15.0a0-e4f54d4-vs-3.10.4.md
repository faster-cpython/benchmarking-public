# Results vs. 3.10.4

- fork: gpshead
- ref: traceback_timestamps
- machine: linux-aarch64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.226x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.21x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 457 ms: 2.48x faster                                                     |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 650 ms: 1.96x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.5 ms: 1.56x faster                                                    |
| nbody          | 166 ms                                                                | 124 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.44x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 27.6 ms: 1.16x faster                                                    |
| regex_dna      | 257 ms                                                                | 232 ms: 1.11x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 381 us: 1.39x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 266 us: 1.37x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 80.8 ms: 1.23x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                    |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| django_template | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 457 ms: 2.48x faster                                                     |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.28x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                   |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 650 ms: 1.96x faster                                                     |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.88x faster                                                    |
| richards_super           | 107 ms                                                                | 59.9 ms: 1.79x faster                                                    |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                     |
| richards                 | 91.7 ms                                                               | 52.1 ms: 1.76x faster                                                    |
| chaos                    | 121 ms                                                                | 70.1 ms: 1.73x faster                                                    |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.65x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 79.2 ms: 1.61x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.88 ms: 1.59x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.6 ms: 1.58x faster                                                    |
| float                    | 135 ms                                                                | 86.5 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                     |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                     |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                     |
| spectral_norm            | 186 ms                                                                | 128 ms: 1.46x faster                                                     |
| regex_compile            | 177 ms                                                                | 122 ms: 1.44x faster                                                     |
| pyflate                  | 795 ms                                                                | 551 ms: 1.44x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 52.1 ms: 1.41x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 381 us: 1.39x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.37x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                                    |
| nbody                    | 166 ms                                                                | 124 ms: 1.33x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.48 us: 1.32x faster                                                    |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.29x faster                                                    |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.68 us: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.46 us: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.8 ms: 1.23x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.21x faster                                                   |
| sympy_str                | 329 ms                                                                | 275 ms: 1.20x faster                                                     |
| nqueens                  | 117 ms                                                                | 99.9 ms: 1.18x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| sympy_expand             | 543 ms                                                                | 464 ms: 1.17x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 27.6 ms: 1.16x faster                                                    |
| fannkuch                 | 546 ms                                                                | 469 ms: 1.16x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                    |
| scimark_fft              | 500 ms                                                                | 431 ms: 1.16x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 999 ms: 1.15x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.06 sec: 1.15x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.72 ms: 1.13x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                                    |
| regex_dna                | 257 ms                                                                | 232 ms: 1.11x faster                                                     |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.86 us: 1.07x faster                                                    |
| json                     | 5.88 ms                                                               | 5.70 ms: 1.03x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.37 ms: 1.10x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.90 ms: 1.66x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.82 ms: 1.69x slower                                                    |
| logging_silent           | 222 ns                                                                | 612 ns: 2.76x slower                                                     |
| coverage                 | 83.6 ms                                                               | 561 ms: 6.71x slower                                                     |
| thrift                   | 1.26 ms                                                               | 192 ms: 152.50x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (2): pidigits, async_generators
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.226x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.35x