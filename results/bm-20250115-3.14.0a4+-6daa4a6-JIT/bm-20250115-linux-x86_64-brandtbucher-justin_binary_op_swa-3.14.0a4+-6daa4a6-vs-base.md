# Results vs. base

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 6daa4a6
- commit date: 2025-01-15
- overall geometric mean: 1.004x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 23.8 ms                                                                | 23.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 474 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_generators, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 204 ms                                                                 | 203 ms: 1.00x faster                                                         |
| regex_compile  | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_v8       | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                        |
| regex_effbot   | 3.06 ms                                                                | 3.12 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process   | 55.7 ms                                                                | 54.8 ms: 1.02x faster                                                        |
| xml_etree_parse     | 137 ms                                                                 | 136 ms: 1.01x faster                                                         |
| json_dumps          | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                        |
| tomli_loads         | 1.85 sec                                                               | 1.83 sec: 1.01x faster                                                       |
| xml_etree_iterparse | 94.2 ms                                                                | 94.9 ms: 1.01x slower                                                        |
| json_loads          | 29.6 us                                                                | 29.8 us: 1.01x slower                                                        |
| pickle_pure_python  | 312 us                                                                 | 316 us: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 7.11 ms: 1.01x slower                                                        |
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.3 ms                                                                | 34.1 ms: 1.02x slower                                                        |
| genshi_xml      | 57.6 ms                                                                | 59.2 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pycparser                  | 1.18 sec                                                               | 1.13 sec: 1.04x faster                                                       |
| pyflate                    | 453 ms                                                                 | 435 ms: 1.04x faster                                                         |
| coroutines                 | 23.8 ms                                                                | 23.2 ms: 1.02x faster                                                        |
| xml_etree_process          | 55.7 ms                                                                | 54.8 ms: 1.02x faster                                                        |
| connected_components       | 441 ms                                                                 | 433 ms: 1.02x faster                                                         |
| logging_silent             | 109 ns                                                                 | 107 ns: 1.01x faster                                                         |
| xml_etree_parse            | 137 ms                                                                 | 136 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.60 ms                                                                | 1.58 ms: 1.01x faster                                                        |
| json_dumps                 | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 110 ms                                                                 | 109 ms: 1.01x faster                                                         |
| tomli_loads                | 1.85 sec                                                               | 1.83 sec: 1.01x faster                                                       |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| coverage                   | 90.7 ms                                                                | 90.0 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                       |
| sqlglot_optimize           | 55.2 ms                                                                | 54.9 ms: 1.01x faster                                                        |
| regex_dna                  | 204 ms                                                                 | 203 ms: 1.00x faster                                                         |
| sqlalchemy_declarative     | 132 ms                                                                 | 131 ms: 1.00x faster                                                         |
| sympy_sum                  | 157 ms                                                                 | 158 ms: 1.00x slower                                                         |
| regex_compile              | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| bench_mp_pool              | 81.1 ms                                                                | 81.6 ms: 1.01x slower                                                        |
| raytrace                   | 289 ms                                                                 | 291 ms: 1.01x slower                                                         |
| sympy_expand               | 475 ms                                                                 | 478 ms: 1.01x slower                                                         |
| sympy_str                  | 281 ms                                                                 | 283 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 94.2 ms                                                                | 94.9 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.06 ms                                                                | 7.11 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 474 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                        |
| json_loads                 | 29.6 us                                                                | 29.8 us: 1.01x slower                                                        |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.44 ms                                                                | 4.47 ms: 1.01x slower                                                        |
| hexiom                     | 7.12 ms                                                                | 7.17 ms: 1.01x slower                                                        |
| sympy_integrate            | 20.6 ms                                                                | 20.8 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                         |
| go                         | 134 ms                                                                 | 136 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.52 sec                                                               | 1.53 sec: 1.01x slower                                                       |
| bpe_tokeniser              | 4.40 sec                                                               | 4.45 sec: 1.01x slower                                                       |
| scimark_monte_carlo        | 62.2 ms                                                                | 63.0 ms: 1.01x slower                                                        |
| many_optionals             | 975 us                                                                 | 988 us: 1.01x slower                                                         |
| dulwich_log                | 67.4 ms                                                                | 68.3 ms: 1.01x slower                                                        |
| subparsers                 | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                                        |
| scimark_fft                | 314 ms                                                                 | 319 ms: 1.02x slower                                                         |
| pickle_pure_python         | 312 us                                                                 | 316 us: 1.02x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                                | 17.2 ms: 1.02x slower                                                        |
| regex_v8                   | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                        |
| nqueens                    | 90.1 ms                                                                | 91.6 ms: 1.02x slower                                                        |
| deepcopy                   | 267 us                                                                 | 272 us: 1.02x slower                                                         |
| deepcopy_memo              | 29.7 us                                                                | 30.3 us: 1.02x slower                                                        |
| deepcopy_reduce            | 2.73 us                                                                | 2.78 us: 1.02x slower                                                        |
| regex_effbot               | 3.06 ms                                                                | 3.12 ms: 1.02x slower                                                        |
| gc_traversal               | 4.93 ms                                                                | 5.04 ms: 1.02x slower                                                        |
| scimark_sor                | 112 ms                                                                 | 115 ms: 1.02x slower                                                         |
| pprint_safe_repr           | 735 ms                                                                 | 752 ms: 1.02x slower                                                         |
| django_template            | 33.3 ms                                                                | 34.1 ms: 1.02x slower                                                        |
| genshi_xml                 | 57.6 ms                                                                | 59.2 ms: 1.03x slower                                                        |
| chaos                      | 61.1 ms                                                                | 63.1 ms: 1.03x slower                                                        |
| fannkuch                   | 383 ms                                                                 | 396 ms: 1.03x slower                                                         |
| scimark_lu                 | 113 ms                                                                 | 117 ms: 1.03x slower                                                         |
| spectral_norm              | 102 ms                                                                 | 106 ms: 1.04x slower                                                         |
| crypto_pyaes               | 67.6 ms                                                                | 71.6 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (37): pathlib, genshi_text, comprehensions, async_tree_io, async_tree_memoization_tg, sqlglot_parse, typing_runtime_protocols, richards, deltablue, docutils, nbody, async_tree_memoization, 2to3, richards_super, async_generators, telco, shortest_path, asyncio_websockets, async_tree_none_tg, generators, bench_thread_pool, pylint, k_core, unpickle_pure_python, xml_etree_generate, sqlite_synth, logging_format, thrift, async_tree_cpu_io_mixed, logging_simple, mako, float, sphinx, async_tree_io_tg, html5lib, json, async_tree_none

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x