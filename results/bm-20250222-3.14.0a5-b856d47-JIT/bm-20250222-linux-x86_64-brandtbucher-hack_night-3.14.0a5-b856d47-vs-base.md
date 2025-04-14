# Results vs. base

- fork: brandtbucher
- ref: hack_night
- machine: linux-x86_64
- commit hash: b856d47
- commit date: 2025-02-22
- overall geometric mean: 1.001x slower
- HPT reliability: 66.15%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 257 ms                                                     | 257 ms: 1.00x faster                                              |
| html5lib       | 60.6 ms                                                    | 62.2 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_generators | 408 ms                                                     | 410 ms: 1.01x slower                                              |
| coroutines       | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                             |
| Geometric mean   | (ref)                                                      | 1.00x slower                                                      |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.7 ms                                                    | 94.0 ms: 1.04x faster                                             |
| pidigits       | 188 ms                                                     | 186 ms: 1.01x faster                                              |
| float          | 69.1 ms                                                    | 70.5 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.20 ms                                                    | 3.10 ms: 1.03x faster                                             |
| regex_compile  | 125 ms                                                     | 125 ms: 1.01x slower                                              |
| regex_v8       | 23.5 ms                                                    | 23.7 ms: 1.01x slower                                             |
| regex_dna      | 206 ms                                                     | 207 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                      | 1.00x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                     | 318 us: 1.02x faster                                              |
| xml_etree_parse      | 139 ms                                                     | 138 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 96.0 ms                                                    | 95.3 ms: 1.01x faster                                             |
| unpickle_pure_python | 199 us                                                     | 202 us: 1.02x slower                                              |
| json_dumps           | 11.7 ms                                                    | 12.0 ms: 1.02x slower                                             |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                      |

Benchmark hidden because not significant (4): tomli_loads, xml_etree_generate, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                    | 12.9 ms: 1.00x slower                                             |
| python_startup_no_site | 7.05 ms                                                    | 7.08 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                    | 49.2 ms: 1.03x faster                                             |
| mako            | 10.5 ms                                                    | 10.2 ms: 1.02x faster                                             |
| django_template | 31.5 ms                                                    | 32.0 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|--------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| coverage                 | 96.8 ms                                                    | 89.7 ms: 1.08x faster                                             |
| nbody                    | 97.7 ms                                                    | 94.0 ms: 1.04x faster                                             |
| generators               | 28.9 ms                                                    | 28.0 ms: 1.03x faster                                             |
| regex_effbot             | 3.20 ms                                                    | 3.10 ms: 1.03x faster                                             |
| scimark_lu               | 118 ms                                                     | 114 ms: 1.03x faster                                              |
| genshi_xml               | 50.5 ms                                                    | 49.2 ms: 1.03x faster                                             |
| mako                     | 10.5 ms                                                    | 10.2 ms: 1.02x faster                                             |
| scimark_sor              | 122 ms                                                     | 120 ms: 1.02x faster                                              |
| pickle_pure_python       | 324 us                                                     | 318 us: 1.02x faster                                              |
| richards                 | 45.0 ms                                                    | 44.2 ms: 1.02x faster                                             |
| richards_super           | 51.3 ms                                                    | 50.6 ms: 1.01x faster                                             |
| scimark_fft              | 317 ms                                                     | 313 ms: 1.01x faster                                              |
| xml_etree_parse          | 139 ms                                                     | 138 ms: 1.01x faster                                              |
| raytrace                 | 279 ms                                                     | 276 ms: 1.01x faster                                              |
| pidigits                 | 188 ms                                                     | 186 ms: 1.01x faster                                              |
| scimark_monte_carlo      | 66.7 ms                                                    | 66.2 ms: 1.01x faster                                             |
| xml_etree_iterparse      | 96.0 ms                                                    | 95.3 ms: 1.01x faster                                             |
| connected_components     | 441 ms                                                     | 439 ms: 1.01x faster                                              |
| dulwich_log              | 66.4 ms                                                    | 66.1 ms: 1.00x faster                                             |
| scimark_sparse_mat_mult  | 4.34 ms                                                    | 4.33 ms: 1.00x faster                                             |
| shortest_path            | 483 ms                                                     | 483 ms: 1.00x faster                                              |
| 2to3                     | 257 ms                                                     | 257 ms: 1.00x faster                                              |
| python_startup           | 12.8 ms                                                    | 12.9 ms: 1.00x slower                                             |
| sqlalchemy_declarative   | 131 ms                                                     | 131 ms: 1.00x slower                                              |
| bench_thread_pool        | 888 us                                                     | 891 us: 1.00x slower                                              |
| sympy_str                | 275 ms                                                     | 276 ms: 1.00x slower                                              |
| bpe_tokeniser            | 4.36 sec                                                   | 4.38 sec: 1.00x slower                                            |
| go                       | 129 ms                                                     | 130 ms: 1.00x slower                                              |
| python_startup_no_site   | 7.05 ms                                                    | 7.08 ms: 1.00x slower                                             |
| deltablue                | 3.38 ms                                                    | 3.39 ms: 1.00x slower                                             |
| regex_compile            | 125 ms                                                     | 125 ms: 1.01x slower                                              |
| sqlglot_transpile        | 1.58 ms                                                    | 1.59 ms: 1.01x slower                                             |
| async_generators         | 408 ms                                                     | 410 ms: 1.01x slower                                              |
| create_gc_cycles         | 2.47 ms                                                    | 2.48 ms: 1.01x slower                                             |
| sqlglot_parse            | 1.27 ms                                                    | 1.28 ms: 1.01x slower                                             |
| meteor_contest           | 109 ms                                                     | 109 ms: 1.01x slower                                              |
| deepcopy                 | 260 us                                                     | 262 us: 1.01x slower                                              |
| many_optionals           | 948 us                                                     | 956 us: 1.01x slower                                              |
| regex_v8                 | 23.5 ms                                                    | 23.7 ms: 1.01x slower                                             |
| json                     | 5.13 ms                                                    | 5.17 ms: 1.01x slower                                             |
| regex_dna                | 206 ms                                                     | 207 ms: 1.01x slower                                              |
| pprint_pformat           | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                            |
| deepcopy_reduce          | 2.66 us                                                    | 2.69 us: 1.01x slower                                             |
| pprint_safe_repr         | 764 ms                                                     | 772 ms: 1.01x slower                                              |
| sympy_expand             | 469 ms                                                     | 474 ms: 1.01x slower                                              |
| sqlite_synth             | 2.74 us                                                    | 2.77 us: 1.01x slower                                             |
| thrift                   | 759 us                                                     | 768 us: 1.01x slower                                              |
| logging_format           | 6.08 us                                                    | 6.16 us: 1.01x slower                                             |
| django_template          | 31.5 ms                                                    | 32.0 ms: 1.01x slower                                             |
| coroutines               | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                             |
| unpickle_pure_python     | 199 us                                                     | 202 us: 1.02x slower                                              |
| fannkuch                 | 395 ms                                                     | 401 ms: 1.02x slower                                              |
| logging_simple           | 5.50 us                                                    | 5.59 us: 1.02x slower                                             |
| deepcopy_memo            | 30.5 us                                                    | 31.0 us: 1.02x slower                                             |
| nqueens                  | 88.5 ms                                                    | 89.9 ms: 1.02x slower                                             |
| subparsers               | 20.6 ms                                                    | 21.0 ms: 1.02x slower                                             |
| float                    | 69.1 ms                                                    | 70.5 ms: 1.02x slower                                             |
| typing_runtime_protocols | 162 us                                                     | 166 us: 1.02x slower                                              |
| json_dumps               | 11.7 ms                                                    | 12.0 ms: 1.02x slower                                             |
| html5lib                 | 60.6 ms                                                    | 62.2 ms: 1.03x slower                                             |
| gc_traversal             | 4.87 ms                                                    | 5.06 ms: 1.04x slower                                             |
| pycparser                | 1.11 sec                                                   | 1.16 sec: 1.05x slower                                            |
| logging_silent           | 103 ns                                                     | 109 ns: 1.05x slower                                              |
| Geometric mean           | (ref)                                                      | 1.00x slower                                                      |

Benchmark hidden because not significant (33): async_tree_none_tg, pathlib, async_tree_cpu_io_mixed_tg, k_core, tomli_loads, async_tree_cpu_io_mixed, asyncio_websockets, sympy_sum, sqlglot_optimize, pyflate, chaos, xml_etree_generate, crypto_pyaes, sqlalchemy_imperative, sympy_integrate, async_tree_memoization_tg, comprehensions, docutils, json_loads, pylint, bench_mp_pool, async_tree_memoization, telco, hexiom, sqlglot_normalize, mdp, async_tree_none, sphinx, xml_etree_process, async_tree_io, async_tree_io_tg, spectral_norm, genshi_text

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 66.15% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x