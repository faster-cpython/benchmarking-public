# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.000x slower
- HPT reliability: 95.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| html5lib       | 71.8 ms                                                                | 70.3 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 552 ms                                                                 | 556 ms: 1.01x slower                                           |
| async_tree_none_tg         | 241 ms                                                                 | 244 ms: 1.01x slower                                           |
| async_tree_memoization     | 367 ms                                                                 | 372 ms: 1.01x slower                                           |
| async_generators           | 436 ms                                                                 | 443 ms: 1.02x slower                                           |
| async_tree_none            | 287 ms                                                                 | 292 ms: 1.02x slower                                           |
| coroutines                 | 25.2 ms                                                                | 25.8 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 482 ms: 1.03x slower                                           |
| async_tree_cpu_io_mixed    | 520 ms                                                                 | 534 ms: 1.03x slower                                           |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 181 ms: 1.06x faster                                           |
| float          | 79.5 ms                                                                | 78.3 ms: 1.02x faster                                          |
| nbody          | 136 ms                                                                 | 137 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 152 ms                                                                 | 152 ms: 1.00x slower                                           |
| regex_v8       | 24.8 ms                                                                | 25.5 ms: 1.03x slower                                          |
| regex_dna      | 216 ms                                                                 | 224 ms: 1.04x slower                                           |
| regex_effbot   | 3.29 ms                                                                | 3.48 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python | 390 us                                                                 | 385 us: 1.01x faster                                           |
| json_dumps         | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                          |
| xml_etree_generate | 96.2 ms                                                                | 96.6 ms: 1.00x slower                                          |
| xml_etree_parse    | 148 ms                                                                 | 148 ms: 1.00x slower                                           |
| tomli_loads        | 2.39 sec                                                               | 2.43 sec: 1.01x slower                                         |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 9.36 ms                                                                | 9.35 ms: 1.00x faster                                          |
| python_startup         | 15.1 ms                                                                | 15.1 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 63.5 ms                                                                | 62.1 ms: 1.02x faster                                          |
| genshi_text     | 30.2 ms                                                                | 29.5 ms: 1.02x faster                                          |
| django_template | 41.7 ms                                                                | 41.6 ms: 1.00x faster                                          |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits                   | 192 ms                                                                 | 181 ms: 1.06x faster                                           |
| mdp                        | 2.90 sec                                                               | 2.75 sec: 1.06x faster                                         |
| richards_super             | 64.8 ms                                                                | 62.8 ms: 1.03x faster                                          |
| logging_format             | 8.04 us                                                                | 7.78 us: 1.03x faster                                          |
| html5lib                   | 71.8 ms                                                                | 70.3 ms: 1.02x faster                                          |
| genshi_xml                 | 63.5 ms                                                                | 62.1 ms: 1.02x faster                                          |
| genshi_text                | 30.2 ms                                                                | 29.5 ms: 1.02x faster                                          |
| logging_simple             | 7.04 us                                                                | 6.93 us: 1.02x faster                                          |
| float                      | 79.5 ms                                                                | 78.3 ms: 1.02x faster                                          |
| scimark_sparse_mat_mult    | 6.21 ms                                                                | 6.12 ms: 1.01x faster                                          |
| logging_silent             | 119 ns                                                                 | 117 ns: 1.01x faster                                           |
| deepcopy_memo              | 40.2 us                                                                | 39.7 us: 1.01x faster                                          |
| raytrace                   | 361 ms                                                                 | 356 ms: 1.01x faster                                           |
| pickle_pure_python         | 390 us                                                                 | 385 us: 1.01x faster                                           |
| coverage                   | 108 ms                                                                 | 107 ms: 1.01x faster                                           |
| pathlib                    | 16.3 ms                                                                | 16.1 ms: 1.01x faster                                          |
| richards                   | 54.8 ms                                                                | 54.2 ms: 1.01x faster                                          |
| deepcopy_reduce            | 3.30 us                                                                | 3.27 us: 1.01x faster                                          |
| sympy_expand               | 538 ms                                                                 | 534 ms: 1.01x faster                                           |
| telco                      | 9.22 ms                                                                | 9.14 ms: 1.01x faster                                          |
| crypto_pyaes               | 92.0 ms                                                                | 91.3 ms: 1.01x faster                                          |
| json_dumps                 | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                          |
| fannkuch                   | 511 ms                                                                 | 507 ms: 1.01x faster                                           |
| comprehensions             | 21.1 us                                                                | 20.9 us: 1.01x faster                                          |
| sqlite_synth               | 2.76 us                                                                | 2.74 us: 1.01x faster                                          |
| scimark_fft                | 421 ms                                                                 | 419 ms: 1.01x faster                                           |
| thrift                     | 972 us                                                                 | 968 us: 1.01x faster                                           |
| chaos                      | 75.3 ms                                                                | 75.0 ms: 1.00x faster                                          |
| sympy_str                  | 323 ms                                                                 | 322 ms: 1.00x faster                                           |
| deepcopy                   | 318 us                                                                 | 317 us: 1.00x faster                                           |
| django_template            | 41.7 ms                                                                | 41.6 ms: 1.00x faster                                          |
| python_startup_no_site     | 9.36 ms                                                                | 9.35 ms: 1.00x faster                                          |
| python_startup             | 15.1 ms                                                                | 15.1 ms: 1.00x slower                                          |
| go                         | 144 ms                                                                 | 144 ms: 1.00x slower                                           |
| connected_components       | 527 ms                                                                 | 528 ms: 1.00x slower                                           |
| dulwich_log                | 70.2 ms                                                                | 70.4 ms: 1.00x slower                                          |
| sympy_integrate            | 24.0 ms                                                                | 24.1 ms: 1.00x slower                                          |
| regex_compile              | 152 ms                                                                 | 152 ms: 1.00x slower                                           |
| xml_etree_generate         | 96.2 ms                                                                | 96.6 ms: 1.00x slower                                          |
| bpe_tokeniser              | 5.07 sec                                                               | 5.09 sec: 1.00x slower                                         |
| xml_etree_parse            | 148 ms                                                                 | 148 ms: 1.00x slower                                           |
| pprint_safe_repr           | 866 ms                                                                 | 869 ms: 1.00x slower                                           |
| generators                 | 31.6 ms                                                                | 31.7 ms: 1.00x slower                                          |
| hexiom                     | 7.80 ms                                                                | 7.83 ms: 1.00x slower                                          |
| async_tree_io_tg           | 552 ms                                                                 | 556 ms: 1.01x slower                                           |
| sympy_sum                  | 178 ms                                                                 | 180 ms: 1.01x slower                                           |
| subparsers                 | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                          |
| nbody                      | 136 ms                                                                 | 137 ms: 1.01x slower                                           |
| async_tree_none_tg         | 241 ms                                                                 | 244 ms: 1.01x slower                                           |
| typing_runtime_protocols   | 212 us                                                                 | 215 us: 1.01x slower                                           |
| async_tree_memoization     | 367 ms                                                                 | 372 ms: 1.01x slower                                           |
| tomli_loads                | 2.39 sec                                                               | 2.43 sec: 1.01x slower                                         |
| pyflate                    | 515 ms                                                                 | 523 ms: 1.01x slower                                           |
| async_generators           | 436 ms                                                                 | 443 ms: 1.02x slower                                           |
| async_tree_none            | 287 ms                                                                 | 292 ms: 1.02x slower                                           |
| coroutines                 | 25.2 ms                                                                | 25.8 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 482 ms: 1.03x slower                                           |
| regex_v8                   | 24.8 ms                                                                | 25.5 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed    | 520 ms                                                                 | 534 ms: 1.03x slower                                           |
| regex_dna                  | 216 ms                                                                 | 224 ms: 1.04x slower                                           |
| pycparser                  | 1.19 sec                                                               | 1.24 sec: 1.04x slower                                         |
| regex_effbot               | 3.29 ms                                                                | 3.48 ms: 1.06x slower                                          |
| gc_traversal               | 4.18 ms                                                                | 4.45 ms: 1.06x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (33): bench_mp_pool, scimark_lu, sqlglot_parse, scimark_sor, sqlglot_transpile, json_loads, deltablue, xml_etree_process, create_gc_cycles, 2to3, many_optionals, k_core, scimark_monte_carlo, pylint, sqlglot_optimize, unpickle_pure_python, bench_thread_pool, sqlalchemy_declarative, shortest_path, pprint_pformat, mako, nqueens, sqlglot_normalize, asyncio_websockets, xml_etree_iterparse, docutils, json, async_tree_io, spectral_norm, sphinx, async_tree_memoization_tg, meteor_contest, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 95.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x