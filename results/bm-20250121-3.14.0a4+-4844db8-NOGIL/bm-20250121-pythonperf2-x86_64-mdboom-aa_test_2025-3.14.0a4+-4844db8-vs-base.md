# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.004x faster
- HPT reliability: 56.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 338 ms                                                                       | 336 ms: 1.01x faster                                                 |
| html5lib       | 74.2 ms                                                                      | 73.9 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 322 ms                                                                       | 320 ms: 1.01x faster                                                 |
| async_tree_none_tg        | 250 ms                                                                       | 248 ms: 1.01x faster                                                 |
| async_tree_memoization    | 357 ms                                                                       | 359 ms: 1.00x slower                                                 |
| async_generators          | 467 ms                                                                       | 470 ms: 1.01x slower                                                 |
| coroutines                | 22.0 ms                                                                      | 22.3 ms: 1.01x slower                                                |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 249 ms                                                                       | 249 ms: 1.00x faster                                                 |
| float          | 74.4 ms                                                                      | 74.6 ms: 1.00x slower                                                |
| nbody          | 132 ms                                                                       | 134 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.19 ms                                                                      | 3.20 ms: 1.00x slower                                                |
| regex_v8       | 25.5 ms                                                                      | 25.9 ms: 1.01x slower                                                |
| regex_dna      | 240 ms                                                                       | 246 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 136 ms                                                                       | 132 ms: 1.03x faster                                                 |
| json_loads           | 28.2 us                                                                      | 27.7 us: 1.02x faster                                                |
| xml_etree_iterparse  | 88.9 ms                                                                      | 87.8 ms: 1.01x faster                                                |
| xml_etree_generate   | 98.3 ms                                                                      | 97.4 ms: 1.01x faster                                                |
| json_dumps           | 13.5 ms                                                                      | 13.4 ms: 1.01x faster                                                |
| unpickle_pure_python | 251 us                                                                       | 250 us: 1.00x faster                                                 |
| pickle_pure_python   | 390 us                                                                       | 392 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                         |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 11.7 ms                                                                      | 11.8 ms: 1.00x slower                                                |
| python_startup         | 18.6 ms                                                                      | 18.7 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 64.7 ms                                                                      | 63.9 ms: 1.01x faster                                                |
| genshi_text    | 30.3 ms                                                                      | 30.2 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20250121-pythonperf2-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal              | 5.00 ms                                                                      | 4.09 ms: 1.22x faster                                                |
| pycparser                 | 1.32 sec                                                                     | 1.27 sec: 1.04x faster                                               |
| xml_etree_parse           | 136 ms                                                                       | 132 ms: 1.03x faster                                                 |
| typing_runtime_protocols  | 231 us                                                                       | 225 us: 1.03x faster                                                 |
| scimark_sparse_mat_mult   | 5.62 ms                                                                      | 5.49 ms: 1.02x faster                                                |
| scimark_monte_carlo       | 85.2 ms                                                                      | 83.3 ms: 1.02x faster                                                |
| spectral_norm             | 102 ms                                                                       | 99.4 ms: 1.02x faster                                                |
| json_loads                | 28.2 us                                                                      | 27.7 us: 1.02x faster                                                |
| fannkuch                  | 482 ms                                                                       | 473 ms: 1.02x faster                                                 |
| deepcopy_memo             | 38.0 us                                                                      | 37.4 us: 1.02x faster                                                |
| richards                  | 58.0 ms                                                                      | 57.1 ms: 1.02x faster                                                |
| bench_thread_pool         | 1.46 ms                                                                      | 1.44 ms: 1.01x faster                                                |
| deepcopy                  | 337 us                                                                       | 332 us: 1.01x faster                                                 |
| telco                     | 9.15 ms                                                                      | 9.03 ms: 1.01x faster                                                |
| genshi_xml                | 64.7 ms                                                                      | 63.9 ms: 1.01x faster                                                |
| xml_etree_iterparse       | 88.9 ms                                                                      | 87.8 ms: 1.01x faster                                                |
| sqlglot_optimize          | 66.2 ms                                                                      | 65.5 ms: 1.01x faster                                                |
| xml_etree_generate        | 98.3 ms                                                                      | 97.4 ms: 1.01x faster                                                |
| raytrace                  | 340 ms                                                                       | 338 ms: 1.01x faster                                                 |
| 2to3                      | 338 ms                                                                       | 336 ms: 1.01x faster                                                 |
| json_dumps                | 13.5 ms                                                                      | 13.4 ms: 1.01x faster                                                |
| sqlglot_normalize         | 131 ms                                                                       | 130 ms: 1.01x faster                                                 |
| async_tree_memoization_tg | 322 ms                                                                       | 320 ms: 1.01x faster                                                 |
| deltablue                 | 4.50 ms                                                                      | 4.47 ms: 1.01x faster                                                |
| json                      | 5.57 ms                                                                      | 5.54 ms: 1.01x faster                                                |
| async_tree_none_tg        | 250 ms                                                                       | 248 ms: 1.01x faster                                                 |
| unpickle_pure_python      | 251 us                                                                       | 250 us: 1.00x faster                                                 |
| go                        | 147 ms                                                                       | 147 ms: 1.00x faster                                                 |
| genshi_text               | 30.3 ms                                                                      | 30.2 ms: 1.00x faster                                                |
| html5lib                  | 74.2 ms                                                                      | 73.9 ms: 1.00x faster                                                |
| mdp                       | 2.78 sec                                                                     | 2.77 sec: 1.00x faster                                               |
| pidigits                  | 249 ms                                                                       | 249 ms: 1.00x faster                                                 |
| float                     | 74.4 ms                                                                      | 74.6 ms: 1.00x slower                                                |
| meteor_contest            | 155 ms                                                                       | 155 ms: 1.00x slower                                                 |
| python_startup_no_site    | 11.7 ms                                                                      | 11.8 ms: 1.00x slower                                                |
| crypto_pyaes              | 92.7 ms                                                                      | 93.0 ms: 1.00x slower                                                |
| sympy_integrate           | 27.1 ms                                                                      | 27.2 ms: 1.00x slower                                                |
| sympy_str                 | 340 ms                                                                       | 341 ms: 1.00x slower                                                 |
| python_startup            | 18.6 ms                                                                      | 18.7 ms: 1.00x slower                                                |
| deepcopy_reduce           | 3.59 us                                                                      | 3.61 us: 1.00x slower                                                |
| chaos                     | 70.8 ms                                                                      | 71.1 ms: 1.00x slower                                                |
| many_optionals            | 1.12 ms                                                                      | 1.13 ms: 1.00x slower                                                |
| async_tree_memoization    | 357 ms                                                                       | 359 ms: 1.00x slower                                                 |
| regex_effbot              | 3.19 ms                                                                      | 3.20 ms: 1.00x slower                                                |
| pickle_pure_python        | 390 us                                                                       | 392 us: 1.01x slower                                                 |
| sympy_sum                 | 176 ms                                                                       | 177 ms: 1.01x slower                                                 |
| async_generators          | 467 ms                                                                       | 470 ms: 1.01x slower                                                 |
| coverage                  | 101 ms                                                                       | 102 ms: 1.01x slower                                                 |
| sqlalchemy_declarative    | 176 ms                                                                       | 177 ms: 1.01x slower                                                 |
| pathlib                   | 16.1 ms                                                                      | 16.2 ms: 1.01x slower                                                |
| scimark_fft               | 341 ms                                                                       | 343 ms: 1.01x slower                                                 |
| shortest_path             | 523 ms                                                                       | 528 ms: 1.01x slower                                                 |
| connected_components      | 490 ms                                                                       | 494 ms: 1.01x slower                                                 |
| logging_simple            | 7.32 us                                                                      | 7.39 us: 1.01x slower                                                |
| k_core                    | 2.38 sec                                                                     | 2.40 sec: 1.01x slower                                               |
| logging_silent            | 101 ns                                                                       | 102 ns: 1.01x slower                                                 |
| pprint_safe_repr          | 911 ms                                                                       | 920 ms: 1.01x slower                                                 |
| pprint_pformat            | 1.88 sec                                                                     | 1.90 sec: 1.01x slower                                               |
| sqlite_synth              | 2.57 us                                                                      | 2.60 us: 1.01x slower                                                |
| thrift                    | 1.02 ms                                                                      | 1.04 ms: 1.01x slower                                                |
| coroutines                | 22.0 ms                                                                      | 22.3 ms: 1.01x slower                                                |
| regex_v8                  | 25.5 ms                                                                      | 25.9 ms: 1.01x slower                                                |
| nbody                     | 132 ms                                                                       | 134 ms: 1.02x slower                                                 |
| regex_dna                 | 240 ms                                                                       | 246 ms: 1.02x slower                                                 |
| Geometric mean            | (ref)                                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (32): richards_super, sqlalchemy_imperative, logging_format, tomli_loads, django_template, async_tree_io_tg, comprehensions, scimark_lu, dulwich_log, pylint, subparsers, regex_compile, hexiom, async_tree_cpu_io_mixed_tg, docutils, mako, bench_mp_pool, xml_etree_process, bpe_tokeniser, async_tree_none, sqlglot_transpile, async_tree_io, scimark_sor, sympy_expand, sphinx, sqlglot_parse, pyflate, asyncio_websockets, nqueens, async_tree_cpu_io_mixed, generators, create_gc_cycles

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 56.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x