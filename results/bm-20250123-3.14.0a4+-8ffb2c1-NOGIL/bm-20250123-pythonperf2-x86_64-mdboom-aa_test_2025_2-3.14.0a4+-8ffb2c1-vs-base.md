# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.000x slower
- HPT reliability: 86.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 338 ms                                                                       | 337 ms: 1.00x faster                                                   |
| html5lib       | 74.2 ms                                                                      | 73.5 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                           |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 575 ms                                                                       | 568 ms: 1.01x faster                                                   |
| async_tree_none_tg         | 250 ms                                                                       | 247 ms: 1.01x faster                                                   |
| async_tree_memoization_tg  | 322 ms                                                                       | 319 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 487 ms                                                                       | 485 ms: 1.00x faster                                                   |
| async_generators           | 467 ms                                                                       | 466 ms: 1.00x faster                                                   |
| coroutines                 | 22.0 ms                                                                      | 22.2 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                           |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 132 ms                                                                       | 134 ms: 1.02x slower                                                   |
| float          | 74.4 ms                                                                      | 76.0 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 240 ms                                                                       | 239 ms: 1.00x faster                                                   |
| regex_compile  | 156 ms                                                                       | 155 ms: 1.00x faster                                                   |
| regex_v8       | 25.5 ms                                                                      | 26.1 ms: 1.02x slower                                                  |
| regex_effbot   | 3.19 ms                                                                      | 3.27 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.42 sec                                                                     | 2.40 sec: 1.01x faster                                                 |
| json_dumps           | 13.5 ms                                                                      | 13.4 ms: 1.01x faster                                                  |
| xml_etree_process    | 74.2 ms                                                                      | 74.4 ms: 1.00x slower                                                  |
| xml_etree_parse      | 136 ms                                                                       | 136 ms: 1.00x slower                                                   |
| pickle_pure_python   | 390 us                                                                       | 392 us: 1.01x slower                                                   |
| json_loads           | 28.2 us                                                                      | 28.4 us: 1.01x slower                                                  |
| unpickle_pure_python | 251 us                                                                       | 254 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 88.9 ms                                                                      | 91.2 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.6 ms                                                                      | 18.7 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 18.0 ms                                                                      | 17.7 ms: 1.01x faster                                                  |
| genshi_xml     | 64.7 ms                                                                      | 65.2 ms: 1.01x slower                                                  |
| genshi_text    | 30.3 ms                                                                      | 30.6 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 5.62 ms                                                                      | 5.43 ms: 1.04x faster                                                  |
| typing_runtime_protocols   | 231 us                                                                       | 226 us: 1.02x faster                                                   |
| pycparser                  | 1.32 sec                                                                     | 1.29 sec: 1.02x faster                                                 |
| mako                       | 18.0 ms                                                                      | 17.7 ms: 1.01x faster                                                  |
| chaos                      | 70.8 ms                                                                      | 69.8 ms: 1.01x faster                                                  |
| scimark_fft                | 341 ms                                                                       | 336 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 66.2 ms                                                                      | 65.3 ms: 1.01x faster                                                  |
| async_tree_io_tg           | 575 ms                                                                       | 568 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 131 ms                                                                       | 129 ms: 1.01x faster                                                   |
| async_tree_none_tg         | 250 ms                                                                       | 247 ms: 1.01x faster                                                   |
| gc_traversal               | 5.00 ms                                                                      | 4.95 ms: 1.01x faster                                                  |
| async_tree_memoization_tg  | 322 ms                                                                       | 319 ms: 1.01x faster                                                   |
| meteor_contest             | 155 ms                                                                       | 153 ms: 1.01x faster                                                   |
| html5lib                   | 74.2 ms                                                                      | 73.5 ms: 1.01x faster                                                  |
| tomli_loads                | 2.42 sec                                                                     | 2.40 sec: 1.01x faster                                                 |
| json_dumps                 | 13.5 ms                                                                      | 13.4 ms: 1.01x faster                                                  |
| deltablue                  | 4.50 ms                                                                      | 4.47 ms: 1.01x faster                                                  |
| subparsers                 | 25.7 ms                                                                      | 25.6 ms: 1.01x faster                                                  |
| logging_format             | 8.21 us                                                                      | 8.15 us: 1.01x faster                                                  |
| deepcopy                   | 337 us                                                                       | 335 us: 1.01x faster                                                   |
| bpe_tokeniser              | 5.25 sec                                                                     | 5.21 sec: 1.01x faster                                                 |
| mdp                        | 2.78 sec                                                                     | 2.76 sec: 1.01x faster                                                 |
| sympy_expand               | 569 ms                                                                       | 565 ms: 1.01x faster                                                   |
| spectral_norm              | 102 ms                                                                       | 101 ms: 1.01x faster                                                   |
| scimark_sor                | 119 ms                                                                       | 119 ms: 1.00x faster                                                   |
| deepcopy_memo              | 38.0 us                                                                      | 37.9 us: 1.00x faster                                                  |
| async_tree_cpu_io_mixed_tg | 487 ms                                                                       | 485 ms: 1.00x faster                                                   |
| many_optionals             | 1.12 ms                                                                      | 1.12 ms: 1.00x faster                                                  |
| regex_dna                  | 240 ms                                                                       | 239 ms: 1.00x faster                                                   |
| 2to3                       | 338 ms                                                                       | 337 ms: 1.00x faster                                                   |
| async_generators           | 467 ms                                                                       | 466 ms: 1.00x faster                                                   |
| regex_compile              | 156 ms                                                                       | 155 ms: 1.00x faster                                                   |
| bench_mp_pool              | 49.1 ms                                                                      | 48.9 ms: 1.00x faster                                                  |
| telco                      | 9.15 ms                                                                      | 9.13 ms: 1.00x faster                                                  |
| python_startup             | 18.6 ms                                                                      | 18.7 ms: 1.00x slower                                                  |
| dulwich_log                | 69.8 ms                                                                      | 70.0 ms: 1.00x slower                                                  |
| xml_etree_process          | 74.2 ms                                                                      | 74.4 ms: 1.00x slower                                                  |
| sqlalchemy_declarative     | 176 ms                                                                       | 177 ms: 1.00x slower                                                   |
| xml_etree_parse            | 136 ms                                                                       | 136 ms: 1.00x slower                                                   |
| pprint_safe_repr           | 911 ms                                                                       | 915 ms: 1.00x slower                                                   |
| pathlib                    | 16.1 ms                                                                      | 16.2 ms: 1.00x slower                                                  |
| pprint_pformat             | 1.88 sec                                                                     | 1.89 sec: 1.00x slower                                                 |
| sqlite_synth               | 2.57 us                                                                      | 2.58 us: 1.00x slower                                                  |
| pickle_pure_python         | 390 us                                                                       | 392 us: 1.01x slower                                                   |
| coroutines                 | 22.0 ms                                                                      | 22.2 ms: 1.01x slower                                                  |
| json_loads                 | 28.2 us                                                                      | 28.4 us: 1.01x slower                                                  |
| scimark_lu                 | 119 ms                                                                       | 120 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 85.2 ms                                                                      | 85.8 ms: 1.01x slower                                                  |
| k_core                     | 2.38 sec                                                                     | 2.40 sec: 1.01x slower                                                 |
| deepcopy_reduce            | 3.59 us                                                                      | 3.62 us: 1.01x slower                                                  |
| genshi_xml                 | 64.7 ms                                                                      | 65.2 ms: 1.01x slower                                                  |
| shortest_path              | 523 ms                                                                       | 528 ms: 1.01x slower                                                   |
| pyflate                    | 490 ms                                                                       | 494 ms: 1.01x slower                                                   |
| connected_components       | 490 ms                                                                       | 494 ms: 1.01x slower                                                   |
| genshi_text                | 30.3 ms                                                                      | 30.6 ms: 1.01x slower                                                  |
| comprehensions             | 21.3 us                                                                      | 21.5 us: 1.01x slower                                                  |
| unpickle_pure_python       | 251 us                                                                       | 254 us: 1.01x slower                                                   |
| go                         | 147 ms                                                                       | 149 ms: 1.01x slower                                                   |
| logging_simple             | 7.32 us                                                                      | 7.43 us: 1.01x slower                                                  |
| fannkuch                   | 482 ms                                                                       | 489 ms: 1.02x slower                                                   |
| nbody                      | 132 ms                                                                       | 134 ms: 1.02x slower                                                   |
| float                      | 74.4 ms                                                                      | 76.0 ms: 1.02x slower                                                  |
| coverage                   | 101 ms                                                                       | 103 ms: 1.02x slower                                                   |
| thrift                     | 1.02 ms                                                                      | 1.05 ms: 1.02x slower                                                  |
| regex_v8                   | 25.5 ms                                                                      | 26.1 ms: 1.02x slower                                                  |
| regex_effbot               | 3.19 ms                                                                      | 3.27 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 88.9 ms                                                                      | 91.2 ms: 1.03x slower                                                  |
| logging_silent             | 101 ns                                                                       | 110 ns: 1.09x slower                                                   |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (28): create_gc_cycles, nqueens, richards, generators, sqlalchemy_imperative, sqlglot_parse, pylint, async_tree_io, docutils, sympy_str, crypto_pyaes, bench_thread_pool, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, sqlglot_transpile, sphinx, sympy_integrate, pidigits, sympy_sum, raytrace, django_template, hexiom, python_startup_no_site, xml_etree_generate, json, richards_super, asyncio_websockets

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 86.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x