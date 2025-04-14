# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.002x faster
- HPT reliability: 96.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 312 ms                                                                 | 309 ms: 1.01x faster                                             |
| docutils       | 2.85 sec                                                               | 2.83 sec: 1.01x faster                                           |
| html5lib       | 71.8 ms                                                                | 69.0 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io              | 603 ms                                                                 | 596 ms: 1.01x faster                                             |
| async_tree_none_tg         | 241 ms                                                                 | 239 ms: 1.01x faster                                             |
| async_generators           | 436 ms                                                                 | 438 ms: 1.00x slower                                             |
| async_tree_cpu_io_mixed    | 520 ms                                                                 | 528 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 480 ms: 1.02x slower                                             |
| coroutines                 | 25.2 ms                                                                | 26.7 ms: 1.06x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 181 ms: 1.06x faster                                             |
| float          | 79.5 ms                                                                | 79.1 ms: 1.01x faster                                            |
| nbody          | 136 ms                                                                 | 140 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 152 ms                                                                 | 150 ms: 1.01x faster                                             |
| regex_v8       | 24.8 ms                                                                | 25.3 ms: 1.02x slower                                            |
| regex_dna      | 216 ms                                                                 | 223 ms: 1.03x slower                                             |
| regex_effbot   | 3.29 ms                                                                | 3.48 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python | 390 us                                                                 | 380 us: 1.03x faster                                             |
| xml_etree_process  | 72.6 ms                                                                | 72.1 ms: 1.01x faster                                            |
| xml_etree_parse    | 148 ms                                                                 | 147 ms: 1.00x faster                                             |
| tomli_loads        | 2.39 sec                                                               | 2.41 sec: 1.01x slower                                           |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (5): json_dumps, json_loads, xml_etree_iterparse, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 9.36 ms                                                                | 9.34 ms: 1.00x faster                                            |
| python_startup         | 15.1 ms                                                                | 15.0 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 30.2 ms                                                                | 29.0 ms: 1.04x faster                                            |
| genshi_xml     | 63.5 ms                                                                | 61.4 ms: 1.03x faster                                            |
| mako           | 16.4 ms                                                                | 16.5 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mdp                        | 2.90 sec                                                               | 2.74 sec: 1.06x faster                                           |
| pidigits                   | 192 ms                                                                 | 181 ms: 1.06x faster                                             |
| genshi_text                | 30.2 ms                                                                | 29.0 ms: 1.04x faster                                            |
| richards_super             | 64.8 ms                                                                | 62.3 ms: 1.04x faster                                            |
| html5lib                   | 71.8 ms                                                                | 69.0 ms: 1.04x faster                                            |
| logging_format             | 8.04 us                                                                | 7.74 us: 1.04x faster                                            |
| genshi_xml                 | 63.5 ms                                                                | 61.4 ms: 1.03x faster                                            |
| pickle_pure_python         | 390 us                                                                 | 380 us: 1.03x faster                                             |
| generators                 | 31.6 ms                                                                | 30.8 ms: 1.02x faster                                            |
| logging_simple             | 7.04 us                                                                | 6.90 us: 1.02x faster                                            |
| richards                   | 54.8 ms                                                                | 53.8 ms: 1.02x faster                                            |
| chaos                      | 75.3 ms                                                                | 74.0 ms: 1.02x faster                                            |
| create_gc_cycles           | 1.73 ms                                                                | 1.70 ms: 1.02x faster                                            |
| raytrace                   | 361 ms                                                                 | 356 ms: 1.02x faster                                             |
| crypto_pyaes               | 92.0 ms                                                                | 90.8 ms: 1.01x faster                                            |
| telco                      | 9.22 ms                                                                | 9.10 ms: 1.01x faster                                            |
| thrift                     | 972 us                                                                 | 960 us: 1.01x faster                                             |
| async_tree_io              | 603 ms                                                                 | 596 ms: 1.01x faster                                             |
| go                         | 144 ms                                                                 | 142 ms: 1.01x faster                                             |
| comprehensions             | 21.1 us                                                                | 20.9 us: 1.01x faster                                            |
| 2to3                       | 312 ms                                                                 | 309 ms: 1.01x faster                                             |
| async_tree_none_tg         | 241 ms                                                                 | 239 ms: 1.01x faster                                             |
| docutils                   | 2.85 sec                                                               | 2.83 sec: 1.01x faster                                           |
| regex_compile              | 152 ms                                                                 | 150 ms: 1.01x faster                                             |
| bench_mp_pool              | 90.0 ms                                                                | 89.3 ms: 1.01x faster                                            |
| sqlalchemy_declarative     | 165 ms                                                                 | 163 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.97 ms                                                                | 1.95 ms: 1.01x faster                                            |
| sympy_integrate            | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                            |
| deepcopy_memo              | 40.2 us                                                                | 39.9 us: 1.01x faster                                            |
| deltablue                  | 4.71 ms                                                                | 4.68 ms: 1.01x faster                                            |
| sympy_str                  | 323 ms                                                                 | 321 ms: 1.01x faster                                             |
| xml_etree_process          | 72.6 ms                                                                | 72.1 ms: 1.01x faster                                            |
| float                      | 79.5 ms                                                                | 79.1 ms: 1.01x faster                                            |
| scimark_monte_carlo        | 87.8 ms                                                                | 87.3 ms: 1.01x faster                                            |
| sqlglot_optimize           | 61.0 ms                                                                | 60.7 ms: 1.00x faster                                            |
| k_core                     | 2.46 sec                                                               | 2.46 sec: 1.00x faster                                           |
| bpe_tokeniser              | 5.07 sec                                                               | 5.05 sec: 1.00x faster                                           |
| hexiom                     | 7.80 ms                                                                | 7.78 ms: 1.00x faster                                            |
| gc_traversal               | 4.18 ms                                                                | 4.17 ms: 1.00x faster                                            |
| xml_etree_parse            | 148 ms                                                                 | 147 ms: 1.00x faster                                             |
| python_startup_no_site     | 9.36 ms                                                                | 9.34 ms: 1.00x faster                                            |
| python_startup             | 15.1 ms                                                                | 15.0 ms: 1.00x faster                                            |
| shortest_path              | 570 ms                                                                 | 572 ms: 1.00x slower                                             |
| nqueens                    | 98.9 ms                                                                | 99.3 ms: 1.00x slower                                            |
| connected_components       | 527 ms                                                                 | 529 ms: 1.00x slower                                             |
| scimark_sor                | 143 ms                                                                 | 143 ms: 1.00x slower                                             |
| async_generators           | 436 ms                                                                 | 438 ms: 1.00x slower                                             |
| tomli_loads                | 2.39 sec                                                               | 2.41 sec: 1.01x slower                                           |
| mako                       | 16.4 ms                                                                | 16.5 ms: 1.01x slower                                            |
| fannkuch                   | 511 ms                                                                 | 514 ms: 1.01x slower                                             |
| json                       | 5.61 ms                                                                | 5.65 ms: 1.01x slower                                            |
| scimark_lu                 | 141 ms                                                                 | 143 ms: 1.01x slower                                             |
| typing_runtime_protocols   | 212 us                                                                 | 215 us: 1.01x slower                                             |
| async_tree_cpu_io_mixed    | 520 ms                                                                 | 528 ms: 1.01x slower                                             |
| logging_silent             | 119 ns                                                                 | 121 ns: 1.02x slower                                             |
| regex_v8                   | 24.8 ms                                                                | 25.3 ms: 1.02x slower                                            |
| scimark_fft                | 421 ms                                                                 | 429 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 480 ms: 1.02x slower                                             |
| pyflate                    | 515 ms                                                                 | 528 ms: 1.03x slower                                             |
| pycparser                  | 1.19 sec                                                               | 1.23 sec: 1.03x slower                                           |
| nbody                      | 136 ms                                                                 | 140 ms: 1.03x slower                                             |
| regex_dna                  | 216 ms                                                                 | 223 ms: 1.03x slower                                             |
| spectral_norm              | 115 ms                                                                 | 119 ms: 1.04x slower                                             |
| regex_effbot               | 3.29 ms                                                                | 3.48 ms: 1.06x slower                                            |
| coroutines                 | 25.2 ms                                                                | 26.7 ms: 1.06x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (31): async_tree_memoization_tg, sqlglot_parse, sympy_expand, json_dumps, sqlalchemy_imperative, sphinx, async_tree_memoization, many_optionals, pylint, json_loads, async_tree_io_tg, pprint_pformat, dulwich_log, sqlite_synth, sqlglot_normalize, xml_etree_iterparse, async_tree_none, deepcopy, pprint_safe_repr, coverage, sympy_sum, django_template, deepcopy_reduce, unpickle_pure_python, xml_etree_generate, bench_thread_pool, asyncio_websockets, meteor_contest, subparsers, pathlib, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 96.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x