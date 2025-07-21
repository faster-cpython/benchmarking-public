# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                              |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                               |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 625 ms: 2.56x faster                                                                |
| async_tree_none         | 692 ms                                                       | 274 ms: 2.52x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 331 ms: 2.48x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 61.5 ms: 1.81x faster                                                               |
| nbody          | 134 ms                                                       | 88.8 ms: 1.51x faster                                                               |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                        | 1.43x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                               |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 204 us: 1.53x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                              |
| pickle_pure_python   | 455 us                                                       | 338 us: 1.35x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 58.2 ms: 1.31x faster                                                               |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                               |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 96.4 ms: 1.15x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 83.2 ms: 1.11x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.70 ms: 1.19x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                               |
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 54.5 ms: 1.16x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                                |
| deltablue                | 7.50 ms                                                      | 2.92 ms: 2.57x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 625 ms: 2.56x faster                                                                |
| async_tree_none          | 692 ms                                                       | 274 ms: 2.52x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 331 ms: 2.48x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.34x faster                                                              |
| richards_super           | 90.6 ms                                                      | 41.6 ms: 2.18x faster                                                               |
| richards                 | 75.1 ms                                                      | 35.5 ms: 2.12x faster                                                               |
| go                       | 262 ms                                                       | 126 ms: 2.08x faster                                                                |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                                |
| float                    | 111 ms                                                       | 61.5 ms: 1.81x faster                                                               |
| chaos                    | 109 ms                                                       | 60.1 ms: 1.81x faster                                                               |
| logging_silent           | 167 ns                                                       | 93.3 ns: 1.79x faster                                                               |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                                |
| spectral_norm            | 139 ms                                                       | 79.4 ms: 1.75x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 28.4 us: 1.75x faster                                                               |
| pyflate                  | 733 ms                                                       | 423 ms: 1.73x faster                                                                |
| scimark_lu               | 167 ms                                                       | 96.4 ms: 1.73x faster                                                               |
| deepcopy                 | 468 us                                                       | 278 us: 1.69x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 64.0 ms: 1.68x faster                                                               |
| raytrace                 | 489 ms                                                       | 292 ms: 1.67x faster                                                                |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 204 us: 1.53x faster                                                                |
| nbody                    | 134 ms                                                       | 88.8 ms: 1.51x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 79.0 ms: 1.51x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                              |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 6.28 ms: 1.50x faster                                                               |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                               |
| django_template          | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                               |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.53 sec: 1.41x faster                                                              |
| logging_simple           | 8.88 us                                                      | 6.32 us: 1.41x faster                                                               |
| thrift                   | 1.18 ms                                                      | 837 us: 1.40x faster                                                                |
| logging_format           | 9.64 us                                                      | 6.87 us: 1.40x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 753 ms: 1.39x faster                                                                |
| dulwich_log              | 81.1 ms                                                      | 59.7 ms: 1.36x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                              |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 338 us: 1.35x faster                                                                |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 58.2 ms: 1.31x faster                                                               |
| fannkuch                 | 483 ms                                                       | 370 ms: 1.30x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                               |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.25x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                               |
| nqueens                  | 115 ms                                                       | 92.6 ms: 1.24x faster                                                               |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                                |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                               |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                                |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 54.5 ms: 1.16x faster                                                               |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                              |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 96.4 ms: 1.15x faster                                                               |
| meteor_contest           | 138 ms                                                       | 123 ms: 1.12x faster                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 83.2 ms: 1.11x faster                                                               |
| regex_v8                 | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                                               |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                               |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.91 ms: 1.04x faster                                                               |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                                |
| async_generators         | 421 ms                                                       | 447 ms: 1.06x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.70 ms: 1.19x slower                                                               |
| coverage                 | 63.3 ms                                                      | 78.7 ms: 1.24x slower                                                               |
| python_startup           | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.85 ms: 1.62x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.90x slower                                                               |
| telco                    | 7.23 ms                                                      | 160 ms: 22.13x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250721-3.15.0a0-53a50eb-JIT/bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.41x