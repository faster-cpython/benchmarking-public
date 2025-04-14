# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-x86_64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.433x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 611 ms: 2.90x faster                                                            |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.76x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.0 ms: 1.65x faster                                                           |
| nbody          | 154 ms                                                 | 96.4 ms: 1.59x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                           |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                            |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                           |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                           |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 611 ms: 2.90x faster                                                            |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                            |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.76x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                           |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                            |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                           |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.92x faster                                                           |
| logging_silent           | 190 ns                                                 | 99.9 ns: 1.90x faster                                                           |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                           |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                            |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                            |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                            |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                           |
| spectral_norm            | 170 ms                                                 | 99.8 ms: 1.70x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 76.3 ms: 1.68x faster                                                           |
| float                    | 117 ms                                                 | 71.0 ms: 1.65x faster                                                           |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                            |
| nbody                    | 154 ms                                                 | 96.4 ms: 1.59x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                          |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                           |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                           |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                           |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                           |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 58.4 ms: 1.44x faster                                                           |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                                           |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 746 ms: 1.36x faster                                                            |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                           |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| scimark_fft              | 466 ms                                                 | 352 ms: 1.32x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                            |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                          |
| async_generators         | 444 ms                                                 | 391 ms: 1.14x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                            |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                           |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                           |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                            |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                           |
| coverage                 | 79.4 ms                                                | 91.9 ms: 1.16x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.38x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 83.2 ms: 3.46x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                    |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.433x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x