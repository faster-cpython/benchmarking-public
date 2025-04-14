# Results vs. base

- fork: brandtbucher
- ref: jit_optimizer_truthy
- machine: linux-x86_64
- commit hash: 1726866
- commit date: 2025-03-07
- overall geometric mean: 1.004x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                       |
| html5lib       | 61.0 ms                                                                | 62.0 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 24.5 ms                                                                | 23.7 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 488 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 255 ms                                                                 | 251 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 478 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none, asyncio_websockets, async_generators, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 69.8 ms: 1.02x faster                                                        |
| nbody          | 89.7 ms                                                                | 88.2 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                | 24.9 ms: 1.01x faster                                                        |
| regex_effbot   | 3.37 ms                                                                | 3.39 ms: 1.01x slower                                                        |
| regex_dna      | 213 ms                                                                 | 219 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 208 us                                                                 | 202 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                                 | 99.4 ms: 1.01x faster                                                        |
| xml_etree_parse      | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| tomli_loads          | 1.85 sec                                                               | 1.87 sec: 1.01x slower                                                       |
| json_dumps           | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.13 ms: 1.00x faster                                                        |
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.4 ms: 1.02x faster                                                        |
| genshi_text     | 21.3 ms                                                                | 21.5 ms: 1.01x slower                                                        |
| mako            | 10.2 ms                                                                | 10.5 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.96 ms                                                                | 4.60 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 2.71 us                                                                | 2.61 us: 1.04x faster                                                        |
| deltablue                  | 3.38 ms                                                                | 3.26 ms: 1.04x faster                                                        |
| coroutines                 | 24.5 ms                                                                | 23.7 ms: 1.03x faster                                                        |
| go                         | 121 ms                                                                 | 117 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 208 us                                                                 | 202 us: 1.03x faster                                                         |
| raytrace                   | 277 ms                                                                 | 270 ms: 1.03x faster                                                         |
| logging_silent             | 109 ns                                                                 | 107 ns: 1.02x faster                                                         |
| float                      | 71.1 ms                                                                | 69.8 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 488 ms: 1.02x faster                                                         |
| chaos                      | 60.3 ms                                                                | 59.2 ms: 1.02x faster                                                        |
| richards                   | 45.0 ms                                                                | 44.3 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 68.9 ms                                                                | 67.8 ms: 1.02x faster                                                        |
| scimark_lu                 | 119 ms                                                                 | 117 ms: 1.02x faster                                                         |
| nbody                      | 89.7 ms                                                                | 88.2 ms: 1.02x faster                                                        |
| django_template            | 31.9 ms                                                                | 31.4 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 107 ms                                                                 | 105 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 255 ms                                                                 | 251 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 478 ms: 1.01x faster                                                         |
| coverage                   | 85.0 ms                                                                | 83.8 ms: 1.01x faster                                                        |
| logging_simple             | 5.61 us                                                                | 5.54 us: 1.01x faster                                                        |
| deepcopy                   | 263 us                                                                 | 259 us: 1.01x faster                                                         |
| bpe_tokeniser              | 4.48 sec                                                               | 4.43 sec: 1.01x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                                 | 99.4 ms: 1.01x faster                                                        |
| richards_super             | 51.2 ms                                                                | 50.7 ms: 1.01x faster                                                        |
| logging_format             | 6.18 us                                                                | 6.11 us: 1.01x faster                                                        |
| xml_etree_parse            | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| regex_v8                   | 25.2 ms                                                                | 24.9 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                        |
| sympy_expand               | 471 ms                                                                 | 467 ms: 1.01x faster                                                         |
| docutils                   | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                       |
| sqlalchemy_declarative     | 131 ms                                                                 | 130 ms: 1.01x faster                                                         |
| 2to3                       | 262 ms                                                                 | 260 ms: 1.01x faster                                                         |
| sympy_str                  | 274 ms                                                                 | 272 ms: 1.01x faster                                                         |
| connected_components       | 442 ms                                                                 | 439 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| comprehensions             | 17.8 us                                                                | 17.7 us: 1.01x faster                                                        |
| generators                 | 28.0 ms                                                                | 27.9 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| create_gc_cycles           | 2.44 ms                                                                | 2.43 ms: 1.00x faster                                                        |
| hexiom                     | 6.39 ms                                                                | 6.37 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.16 ms                                                                | 7.13 ms: 1.00x faster                                                        |
| sympy_integrate            | 20.2 ms                                                                | 20.1 ms: 1.00x faster                                                        |
| sqlglot_optimize           | 53.7 ms                                                                | 53.5 ms: 1.00x faster                                                        |
| python_startup             | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                        |
| shortest_path              | 480 ms                                                                 | 482 ms: 1.00x slower                                                         |
| dulwich_log                | 67.0 ms                                                                | 67.3 ms: 1.00x slower                                                        |
| scimark_sparse_mat_mult    | 4.54 ms                                                                | 4.55 ms: 1.00x slower                                                        |
| regex_effbot               | 3.37 ms                                                                | 3.39 ms: 1.01x slower                                                        |
| crypto_pyaes               | 74.3 ms                                                                | 74.7 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.70 us                                                                | 2.72 us: 1.01x slower                                                        |
| tomli_loads                | 1.85 sec                                                               | 1.87 sec: 1.01x slower                                                       |
| subparsers                 | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                        |
| fannkuch                   | 398 ms                                                                 | 402 ms: 1.01x slower                                                         |
| scimark_sor                | 120 ms                                                                 | 121 ms: 1.01x slower                                                         |
| json_dumps                 | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                        |
| genshi_text                | 21.3 ms                                                                | 21.5 ms: 1.01x slower                                                        |
| nqueens                    | 80.5 ms                                                                | 81.5 ms: 1.01x slower                                                        |
| html5lib                   | 61.0 ms                                                                | 62.0 ms: 1.02x slower                                                        |
| scimark_fft                | 311 ms                                                                 | 317 ms: 1.02x slower                                                         |
| pprint_safe_repr           | 733 ms                                                                 | 747 ms: 1.02x slower                                                         |
| regex_dna                  | 213 ms                                                                 | 219 ms: 1.03x slower                                                         |
| mako                       | 10.2 ms                                                                | 10.5 ms: 1.03x slower                                                        |
| pyflate                    | 429 ms                                                                 | 443 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (32): async_tree_io, async_tree_memoization_tg, pycparser, async_tree_memoization, spectral_norm, bench_mp_pool, k_core, pylint, thrift, sphinx, async_tree_none, asyncio_websockets, deepcopy_memo, async_generators, xml_etree_process, pidigits, sympy_sum, mdp, pprint_pformat, many_optionals, telco, regex_compile, bench_thread_pool, json, xml_etree_generate, json_loads, genshi_xml, sqlalchemy_imperative, pathlib, typing_runtime_protocols, async_tree_io_tg, pickle_pure_python

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x