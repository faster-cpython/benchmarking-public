# Results vs. 3.10.4

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 2d69c9f
- commit date: 2025-03-25
- overall geometric mean: 1.443x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                       |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                         |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 318 ms: 2.73x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                         |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                        |
| nbody          | 154 ms                                                 | 96.4 ms: 1.59x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.40x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                         |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.19 ms: 1.14x faster                                        |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                  | 1.21x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                       |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                         |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.51x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                        |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                        |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.52x faster                                        |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                        |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                        |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                         |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                         |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                         |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 318 ms: 2.73x faster                                         |
| deltablue                | 7.91 ms                                                | 3.09 ms: 2.56x faster                                        |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                        |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                         |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                        |
| logging_silent           | 190 ns                                                 | 98.6 ns: 1.92x faster                                        |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                         |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.91x faster                                        |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                         |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                         |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                        |
| spectral_norm            | 170 ms                                                 | 98.4 ms: 1.73x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.9 ms: 1.71x faster                                        |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 76.1 ms: 1.68x faster                                        |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.66x faster                                        |
| nbody                    | 154 ms                                                 | 96.4 ms: 1.59x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                       |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                        |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                         |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                         |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.52x faster                                        |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.51x faster                                         |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.51x faster                                        |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                        |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                        |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                        |
| dulwich_log              | 84.3 ms                                                | 58.4 ms: 1.44x faster                                        |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                         |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                       |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.37x faster                                        |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                        |
| scimark_fft              | 466 ms                                                 | 344 ms: 1.35x faster                                         |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                        |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                        |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                         |
| nqueens                  | 106 ms                                                 | 82.7 ms: 1.28x faster                                        |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                       |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                        |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                         |
| fannkuch                 | 532 ms                                                 | 431 ms: 1.23x faster                                         |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                        |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                        |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                       |
| regex_effbot             | 3.63 ms                                                | 3.19 ms: 1.14x faster                                        |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                         |
| async_generators         | 444 ms                                                 | 396 ms: 1.12x faster                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                         |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                        |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                        |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                        |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                        |
| coverage                 | 79.4 ms                                                | 91.4 ms: 1.15x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                        |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.39x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                 |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250325-3.14.0a6+-2d69c9f/bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.443x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x