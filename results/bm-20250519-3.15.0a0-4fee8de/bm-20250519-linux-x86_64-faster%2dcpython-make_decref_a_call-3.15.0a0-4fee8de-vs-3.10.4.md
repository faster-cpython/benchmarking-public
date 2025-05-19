# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.384x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                          |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                        |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                          |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.71x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 505 ms: 2.01x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                         |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                          |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                          |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                         |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 337 us: 1.44x faster                                                          |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 64.1 ms: 1.24x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 91.2 ms: 1.09x faster                                                         |
| json_loads           | 31.2 us                                                | 31.5 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                         |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                         |
| mako            | 16.3 ms                                                | 12.0 ms: 1.36x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 175 us: 3.10x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                          |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.71x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                          |
| generators               | 80.1 ms                                                | 31.8 ms: 2.52x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.53 ms: 2.24x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.29 sec: 2.21x faster                                                        |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 505 ms: 2.01x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                         |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                          |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                         |
| richards_super           | 94.7 ms                                                | 51.1 ms: 1.85x faster                                                         |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                          |
| richards                 | 79.3 ms                                                | 44.4 ms: 1.79x faster                                                         |
| deepcopy                 | 479 us                                                 | 270 us: 1.78x faster                                                          |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 70.0 ms: 1.69x faster                                                         |
| djangocms                | 38.4 us                                                | 23.0 us: 1.67x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 77.3 ms: 1.65x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.62x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.42 ms: 1.62x faster                                                         |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                         |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.58x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                        |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                          |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                          |
| scimark_lu               | 176 ms                                                 | 121 ms: 1.46x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.89 us: 1.45x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 337 us: 1.44x faster                                                          |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                          |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                         |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                                         |
| coroutines               | 35.1 ms                                                | 25.3 ms: 1.39x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                         |
| mako                     | 16.3 ms                                                | 12.0 ms: 1.36x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 769 ms: 1.32x faster                                                          |
| thrift                   | 1.07 ms                                                | 811 us: 1.32x faster                                                          |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                          |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                          |
| logging_simple           | 8.30 us                                                | 6.47 us: 1.28x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                         |
| logging_format           | 9.09 us                                                | 7.19 us: 1.26x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                         |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 64.1 ms: 1.24x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.27 ms: 1.23x faster                                                         |
| nqueens                  | 106 ms                                                 | 87.0 ms: 1.22x faster                                                         |
| scimark_fft              | 466 ms                                                 | 385 ms: 1.21x faster                                                          |
| fannkuch                 | 532 ms                                                 | 440 ms: 1.21x faster                                                          |
| sympy_expand             | 566 ms                                                 | 473 ms: 1.20x faster                                                          |
| python_startup           | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                         |
| pathlib                  | 20.5 ms                                                | 17.5 ms: 1.17x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 91.2 ms: 1.09x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 913 us: 1.08x faster                                                          |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                         |
| async_generators         | 444 ms                                                 | 424 ms: 1.05x faster                                                          |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                                         |
| json                     | 5.69 ms                                                | 5.56 ms: 1.02x faster                                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                          |
| json_loads               | 31.2 us                                                | 31.5 us: 1.01x slower                                                         |
| telco                    | 7.27 ms                                                | 8.43 ms: 1.16x slower                                                         |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                                         |
| dask                     | 441 ms                                                 | 779 ms: 1.77x slower                                                          |
| logging_silent           | 190 ns                                                 | 495 ns: 2.61x slower                                                          |
| bench_mp_pool            | 24.0 ms                                                | 94.8 ms: 3.95x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                                  |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.384x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.30x