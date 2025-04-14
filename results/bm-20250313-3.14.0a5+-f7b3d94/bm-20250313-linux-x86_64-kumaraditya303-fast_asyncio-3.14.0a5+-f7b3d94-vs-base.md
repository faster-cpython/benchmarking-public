# Results vs. base

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.002x slower
- HPT reliability: 78.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 519 ms                                                                 | 522 ms: 1.01x slower                                                   |
| docutils       | 5.21 sec                                                               | 5.25 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 510 ms                                                                 | 498 ms: 1.02x faster                                                   |
| asyncio_websockets         | 1.10 sec                                                               | 1.09 sec: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 965 ms                                                                 | 973 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed    | 991 ms                                                                 | 1.00 sec: 1.01x slower                                                 |
| async_generators           | 775 ms                                                                 | 787 ms: 1.02x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_io, coroutines, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 387 ms                                                                 | 372 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 437 ms                                                                 | 427 ms: 1.02x faster                                                   |
| regex_v8       | 47.3 ms                                                                | 46.5 ms: 1.02x faster                                                  |
| regex_effbot   | 6.65 ms                                                                | 6.83 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads        | 3.95 sec                                                               | 3.88 sec: 1.02x faster                                                 |
| xml_etree_generate | 168 ms                                                                 | 171 ms: 1.02x slower                                                   |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (7): json_loads, json_dumps, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 42.9 ms                                                                | 43.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits                   | 387 ms                                                                 | 372 ms: 1.04x faster                                                   |
| logging_simple             | 11.3 us                                                                | 10.9 us: 1.03x faster                                                  |
| logging_format             | 12.3 us                                                                | 12.0 us: 1.02x faster                                                  |
| regex_dna                  | 437 ms                                                                 | 427 ms: 1.02x faster                                                   |
| async_tree_none_tg         | 510 ms                                                                 | 498 ms: 1.02x faster                                                   |
| connected_components       | 967 ms                                                                 | 948 ms: 1.02x faster                                                   |
| tomli_loads                | 3.95 sec                                                               | 3.88 sec: 1.02x faster                                                 |
| regex_v8                   | 47.3 ms                                                                | 46.5 ms: 1.02x faster                                                  |
| asyncio_websockets         | 1.10 sec                                                               | 1.09 sec: 1.01x faster                                                 |
| pprint_pformat             | 3.02 sec                                                               | 2.99 sec: 1.01x faster                                                 |
| pprint_safe_repr           | 1.48 sec                                                               | 1.47 sec: 1.01x faster                                                 |
| shortest_path              | 1.04 sec                                                               | 1.03 sec: 1.01x faster                                                 |
| sympy_expand               | 910 ms                                                                 | 905 ms: 1.01x faster                                                   |
| 2to3                       | 519 ms                                                                 | 522 ms: 1.01x slower                                                   |
| docutils                   | 5.21 sec                                                               | 5.25 sec: 1.01x slower                                                 |
| bpe_tokeniser              | 9.07 sec                                                               | 9.15 sec: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 965 ms                                                                 | 973 ms: 1.01x slower                                                   |
| pyflate                    | 907 ms                                                                 | 916 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed    | 991 ms                                                                 | 1.00 sec: 1.01x slower                                                 |
| raytrace                   | 535 ms                                                                 | 542 ms: 1.01x slower                                                   |
| async_generators           | 775 ms                                                                 | 787 ms: 1.02x slower                                                   |
| thrift                     | 1.54 ms                                                                | 1.56 ms: 1.02x slower                                                  |
| xml_etree_generate         | 168 ms                                                                 | 171 ms: 1.02x slower                                                   |
| crypto_pyaes               | 152 ms                                                                 | 154 ms: 1.02x slower                                                   |
| scimark_fft                | 704 ms                                                                 | 717 ms: 1.02x slower                                                   |
| genshi_text                | 42.9 ms                                                                | 43.8 ms: 1.02x slower                                                  |
| hexiom                     | 12.2 ms                                                                | 12.5 ms: 1.02x slower                                                  |
| fannkuch                   | 840 ms                                                                 | 860 ms: 1.02x slower                                                   |
| logging_silent             | 195 ns                                                                 | 201 ns: 1.03x slower                                                   |
| deltablue                  | 6.23 ms                                                                | 6.40 ms: 1.03x slower                                                  |
| regex_effbot               | 6.65 ms                                                                | 6.83 ms: 1.03x slower                                                  |
| pycparser                  | 2.27 sec                                                               | 2.35 sec: 1.04x slower                                                 |
| scimark_lu                 | 227 ms                                                                 | 236 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 9.27 ms                                                                | 9.84 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (62): async_tree_memoization_tg, json_loads, sqlite_synth, async_tree_io_tg, sqlalchemy_imperative, deepcopy_memo, genshi_xml, async_tree_none, async_tree_io, bench_thread_pool, comprehensions, coverage, mako, deepcopy_reduce, nqueens, json_dumps, k_core, pickle_pure_python, sqlglot_v2_optimize, meteor_contest, unpickle_pure_python, sqlalchemy_declarative, richards, xml_etree_iterparse, sympy_str, mdp, coroutines, subparsers, django_template, float, bench_mp_pool, scimark_sor, pylint, python_startup, async_tree_memoization, sympy_integrate, pathlib, sphinx, sqlglot_v2_parse, python_startup_no_site, sympy_sum, typing_runtime_protocols, go, json, xml_etree_parse, deepcopy, dulwich_log, nbody, richards_super, sqlglot_v2_transpile, scimark_monte_carlo, sqlglot_v2_normalize, regex_compile, many_optionals, spectral_norm, telco, html5lib, chaos, generators, xml_etree_process, create_gc_cycles, gc_traversal

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 78.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x