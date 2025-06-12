# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 5606078
- commit date: 2025-06-11
- overall geometric mean: 1.010x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 262 ms                                                | 259 ms: 1.01x faster                                              |
| docutils       | 2.66 sec                                              | 2.64 sec: 1.01x faster                                            |
| Geometric mean | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                               | 24.7 ms: 1.02x faster                                             |
| async_generators           | 434 ms                                                | 425 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 499 ms                                                | 490 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 492 ms                                                | 485 ms: 1.01x faster                                              |
| Geometric mean             | (ref)                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (7): async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 94.6 ms                                               | 90.2 ms: 1.05x faster                                             |
| float          | 65.9 ms                                               | 65.0 ms: 1.01x faster                                             |
| pidigits       | 187 ms                                                | 187 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                 | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 128 ms                                                | 127 ms: 1.00x faster                                              |
| regex_v8       | 22.6 ms                                               | 23.5 ms: 1.04x slower                                             |
| regex_effbot   | 3.25 ms                                               | 3.43 ms: 1.05x slower                                             |
| regex_dna      | 199 ms                                                | 215 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                 | 1.04x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 28.5 us                                               | 27.8 us: 1.03x faster                                             |
| unpickle_pure_python | 201 us                                                | 196 us: 1.02x faster                                              |
| json_dumps           | 11.2 ms                                               | 11.0 ms: 1.02x faster                                             |
| tomli_loads          | 1.90 sec                                              | 1.86 sec: 1.02x faster                                            |
| xml_etree_process    | 56.3 ms                                               | 55.4 ms: 1.02x faster                                             |
| pickle_pure_python   | 326 us                                                | 322 us: 1.01x faster                                              |
| xml_etree_generate   | 81.0 ms                                               | 80.2 ms: 1.01x faster                                             |
| xml_etree_iterparse  | 98.2 ms                                               | 98.0 ms: 1.00x faster                                             |
| Geometric mean       | (ref)                                                 | 1.02x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                               | 6.91 ms: 1.01x faster                                             |
| python_startup         | 12.2 ms                                               | 12.1 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                 | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|-----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                               | 21.0 ms: 1.02x faster                                             |
| django_template | 33.1 ms                                               | 32.6 ms: 1.02x faster                                             |
| genshi_xml      | 50.6 ms                                               | 49.8 ms: 1.02x faster                                             |
| mako            | 10.7 ms                                               | 10.5 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                 | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| go                         | 124 ms                                                | 116 ms: 1.07x faster                                              |
| richards                   | 34.3 ms                                               | 32.6 ms: 1.05x faster                                             |
| nbody                      | 94.6 ms                                               | 90.2 ms: 1.05x faster                                             |
| richards_super             | 39.6 ms                                               | 38.0 ms: 1.04x faster                                             |
| json                       | 5.30 ms                                               | 5.10 ms: 1.04x faster                                             |
| fannkuch                   | 418 ms                                                | 401 ms: 1.04x faster                                              |
| pprint_pformat             | 1.69 sec                                              | 1.63 sec: 1.04x faster                                            |
| crypto_pyaes               | 76.8 ms                                               | 74.0 ms: 1.04x faster                                             |
| pprint_safe_repr           | 815 ms                                                | 785 ms: 1.04x faster                                              |
| spectral_norm              | 102 ms                                                | 98.9 ms: 1.03x faster                                             |
| chaos                      | 63.7 ms                                               | 61.7 ms: 1.03x faster                                             |
| scimark_sor                | 124 ms                                                | 120 ms: 1.03x faster                                              |
| scimark_fft                | 332 ms                                                | 323 ms: 1.03x faster                                              |
| pyflate                    | 424 ms                                                | 412 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult    | 4.96 ms                                               | 4.83 ms: 1.03x faster                                             |
| json_loads                 | 28.5 us                                               | 27.8 us: 1.03x faster                                             |
| scimark_monte_carlo        | 67.3 ms                                               | 65.6 ms: 1.03x faster                                             |
| unpickle_pure_python       | 201 us                                                | 196 us: 1.02x faster                                              |
| coroutines                 | 25.3 ms                                               | 24.7 ms: 1.02x faster                                             |
| typing_runtime_protocols   | 172 us                                                | 168 us: 1.02x faster                                              |
| json_dumps                 | 11.2 ms                                               | 11.0 ms: 1.02x faster                                             |
| raytrace                   | 280 ms                                                | 274 ms: 1.02x faster                                              |
| deltablue                  | 3.13 ms                                               | 3.07 ms: 1.02x faster                                             |
| async_generators           | 434 ms                                                | 425 ms: 1.02x faster                                              |
| genshi_text                | 21.5 ms                                               | 21.0 ms: 1.02x faster                                             |
| tomli_loads                | 1.90 sec                                              | 1.86 sec: 1.02x faster                                            |
| generators                 | 30.6 ms                                               | 30.0 ms: 1.02x faster                                             |
| comprehensions             | 17.0 us                                               | 16.7 us: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 499 ms                                                | 490 ms: 1.02x faster                                              |
| deepcopy_reduce            | 2.80 us                                               | 2.75 us: 1.02x faster                                             |
| xml_etree_process          | 56.3 ms                                               | 55.4 ms: 1.02x faster                                             |
| django_template            | 33.1 ms                                               | 32.6 ms: 1.02x faster                                             |
| genshi_xml                 | 50.6 ms                                               | 49.8 ms: 1.02x faster                                             |
| sqlglot_v2_parse           | 1.28 ms                                               | 1.26 ms: 1.01x faster                                             |
| bpe_tokeniser              | 4.43 sec                                              | 4.36 sec: 1.01x faster                                            |
| hexiom                     | 6.41 ms                                               | 6.32 ms: 1.01x faster                                             |
| float                      | 65.9 ms                                               | 65.0 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed_tg | 492 ms                                                | 485 ms: 1.01x faster                                              |
| subparsers                 | 23.8 ms                                               | 23.5 ms: 1.01x faster                                             |
| sqlglot_v2_transpile       | 1.60 ms                                               | 1.58 ms: 1.01x faster                                             |
| pickle_pure_python         | 326 us                                                | 322 us: 1.01x faster                                              |
| mako                       | 10.7 ms                                               | 10.5 ms: 1.01x faster                                             |
| pathlib                    | 17.2 ms                                               | 17.0 ms: 1.01x faster                                             |
| 2to3                       | 262 ms                                                | 259 ms: 1.01x faster                                              |
| xml_etree_generate         | 81.0 ms                                               | 80.2 ms: 1.01x faster                                             |
| many_optionals             | 986 us                                                | 978 us: 1.01x faster                                              |
| docutils                   | 2.66 sec                                              | 2.64 sec: 1.01x faster                                            |
| python_startup_no_site     | 6.96 ms                                               | 6.91 ms: 1.01x faster                                             |
| create_gc_cycles           | 2.60 ms                                               | 2.58 ms: 1.01x faster                                             |
| dulwich_log                | 62.1 ms                                               | 61.8 ms: 1.01x faster                                             |
| python_startup             | 12.2 ms                                               | 12.1 ms: 1.00x faster                                             |
| sympy_integrate            | 19.5 ms                                               | 19.4 ms: 1.00x faster                                             |
| regex_compile              | 128 ms                                                | 127 ms: 1.00x faster                                              |
| xml_etree_iterparse        | 98.2 ms                                               | 98.0 ms: 1.00x faster                                             |
| pidigits                   | 187 ms                                                | 187 ms: 1.00x slower                                              |
| sympy_expand               | 468 ms                                                | 469 ms: 1.00x slower                                              |
| gc_traversal               | 5.01 ms                                               | 5.03 ms: 1.00x slower                                             |
| connected_components       | 456 ms                                                | 459 ms: 1.01x slower                                              |
| sqlite_synth               | 2.79 us                                               | 2.81 us: 1.01x slower                                             |
| coverage                   | 424 ms                                                | 428 ms: 1.01x slower                                              |
| shortest_path              | 496 ms                                                | 500 ms: 1.01x slower                                              |
| mdp                        | 1.25 sec                                              | 1.26 sec: 1.01x slower                                            |
| deepcopy                   | 258 us                                                | 262 us: 1.01x slower                                              |
| pycparser                  | 1.14 sec                                              | 1.16 sec: 1.02x slower                                            |
| scimark_lu                 | 120 ms                                                | 122 ms: 1.02x slower                                              |
| regex_v8                   | 22.6 ms                                               | 23.5 ms: 1.04x slower                                             |
| regex_effbot               | 3.25 ms                                               | 3.43 ms: 1.05x slower                                             |
| regex_dna                  | 199 ms                                                | 215 ms: 1.08x slower                                              |
| Geometric mean             | (ref)                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (24): telco, async_tree_io_tg, pylint, xml_etree_parse, logging_format, sqlglot_v2_normalize, logging_simple, sphinx, deepcopy_memo, sqlglot_v2_optimize, logging_silent, k_core, asyncio_websockets, html5lib, sympy_sum, thrift, sympy_str, async_tree_io, meteor_contest, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, nqueens, async_tree_none

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x