# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.001x faster
- HPT reliability: 70.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                       | 282 ms: 1.01x slower                                                 |
| docutils       | 2.89 sec                                                                     | 2.88 sec: 1.00x faster                                               |
| html5lib       | 67.4 ms                                                                      | 66.5 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg        | 270 ms                                                                       | 266 ms: 1.01x faster                                                 |
| async_tree_memoization_tg | 329 ms                                                                       | 325 ms: 1.01x faster                                                 |
| async_generators          | 408 ms                                                                       | 410 ms: 1.00x slower                                                 |
| coroutines                | 20.9 ms                                                                      | 21.0 ms: 1.01x slower                                                |
| Geometric mean            | (ref)                                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 253 ms                                                                       | 254 ms: 1.00x slower                                                 |
| nbody          | 86.5 ms                                                                      | 87.1 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                       | 135 ms: 1.00x faster                                                 |
| regex_effbot   | 3.06 ms                                                                      | 3.11 ms: 1.02x slower                                                |
| regex_v8       | 25.9 ms                                                                      | 26.4 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process  | 62.7 ms                                                                      | 60.7 ms: 1.03x faster                                                |
| xml_etree_generate | 83.8 ms                                                                      | 83.2 ms: 1.01x faster                                                |
| json_dumps         | 11.6 ms                                                                      | 11.5 ms: 1.01x faster                                                |
| json_loads         | 25.3 us                                                                      | 25.5 us: 1.01x slower                                                |
| tomli_loads        | 2.06 sec                                                                     | 2.08 sec: 1.01x slower                                               |
| pickle_pure_python | 334 us                                                                       | 339 us: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.98 ms                                                                      | 9.01 ms: 1.00x slower                                                |
| python_startup         | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 36.2 ms                                                                      | 36.0 ms: 1.01x faster                                                |
| genshi_xml      | 54.2 ms                                                                      | 54.6 ms: 1.01x slower                                                |
| mako            | 10.9 ms                                                                      | 11.0 ms: 1.01x slower                                                |
| genshi_text     | 24.1 ms                                                                      | 24.9 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                                        | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| fannkuch                  | 375 ms                                                                       | 356 ms: 1.05x faster                                                 |
| coverage                  | 78.0 ms                                                                      | 74.1 ms: 1.05x faster                                                |
| telco                     | 8.26 ms                                                                      | 7.99 ms: 1.03x faster                                                |
| xml_etree_process         | 62.7 ms                                                                      | 60.7 ms: 1.03x faster                                                |
| gc_traversal              | 6.55 ms                                                                      | 6.36 ms: 1.03x faster                                                |
| generators                | 28.8 ms                                                                      | 28.1 ms: 1.03x faster                                                |
| raytrace                  | 274 ms                                                                       | 267 ms: 1.02x faster                                                 |
| dulwich_log               | 67.4 ms                                                                      | 66.1 ms: 1.02x faster                                                |
| scimark_fft               | 306 ms                                                                       | 301 ms: 1.02x faster                                                 |
| crypto_pyaes              | 75.0 ms                                                                      | 73.9 ms: 1.02x faster                                                |
| html5lib                  | 67.4 ms                                                                      | 66.5 ms: 1.01x faster                                                |
| async_tree_none_tg        | 270 ms                                                                       | 266 ms: 1.01x faster                                                 |
| comprehensions            | 17.7 us                                                                      | 17.5 us: 1.01x faster                                                |
| async_tree_memoization_tg | 329 ms                                                                       | 325 ms: 1.01x faster                                                 |
| many_optionals            | 1.02 ms                                                                      | 1.01 ms: 1.01x faster                                                |
| spectral_norm             | 84.4 ms                                                                      | 83.7 ms: 1.01x faster                                                |
| xml_etree_generate        | 83.8 ms                                                                      | 83.2 ms: 1.01x faster                                                |
| django_template           | 36.2 ms                                                                      | 36.0 ms: 1.01x faster                                                |
| json_dumps                | 11.6 ms                                                                      | 11.5 ms: 1.01x faster                                                |
| richards                  | 45.8 ms                                                                      | 45.5 ms: 1.01x faster                                                |
| scimark_monte_carlo       | 63.0 ms                                                                      | 62.6 ms: 1.01x faster                                                |
| meteor_contest            | 127 ms                                                                       | 127 ms: 1.00x faster                                                 |
| docutils                  | 2.89 sec                                                                     | 2.88 sec: 1.00x faster                                               |
| pprint_safe_repr          | 782 ms                                                                       | 779 ms: 1.00x faster                                                 |
| sympy_str                 | 290 ms                                                                       | 289 ms: 1.00x faster                                                 |
| go                        | 126 ms                                                                       | 126 ms: 1.00x faster                                                 |
| regex_compile             | 135 ms                                                                       | 135 ms: 1.00x faster                                                 |
| connected_components      | 416 ms                                                                       | 415 ms: 1.00x faster                                                 |
| mdp                       | 2.44 sec                                                                     | 2.44 sec: 1.00x faster                                               |
| shortest_path             | 444 ms                                                                       | 445 ms: 1.00x slower                                                 |
| bpe_tokeniser             | 4.68 sec                                                                     | 4.69 sec: 1.00x slower                                               |
| python_startup_no_site    | 8.98 ms                                                                      | 9.01 ms: 1.00x slower                                                |
| pidigits                  | 253 ms                                                                       | 254 ms: 1.00x slower                                                 |
| richards_super            | 52.4 ms                                                                      | 52.6 ms: 1.00x slower                                                |
| async_generators          | 408 ms                                                                       | 410 ms: 1.00x slower                                                 |
| python_startup            | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                |
| pprint_pformat            | 1.58 sec                                                                     | 1.59 sec: 1.00x slower                                               |
| hexiom                    | 5.97 ms                                                                      | 6.00 ms: 1.00x slower                                                |
| json_loads                | 25.3 us                                                                      | 25.5 us: 1.01x slower                                                |
| coroutines                | 20.9 ms                                                                      | 21.0 ms: 1.01x slower                                                |
| 2to3                      | 280 ms                                                                       | 282 ms: 1.01x slower                                                 |
| nbody                     | 86.5 ms                                                                      | 87.1 ms: 1.01x slower                                                |
| sympy_expand              | 493 ms                                                                       | 497 ms: 1.01x slower                                                 |
| scimark_lu                | 95.6 ms                                                                      | 96.3 ms: 1.01x slower                                                |
| sympy_integrate           | 23.0 ms                                                                      | 23.1 ms: 1.01x slower                                                |
| scimark_sor               | 110 ms                                                                       | 111 ms: 1.01x slower                                                 |
| genshi_xml                | 54.2 ms                                                                      | 54.6 ms: 1.01x slower                                                |
| sqlalchemy_imperative     | 17.8 ms                                                                      | 18.0 ms: 1.01x slower                                                |
| tomli_loads               | 2.06 sec                                                                     | 2.08 sec: 1.01x slower                                               |
| sqlglot_parse             | 1.30 ms                                                                      | 1.31 ms: 1.01x slower                                                |
| mako                      | 10.9 ms                                                                      | 11.0 ms: 1.01x slower                                                |
| deepcopy                  | 281 us                                                                       | 283 us: 1.01x slower                                                 |
| pathlib                   | 15.8 ms                                                                      | 16.0 ms: 1.01x slower                                                |
| json                      | 5.30 ms                                                                      | 5.36 ms: 1.01x slower                                                |
| pickle_pure_python        | 334 us                                                                       | 339 us: 1.01x slower                                                 |
| sqlalchemy_declarative    | 144 ms                                                                       | 146 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult   | 4.52 ms                                                                      | 4.59 ms: 1.01x slower                                                |
| deepcopy_memo             | 29.8 us                                                                      | 30.3 us: 1.02x slower                                                |
| deepcopy_reduce           | 2.90 us                                                                      | 2.95 us: 1.02x slower                                                |
| regex_effbot              | 3.06 ms                                                                      | 3.11 ms: 1.02x slower                                                |
| regex_v8                  | 25.9 ms                                                                      | 26.4 ms: 1.02x slower                                                |
| logging_simple            | 6.56 us                                                                      | 6.69 us: 1.02x slower                                                |
| logging_format            | 7.14 us                                                                      | 7.28 us: 1.02x slower                                                |
| deltablue                 | 3.28 ms                                                                      | 3.36 ms: 1.02x slower                                                |
| genshi_text               | 24.1 ms                                                                      | 24.9 ms: 1.04x slower                                                |
| typing_runtime_protocols  | 176 us                                                                       | 183 us: 1.04x slower                                                 |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (30): bench_thread_pool, async_tree_memoization, create_gc_cycles, subparsers, async_tree_none, async_tree_cpu_io_mixed_tg, xml_etree_parse, unpickle_pure_python, pyflate, regex_dna, thrift, async_tree_io_tg, pycparser, sqlglot_optimize, async_tree_cpu_io_mixed, sqlite_synth, nqueens, float, sqlglot_transpile, logging_silent, sympy_sum, asyncio_websockets, k_core, sphinx, async_tree_io, chaos, sqlglot_normalize, xml_etree_iterparse, pylint, bench_mp_pool

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 70.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x