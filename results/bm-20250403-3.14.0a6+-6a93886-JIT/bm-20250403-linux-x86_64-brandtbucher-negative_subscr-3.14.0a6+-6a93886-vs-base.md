# Results vs. base

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.001x faster
- HPT reliability: 75.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                 | 254 ms: 1.01x faster                                                    |
| html5lib       | 61.9 ms                                                                | 61.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 473 ms: 1.01x faster                                                    |
| async_generators           | 414 ms                                                                 | 410 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 488 ms: 1.01x faster                                                    |
| async_tree_memoization     | 313 ms                                                                 | 311 ms: 1.01x faster                                                    |
| asyncio_websockets         | 551 ms                                                                 | 554 ms: 1.00x slower                                                    |
| coroutines                 | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| float          | 61.5 ms                                                                | 62.0 ms: 1.01x slower                                                   |
| nbody          | 86.4 ms                                                                | 89.7 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 210 ms: 1.05x faster                                                    |
| regex_effbot   | 3.35 ms                                                                | 3.26 ms: 1.03x faster                                                   |
| regex_v8       | 23.2 ms                                                                | 24.0 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 209 us                                                                 | 206 us: 1.01x faster                                                    |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                    |
| json_loads           | 29.6 us                                                                | 29.8 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_iterparse, pickle_pure_python, xml_etree_generate, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.19 ms                                                                | 8.23 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 49.9 ms                                                                | 48.8 ms: 1.02x faster                                                   |
| django_template | 32.6 ms                                                                | 32.2 ms: 1.01x faster                                                   |
| genshi_text     | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                                   |
| mako            | 10.9 ms                                                                | 11.0 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna                  | 221 ms                                                                 | 210 ms: 1.05x faster                                                    |
| nqueens                    | 84.7 ms                                                                | 81.6 ms: 1.04x faster                                                   |
| spectral_norm              | 100 ms                                                                 | 96.9 ms: 1.04x faster                                                   |
| typing_runtime_protocols   | 173 us                                                                 | 167 us: 1.03x faster                                                    |
| pyflate                    | 429 ms                                                                 | 416 ms: 1.03x faster                                                    |
| fannkuch                   | 415 ms                                                                 | 403 ms: 1.03x faster                                                    |
| regex_effbot               | 3.35 ms                                                                | 3.26 ms: 1.03x faster                                                   |
| pycparser                  | 1.17 sec                                                               | 1.14 sec: 1.03x faster                                                  |
| telco                      | 8.02 ms                                                                | 7.82 ms: 1.02x faster                                                   |
| genshi_xml                 | 49.9 ms                                                                | 48.8 ms: 1.02x faster                                                   |
| html5lib                   | 61.9 ms                                                                | 61.0 ms: 1.02x faster                                                   |
| django_template            | 32.6 ms                                                                | 32.2 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 473 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 209 us                                                                 | 206 us: 1.01x faster                                                    |
| logging_silent             | 95.9 ns                                                                | 94.9 ns: 1.01x faster                                                   |
| sqlglot_v2_transpile       | 1.58 ms                                                                | 1.56 ms: 1.01x faster                                                   |
| 2to3                       | 257 ms                                                                 | 254 ms: 1.01x faster                                                    |
| shortest_path              | 493 ms                                                                 | 489 ms: 1.01x faster                                                    |
| sqlglot_v2_parse           | 1.25 ms                                                                | 1.24 ms: 1.01x faster                                                   |
| async_generators           | 414 ms                                                                 | 410 ms: 1.01x faster                                                    |
| xml_etree_parse            | 140 ms                                                                 | 139 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 4.55 sec                                                               | 4.52 sec: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 488 ms: 1.01x faster                                                    |
| async_tree_memoization     | 313 ms                                                                 | 311 ms: 1.01x faster                                                    |
| genshi_text                | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                                   |
| scimark_sor                | 117 ms                                                                 | 117 ms: 1.00x faster                                                    |
| mdp                        | 1.22 sec                                                               | 1.22 sec: 1.00x faster                                                  |
| connected_components       | 451 ms                                                                 | 449 ms: 1.00x faster                                                    |
| bench_thread_pool          | 890 us                                                                 | 887 us: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| create_gc_cycles           | 2.50 ms                                                                | 2.50 ms: 1.00x slower                                                   |
| generators                 | 29.5 ms                                                                | 29.6 ms: 1.00x slower                                                   |
| asyncio_websockets         | 551 ms                                                                 | 554 ms: 1.00x slower                                                    |
| sympy_sum                  | 150 ms                                                                 | 151 ms: 1.00x slower                                                    |
| sqlglot_v2_normalize       | 108 ms                                                                 | 109 ms: 1.00x slower                                                    |
| dulwich_log                | 60.2 ms                                                                | 60.5 ms: 1.00x slower                                                   |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                   |
| python_startup_no_site     | 8.19 ms                                                                | 8.23 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.2 ms: 1.01x slower                                                   |
| sympy_expand               | 469 ms                                                                 | 472 ms: 1.01x slower                                                    |
| go                         | 123 ms                                                                 | 124 ms: 1.01x slower                                                    |
| json                       | 5.27 ms                                                                | 5.30 ms: 1.01x slower                                                   |
| json_loads                 | 29.6 us                                                                | 29.8 us: 1.01x slower                                                   |
| crypto_pyaes               | 74.4 ms                                                                | 75.0 ms: 1.01x slower                                                   |
| bench_mp_pool              | 82.7 ms                                                                | 83.4 ms: 1.01x slower                                                   |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                    |
| hexiom                     | 6.70 ms                                                                | 6.76 ms: 1.01x slower                                                   |
| float                      | 61.5 ms                                                                | 62.0 ms: 1.01x slower                                                   |
| mako                       | 10.9 ms                                                                | 11.0 ms: 1.01x slower                                                   |
| logging_format             | 6.15 us                                                                | 6.22 us: 1.01x slower                                                   |
| coroutines                 | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 4.64 ms                                                                | 4.70 ms: 1.01x slower                                                   |
| scimark_lu                 | 116 ms                                                                 | 117 ms: 1.01x slower                                                    |
| gc_traversal               | 4.82 ms                                                                | 4.89 ms: 1.01x slower                                                   |
| deepcopy_memo              | 28.6 us                                                                | 29.0 us: 1.01x slower                                                   |
| pprint_safe_repr           | 750 ms                                                                 | 761 ms: 1.01x slower                                                    |
| pathlib                    | 16.6 ms                                                                | 16.8 ms: 1.02x slower                                                   |
| chaos                      | 56.8 ms                                                                | 57.7 ms: 1.02x slower                                                   |
| raytrace                   | 259 ms                                                                 | 264 ms: 1.02x slower                                                    |
| regex_v8                   | 23.2 ms                                                                | 24.0 ms: 1.04x slower                                                   |
| nbody                      | 86.4 ms                                                                | 89.7 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (34): async_tree_none_tg, richards, sphinx, deepcopy_reduce, xml_etree_process, scimark_monte_carlo, sqlite_synth, comprehensions, sqlalchemy_declarative, async_tree_none, logging_simple, xml_etree_iterparse, pickle_pure_python, xml_etree_generate, pylint, deltablue, sympy_integrate, docutils, coverage, sqlglot_v2_optimize, richards_super, many_optionals, regex_compile, async_tree_memoization_tg, scimark_fft, sympy_str, async_tree_io_tg, subparsers, k_core, async_tree_io, deepcopy, tomli_loads, json_dumps, pprint_pformat

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 75.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x