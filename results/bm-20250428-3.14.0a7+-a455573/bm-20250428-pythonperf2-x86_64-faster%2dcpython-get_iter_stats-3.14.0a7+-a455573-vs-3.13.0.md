# Results vs. 3.13.0

- fork: faster-cpython
- ref: get_iter_stats
- machine: linux-x86_64
- commit hash: a455573
- commit date: 2025-04-28
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 274 ms: 1.07x faster                                                             |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                           |
| html5lib       | 73.5 ms                                                      | 66.6 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization  | 453 ms                                                       | 321 ms: 1.41x faster                                                             |
| async_tree_none         | 376 ms                                                       | 278 ms: 1.35x faster                                                             |
| async_tree_io           | 843 ms                                                       | 625 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed | 604 ms                                                       | 495 ms: 1.22x faster                                                             |
| async_generators        | 457 ms                                                       | 409 ms: 1.12x faster                                                             |
| coroutines              | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                            |
| Geometric mean          | (ref)                                                        | 1.19x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.4 ms: 1.21x faster                                                            |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                             |
| nbody          | 89.3 ms                                                      | 94.9 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.25 ms: 1.13x faster                                                            |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                             |
| regex_v8       | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                                            |
| regex_dna      | 247 ms                                                       | 240 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                           |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 103 ms                                                       | 96.6 ms: 1.06x faster                                                            |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                             |
| xml_etree_process    | 61.2 ms                                                      | 58.3 ms: 1.05x faster                                                            |
| xml_etree_generate   | 86.5 ms                                                      | 83.8 ms: 1.03x faster                                                            |
| pickle_pure_python   | 323 us                                                       | 324 us: 1.00x slower                                                             |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                            |
| json_loads           | 24.7 us                                                      | 25.9 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.9 ms: 1.00x slower                                                            |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                            |
| genshi_xml      | 57.1 ms                                                      | 52.1 ms: 1.10x faster                                                            |
| django_template | 36.4 ms                                                      | 34.5 ms: 1.05x faster                                                            |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                      | 2.54 sec                                                     | 1.27 sec: 2.01x faster                                                           |
| deepcopy                 | 392 us                                                       | 270 us: 1.45x faster                                                             |
| async_tree_memoization   | 453 ms                                                       | 321 ms: 1.41x faster                                                             |
| deepcopy_memo            | 38.6 us                                                      | 27.5 us: 1.40x faster                                                            |
| async_tree_none          | 376 ms                                                       | 278 ms: 1.35x faster                                                             |
| async_tree_io            | 843 ms                                                       | 625 ms: 1.35x faster                                                             |
| go                       | 162 ms                                                       | 122 ms: 1.33x faster                                                             |
| deepcopy_reduce          | 3.54 us                                                      | 2.86 us: 1.24x faster                                                            |
| async_tree_cpu_io_mixed  | 604 ms                                                       | 495 ms: 1.22x faster                                                             |
| float                    | 81.3 ms                                                      | 67.4 ms: 1.21x faster                                                            |
| tomli_loads              | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                           |
| richards                 | 52.9 ms                                                      | 44.6 ms: 1.19x faster                                                            |
| richards_super           | 59.6 ms                                                      | 50.3 ms: 1.18x faster                                                            |
| scimark_sor              | 123 ms                                                       | 105 ms: 1.17x faster                                                             |
| pyflate                  | 503 ms                                                       | 439 ms: 1.15x faster                                                             |
| generators               | 33.6 ms                                                      | 29.4 ms: 1.15x faster                                                            |
| genshi_text              | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                            |
| regex_effbot             | 3.67 ms                                                      | 3.25 ms: 1.13x faster                                                            |
| telco                    | 8.79 ms                                                      | 7.81 ms: 1.12x faster                                                            |
| async_generators         | 457 ms                                                       | 409 ms: 1.12x faster                                                             |
| dulwich_log              | 68.2 ms                                                      | 61.1 ms: 1.12x faster                                                            |
| deltablue                | 3.42 ms                                                      | 3.08 ms: 1.11x faster                                                            |
| html5lib                 | 73.5 ms                                                      | 66.6 ms: 1.10x faster                                                            |
| hexiom                   | 6.55 ms                                                      | 5.94 ms: 1.10x faster                                                            |
| genshi_xml               | 57.1 ms                                                      | 52.1 ms: 1.10x faster                                                            |
| pprint_pformat           | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                           |
| pprint_safe_repr         | 843 ms                                                       | 770 ms: 1.09x faster                                                             |
| logging_simple           | 6.39 us                                                      | 5.87 us: 1.09x faster                                                            |
| spectral_norm            | 97.0 ms                                                      | 89.2 ms: 1.09x faster                                                            |
| pylint                   | 347 ms                                                       | 319 ms: 1.09x faster                                                             |
| logging_silent           | 97.9 ns                                                      | 90.2 ns: 1.08x faster                                                            |
| regex_compile            | 143 ms                                                       | 132 ms: 1.08x faster                                                             |
| bpe_tokeniser            | 5.09 sec                                                     | 4.71 sec: 1.08x faster                                                           |
| sympy_integrate          | 23.6 ms                                                      | 21.9 ms: 1.08x faster                                                            |
| scimark_fft              | 328 ms                                                       | 304 ms: 1.08x faster                                                             |
| scimark_monte_carlo      | 66.1 ms                                                      | 61.6 ms: 1.07x faster                                                            |
| 2to3                     | 293 ms                                                       | 274 ms: 1.07x faster                                                             |
| xml_etree_parse          | 150 ms                                                       | 141 ms: 1.07x faster                                                             |
| logging_format           | 6.94 us                                                      | 6.51 us: 1.07x faster                                                            |
| xml_etree_iterparse      | 103 ms                                                       | 96.6 ms: 1.06x faster                                                            |
| json                     | 5.69 ms                                                      | 5.38 ms: 1.06x faster                                                            |
| django_template          | 36.4 ms                                                      | 34.5 ms: 1.05x faster                                                            |
| sympy_expand             | 509 ms                                                       | 485 ms: 1.05x faster                                                             |
| unpickle_pure_python     | 217 us                                                       | 207 us: 1.05x faster                                                             |
| regex_v8                 | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                                            |
| xml_etree_process        | 61.2 ms                                                      | 58.3 ms: 1.05x faster                                                            |
| sympy_str                | 298 ms                                                       | 285 ms: 1.05x faster                                                             |
| pathlib                  | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                            |
| meteor_contest           | 130 ms                                                       | 125 ms: 1.04x faster                                                             |
| xml_etree_generate       | 86.5 ms                                                      | 83.8 ms: 1.03x faster                                                            |
| scimark_sparse_mat_mult  | 4.77 ms                                                      | 4.63 ms: 1.03x faster                                                            |
| sqlalchemy_imperative    | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                            |
| sympy_sum                | 155 ms                                                       | 150 ms: 1.03x faster                                                             |
| scimark_lu               | 98.7 ms                                                      | 96.1 ms: 1.03x faster                                                            |
| regex_dna                | 247 ms                                                       | 240 ms: 1.03x faster                                                             |
| chaos                    | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                                            |
| sqlite_synth             | 2.91 us                                                      | 2.86 us: 1.02x faster                                                            |
| typing_runtime_protocols | 169 us                                                       | 167 us: 1.01x faster                                                             |
| sqlalchemy_declarative   | 148 ms                                                       | 147 ms: 1.01x faster                                                             |
| raytrace                 | 273 ms                                                       | 270 ms: 1.01x faster                                                             |
| python_startup           | 15.9 ms                                                      | 15.9 ms: 1.00x slower                                                            |
| comprehensions           | 17.0 us                                                      | 17.1 us: 1.00x slower                                                            |
| pickle_pure_python       | 323 us                                                       | 324 us: 1.00x slower                                                             |
| pycparser                | 1.24 sec                                                     | 1.25 sec: 1.01x slower                                                           |
| pidigits                 | 252 ms                                                       | 254 ms: 1.01x slower                                                             |
| docutils                 | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                           |
| json_dumps               | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                            |
| coroutines               | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                            |
| nqueens                  | 90.7 ms                                                      | 92.5 ms: 1.02x slower                                                            |
| coverage                 | 80.0 ms                                                      | 81.6 ms: 1.02x slower                                                            |
| bench_thread_pool        | 942 us                                                       | 968 us: 1.03x slower                                                             |
| create_gc_cycles         | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                            |
| json_loads               | 24.7 us                                                      | 25.9 us: 1.05x slower                                                            |
| mako                     | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                            |
| nbody                    | 89.3 ms                                                      | 94.9 ms: 1.06x slower                                                            |
| crypto_pyaes             | 73.3 ms                                                      | 78.8 ms: 1.08x slower                                                            |
| many_optionals           | 930 us                                                       | 1.00 ms: 1.08x slower                                                            |
| python_startup_no_site   | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                            |
| subparsers               | 17.5 ms                                                      | 22.4 ms: 1.28x slower                                                            |
| gc_traversal             | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                            |
| bench_mp_pool            | 5.12 ms                                                      | 1.41 sec: 275.20x slower                                                         |
| Geometric mean           | (ref)                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, fannkuch
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250428-3.14.0a7+-a455573/bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x