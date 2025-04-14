# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: b13591a
- commit date: 2025-03-04
- overall geometric mean: 1.004x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                       |
| html5lib       | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines              | 24.5 ms                                                                | 23.9 ms: 1.02x faster                                                        |
| async_tree_none_tg      | 255 ms                                                                 | 251 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed | 497 ms                                                                 | 494 ms: 1.01x faster                                                         |
| async_generators        | 408 ms                                                                 | 414 ms: 1.01x slower                                                         |
| async_tree_io_tg        | 615 ms                                                                 | 627 ms: 1.02x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 89.7 ms                                                                | 86.7 ms: 1.03x faster                                                        |
| float          | 71.1 ms                                                                | 69.0 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                | 25.6 ms: 1.02x slower                                                        |
| regex_effbot   | 3.37 ms                                                                | 3.46 ms: 1.03x slower                                                        |
| regex_dna      | 213 ms                                                                 | 225 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                                 | 99.0 ms: 1.02x faster                                                        |
| xml_etree_parse      | 148 ms                                                                 | 146 ms: 1.02x faster                                                         |
| xml_etree_process    | 56.0 ms                                                                | 55.2 ms: 1.01x faster                                                        |
| unpickle_pure_python | 208 us                                                                 | 206 us: 1.01x faster                                                         |
| json_loads           | 30.0 us                                                                | 29.8 us: 1.00x faster                                                        |
| json_dumps           | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                        |
| pickle_pure_python   | 320 us                                                                 | 325 us: 1.01x slower                                                         |
| tomli_loads          | 1.85 sec                                                               | 1.88 sec: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.12 ms: 1.01x faster                                                        |
| python_startup         | 13.0 ms                                                                | 12.9 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.8 ms: 1.00x faster                                                        |
| mako            | 10.2 ms                                                                | 10.5 ms: 1.03x slower                                                        |
| genshi_text     | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 4.96 ms                                                                | 4.63 ms: 1.07x faster                                                        |
| nbody                   | 89.7 ms                                                                | 86.7 ms: 1.03x faster                                                        |
| float                   | 71.1 ms                                                                | 69.0 ms: 1.03x faster                                                        |
| richards                | 45.0 ms                                                                | 43.9 ms: 1.03x faster                                                        |
| scimark_lu              | 119 ms                                                                 | 116 ms: 1.02x faster                                                         |
| deltablue               | 3.38 ms                                                                | 3.30 ms: 1.02x faster                                                        |
| coroutines              | 24.5 ms                                                                | 23.9 ms: 1.02x faster                                                        |
| go                      | 121 ms                                                                 | 118 ms: 1.02x faster                                                         |
| logging_simple          | 5.61 us                                                                | 5.49 us: 1.02x faster                                                        |
| shortest_path           | 480 ms                                                                 | 470 ms: 1.02x faster                                                         |
| logging_silent          | 109 ns                                                                 | 107 ns: 1.02x faster                                                         |
| connected_components    | 442 ms                                                                 | 434 ms: 1.02x faster                                                         |
| k_core                  | 2.32 sec                                                               | 2.27 sec: 1.02x faster                                                       |
| chaos                   | 60.3 ms                                                                | 59.2 ms: 1.02x faster                                                        |
| scimark_monte_carlo     | 68.9 ms                                                                | 67.8 ms: 1.02x faster                                                        |
| raytrace                | 277 ms                                                                 | 272 ms: 1.02x faster                                                         |
| richards_super          | 51.2 ms                                                                | 50.5 ms: 1.02x faster                                                        |
| pprint_pformat          | 1.50 sec                                                               | 1.48 sec: 1.02x faster                                                       |
| xml_etree_iterparse     | 101 ms                                                                 | 99.0 ms: 1.02x faster                                                        |
| xml_etree_parse         | 148 ms                                                                 | 146 ms: 1.02x faster                                                         |
| xml_etree_process       | 56.0 ms                                                                | 55.2 ms: 1.01x faster                                                        |
| deepcopy                | 263 us                                                                 | 259 us: 1.01x faster                                                         |
| async_tree_none_tg      | 255 ms                                                                 | 251 ms: 1.01x faster                                                         |
| sqlglot_parse           | 1.30 ms                                                                | 1.28 ms: 1.01x faster                                                        |
| sqlglot_normalize       | 107 ms                                                                 | 106 ms: 1.01x faster                                                         |
| unpickle_pure_python    | 208 us                                                                 | 206 us: 1.01x faster                                                         |
| pprint_safe_repr        | 733 ms                                                                 | 725 ms: 1.01x faster                                                         |
| comprehensions          | 17.8 us                                                                | 17.6 us: 1.01x faster                                                        |
| sqlglot_transpile       | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 53.7 ms                                                                | 53.2 ms: 1.01x faster                                                        |
| meteor_contest          | 108 ms                                                                 | 107 ms: 1.01x faster                                                         |
| 2to3                    | 262 ms                                                                 | 260 ms: 1.01x faster                                                         |
| sqlalchemy_imperative   | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                        |
| docutils                | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                       |
| async_tree_cpu_io_mixed | 497 ms                                                                 | 494 ms: 1.01x faster                                                         |
| spectral_norm           | 96.0 ms                                                                | 95.4 ms: 1.01x faster                                                        |
| scimark_fft             | 311 ms                                                                 | 310 ms: 1.01x faster                                                         |
| sqlalchemy_declarative  | 131 ms                                                                 | 130 ms: 1.01x faster                                                         |
| python_startup_no_site  | 7.16 ms                                                                | 7.12 ms: 1.01x faster                                                        |
| hexiom                  | 6.39 ms                                                                | 6.36 ms: 1.01x faster                                                        |
| mdp                     | 2.51 sec                                                               | 2.49 sec: 1.01x faster                                                       |
| python_startup          | 13.0 ms                                                                | 12.9 ms: 1.00x faster                                                        |
| json_loads              | 30.0 us                                                                | 29.8 us: 1.00x faster                                                        |
| dulwich_log             | 67.0 ms                                                                | 66.8 ms: 1.00x faster                                                        |
| sympy_expand            | 471 ms                                                                 | 469 ms: 1.00x faster                                                         |
| create_gc_cycles        | 2.44 ms                                                                | 2.43 ms: 1.00x faster                                                        |
| django_template         | 31.9 ms                                                                | 31.8 ms: 1.00x faster                                                        |
| sympy_integrate         | 20.2 ms                                                                | 20.1 ms: 1.00x faster                                                        |
| json_dumps              | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                        |
| deepcopy_memo           | 29.2 us                                                                | 29.4 us: 1.01x slower                                                        |
| sqlite_synth            | 2.70 us                                                                | 2.73 us: 1.01x slower                                                        |
| pickle_pure_python      | 320 us                                                                 | 325 us: 1.01x slower                                                         |
| fannkuch                | 398 ms                                                                 | 404 ms: 1.01x slower                                                         |
| async_generators        | 408 ms                                                                 | 414 ms: 1.01x slower                                                         |
| regex_v8                | 25.2 ms                                                                | 25.6 ms: 1.02x slower                                                        |
| tomli_loads             | 1.85 sec                                                               | 1.88 sec: 1.02x slower                                                       |
| async_tree_io_tg        | 615 ms                                                                 | 627 ms: 1.02x slower                                                         |
| html5lib                | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                        |
| scimark_sor             | 120 ms                                                                 | 123 ms: 1.02x slower                                                         |
| mako                    | 10.2 ms                                                                | 10.5 ms: 1.03x slower                                                        |
| regex_effbot            | 3.37 ms                                                                | 3.46 ms: 1.03x slower                                                        |
| genshi_text             | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult | 4.54 ms                                                                | 4.69 ms: 1.03x slower                                                        |
| pyflate                 | 429 ms                                                                 | 445 ms: 1.04x slower                                                         |
| regex_dna               | 213 ms                                                                 | 225 ms: 1.05x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (31): async_tree_io, pycparser, pylint, logging_format, json, crypto_pyaes, deepcopy_reduce, async_tree_memoization_tg, bench_mp_pool, bpe_tokeniser, sphinx, xml_etree_generate, regex_compile, sympy_str, bench_thread_pool, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none, pidigits, generators, genshi_xml, async_tree_memoization, telco, coverage, typing_runtime_protocols, sympy_sum, pathlib, many_optionals, subparsers, thrift, nqueens

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x