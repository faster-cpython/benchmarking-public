# Results vs. base

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.001x slower
- HPT reliability: 56.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| html5lib       | 61.3 ms                                                                | 59.8 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 482 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                 | 458 ms: 1.02x faster                                         |
| async_generators           | 385 ms                                                                 | 382 ms: 1.01x faster                                         |
| coroutines                 | 22.9 ms                                                                | 23.0 ms: 1.00x slower                                        |
| async_tree_io_tg           | 580 ms                                                                 | 584 ms: 1.01x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 95.5 ms                                                                | 94.3 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                         |
| float          | 68.2 ms                                                                | 70.3 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                                | 3.29 ms: 1.01x faster                                        |
| regex_v8       | 25.6 ms                                                                | 26.1 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_process    | 59.6 ms                                                                | 59.1 ms: 1.01x faster                                        |
| tomli_loads          | 1.93 sec                                                               | 1.94 sec: 1.01x slower                                       |
| unpickle_pure_python | 215 us                                                                 | 218 us: 1.01x slower                                         |
| json_dumps           | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (5): json_loads, xml_etree_generate, pickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                        |
| python_startup_no_site | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.3 ms                                                                | 11.2 ms: 1.00x faster                                        |
| django_template | 31.7 ms                                                                | 31.9 ms: 1.01x slower                                        |
| genshi_xml      | 47.9 ms                                                                | 48.7 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| generators                 | 29.2 ms                                                                | 28.0 ms: 1.04x faster                                        |
| gc_traversal               | 4.94 ms                                                                | 4.78 ms: 1.03x faster                                        |
| html5lib                   | 61.3 ms                                                                | 59.8 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 482 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                 | 458 ms: 1.02x faster                                         |
| spectral_norm              | 95.0 ms                                                                | 93.5 ms: 1.02x faster                                        |
| nqueens                    | 81.0 ms                                                                | 79.8 ms: 1.02x faster                                        |
| deepcopy_memo              | 30.8 us                                                                | 30.4 us: 1.01x faster                                        |
| scimark_sparse_mat_mult    | 4.69 ms                                                                | 4.63 ms: 1.01x faster                                        |
| nbody                      | 95.5 ms                                                                | 94.3 ms: 1.01x faster                                        |
| pathlib                    | 16.3 ms                                                                | 16.1 ms: 1.01x faster                                        |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                        |
| logging_format             | 6.07 us                                                                | 6.01 us: 1.01x faster                                        |
| regex_effbot               | 3.32 ms                                                                | 3.29 ms: 1.01x faster                                        |
| async_generators           | 385 ms                                                                 | 382 ms: 1.01x faster                                         |
| sqlglot_optimize           | 52.9 ms                                                                | 52.4 ms: 1.01x faster                                        |
| richards                   | 43.7 ms                                                                | 43.4 ms: 1.01x faster                                        |
| xml_etree_process          | 59.6 ms                                                                | 59.1 ms: 1.01x faster                                        |
| logging_simple             | 5.45 us                                                                | 5.41 us: 1.01x faster                                        |
| sympy_expand               | 449 ms                                                                 | 446 ms: 1.01x faster                                         |
| scimark_fft                | 345 ms                                                                 | 343 ms: 1.00x faster                                         |
| sympy_str                  | 264 ms                                                                 | 263 ms: 1.00x faster                                         |
| many_optionals             | 937 us                                                                 | 933 us: 1.00x faster                                         |
| create_gc_cycles           | 2.46 ms                                                                | 2.45 ms: 1.00x faster                                        |
| mako                       | 11.3 ms                                                                | 11.2 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                         |
| hexiom                     | 6.23 ms                                                                | 6.24 ms: 1.00x slower                                        |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                        |
| sympy_integrate            | 19.6 ms                                                                | 19.7 ms: 1.00x slower                                        |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.00x slower                                         |
| python_startup_no_site     | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                        |
| pprint_pformat             | 1.47 sec                                                               | 1.48 sec: 1.00x slower                                       |
| coroutines                 | 22.9 ms                                                                | 23.0 ms: 1.00x slower                                        |
| bpe_tokeniser              | 4.46 sec                                                               | 4.49 sec: 1.01x slower                                       |
| django_template            | 31.7 ms                                                                | 31.9 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 67.7 ms                                                                | 68.1 ms: 1.01x slower                                        |
| go                         | 116 ms                                                                 | 117 ms: 1.01x slower                                         |
| async_tree_io_tg           | 580 ms                                                                 | 584 ms: 1.01x slower                                         |
| mdp                        | 2.46 sec                                                               | 2.47 sec: 1.01x slower                                       |
| scimark_lu                 | 115 ms                                                                 | 116 ms: 1.01x slower                                         |
| scimark_sor                | 121 ms                                                                 | 122 ms: 1.01x slower                                         |
| tomli_loads                | 1.93 sec                                                               | 1.94 sec: 1.01x slower                                       |
| logging_silent             | 105 ns                                                                 | 106 ns: 1.01x slower                                         |
| unpickle_pure_python       | 215 us                                                                 | 218 us: 1.01x slower                                         |
| sqlglot_transpile          | 1.54 ms                                                                | 1.56 ms: 1.01x slower                                        |
| deepcopy_reduce            | 2.57 us                                                                | 2.60 us: 1.01x slower                                        |
| shortest_path              | 479 ms                                                                 | 485 ms: 1.01x slower                                         |
| chaos                      | 57.4 ms                                                                | 58.1 ms: 1.01x slower                                        |
| json_dumps                 | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                        |
| raytrace                   | 267 ms                                                                 | 271 ms: 1.01x slower                                         |
| comprehensions             | 16.8 us                                                                | 17.0 us: 1.01x slower                                        |
| sqlglot_parse              | 1.23 ms                                                                | 1.25 ms: 1.02x slower                                        |
| genshi_xml                 | 47.9 ms                                                                | 48.7 ms: 1.02x slower                                        |
| connected_components       | 440 ms                                                                 | 448 ms: 1.02x slower                                         |
| regex_v8                   | 25.6 ms                                                                | 26.1 ms: 1.02x slower                                        |
| deltablue                  | 3.15 ms                                                                | 3.22 ms: 1.02x slower                                        |
| float                      | 68.2 ms                                                                | 70.3 ms: 1.03x slower                                        |
| pyflate                    | 451 ms                                                                 | 474 ms: 1.05x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (38): telco, coverage, json_loads, pprint_safe_repr, subparsers, k_core, pycparser, sphinx, pylint, richards_super, docutils, crypto_pyaes, sqlalchemy_declarative, xml_etree_generate, bench_thread_pool, 2to3, dulwich_log, sqlglot_normalize, thrift, fannkuch, json, pickle_pure_python, asyncio_websockets, bench_mp_pool, regex_compile, regex_dna, deepcopy, async_tree_none, sqlite_synth, async_tree_none_tg, xml_etree_parse, sympy_sum, async_tree_memoization, xml_etree_iterparse, genshi_text, async_tree_io, async_tree_memoization_tg, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 56.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x