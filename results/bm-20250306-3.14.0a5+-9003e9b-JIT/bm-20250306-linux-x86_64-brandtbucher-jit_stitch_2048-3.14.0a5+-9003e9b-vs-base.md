# Results vs. base

- fork: brandtbucher
- ref: jit_stitch_2048
- machine: linux-x86_64
- commit hash: 9003e9b
- commit date: 2025-03-06
- overall geometric mean: 1.001x faster
- HPT reliability: 54.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                    |
| html5lib       | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines                 | 24.5 ms                                                                | 23.9 ms: 1.03x faster                                                   |
| async_generators           | 408 ms                                                                 | 410 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 489 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 69.4 ms: 1.02x faster                                                   |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 89.7 ms                                                                | 92.7 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                    |
| regex_v8       | 25.2 ms                                                                | 25.7 ms: 1.02x slower                                                   |
| regex_effbot   | 3.37 ms                                                                | 3.49 ms: 1.03x slower                                                   |
| regex_dna      | 213 ms                                                                 | 225 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 208 us                                                                 | 202 us: 1.03x faster                                                    |
| xml_etree_process    | 56.0 ms                                                                | 55.3 ms: 1.01x faster                                                   |
| xml_etree_generate   | 79.2 ms                                                                | 78.5 ms: 1.01x faster                                                   |
| pickle_pure_python   | 320 us                                                                 | 324 us: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, json_loads, json_dumps, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.15 ms: 1.00x faster                                                   |
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                   |
| genshi_text     | 21.3 ms                                                                | 21.2 ms: 1.01x faster                                                   |
| mako            | 10.2 ms                                                                | 10.2 ms: 1.00x faster                                                   |
| genshi_xml      | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.96 ms                                                                | 4.56 ms: 1.09x faster                                                   |
| richards                   | 45.0 ms                                                                | 43.4 ms: 1.04x faster                                                   |
| logging_silent             | 109 ns                                                                 | 106 ns: 1.03x faster                                                    |
| unpickle_pure_python       | 208 us                                                                 | 202 us: 1.03x faster                                                    |
| richards_super             | 51.2 ms                                                                | 49.9 ms: 1.03x faster                                                   |
| coroutines                 | 24.5 ms                                                                | 23.9 ms: 1.03x faster                                                   |
| raytrace                   | 277 ms                                                                 | 270 ms: 1.02x faster                                                    |
| float                      | 71.1 ms                                                                | 69.4 ms: 1.02x faster                                                   |
| go                         | 121 ms                                                                 | 118 ms: 1.02x faster                                                    |
| hexiom                     | 6.39 ms                                                                | 6.27 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 68.9 ms                                                                | 67.9 ms: 1.01x faster                                                   |
| deepcopy_memo              | 29.2 us                                                                | 28.8 us: 1.01x faster                                                   |
| xml_etree_process          | 56.0 ms                                                                | 55.3 ms: 1.01x faster                                                   |
| logging_simple             | 5.61 us                                                                | 5.55 us: 1.01x faster                                                   |
| chaos                      | 60.3 ms                                                                | 59.5 ms: 1.01x faster                                                   |
| django_template            | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                   |
| scimark_lu                 | 119 ms                                                                 | 118 ms: 1.01x faster                                                    |
| deltablue                  | 3.38 ms                                                                | 3.34 ms: 1.01x faster                                                   |
| xml_etree_generate         | 79.2 ms                                                                | 78.5 ms: 1.01x faster                                                   |
| pathlib                    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                   |
| deepcopy                   | 263 us                                                                 | 260 us: 1.01x faster                                                    |
| 2to3                       | 262 ms                                                                 | 260 ms: 1.01x faster                                                    |
| regex_compile              | 128 ms                                                                 | 127 ms: 1.01x faster                                                    |
| sqlalchemy_declarative     | 131 ms                                                                 | 130 ms: 1.01x faster                                                    |
| thrift                     | 756 us                                                                 | 751 us: 1.01x faster                                                    |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 4.48 sec                                                               | 4.46 sec: 1.01x faster                                                  |
| genshi_text                | 21.3 ms                                                                | 21.2 ms: 1.01x faster                                                   |
| generators                 | 28.0 ms                                                                | 27.9 ms: 1.01x faster                                                   |
| sqlglot_parse              | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                   |
| telco                      | 7.68 ms                                                                | 7.63 ms: 1.01x faster                                                   |
| create_gc_cycles           | 2.44 ms                                                                | 2.43 ms: 1.00x faster                                                   |
| mako                       | 10.2 ms                                                                | 10.2 ms: 1.00x faster                                                   |
| python_startup_no_site     | 7.16 ms                                                                | 7.15 ms: 1.00x faster                                                   |
| python_startup             | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| scimark_fft                | 311 ms                                                                 | 312 ms: 1.00x slower                                                    |
| sympy_str                  | 274 ms                                                                 | 275 ms: 1.00x slower                                                    |
| sqlite_synth               | 2.70 us                                                                | 2.71 us: 1.00x slower                                                   |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.9 ms: 1.00x slower                                                   |
| async_generators           | 408 ms                                                                 | 410 ms: 1.01x slower                                                    |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 489 ms: 1.01x slower                                                    |
| connected_components       | 442 ms                                                                 | 446 ms: 1.01x slower                                                    |
| sympy_sum                  | 150 ms                                                                 | 151 ms: 1.01x slower                                                    |
| fannkuch                   | 398 ms                                                                 | 403 ms: 1.01x slower                                                    |
| pickle_pure_python         | 320 us                                                                 | 324 us: 1.01x slower                                                    |
| scimark_sor                | 120 ms                                                                 | 122 ms: 1.01x slower                                                    |
| genshi_xml                 | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                                   |
| shortest_path              | 480 ms                                                                 | 489 ms: 1.02x slower                                                    |
| subparsers                 | 20.7 ms                                                                | 21.1 ms: 1.02x slower                                                   |
| regex_v8                   | 25.2 ms                                                                | 25.7 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 733 ms                                                                 | 748 ms: 1.02x slower                                                    |
| html5lib                   | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                   |
| nbody                      | 89.7 ms                                                                | 92.7 ms: 1.03x slower                                                   |
| regex_effbot               | 3.37 ms                                                                | 3.49 ms: 1.03x slower                                                   |
| pyflate                    | 429 ms                                                                 | 444 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 161 us                                                                 | 168 us: 1.05x slower                                                    |
| spectral_norm              | 96.0 ms                                                                | 101 ms: 1.05x slower                                                    |
| regex_dna                  | 213 ms                                                                 | 225 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (36): k_core, scimark_sparse_mat_mult, pylint, crypto_pyaes, deepcopy_reduce, comprehensions, xml_etree_parse, coverage, pprint_pformat, json_loads, dulwich_log, async_tree_cpu_io_mixed, sympy_integrate, many_optionals, json_dumps, asyncio_websockets, bench_thread_pool, tomli_loads, docutils, sqlglot_normalize, nqueens, async_tree_memoization, logging_format, sphinx, mdp, sympy_expand, async_tree_none_tg, bench_mp_pool, xml_etree_iterparse, sqlglot_optimize, async_tree_io, pycparser, json, async_tree_none, async_tree_memoization_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 54.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x