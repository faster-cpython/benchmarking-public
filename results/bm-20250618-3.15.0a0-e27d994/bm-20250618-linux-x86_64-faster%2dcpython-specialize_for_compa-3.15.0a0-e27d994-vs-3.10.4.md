# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-x86_64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.460x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 595 ms: 2.97x faster                                                            |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.82x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 309 ms: 2.82x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.5 ms: 1.61x faster                                                           |
| nbody          | 154 ms                                                 | 98.5 ms: 1.56x faster                                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                            |
| regex_v8       | 27.8 ms                                                | 22.2 ms: 1.25x faster                                                           |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                            |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                           |
| django_template | 48.2 ms                                                | 32.9 ms: 1.46x faster                                                           |
| mako            | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 595 ms: 2.97x faster                                                            |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.82x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 309 ms: 2.82x faster                                                            |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.49 ms: 2.27x faster                                                           |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                           |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                            |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.6 ms: 1.91x faster                                                           |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                            |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                            |
| richards                 | 79.3 ms                                                | 43.3 ms: 1.83x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.79x faster                                                           |
| djangocms                | 38.4 us                                                | 21.8 us: 1.76x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.00 ms: 1.73x faster                                                           |
| spectral_norm            | 170 ms                                                 | 99.3 ms: 1.71x faster                                                           |
| pyflate                  | 716 ms                                                 | 419 ms: 1.71x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 76.4 ms: 1.67x faster                                                           |
| float                    | 117 ms                                                 | 72.5 ms: 1.61x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                          |
| nbody                    | 154 ms                                                 | 98.5 ms: 1.56x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                           |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                            |
| django_template          | 48.2 ms                                                | 32.9 ms: 1.46x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 58.8 ms: 1.43x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                          |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                            |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                           |
| logging_simple           | 8.30 us                                                | 6.05 us: 1.37x faster                                                           |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.37x faster                                                           |
| logging_format           | 9.09 us                                                | 6.65 us: 1.37x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                           |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                            |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.63 sec: 1.29x faster                                                          |
| scimark_fft              | 466 ms                                                 | 362 ms: 1.29x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.06 ms: 1.28x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 797 ms: 1.28x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                           |
| sympy_expand             | 566 ms                                                 | 449 ms: 1.26x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 22.2 ms: 1.25x faster                                                           |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                                            |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                           |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| coverage                 | 79.4 ms                                                | 87.8 ms: 1.11x slower                                                           |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.16x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.11 ms: 1.41x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                                           |
| logging_silent           | 190 ns                                                 | 469 ns: 2.47x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.460x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.31x