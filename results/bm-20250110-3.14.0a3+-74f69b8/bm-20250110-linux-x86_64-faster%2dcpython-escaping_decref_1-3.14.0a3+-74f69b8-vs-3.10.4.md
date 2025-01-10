# Results vs. 3.10.4

- fork: faster-cpython
- ref: escaping_decref_1
- machine: linux-x86_64
- commit hash: 74f69b8
- commit date: 2025-01-10
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                          |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                        |
| html5lib       | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                          |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 323 ms: 2.70x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 480 ms: 2.12x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                         |
| nbody          | 154 ms                                                 | 95.7 ms: 1.60x faster                                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                          |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                         |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                                         |
| json_loads           | 31.2 us                                                | 26.4 us: 1.18x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                         |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                         |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                          |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                         |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 323 ms: 2.70x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 480 ms: 2.12x faster                                                          |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                                          |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                          |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.91x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.0 ms: 1.90x faster                                                         |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                                          |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                          |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.81x faster                                                         |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                         |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                         |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                         |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.61x faster                                                          |
| nbody                    | 154 ms                                                 | 95.7 ms: 1.60x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                        |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                          |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                          |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                         |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                         |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                         |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                         |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                         |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.59 ms: 1.41x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                        |
| thrift                   | 1.07 ms                                                | 774 us: 1.38x faster                                                          |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                          |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                         |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                          |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                          |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 63.8 ms: 1.32x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 52.8 ms: 1.31x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                         |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                         |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                        |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                                         |
| json_loads               | 31.2 us                                                | 26.4 us: 1.18x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                         |
| json                     | 5.69 ms                                                | 4.89 ms: 1.16x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                          |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                          |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                         |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                         |
| async_generators         | 444 ms                                                 | 421 ms: 1.05x faster                                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                                         |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                  |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250110-3.14.0a3+-74f69b8/bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x