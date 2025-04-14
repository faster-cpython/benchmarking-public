# Results vs. base

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.001x faster
- HPT reliability: 93.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                       | 286 ms: 1.01x faster                                               |
| docutils       | 2.94 sec                                                                     | 2.91 sec: 1.01x faster                                             |
| html5lib       | 72.0 ms                                                                      | 70.2 ms: 1.03x faster                                              |
| sphinx         | 1.12 sec                                                                     | 1.11 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization  | 354 ms                                                                       | 350 ms: 1.01x faster                                               |
| async_tree_none         | 293 ms                                                                       | 291 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed | 525 ms                                                                       | 522 ms: 1.01x faster                                               |
| coroutines              | 21.0 ms                                                                      | 20.9 ms: 1.00x faster                                              |
| Geometric mean          | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_generators, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 104 ms                                                                       | 101 ms: 1.02x faster                                               |
| pidigits       | 254 ms                                                                       | 255 ms: 1.00x slower                                               |
| float          | 71.5 ms                                                                      | 72.5 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.2 ms                                                                      | 23.9 ms: 1.03x slower                                              |
| regex_dna      | 230 ms                                                                       | 246 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                       |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|--------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse    | 142 ms                                                                       | 136 ms: 1.04x faster                                               |
| tomli_loads        | 2.19 sec                                                                     | 2.14 sec: 1.02x faster                                             |
| xml_etree_process  | 59.8 ms                                                                      | 60.5 ms: 1.01x slower                                              |
| xml_etree_generate | 84.1 ms                                                                      | 85.7 ms: 1.02x slower                                              |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_dumps, pickle_pure_python, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 16.4 ms                                                                      | 16.4 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 24.7 ms                                                                      | 23.6 ms: 1.05x faster                                              |
| django_template | 37.5 ms                                                                      | 36.4 ms: 1.03x faster                                              |
| mako            | 11.0 ms                                                                      | 11.1 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|--------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text              | 24.7 ms                                                                      | 23.6 ms: 1.05x faster                                              |
| xml_etree_parse          | 142 ms                                                                       | 136 ms: 1.04x faster                                               |
| logging_simple           | 6.71 us                                                                      | 6.49 us: 1.03x faster                                              |
| comprehensions           | 18.2 us                                                                      | 17.6 us: 1.03x faster                                              |
| django_template          | 37.5 ms                                                                      | 36.4 ms: 1.03x faster                                              |
| html5lib                 | 72.0 ms                                                                      | 70.2 ms: 1.03x faster                                              |
| tomli_loads              | 2.19 sec                                                                     | 2.14 sec: 1.02x faster                                             |
| raytrace                 | 305 ms                                                                       | 298 ms: 1.02x faster                                               |
| nbody                    | 104 ms                                                                       | 101 ms: 1.02x faster                                               |
| coverage                 | 82.3 ms                                                                      | 80.6 ms: 1.02x faster                                              |
| telco                    | 8.18 ms                                                                      | 8.02 ms: 1.02x faster                                              |
| scimark_fft              | 320 ms                                                                       | 314 ms: 1.02x faster                                               |
| sqlalchemy_imperative    | 18.3 ms                                                                      | 18.0 ms: 1.02x faster                                              |
| bench_thread_pool        | 967 us                                                                       | 952 us: 1.02x faster                                               |
| deltablue                | 3.42 ms                                                                      | 3.36 ms: 1.02x faster                                              |
| typing_runtime_protocols | 173 us                                                                       | 171 us: 1.01x faster                                               |
| docutils                 | 2.94 sec                                                                     | 2.91 sec: 1.01x faster                                             |
| logging_format           | 7.30 us                                                                      | 7.21 us: 1.01x faster                                              |
| meteor_contest           | 128 ms                                                                       | 126 ms: 1.01x faster                                               |
| sqlglot_v2_transpile     | 1.79 ms                                                                      | 1.77 ms: 1.01x faster                                              |
| async_tree_memoization   | 354 ms                                                                       | 350 ms: 1.01x faster                                               |
| many_optionals           | 1.05 ms                                                                      | 1.04 ms: 1.01x faster                                              |
| dulwich_log              | 63.4 ms                                                                      | 62.8 ms: 1.01x faster                                              |
| sympy_sum                | 156 ms                                                                       | 155 ms: 1.01x faster                                               |
| sqlglot_v2_parse         | 1.40 ms                                                                      | 1.39 ms: 1.01x faster                                              |
| sympy_integrate          | 23.6 ms                                                                      | 23.4 ms: 1.01x faster                                              |
| sphinx                   | 1.12 sec                                                                     | 1.11 sec: 1.01x faster                                             |
| sympy_expand             | 509 ms                                                                       | 505 ms: 1.01x faster                                               |
| async_tree_none          | 293 ms                                                                       | 291 ms: 1.01x faster                                               |
| spectral_norm            | 90.8 ms                                                                      | 90.2 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed  | 525 ms                                                                       | 522 ms: 1.01x faster                                               |
| pycparser                | 1.29 sec                                                                     | 1.29 sec: 1.01x faster                                             |
| scimark_monte_carlo      | 66.7 ms                                                                      | 66.2 ms: 1.01x faster                                              |
| mdp                      | 2.52 sec                                                                     | 2.51 sec: 1.01x faster                                             |
| 2to3                     | 287 ms                                                                       | 286 ms: 1.01x faster                                               |
| sqlglot_v2_normalize     | 120 ms                                                                       | 119 ms: 1.00x faster                                               |
| coroutines               | 21.0 ms                                                                      | 20.9 ms: 1.00x faster                                              |
| connected_components     | 431 ms                                                                       | 430 ms: 1.00x faster                                               |
| python_startup           | 16.4 ms                                                                      | 16.4 ms: 1.00x faster                                              |
| bpe_tokeniser            | 4.85 sec                                                                     | 4.84 sec: 1.00x faster                                             |
| pidigits                 | 254 ms                                                                       | 255 ms: 1.00x slower                                               |
| shortest_path            | 457 ms                                                                       | 458 ms: 1.00x slower                                               |
| pyflate                  | 462 ms                                                                       | 464 ms: 1.00x slower                                               |
| crypto_pyaes             | 84.2 ms                                                                      | 84.7 ms: 1.01x slower                                              |
| subparsers               | 23.7 ms                                                                      | 23.9 ms: 1.01x slower                                              |
| pprint_pformat           | 1.67 sec                                                                     | 1.69 sec: 1.01x slower                                             |
| xml_etree_process        | 59.8 ms                                                                      | 60.5 ms: 1.01x slower                                              |
| pprint_safe_repr         | 826 ms                                                                       | 835 ms: 1.01x slower                                               |
| hexiom                   | 6.44 ms                                                                      | 6.51 ms: 1.01x slower                                              |
| mako                     | 11.0 ms                                                                      | 11.1 ms: 1.01x slower                                              |
| fannkuch                 | 383 ms                                                                       | 388 ms: 1.01x slower                                               |
| float                    | 71.5 ms                                                                      | 72.5 ms: 1.01x slower                                              |
| chaos                    | 64.3 ms                                                                      | 65.2 ms: 1.01x slower                                              |
| scimark_sor              | 109 ms                                                                       | 111 ms: 1.02x slower                                               |
| xml_etree_generate       | 84.1 ms                                                                      | 85.7 ms: 1.02x slower                                              |
| deepcopy_reduce          | 3.02 us                                                                      | 3.08 us: 1.02x slower                                              |
| scimark_sparse_mat_mult  | 4.74 ms                                                                      | 4.85 ms: 1.02x slower                                              |
| deepcopy                 | 288 us                                                                       | 296 us: 1.03x slower                                               |
| richards                 | 48.1 ms                                                                      | 49.5 ms: 1.03x slower                                              |
| regex_v8                 | 23.2 ms                                                                      | 23.9 ms: 1.03x slower                                              |
| richards_super           | 54.0 ms                                                                      | 55.8 ms: 1.03x slower                                              |
| regex_dna                | 230 ms                                                                       | 246 ms: 1.07x slower                                               |
| gc_traversal             | 6.14 ms                                                                      | 6.61 ms: 1.08x slower                                              |
| bench_mp_pool            | 766 ms                                                                       | 1.22 sec: 1.60x slower                                             |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (32): pylint, genshi_xml, xml_etree_iterparse, sqlalchemy_declarative, async_tree_cpu_io_mixed_tg, scimark_lu, json, nqueens, json_dumps, go, async_tree_memoization_tg, pathlib, sqlglot_v2_optimize, python_startup_no_site, sympy_str, async_tree_io, asyncio_websockets, deepcopy_memo, pickle_pure_python, unpickle_pure_python, k_core, regex_compile, json_loads, async_generators, async_tree_none_tg, logging_silent, sqlite_synth, thrift, regex_effbot, create_gc_cycles, generators, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 93.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x