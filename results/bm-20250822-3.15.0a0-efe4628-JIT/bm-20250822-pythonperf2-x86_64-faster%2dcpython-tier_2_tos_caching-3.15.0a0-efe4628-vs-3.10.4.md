# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                              |
| html5lib       | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                               |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 621 ms: 2.57x faster                                                                |
| async_tree_none         | 692 ms                                                       | 273 ms: 2.53x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 329 ms: 2.49x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 59.7 ms: 1.86x faster                                                               |
| nbody          | 134 ms                                                       | 86.9 ms: 1.54x faster                                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                        | 1.45x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.2 ms: 1.17x faster                                                               |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                                |
| regex_effbot   | 3.09 ms                                                      | 3.68 ms: 1.19x slower                                                               |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 192 us: 1.62x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                              |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                               |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.20x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 79.6 ms: 1.16x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 99.3 ms: 1.11x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.31x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.95 ms: 1.48x faster                                                               |
| django_template | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 22.6 ms: 1.39x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 54.8 ms: 1.15x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                                |
| deltablue                | 7.50 ms                                                      | 2.88 ms: 2.60x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 621 ms: 2.57x faster                                                                |
| async_tree_none          | 692 ms                                                       | 273 ms: 2.53x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 329 ms: 2.49x faster                                                                |
| richards_super           | 90.6 ms                                                      | 38.6 ms: 2.35x faster                                                               |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.34x faster                                                              |
| richards                 | 75.1 ms                                                      | 33.4 ms: 2.25x faster                                                               |
| go                       | 262 ms                                                       | 122 ms: 2.14x faster                                                                |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.97x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                                |
| float                    | 111 ms                                                       | 59.7 ms: 1.86x faster                                                               |
| chaos                    | 109 ms                                                       | 59.2 ms: 1.83x faster                                                               |
| logging_silent           | 167 ns                                                       | 92.2 ns: 1.81x faster                                                               |
| pyflate                  | 733 ms                                                       | 408 ms: 1.80x faster                                                                |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.79x faster                                                               |
| spectral_norm            | 139 ms                                                       | 79.4 ms: 1.75x faster                                                               |
| raytrace                 | 489 ms                                                       | 281 ms: 1.74x faster                                                                |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                               |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                                |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 64.0 ms: 1.68x faster                                                               |
| deepcopy                 | 468 us                                                       | 281 us: 1.67x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 192 us: 1.62x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 75.8 ms: 1.57x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 5.99 ms: 1.57x faster                                                               |
| nbody                    | 134 ms                                                       | 86.9 ms: 1.54x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                              |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                               |
| logging_simple           | 8.88 us                                                      | 5.91 us: 1.50x faster                                                               |
| mako                     | 14.7 ms                                                      | 9.95 ms: 1.48x faster                                                               |
| logging_format           | 9.64 us                                                      | 6.54 us: 1.47x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.48 sec: 1.46x faster                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 731 ms: 1.44x faster                                                                |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.18 sec: 1.41x faster                                                              |
| html5lib                 | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                               |
| thrift                   | 1.18 ms                                                      | 840 us: 1.40x faster                                                                |
| genshi_text              | 31.4 ms                                                      | 22.6 ms: 1.39x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                                |
| dulwich_log              | 81.1 ms                                                      | 59.0 ms: 1.38x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                               |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                                |
| deepcopy_reduce          | 4.01 us                                                      | 3.01 us: 1.33x faster                                                               |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                               |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                               |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                |
| nqueens                  | 115 ms                                                       | 92.9 ms: 1.24x faster                                                               |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                                |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                                |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.20x faster                                                               |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                              |
| regex_v8                 | 27.2 ms                                                      | 23.2 ms: 1.17x faster                                                               |
| xml_etree_generate       | 92.3 ms                                                      | 79.6 ms: 1.16x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 54.8 ms: 1.15x faster                                                               |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                                |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 99.3 ms: 1.11x faster                                                               |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                               |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.00 ms: 1.02x faster                                                               |
| async_generators         | 421 ms                                                       | 451 ms: 1.07x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.68 ms: 1.19x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                               |
| coverage                 | 63.3 ms                                                      | 79.0 ms: 1.25x slower                                                               |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.94 ms: 1.67x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.72 ms: 1.97x slower                                                               |
| telco                    | 7.23 ms                                                      | 158 ms: 21.79x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.41x