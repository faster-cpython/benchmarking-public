# Results vs. base

- fork: brandtbucher
- ref: jit_optimizer_equali
- machine: linux-x86_64
- commit hash: 3f0f396
- commit date: 2025-03-06
- overall geometric mean: 1.000x slower
- HPT reliability: 75.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 261 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.67 sec: 1.00x faster                                                       |
| html5lib       | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 487 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 478 ms: 1.02x faster                                                         |
| async_generators           | 408 ms                                                                 | 404 ms: 1.01x faster                                                         |
| coroutines                 | 24.5 ms                                                                | 24.4 ms: 1.00x faster                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (7): async_tree_none_tg, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 70.0 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| nbody          | 89.7 ms                                                                | 98.9 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                         |
| regex_effbot   | 3.37 ms                                                                | 3.40 ms: 1.01x slower                                                        |
| regex_v8       | 25.2 ms                                                                | 25.5 ms: 1.01x slower                                                        |
| regex_dna      | 213 ms                                                                 | 221 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse | 101 ms                                                                 | 98.7 ms: 1.02x faster                                                        |
| xml_etree_parse     | 148 ms                                                                 | 146 ms: 1.01x faster                                                         |
| json_loads          | 30.0 us                                                                | 29.7 us: 1.01x faster                                                        |
| pickle_pure_python  | 320 us                                                                 | 323 us: 1.01x slower                                                         |
| json_dumps          | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                        |
| xml_etree_process   | 56.0 ms                                                                | 56.9 ms: 1.02x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): unpickle_pure_python, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.16 ms                                                                | 7.15 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                                        |
| mako           | 10.2 ms                                                                | 10.6 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| logging_simple             | 5.61 us                                                                | 5.45 us: 1.03x faster                                                        |
| logging_silent             | 109 ns                                                                 | 106 ns: 1.03x faster                                                         |
| richards                   | 45.0 ms                                                                | 44.1 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 487 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 4.54 ms                                                                | 4.44 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                                 | 98.7 ms: 1.02x faster                                                        |
| richards_super             | 51.2 ms                                                                | 50.4 ms: 1.02x faster                                                        |
| logging_format             | 6.18 us                                                                | 6.08 us: 1.02x faster                                                        |
| spectral_norm              | 96.0 ms                                                                | 94.4 ms: 1.02x faster                                                        |
| float                      | 71.1 ms                                                                | 70.0 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 478 ms: 1.02x faster                                                         |
| coverage                   | 85.0 ms                                                                | 83.8 ms: 1.01x faster                                                        |
| deepcopy                   | 263 us                                                                 | 259 us: 1.01x faster                                                         |
| deltablue                  | 3.38 ms                                                                | 3.34 ms: 1.01x faster                                                        |
| sympy_expand               | 471 ms                                                                 | 466 ms: 1.01x faster                                                         |
| chaos                      | 60.3 ms                                                                | 59.6 ms: 1.01x faster                                                        |
| xml_etree_parse            | 148 ms                                                                 | 146 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 107 ms                                                                 | 106 ms: 1.01x faster                                                         |
| comprehensions             | 17.8 us                                                                | 17.6 us: 1.01x faster                                                        |
| async_generators           | 408 ms                                                                 | 404 ms: 1.01x faster                                                         |
| go                         | 121 ms                                                                 | 120 ms: 1.01x faster                                                         |
| deepcopy_reduce            | 2.71 us                                                                | 2.69 us: 1.01x faster                                                        |
| sqlglot_parse              | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                        |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                        |
| sympy_str                  | 274 ms                                                                 | 272 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| json_loads                 | 30.0 us                                                                | 29.7 us: 1.01x faster                                                        |
| mdp                        | 2.51 sec                                                               | 2.49 sec: 1.01x faster                                                       |
| many_optionals             | 963 us                                                                 | 958 us: 1.01x faster                                                         |
| connected_components       | 442 ms                                                                 | 439 ms: 1.01x faster                                                         |
| 2to3                       | 262 ms                                                                 | 261 ms: 1.01x faster                                                         |
| sqlalchemy_declarative     | 131 ms                                                                 | 130 ms: 1.00x faster                                                         |
| pyflate                    | 429 ms                                                                 | 427 ms: 1.00x faster                                                         |
| docutils                   | 2.68 sec                                                               | 2.67 sec: 1.00x faster                                                       |
| bpe_tokeniser              | 4.48 sec                                                               | 4.47 sec: 1.00x faster                                                       |
| coroutines                 | 24.5 ms                                                                | 24.4 ms: 1.00x faster                                                        |
| sympy_integrate            | 20.2 ms                                                                | 20.1 ms: 1.00x faster                                                        |
| python_startup             | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.16 ms                                                                | 7.15 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| create_gc_cycles           | 2.44 ms                                                                | 2.44 ms: 1.00x slower                                                        |
| scimark_fft                | 311 ms                                                                 | 313 ms: 1.00x slower                                                         |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x slower                                                         |
| sympy_sum                  | 150 ms                                                                 | 150 ms: 1.00x slower                                                         |
| generators                 | 28.0 ms                                                                | 28.2 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                         |
| regex_effbot               | 3.37 ms                                                                | 3.40 ms: 1.01x slower                                                        |
| gc_traversal               | 4.96 ms                                                                | 5.00 ms: 1.01x slower                                                        |
| genshi_text                | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                                        |
| pickle_pure_python         | 320 us                                                                 | 323 us: 1.01x slower                                                         |
| sqlite_synth               | 2.70 us                                                                | 2.73 us: 1.01x slower                                                        |
| scimark_sor                | 120 ms                                                                 | 122 ms: 1.01x slower                                                         |
| regex_v8                   | 25.2 ms                                                                | 25.5 ms: 1.01x slower                                                        |
| json_dumps                 | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                        |
| xml_etree_process          | 56.0 ms                                                                | 56.9 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.50 sec                                                               | 1.53 sec: 1.02x slower                                                       |
| deepcopy_memo              | 29.2 us                                                                | 29.7 us: 1.02x slower                                                        |
| pathlib                    | 16.8 ms                                                                | 17.1 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 161 us                                                                 | 164 us: 1.02x slower                                                         |
| html5lib                   | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                        |
| nqueens                    | 80.5 ms                                                                | 82.8 ms: 1.03x slower                                                        |
| regex_dna                  | 213 ms                                                                 | 221 ms: 1.03x slower                                                         |
| mako                       | 10.2 ms                                                                | 10.6 ms: 1.04x slower                                                        |
| nbody                      | 89.7 ms                                                                | 98.9 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (32): async_tree_none_tg, scimark_lu, k_core, bench_mp_pool, unpickle_pure_python, crypto_pyaes, telco, subparsers, scimark_monte_carlo, asyncio_websockets, sqlglot_optimize, pylint, json, django_template, shortest_path, dulwich_log, tomli_loads, hexiom, bench_thread_pool, sphinx, raytrace, genshi_xml, thrift, async_tree_memoization, async_tree_io, xml_etree_generate, pprint_safe_repr, async_tree_memoization_tg, pycparser, async_tree_none, async_tree_io_tg, fannkuch

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 75.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x