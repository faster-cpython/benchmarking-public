# Results vs. base

- fork: brandtbucher
- ref: jit_optimizer_truthy
- machine: linux-x86_64
- commit hash: 7c487a0
- commit date: 2025-03-06
- overall geometric mean: 1.000x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.67 sec: 1.00x faster                                                       |
| html5lib       | 61.0 ms                                                                | 62.7 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 497 ms                                                                 | 491 ms: 1.01x faster                                                         |
| coroutines              | 24.5 ms                                                                | 24.3 ms: 1.01x faster                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none, async_generators, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 68.9 ms: 1.03x faster                                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                | 25.2 ms: 1.00x slower                                                        |
| regex_effbot   | 3.37 ms                                                                | 3.48 ms: 1.03x slower                                                        |
| regex_dna      | 213 ms                                                                 | 226 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse | 101 ms                                                                 | 99.2 ms: 1.01x faster                                                        |
| xml_etree_generate  | 79.2 ms                                                                | 78.5 ms: 1.01x faster                                                        |
| xml_etree_parse     | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| tomli_loads         | 1.85 sec                                                               | 1.84 sec: 1.00x faster                                                       |
| json_loads          | 30.0 us                                                                | 30.1 us: 1.00x slower                                                        |
| json_dumps          | 11.2 ms                                                                | 11.5 ms: 1.02x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.16 ms                                                                | 7.17 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.8 ms: 1.00x faster                                                        |
| mako            | 10.2 ms                                                                | 10.2 ms: 1.00x faster                                                        |
| genshi_xml      | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                        |
| genshi_text     | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| logging_silent          | 109 ns                                                                 | 103 ns: 1.06x faster                                                         |
| deltablue               | 3.38 ms                                                                | 3.26 ms: 1.04x faster                                                        |
| float                   | 71.1 ms                                                                | 68.9 ms: 1.03x faster                                                        |
| go                      | 121 ms                                                                 | 117 ms: 1.03x faster                                                         |
| richards                | 45.0 ms                                                                | 43.8 ms: 1.03x faster                                                        |
| richards_super          | 51.2 ms                                                                | 50.0 ms: 1.02x faster                                                        |
| raytrace                | 277 ms                                                                 | 270 ms: 1.02x faster                                                         |
| chaos                   | 60.3 ms                                                                | 59.1 ms: 1.02x faster                                                        |
| scimark_lu              | 119 ms                                                                 | 117 ms: 1.02x faster                                                         |
| logging_simple          | 5.61 us                                                                | 5.52 us: 1.02x faster                                                        |
| scimark_monte_carlo     | 68.9 ms                                                                | 67.7 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 101 ms                                                                 | 99.2 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 497 ms                                                                 | 491 ms: 1.01x faster                                                         |
| hexiom                  | 6.39 ms                                                                | 6.32 ms: 1.01x faster                                                        |
| thrift                  | 756 us                                                                 | 748 us: 1.01x faster                                                         |
| xml_etree_generate      | 79.2 ms                                                                | 78.5 ms: 1.01x faster                                                        |
| xml_etree_parse         | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| mdp                     | 2.51 sec                                                               | 2.49 sec: 1.01x faster                                                       |
| deepcopy_memo           | 29.2 us                                                                | 29.0 us: 1.01x faster                                                        |
| pathlib                 | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                        |
| 2to3                    | 262 ms                                                                 | 260 ms: 1.01x faster                                                         |
| sqlglot_parse           | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                        |
| sqlalchemy_declarative  | 131 ms                                                                 | 130 ms: 1.01x faster                                                         |
| bpe_tokeniser           | 4.48 sec                                                               | 4.46 sec: 1.01x faster                                                       |
| scimark_sor             | 120 ms                                                                 | 120 ms: 1.01x faster                                                         |
| coroutines              | 24.5 ms                                                                | 24.3 ms: 1.01x faster                                                        |
| many_optionals          | 963 us                                                                 | 958 us: 1.01x faster                                                         |
| meteor_contest          | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| tomli_loads             | 1.85 sec                                                               | 1.84 sec: 1.00x faster                                                       |
| comprehensions          | 17.8 us                                                                | 17.7 us: 1.00x faster                                                        |
| django_template         | 31.9 ms                                                                | 31.8 ms: 1.00x faster                                                        |
| docutils                | 2.68 sec                                                               | 2.67 sec: 1.00x faster                                                       |
| mako                    | 10.2 ms                                                                | 10.2 ms: 1.00x faster                                                        |
| python_startup          | 13.0 ms                                                                | 13.0 ms: 1.00x slower                                                        |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| python_startup_no_site  | 7.16 ms                                                                | 7.17 ms: 1.00x slower                                                        |
| scimark_fft             | 311 ms                                                                 | 312 ms: 1.00x slower                                                         |
| regex_v8                | 25.2 ms                                                                | 25.2 ms: 1.00x slower                                                        |
| connected_components    | 442 ms                                                                 | 443 ms: 1.00x slower                                                         |
| sympy_expand            | 471 ms                                                                 | 473 ms: 1.00x slower                                                         |
| json_loads              | 30.0 us                                                                | 30.1 us: 1.00x slower                                                        |
| genshi_xml              | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                        |
| sympy_sum               | 150 ms                                                                 | 151 ms: 1.01x slower                                                         |
| create_gc_cycles        | 2.44 ms                                                                | 2.46 ms: 1.01x slower                                                        |
| sqlite_synth            | 2.70 us                                                                | 2.72 us: 1.01x slower                                                        |
| subparsers              | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                        |
| gc_traversal            | 4.96 ms                                                                | 5.02 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.50 sec                                                               | 1.53 sec: 1.02x slower                                                       |
| nqueens                 | 80.5 ms                                                                | 81.9 ms: 1.02x slower                                                        |
| json_dumps              | 11.2 ms                                                                | 11.5 ms: 1.02x slower                                                        |
| html5lib                | 61.0 ms                                                                | 62.7 ms: 1.03x slower                                                        |
| genshi_text             | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                        |
| fannkuch                | 398 ms                                                                 | 411 ms: 1.03x slower                                                         |
| regex_effbot            | 3.37 ms                                                                | 3.48 ms: 1.03x slower                                                        |
| spectral_norm           | 96.0 ms                                                                | 99.8 ms: 1.04x slower                                                        |
| pyflate                 | 429 ms                                                                 | 448 ms: 1.04x slower                                                         |
| regex_dna               | 213 ms                                                                 | 226 ms: 1.06x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (39): async_tree_io, async_tree_none_tg, k_core, async_tree_memoization, sqlglot_transpile, async_tree_cpu_io_mixed_tg, pylint, logging_format, sqlalchemy_imperative, async_tree_memoization_tg, xml_etree_process, sympy_str, typing_runtime_protocols, deepcopy_reduce, pprint_safe_repr, deepcopy, asyncio_websockets, unpickle_pure_python, generators, shortest_path, crypto_pyaes, async_tree_none, pickle_pure_python, sympy_integrate, bench_mp_pool, async_generators, dulwich_log, sqlglot_normalize, json, nbody, coverage, bench_thread_pool, regex_compile, telco, sqlglot_optimize, sphinx, pycparser, scimark_sparse_mat_mult, async_tree_io_tg

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x