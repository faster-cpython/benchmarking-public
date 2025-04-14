# Results vs. 3.10.4

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.451x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                       |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 607 ms: 2.91x faster                                         |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                         |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.5 ms: 1.68x faster                                        |
| nbody          | 154 ms                                                 | 93.8 ms: 1.64x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.41x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                         |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.09 ms: 1.18x faster                                        |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                       |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                         |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                        |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                        |
| json_loads           | 31.2 us                                                | 30.5 us: 1.02x faster                                        |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                        |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                        |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                        |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                         |
| async_tree_io            | 1.77 sec                                               | 607 ms: 2.91x faster                                         |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                        |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                         |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.53x faster                                        |
| go                       | 240 ms                                                 | 114 ms: 2.10x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                         |
| logging_silent           | 190 ns                                                 | 94.2 ns: 2.01x faster                                        |
| pylint                   | 551 ms                                                 | 275 ms: 2.00x faster                                         |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                        |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                         |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                        |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                         |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                         |
| richards                 | 79.3 ms                                                | 43.3 ms: 1.83x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                        |
| spectral_norm            | 170 ms                                                 | 97.8 ms: 1.74x faster                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                        |
| float                    | 117 ms                                                 | 69.5 ms: 1.68x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                        |
| nbody                    | 154 ms                                                 | 93.8 ms: 1.64x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                       |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.54x faster                                        |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                         |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                         |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                        |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                        |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                        |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                         |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                        |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                        |
| dulwich_log              | 84.3 ms                                                | 57.9 ms: 1.46x faster                                        |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                        |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                        |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.40x faster                                         |
| thrift                   | 1.07 ms                                                | 768 us: 1.39x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                        |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                        |
| scimark_fft              | 466 ms                                                 | 348 ms: 1.34x faster                                         |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                         |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                        |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                         |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                       |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.26x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                        |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                        |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                        |
| regex_effbot             | 3.63 ms                                                | 3.09 ms: 1.18x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                        |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                       |
| async_generators         | 444 ms                                                 | 391 ms: 1.13x faster                                         |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                         |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                        |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                        |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                         |
| json_loads               | 31.2 us                                                | 30.5 us: 1.02x faster                                        |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                        |
| coverage                 | 79.4 ms                                                | 91.7 ms: 1.15x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.65 ms: 1.28x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 82.8 ms: 3.45x slower                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                 |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-50dd66b/bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.451x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x