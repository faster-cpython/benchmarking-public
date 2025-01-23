# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.000x faster
- HPT reliability: 58.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                       | 281 ms: 1.00x slower                                                   |
| docutils       | 2.89 sec                                                                     | 2.87 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|---------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators          | 408 ms                                                                       | 403 ms: 1.01x faster                                                   |
| async_tree_none_tg        | 270 ms                                                                       | 267 ms: 1.01x faster                                                   |
| async_tree_memoization_tg | 329 ms                                                                       | 327 ms: 1.01x faster                                                   |
| coroutines                | 20.9 ms                                                                      | 21.0 ms: 1.01x slower                                                  |
| Geometric mean            | (ref)                                                                        | 1.00x faster                                                           |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 253 ms                                                                       | 255 ms: 1.01x slower                                                   |
| nbody          | 86.5 ms                                                                      | 87.8 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.06 ms                                                                      | 3.04 ms: 1.01x faster                                                  |
| regex_compile  | 135 ms                                                                       | 135 ms: 1.00x faster                                                   |
| regex_v8       | 25.9 ms                                                                      | 26.2 ms: 1.01x slower                                                  |
| regex_dna      | 236 ms                                                                       | 240 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process  | 62.7 ms                                                                      | 61.0 ms: 1.03x faster                                                  |
| xml_etree_parse    | 138 ms                                                                       | 134 ms: 1.02x faster                                                   |
| xml_etree_generate | 83.8 ms                                                                      | 83.2 ms: 1.01x faster                                                  |
| Geometric mean     | (ref)                                                                        | 1.01x faster                                                           |

Benchmark hidden because not significant (6): xml_etree_iterparse, unpickle_pure_python, json_loads, pickle_pure_python, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 36.2 ms                                                                      | 36.0 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                 | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|---------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pyflate                   | 447 ms                                                                       | 431 ms: 1.04x faster                                                   |
| fannkuch                  | 375 ms                                                                       | 362 ms: 1.04x faster                                                   |
| xml_etree_process         | 62.7 ms                                                                      | 61.0 ms: 1.03x faster                                                  |
| crypto_pyaes              | 75.0 ms                                                                      | 73.1 ms: 1.03x faster                                                  |
| telco                     | 8.26 ms                                                                      | 8.06 ms: 1.02x faster                                                  |
| xml_etree_parse           | 138 ms                                                                       | 134 ms: 1.02x faster                                                   |
| generators                | 28.8 ms                                                                      | 28.2 ms: 1.02x faster                                                  |
| scimark_fft               | 306 ms                                                                       | 301 ms: 1.02x faster                                                   |
| gc_traversal              | 6.55 ms                                                                      | 6.47 ms: 1.01x faster                                                  |
| comprehensions            | 17.7 us                                                                      | 17.5 us: 1.01x faster                                                  |
| async_generators          | 408 ms                                                                       | 403 ms: 1.01x faster                                                   |
| scimark_sor               | 110 ms                                                                       | 108 ms: 1.01x faster                                                   |
| chaos                     | 59.3 ms                                                                      | 58.6 ms: 1.01x faster                                                  |
| async_tree_none_tg        | 270 ms                                                                       | 267 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult   | 4.52 ms                                                                      | 4.48 ms: 1.01x faster                                                  |
| nqueens                   | 89.7 ms                                                                      | 88.8 ms: 1.01x faster                                                  |
| scimark_lu                | 95.6 ms                                                                      | 94.7 ms: 1.01x faster                                                  |
| xml_etree_generate        | 83.8 ms                                                                      | 83.2 ms: 1.01x faster                                                  |
| regex_effbot              | 3.06 ms                                                                      | 3.04 ms: 1.01x faster                                                  |
| dulwich_log               | 67.4 ms                                                                      | 67.0 ms: 1.01x faster                                                  |
| raytrace                  | 274 ms                                                                       | 272 ms: 1.01x faster                                                   |
| async_tree_memoization_tg | 329 ms                                                                       | 327 ms: 1.01x faster                                                   |
| django_template           | 36.2 ms                                                                      | 36.0 ms: 1.01x faster                                                  |
| docutils                  | 2.89 sec                                                                     | 2.87 sec: 1.01x faster                                                 |
| regex_compile             | 135 ms                                                                       | 135 ms: 1.00x faster                                                   |
| 2to3                      | 280 ms                                                                       | 281 ms: 1.00x slower                                                   |
| shortest_path             | 444 ms                                                                       | 445 ms: 1.00x slower                                                   |
| bpe_tokeniser             | 4.68 sec                                                                     | 4.69 sec: 1.00x slower                                                 |
| deepcopy_memo             | 29.8 us                                                                      | 29.9 us: 1.00x slower                                                  |
| deepcopy                  | 281 us                                                                       | 282 us: 1.00x slower                                                   |
| sqlalchemy_declarative    | 144 ms                                                                       | 144 ms: 1.00x slower                                                   |
| deepcopy_reduce           | 2.90 us                                                                      | 2.92 us: 1.00x slower                                                  |
| sqlglot_normalize         | 115 ms                                                                       | 116 ms: 1.00x slower                                                   |
| connected_components      | 416 ms                                                                       | 419 ms: 1.01x slower                                                   |
| coroutines                | 20.9 ms                                                                      | 21.0 ms: 1.01x slower                                                  |
| pidigits                  | 253 ms                                                                       | 255 ms: 1.01x slower                                                   |
| sqlglot_transpile         | 1.69 ms                                                                      | 1.70 ms: 1.01x slower                                                  |
| thrift                    | 867 us                                                                       | 872 us: 1.01x slower                                                   |
| sympy_integrate           | 23.0 ms                                                                      | 23.1 ms: 1.01x slower                                                  |
| go                        | 126 ms                                                                       | 127 ms: 1.01x slower                                                   |
| pprint_safe_repr          | 782 ms                                                                       | 788 ms: 1.01x slower                                                   |
| pathlib                   | 15.8 ms                                                                      | 15.9 ms: 1.01x slower                                                  |
| meteor_contest            | 127 ms                                                                       | 128 ms: 1.01x slower                                                   |
| deltablue                 | 3.28 ms                                                                      | 3.31 ms: 1.01x slower                                                  |
| hexiom                    | 5.97 ms                                                                      | 6.03 ms: 1.01x slower                                                  |
| regex_v8                  | 25.9 ms                                                                      | 26.2 ms: 1.01x slower                                                  |
| typing_runtime_protocols  | 176 us                                                                       | 178 us: 1.01x slower                                                   |
| mdp                       | 2.44 sec                                                                     | 2.48 sec: 1.01x slower                                                 |
| richards_super            | 52.4 ms                                                                      | 53.1 ms: 1.01x slower                                                  |
| coverage                  | 78.0 ms                                                                      | 79.1 ms: 1.01x slower                                                  |
| nbody                     | 86.5 ms                                                                      | 87.8 ms: 1.01x slower                                                  |
| pprint_pformat            | 1.58 sec                                                                     | 1.60 sec: 1.01x slower                                                 |
| sqlglot_parse             | 1.30 ms                                                                      | 1.32 ms: 1.01x slower                                                  |
| regex_dna                 | 236 ms                                                                       | 240 ms: 1.02x slower                                                   |
| logging_format            | 7.14 us                                                                      | 7.27 us: 1.02x slower                                                  |
| richards                  | 45.8 ms                                                                      | 46.7 ms: 1.02x slower                                                  |
| create_gc_cycles          | 2.76 ms                                                                      | 2.83 ms: 1.02x slower                                                  |
| spectral_norm             | 84.4 ms                                                                      | 86.6 ms: 1.03x slower                                                  |
| scimark_monte_carlo       | 63.0 ms                                                                      | 64.7 ms: 1.03x slower                                                  |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (37): html5lib, xml_etree_iterparse, async_tree_cpu_io_mixed, json, async_tree_none, async_tree_memoization, unpickle_pure_python, sphinx, bench_mp_pool, logging_silent, python_startup_no_site, many_optionals, logging_simple, json_loads, async_tree_io, subparsers, sympy_str, sqlglot_optimize, genshi_text, python_startup, sympy_sum, async_tree_cpu_io_mixed_tg, async_tree_io_tg, sympy_expand, pycparser, pickle_pure_python, tomli_loads, float, sqlalchemy_imperative, k_core, pylint, asyncio_websockets, sqlite_synth, genshi_xml, mako, bench_thread_pool, json_dumps

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 58.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x