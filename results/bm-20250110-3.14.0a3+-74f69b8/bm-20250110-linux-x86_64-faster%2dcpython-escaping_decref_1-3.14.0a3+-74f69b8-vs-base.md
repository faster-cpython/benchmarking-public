# Results vs. base

- fork: faster-cpython
- ref: escaping_decref_1
- machine: linux-x86_64
- commit hash: 74f69b8
- commit date: 2025-01-10
- overall geometric mean: 1.004x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 254 ms: 1.01x faster                                                          |
| docutils       | 2.61 sec                                                               | 2.58 sec: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 249 ms                                                                 | 246 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 589 ms                                                                 | 582 ms: 1.01x faster                                                          |
| async_tree_memoization     | 326 ms                                                                 | 323 ms: 1.01x faster                                                          |
| async_tree_memoization_tg  | 308 ms                                                                 | 305 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed    | 485 ms                                                                 | 480 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 461 ms                                                                 | 457 ms: 1.01x faster                                                          |
| coroutines                 | 22.7 ms                                                                | 23.2 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): async_tree_io, async_tree_none, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.6 ms                                                                | 70.6 ms: 1.03x faster                                                         |
| pidigits       | 190 ms                                                                 | 186 ms: 1.02x faster                                                          |
| nbody          | 93.9 ms                                                                | 95.7 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                                | 25.3 ms: 1.03x faster                                                         |
| regex_dna      | 215 ms                                                                 | 211 ms: 1.02x faster                                                          |
| regex_compile  | 128 ms                                                                 | 126 ms: 1.01x faster                                                          |
| regex_effbot   | 3.41 ms                                                                | 3.43 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|---------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse | 97.2 ms                                                                | 96.4 ms: 1.01x faster                                                         |
| xml_etree_parse     | 139 ms                                                                 | 138 ms: 1.01x faster                                                          |
| tomli_loads         | 2.00 sec                                                               | 1.99 sec: 1.01x faster                                                        |
| json_loads          | 26.3 us                                                                | 26.4 us: 1.01x slower                                                         |
| xml_etree_process   | 58.6 ms                                                                | 59.2 ms: 1.01x slower                                                         |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_pure_python, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                         |
| python_startup_no_site | 7.03 ms                                                                | 7.06 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                                | 49.0 ms: 1.03x faster                                                         |
| mako            | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                         |
| django_template | 31.3 ms                                                                | 32.3 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3+-b2adf55 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pycparser                  | 1.17 sec                                                               | 1.12 sec: 1.05x faster                                                        |
| gc_traversal               | 4.92 ms                                                                | 4.75 ms: 1.04x faster                                                         |
| regex_v8                   | 26.1 ms                                                                | 25.3 ms: 1.03x faster                                                         |
| logging_silent             | 110 ns                                                                 | 106 ns: 1.03x faster                                                          |
| float                      | 72.6 ms                                                                | 70.6 ms: 1.03x faster                                                         |
| genshi_xml                 | 50.3 ms                                                                | 49.0 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult    | 4.71 ms                                                                | 4.59 ms: 1.03x faster                                                         |
| telco                      | 7.92 ms                                                                | 7.72 ms: 1.03x faster                                                         |
| scimark_lu                 | 115 ms                                                                 | 113 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 733 ms                                                                 | 717 ms: 1.02x faster                                                          |
| scimark_sor                | 124 ms                                                                 | 121 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.50 sec                                                               | 1.47 sec: 1.02x faster                                                        |
| pidigits                   | 190 ms                                                                 | 186 ms: 1.02x faster                                                          |
| deltablue                  | 3.28 ms                                                                | 3.22 ms: 1.02x faster                                                         |
| regex_dna                  | 215 ms                                                                 | 211 ms: 1.02x faster                                                          |
| meteor_contest             | 107 ms                                                                 | 105 ms: 1.02x faster                                                          |
| mako                       | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                         |
| scimark_fft                | 346 ms                                                                 | 341 ms: 1.01x faster                                                          |
| async_tree_none_tg         | 249 ms                                                                 | 246 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 589 ms                                                                 | 582 ms: 1.01x faster                                                          |
| bpe_tokeniser              | 4.59 sec                                                               | 4.53 sec: 1.01x faster                                                        |
| docutils                   | 2.61 sec                                                               | 2.58 sec: 1.01x faster                                                        |
| richards_super             | 50.6 ms                                                                | 50.0 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.27 ms                                                                | 1.26 ms: 1.01x faster                                                         |
| regex_compile              | 128 ms                                                                 | 126 ms: 1.01x faster                                                          |
| connected_components       | 441 ms                                                                 | 437 ms: 1.01x faster                                                          |
| async_tree_memoization     | 326 ms                                                                 | 323 ms: 1.01x faster                                                          |
| async_tree_memoization_tg  | 308 ms                                                                 | 305 ms: 1.01x faster                                                          |
| hexiom                     | 6.26 ms                                                                | 6.19 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 485 ms                                                                 | 480 ms: 1.01x faster                                                          |
| richards                   | 44.5 ms                                                                | 44.1 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 461 ms                                                                 | 457 ms: 1.01x faster                                                          |
| raytrace                   | 273 ms                                                                 | 270 ms: 1.01x faster                                                          |
| sqlalchemy_imperative      | 16.5 ms                                                                | 16.4 ms: 1.01x faster                                                         |
| scimark_monte_carlo        | 67.7 ms                                                                | 67.2 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 97.2 ms                                                                | 96.4 ms: 1.01x faster                                                         |
| sqlite_synth               | 2.83 us                                                                | 2.81 us: 1.01x faster                                                         |
| sqlglot_transpile          | 1.58 ms                                                                | 1.57 ms: 1.01x faster                                                         |
| logging_simple             | 5.65 us                                                                | 5.61 us: 1.01x faster                                                         |
| xml_etree_parse            | 139 ms                                                                 | 138 ms: 1.01x faster                                                          |
| go                         | 117 ms                                                                 | 116 ms: 1.01x faster                                                          |
| 2to3                       | 255 ms                                                                 | 254 ms: 1.01x faster                                                          |
| subparsers                 | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                         |
| tomli_loads                | 2.00 sec                                                               | 1.99 sec: 1.01x faster                                                        |
| sympy_integrate            | 19.8 ms                                                                | 19.7 ms: 1.00x faster                                                         |
| deepcopy_memo              | 30.9 us                                                                | 30.8 us: 1.00x faster                                                         |
| bench_thread_pool          | 863 us                                                                 | 860 us: 1.00x faster                                                          |
| dulwich_log                | 63.6 ms                                                                | 63.8 ms: 1.00x slower                                                         |
| deepcopy                   | 259 us                                                                 | 260 us: 1.00x slower                                                          |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                         |
| regex_effbot               | 3.41 ms                                                                | 3.43 ms: 1.00x slower                                                         |
| chaos                      | 60.3 ms                                                                | 60.6 ms: 1.00x slower                                                         |
| python_startup_no_site     | 7.03 ms                                                                | 7.06 ms: 1.00x slower                                                         |
| json_loads                 | 26.3 us                                                                | 26.4 us: 1.01x slower                                                         |
| thrift                     | 769 us                                                                 | 774 us: 1.01x slower                                                          |
| logging_format             | 6.21 us                                                                | 6.27 us: 1.01x slower                                                         |
| sqlglot_optimize           | 52.4 ms                                                                | 52.8 ms: 1.01x slower                                                         |
| many_optionals             | 937 us                                                                 | 946 us: 1.01x slower                                                          |
| spectral_norm              | 105 ms                                                                 | 106 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 103 ms                                                                 | 104 ms: 1.01x slower                                                          |
| xml_etree_process          | 58.6 ms                                                                | 59.2 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 2.65 us                                                                | 2.68 us: 1.01x slower                                                         |
| fannkuch                   | 395 ms                                                                 | 400 ms: 1.01x slower                                                          |
| generators                 | 27.2 ms                                                                | 27.7 ms: 1.02x slower                                                         |
| coverage                   | 83.5 ms                                                                | 85.0 ms: 1.02x slower                                                         |
| nbody                      | 93.9 ms                                                                | 95.7 ms: 1.02x slower                                                         |
| coroutines                 | 22.7 ms                                                                | 23.2 ms: 1.03x slower                                                         |
| django_template            | 31.3 ms                                                                | 32.3 ms: 1.03x slower                                                         |
| mdp                        | 2.47 sec                                                               | 2.66 sec: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (27): async_tree_io, async_tree_none, shortest_path, typing_runtime_protocols, k_core, genshi_text, sphinx, pyflate, unpickle_pure_python, sympy_sum, pylint, comprehensions, crypto_pyaes, pickle_pure_python, asyncio_websockets, sqlalchemy_declarative, async_generators, json, bench_mp_pool, nqueens, create_gc_cycles, pathlib, sympy_expand, sympy_str, xml_etree_generate, html5lib, json_dumps

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x