# Results vs. base

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.007x faster
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 5.68 sec                                                               | 5.62 sec: 1.01x faster                                                 |
| sphinx         | 2.26 sec                                                               | 2.23 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 472 ms                                                                 | 458 ms: 1.03x faster                                                   |
| async_tree_none            | 559 ms                                                                 | 547 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 944 ms                                                                 | 925 ms: 1.02x faster                                                   |
| async_tree_memoization     | 707 ms                                                                 | 693 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed    | 1.03 sec                                                               | 1.01 sec: 1.02x faster                                                 |
| async_tree_memoization_tg  | 626 ms                                                                 | 615 ms: 1.02x faster                                                   |
| async_tree_io_tg           | 1.06 sec                                                               | 1.04 sec: 1.02x faster                                                 |
| async_tree_io              | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                                 |
| async_generators           | 870 ms                                                                 | 862 ms: 1.01x faster                                                   |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 268 ms                                                                 | 277 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 47.2 ms                                                                | 45.1 ms: 1.05x faster                                                  |
| regex_dna      | 448 ms                                                                 | 432 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse | 181 ms                                                                 | 185 ms: 1.03x slower                                                   |
| xml_etree_process   | 134 ms                                                                 | 138 ms: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (7): json_loads, json_dumps, xml_etree_parse, tomli_loads, xml_etree_generate, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 35.3 ms                                                                | 32.6 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 32.9 ms                                                                | 32.3 ms: 1.02x faster                                                  |
| genshi_xml     | 117 ms                                                                 | 123 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250313-linux-x86_64-python-dd6d24e9d20407ea31a3-3.14.0a5+-dd6d24e | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| sqlalchemy_imperative      | 46.3 ms                                                                | 40.8 ms: 1.14x faster                                                  |
| dulwich_log                | 139 ms                                                                 | 126 ms: 1.10x faster                                                   |
| python_startup             | 35.3 ms                                                                | 32.6 ms: 1.08x faster                                                  |
| pycparser                  | 2.37 sec                                                               | 2.27 sec: 1.05x faster                                                 |
| mdp                        | 5.74 sec                                                               | 5.49 sec: 1.05x faster                                                 |
| spectral_norm              | 234 ms                                                                 | 224 ms: 1.05x faster                                                   |
| regex_v8                   | 47.2 ms                                                                | 45.1 ms: 1.05x faster                                                  |
| sympy_sum                  | 367 ms                                                                 | 352 ms: 1.04x faster                                                   |
| many_optionals             | 2.26 ms                                                                | 2.17 ms: 1.04x faster                                                  |
| regex_dna                  | 448 ms                                                                 | 432 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 472 ms                                                                 | 458 ms: 1.03x faster                                                   |
| sympy_str                  | 653 ms                                                                 | 637 ms: 1.03x faster                                                   |
| sympy_integrate            | 48.2 ms                                                                | 47.1 ms: 1.02x faster                                                  |
| async_tree_none            | 559 ms                                                                 | 547 ms: 1.02x faster                                                   |
| sympy_expand               | 1.09 sec                                                               | 1.07 sec: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 944 ms                                                                 | 925 ms: 1.02x faster                                                   |
| async_tree_memoization     | 707 ms                                                                 | 693 ms: 1.02x faster                                                   |
| mako                       | 32.9 ms                                                                | 32.3 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed    | 1.03 sec                                                               | 1.01 sec: 1.02x faster                                                 |
| async_tree_memoization_tg  | 626 ms                                                                 | 615 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 12.7 ms                                                                | 12.5 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 1.06 sec                                                               | 1.04 sec: 1.02x faster                                                 |
| nqueens                    | 200 ms                                                                 | 196 ms: 1.02x faster                                                   |
| bench_mp_pool              | 144 ms                                                                 | 142 ms: 1.01x faster                                                   |
| async_tree_io              | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                                 |
| sphinx                     | 2.26 sec                                                               | 2.23 sec: 1.01x faster                                                 |
| docutils                   | 5.68 sec                                                               | 5.62 sec: 1.01x faster                                                 |
| k_core                     | 4.95 sec                                                               | 4.90 sec: 1.01x faster                                                 |
| sqlalchemy_declarative     | 323 ms                                                                 | 320 ms: 1.01x faster                                                   |
| async_generators           | 870 ms                                                                 | 862 ms: 1.01x faster                                                   |
| fannkuch                   | 1.05 sec                                                               | 1.05 sec: 1.01x faster                                                 |
| bpe_tokeniser              | 10.2 sec                                                               | 10.1 sec: 1.00x faster                                                 |
| pprint_pformat             | 3.46 sec                                                               | 3.50 sec: 1.01x slower                                                 |
| raytrace                   | 658 ms                                                                 | 667 ms: 1.01x slower                                                   |
| scimark_sor                | 274 ms                                                                 | 278 ms: 1.01x slower                                                   |
| richards_super             | 125 ms                                                                 | 127 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 181 ms                                                                 | 185 ms: 1.03x slower                                                   |
| go                         | 277 ms                                                                 | 284 ms: 1.03x slower                                                   |
| xml_etree_process          | 134 ms                                                                 | 138 ms: 1.03x slower                                                   |
| shortest_path              | 1.15 sec                                                               | 1.18 sec: 1.03x slower                                                 |
| nbody                      | 268 ms                                                                 | 277 ms: 1.03x slower                                                   |
| connected_components       | 1.08 sec                                                               | 1.12 sec: 1.04x slower                                                 |
| deepcopy_memo              | 76.4 us                                                                | 79.7 us: 1.04x slower                                                  |
| deepcopy_reduce            | 6.30 us                                                                | 6.58 us: 1.04x slower                                                  |
| genshi_xml                 | 117 ms                                                                 | 123 ms: 1.05x slower                                                   |
| gc_traversal               | 4.33 ms                                                                | 4.55 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (50): pylint, comprehensions, logging_format, json_loads, json_dumps, thrift, crypto_pyaes, xml_etree_parse, regex_compile, sqlglot_v2_normalize, meteor_contest, pidigits, django_template, sqlglot_v2_parse, pyflate, coroutines, python_startup_no_site, logging_simple, bench_thread_pool, logging_silent, tomli_loads, telco, sqlite_synth, float, xml_etree_generate, asyncio_websockets, deltablue, typing_runtime_protocols, genshi_text, 2to3, scimark_fft, sqlglot_v2_optimize, scimark_lu, pprint_safe_repr, richards, generators, scimark_monte_carlo, coverage, sqlglot_v2_transpile, pickle_pure_python, subparsers, unpickle_pure_python, deepcopy, pathlib, json, regex_effbot, hexiom, html5lib, chaos, create_gc_cycles

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 99.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x