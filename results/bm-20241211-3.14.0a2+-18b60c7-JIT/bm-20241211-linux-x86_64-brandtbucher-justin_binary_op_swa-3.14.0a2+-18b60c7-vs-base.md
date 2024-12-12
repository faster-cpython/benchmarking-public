# Results vs. base

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18b60c7
- commit date: 2024-12-11
- overall geometric mean: 1.005x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 258 ms: 1.00x slower                                                         |
| html5lib       | 64.7 ms                                                                | 63.2 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators          | 449 ms                                                                 | 445 ms: 1.01x faster                                                         |
| async_tree_memoization_tg | 317 ms                                                                 | 318 ms: 1.01x slower                                                         |
| coroutines                | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                        |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 75.6 ms                                                                | 77.2 ms: 1.02x slower                                                        |
| nbody          | 80.8 ms                                                                | 93.8 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.19 ms: 1.10x faster                                                        |
| regex_dna      | 220 ms                                                                 | 211 ms: 1.04x faster                                                         |
| regex_v8       | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                        |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads         | 26.3 us                                                                | 25.9 us: 1.01x faster                                                        |
| xml_etree_process  | 54.9 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| xml_etree_parse    | 137 ms                                                                 | 138 ms: 1.01x slower                                                         |
| tomli_loads        | 1.93 sec                                                               | 1.96 sec: 1.02x slower                                                       |
| xml_etree_generate | 78.2 ms                                                                | 81.2 ms: 1.04x slower                                                        |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (4): unpickle_pure_python, json_dumps, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                        |
| python_startup_no_site | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.0 ms                                                                | 56.3 ms: 1.01x faster                                                        |
| django_template | 34.2 ms                                                                | 33.9 ms: 1.01x faster                                                        |
| genshi_text     | 24.0 ms                                                                | 23.9 ms: 1.01x faster                                                        |
| mako            | 10.2 ms                                                                | 10.2 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot              | 3.51 ms                                                                | 3.19 ms: 1.10x faster                                                        |
| mdp                       | 2.77 sec                                                               | 2.57 sec: 1.08x faster                                                       |
| regex_dna                 | 220 ms                                                                 | 211 ms: 1.04x faster                                                         |
| deepcopy_reduce           | 2.81 us                                                                | 2.70 us: 1.04x faster                                                        |
| deepcopy                  | 275 us                                                                 | 267 us: 1.03x faster                                                         |
| json                      | 4.92 ms                                                                | 4.80 ms: 1.02x faster                                                        |
| html5lib                  | 64.7 ms                                                                | 63.2 ms: 1.02x faster                                                        |
| richards_super            | 44.7 ms                                                                | 43.8 ms: 1.02x faster                                                        |
| regex_v8                  | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                        |
| logging_format            | 6.30 us                                                                | 6.19 us: 1.02x faster                                                        |
| json_loads                | 26.3 us                                                                | 25.9 us: 1.01x faster                                                        |
| genshi_xml                | 57.0 ms                                                                | 56.3 ms: 1.01x faster                                                        |
| logging_simple            | 5.75 us                                                                | 5.68 us: 1.01x faster                                                        |
| sqlite_synth              | 2.82 us                                                                | 2.79 us: 1.01x faster                                                        |
| thrift                    | 786 us                                                                 | 777 us: 1.01x faster                                                         |
| richards                  | 37.3 ms                                                                | 36.9 ms: 1.01x faster                                                        |
| async_generators          | 449 ms                                                                 | 445 ms: 1.01x faster                                                         |
| django_template           | 34.2 ms                                                                | 33.9 ms: 1.01x faster                                                        |
| subparsers                | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                        |
| xml_etree_process         | 54.9 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| genshi_text               | 24.0 ms                                                                | 23.9 ms: 1.01x faster                                                        |
| 2to3                      | 258 ms                                                                 | 258 ms: 1.00x slower                                                         |
| shortest_path             | 478 ms                                                                 | 479 ms: 1.00x slower                                                         |
| fannkuch                  | 385 ms                                                                 | 386 ms: 1.00x slower                                                         |
| bpe_tokeniser             | 4.39 sec                                                               | 4.40 sec: 1.00x slower                                                       |
| connected_components      | 434 ms                                                                 | 436 ms: 1.00x slower                                                         |
| meteor_contest            | 108 ms                                                                 | 108 ms: 1.00x slower                                                         |
| comprehensions            | 17.2 us                                                                | 17.3 us: 1.00x slower                                                        |
| sqlalchemy_imperative     | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                                        |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                        |
| sqlglot_normalize         | 110 ms                                                                 | 111 ms: 1.01x slower                                                         |
| python_startup_no_site    | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                        |
| async_tree_memoization_tg | 317 ms                                                                 | 318 ms: 1.01x slower                                                         |
| logging_silent            | 101 ns                                                                 | 101 ns: 1.01x slower                                                         |
| pathlib                   | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                        |
| xml_etree_parse           | 137 ms                                                                 | 138 ms: 1.01x slower                                                         |
| sympy_expand              | 473 ms                                                                 | 476 ms: 1.01x slower                                                         |
| mako                      | 10.2 ms                                                                | 10.2 ms: 1.01x slower                                                        |
| sqlglot_transpile         | 1.64 ms                                                                | 1.65 ms: 1.01x slower                                                        |
| deltablue                 | 3.17 ms                                                                | 3.19 ms: 1.01x slower                                                        |
| sqlglot_parse             | 1.32 ms                                                                | 1.33 ms: 1.01x slower                                                        |
| typing_runtime_protocols  | 169 us                                                                 | 170 us: 1.01x slower                                                         |
| create_gc_cycles          | 2.44 ms                                                                | 2.47 ms: 1.01x slower                                                        |
| sympy_str                 | 280 ms                                                                 | 283 ms: 1.01x slower                                                         |
| regex_compile             | 128 ms                                                                 | 130 ms: 1.01x slower                                                         |
| coroutines                | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                        |
| pprint_pformat            | 1.46 sec                                                               | 1.47 sec: 1.01x slower                                                       |
| scimark_monte_carlo       | 64.8 ms                                                                | 65.6 ms: 1.01x slower                                                        |
| hexiom                    | 6.98 ms                                                                | 7.07 ms: 1.01x slower                                                        |
| telco                     | 7.56 ms                                                                | 7.66 ms: 1.01x slower                                                        |
| sympy_integrate           | 20.5 ms                                                                | 20.8 ms: 1.01x slower                                                        |
| tomli_loads               | 1.93 sec                                                               | 1.96 sec: 1.02x slower                                                       |
| djangocms                 | 22.3 us                                                                | 22.8 us: 1.02x slower                                                        |
| sympy_sum                 | 153 ms                                                                 | 156 ms: 1.02x slower                                                         |
| coverage                  | 82.6 ms                                                                | 84.3 ms: 1.02x slower                                                        |
| float                     | 75.6 ms                                                                | 77.2 ms: 1.02x slower                                                        |
| crypto_pyaes              | 68.6 ms                                                                | 70.8 ms: 1.03x slower                                                        |
| pyflate                   | 447 ms                                                                 | 462 ms: 1.03x slower                                                         |
| raytrace                  | 282 ms                                                                 | 291 ms: 1.03x slower                                                         |
| spectral_norm             | 114 ms                                                                 | 118 ms: 1.04x slower                                                         |
| pycparser                 | 1.15 sec                                                               | 1.19 sec: 1.04x slower                                                       |
| xml_etree_generate        | 78.2 ms                                                                | 81.2 ms: 1.04x slower                                                        |
| gc_traversal              | 4.75 ms                                                                | 4.95 ms: 1.04x slower                                                        |
| scimark_fft               | 321 ms                                                                 | 343 ms: 1.07x slower                                                         |
| chaos                     | 59.1 ms                                                                | 63.7 ms: 1.08x slower                                                        |
| scimark_sparse_mat_mult   | 4.57 ms                                                                | 5.13 ms: 1.12x slower                                                        |
| nbody                     | 80.8 ms                                                                | 93.8 ms: 1.16x slower                                                        |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (31): sphinx, pprint_safe_repr, async_tree_cpu_io_mixed_tg, unpickle_pure_python, go, many_optionals, deepcopy_memo, docutils, scimark_lu, json_dumps, async_tree_cpu_io_mixed, sqlalchemy_declarative, dulwich_log, pidigits, nqueens, bench_mp_pool, sqlglot_optimize, bench_thread_pool, async_tree_none, asyncio_websockets, k_core, xml_etree_iterparse, scimark_sor, pylint, generators, async_tree_memoization, mypy2, async_tree_io, async_tree_none_tg, pickle_pure_python, async_tree_io_tg

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x