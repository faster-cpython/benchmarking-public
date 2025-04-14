# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: 54e07d1
- commit date: 2025-03-20
- overall geometric mean: 1.446x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                              |
| html5lib       | 88.9 ms                                                | 62.8 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.80x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.72x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                               |
| nbody          | 154 ms                                                 | 101 ms: 1.53x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.21 ms: 1.13x faster                                               |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                              |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.53x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                               |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                               |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.80x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.72x faster                                                |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                               |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.28x faster                                              |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                |
| pylint                   | 551 ms                                                 | 278 ms: 1.99x faster                                                |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                               |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.95x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.93x faster                                               |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                               |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.80x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 69.2 ms: 1.71x faster                                               |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.9 ms: 1.68x faster                                               |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                               |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                              |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                               |
| nbody                    | 154 ms                                                 | 101 ms: 1.53x faster                                                |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.53x faster                                               |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                               |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                               |
| dulwich_log              | 84.3 ms                                                | 58.7 ms: 1.44x faster                                               |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.8 ms: 1.41x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.69 ms: 1.38x faster                                               |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.34x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                |
| scimark_fft              | 466 ms                                                 | 355 ms: 1.31x faster                                                |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                               |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                               |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                               |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                |
| fannkuch                 | 532 ms                                                 | 436 ms: 1.22x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.21 ms: 1.13x faster                                               |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| async_generators         | 444 ms                                                 | 403 ms: 1.10x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                               |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                               |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                               |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                               |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.2 ms: 3.47x slower                                               |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250320-3.14.0a6+-54e07d1/bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.446x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x