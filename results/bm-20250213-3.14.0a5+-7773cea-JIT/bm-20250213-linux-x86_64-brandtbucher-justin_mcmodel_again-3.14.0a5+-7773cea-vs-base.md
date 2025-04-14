# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 7773cea
- commit date: 2025-02-13
- overall geometric mean: 1.006x slower
- HPT reliability: 93.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 258 ms: 1.00x slower                                                         |
| docutils       | 2.65 sec                                                               | 2.63 sec: 1.01x faster                                                       |
| html5lib       | 60.6 ms                                                                | 61.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                                 | 254 ms: 1.01x faster                                                         |
| async_tree_none            | 268 ms                                                                 | 265 ms: 1.01x faster                                                         |
| coroutines                 | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 487 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 496 ms: 1.01x slower                                                         |
| async_generators           | 403 ms                                                                 | 413 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): async_tree_memoization, asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.0 ms                                                                | 85.8 ms: 1.05x faster                                                        |
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| float          | 70.5 ms                                                                | 71.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 23.5 ms: 1.02x faster                                                        |
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                         |
| regex_dna      | 202 ms                                                                 | 209 ms: 1.03x slower                                                         |
| regex_effbot   | 3.01 ms                                                                | 3.26 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 138 ms                                                                 | 137 ms: 1.01x faster                                                         |
| xml_etree_process   | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                                        |
| xml_etree_iterparse | 96.2 ms                                                                | 97.0 ms: 1.01x slower                                                        |
| tomli_loads         | 1.84 sec                                                               | 1.89 sec: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_generate, json_loads, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.06 ms: 1.00x faster                                                        |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.92 ms                                                                | 9.99 ms: 1.01x slower                                                        |
| genshi_text     | 21.3 ms                                                                | 21.5 ms: 1.01x slower                                                        |
| django_template | 31.6 ms                                                                | 32.5 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pycparser                  | 1.17 sec                                                               | 1.12 sec: 1.05x faster                                                       |
| nbody                      | 90.0 ms                                                                | 85.8 ms: 1.05x faster                                                        |
| regex_v8                   | 24.0 ms                                                                | 23.5 ms: 1.02x faster                                                        |
| telco                      | 7.72 ms                                                                | 7.57 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 727 ms                                                                 | 715 ms: 1.02x faster                                                         |
| nqueens                    | 83.3 ms                                                                | 82.0 ms: 1.01x faster                                                        |
| comprehensions             | 17.2 us                                                                | 17.0 us: 1.01x faster                                                        |
| async_tree_none_tg         | 258 ms                                                                 | 254 ms: 1.01x faster                                                         |
| async_tree_none            | 268 ms                                                                 | 265 ms: 1.01x faster                                                         |
| hexiom                     | 6.67 ms                                                                | 6.59 ms: 1.01x faster                                                        |
| coroutines                 | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                        |
| xml_etree_parse            | 138 ms                                                                 | 137 ms: 1.01x faster                                                         |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| xml_etree_process          | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                                        |
| scimark_fft                | 313 ms                                                                 | 310 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.48 ms                                                                | 2.47 ms: 1.01x faster                                                        |
| docutils                   | 2.65 sec                                                               | 2.63 sec: 1.01x faster                                                       |
| sqlglot_parse              | 1.29 ms                                                                | 1.29 ms: 1.00x faster                                                        |
| connected_components       | 440 ms                                                                 | 438 ms: 1.00x faster                                                         |
| python_startup_no_site     | 7.08 ms                                                                | 7.06 ms: 1.00x faster                                                        |
| dulwich_log                | 66.5 ms                                                                | 66.3 ms: 1.00x faster                                                        |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| gc_traversal               | 4.80 ms                                                                | 4.80 ms: 1.00x slower                                                        |
| 2to3                       | 258 ms                                                                 | 258 ms: 1.00x slower                                                         |
| sympy_str                  | 273 ms                                                                 | 274 ms: 1.00x slower                                                         |
| sympy_integrate            | 20.0 ms                                                                | 20.2 ms: 1.01x slower                                                        |
| mako                       | 9.92 ms                                                                | 9.99 ms: 1.01x slower                                                        |
| sympy_sum                  | 149 ms                                                                 | 150 ms: 1.01x slower                                                         |
| subparsers                 | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 96.2 ms                                                                | 97.0 ms: 1.01x slower                                                        |
| scimark_lu                 | 116 ms                                                                 | 117 ms: 1.01x slower                                                         |
| pathlib                    | 16.1 ms                                                                | 16.3 ms: 1.01x slower                                                        |
| genshi_text                | 21.3 ms                                                                | 21.5 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 162 us                                                                 | 164 us: 1.01x slower                                                         |
| deepcopy                   | 261 us                                                                 | 263 us: 1.01x slower                                                         |
| regex_compile              | 126 ms                                                                 | 127 ms: 1.01x slower                                                         |
| sqlglot_optimize           | 53.2 ms                                                                | 53.7 ms: 1.01x slower                                                        |
| float                      | 70.5 ms                                                                | 71.3 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 487 ms: 1.01x slower                                                         |
| mdp                        | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 496 ms: 1.01x slower                                                         |
| richards_super             | 50.2 ms                                                                | 50.9 ms: 1.02x slower                                                        |
| deepcopy_memo              | 30.4 us                                                                | 30.9 us: 1.02x slower                                                        |
| crypto_pyaes               | 71.4 ms                                                                | 72.6 ms: 1.02x slower                                                        |
| coverage                   | 88.6 ms                                                                | 90.1 ms: 1.02x slower                                                        |
| raytrace                   | 272 ms                                                                 | 277 ms: 1.02x slower                                                         |
| generators                 | 27.7 ms                                                                | 28.3 ms: 1.02x slower                                                        |
| html5lib                   | 60.6 ms                                                                | 61.9 ms: 1.02x slower                                                        |
| async_generators           | 403 ms                                                                 | 413 ms: 1.02x slower                                                         |
| sqlglot_normalize          | 105 ms                                                                 | 107 ms: 1.03x slower                                                         |
| thrift                     | 751 us                                                                 | 770 us: 1.03x slower                                                         |
| tomli_loads                | 1.84 sec                                                               | 1.89 sec: 1.03x slower                                                       |
| chaos                      | 58.7 ms                                                                | 60.4 ms: 1.03x slower                                                        |
| richards                   | 43.6 ms                                                                | 44.9 ms: 1.03x slower                                                        |
| django_template            | 31.6 ms                                                                | 32.5 ms: 1.03x slower                                                        |
| regex_dna                  | 202 ms                                                                 | 209 ms: 1.03x slower                                                         |
| scimark_sor                | 119 ms                                                                 | 123 ms: 1.03x slower                                                         |
| scimark_monte_carlo        | 66.4 ms                                                                | 68.8 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.49 ms                                                                | 4.68 ms: 1.04x slower                                                        |
| deltablue                  | 3.28 ms                                                                | 3.44 ms: 1.05x slower                                                        |
| spectral_norm              | 94.6 ms                                                                | 100 ms: 1.06x slower                                                         |
| regex_effbot               | 3.01 ms                                                                | 3.26 ms: 1.08x slower                                                        |
| logging_silent             | 102 ns                                                                 | 110 ns: 1.09x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (33): unpickle_pure_python, shortest_path, logging_format, logging_simple, pyflate, sqlite_synth, xml_etree_generate, pprint_pformat, deepcopy_reduce, fannkuch, sqlglot_transpile, k_core, meteor_contest, bench_mp_pool, json_loads, async_tree_memoization, json, bench_thread_pool, sympy_expand, pickle_pure_python, sqlalchemy_declarative, genshi_xml, many_optionals, asyncio_websockets, bpe_tokeniser, sqlalchemy_imperative, async_tree_io, async_tree_memoization_tg, go, async_tree_io_tg, sphinx, json_dumps, pylint

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 93.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x