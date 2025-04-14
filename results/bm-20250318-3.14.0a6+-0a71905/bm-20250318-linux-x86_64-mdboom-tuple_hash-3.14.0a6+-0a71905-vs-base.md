# Results vs. base

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.002x faster
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 257 ms                                                                 | 256 ms: 1.01x faster                                         |
| html5lib       | 62.9 ms                                                                | 61.3 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 487 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 471 ms: 1.02x faster                                         |
| async_generators           | 394 ms                                                                 | 390 ms: 1.01x faster                                         |
| coroutines                 | 23.4 ms                                                                | 24.2 ms: 1.03x slower                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                         |
| float          | 69.3 ms                                                                | 70.0 ms: 1.01x slower                                        |
| nbody          | 96.0 ms                                                                | 98.1 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.48 ms                                                                | 3.26 ms: 1.06x faster                                        |
| regex_dna      | 225 ms                                                                 | 221 ms: 1.02x faster                                         |
| regex_v8       | 24.3 ms                                                                | 24.2 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 222 us                                                                 | 218 us: 1.02x faster                                         |
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                        |
| pickle_pure_python   | 316 us                                                                 | 315 us: 1.01x faster                                         |
| xml_etree_process    | 58.0 ms                                                                | 58.3 ms: 1.00x slower                                        |
| json_loads           | 29.9 us                                                                | 30.1 us: 1.00x slower                                        |
| xml_etree_generate   | 83.4 ms                                                                | 84.2 ms: 1.01x slower                                        |
| xml_etree_parse      | 140 ms                                                                 | 142 ms: 1.01x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.20 ms                                                                | 8.21 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 21.6 ms                                                                | 21.5 ms: 1.01x faster                                        |
| mako           | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot               | 3.48 ms                                                                | 3.26 ms: 1.06x faster                                        |
| pycparser                  | 1.18 sec                                                               | 1.13 sec: 1.04x faster                                       |
| logging_silent             | 98.0 ns                                                                | 94.2 ns: 1.04x faster                                        |
| telco                      | 8.03 ms                                                                | 7.80 ms: 1.03x faster                                        |
| scimark_fft                | 360 ms                                                                 | 350 ms: 1.03x faster                                         |
| html5lib                   | 62.9 ms                                                                | 61.3 ms: 1.03x faster                                        |
| pprint_pformat             | 1.51 sec                                                               | 1.47 sec: 1.03x faster                                       |
| spectral_norm              | 100.0 ms                                                               | 97.7 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 487 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 471 ms: 1.02x faster                                         |
| regex_dna                  | 225 ms                                                                 | 221 ms: 1.02x faster                                         |
| nqueens                    | 85.9 ms                                                                | 84.3 ms: 1.02x faster                                        |
| unpickle_pure_python       | 222 us                                                                 | 218 us: 1.02x faster                                         |
| deepcopy_memo              | 29.6 us                                                                | 29.1 us: 1.02x faster                                        |
| pprint_safe_repr           | 736 ms                                                                 | 725 ms: 1.02x faster                                         |
| coverage                   | 92.1 ms                                                                | 90.8 ms: 1.01x faster                                        |
| deepcopy                   | 258 us                                                                 | 255 us: 1.01x faster                                         |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                         |
| async_generators           | 394 ms                                                                 | 390 ms: 1.01x faster                                         |
| go                         | 114 ms                                                                 | 113 ms: 1.01x faster                                         |
| richards                   | 42.5 ms                                                                | 42.1 ms: 1.01x faster                                        |
| many_optionals             | 956 us                                                                 | 949 us: 1.01x faster                                         |
| deepcopy_reduce            | 2.68 us                                                                | 2.66 us: 1.01x faster                                        |
| json_dumps                 | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                        |
| genshi_text                | 21.6 ms                                                                | 21.5 ms: 1.01x faster                                        |
| pathlib                    | 16.7 ms                                                                | 16.5 ms: 1.01x faster                                        |
| 2to3                       | 257 ms                                                                 | 256 ms: 1.01x faster                                         |
| pickle_pure_python         | 316 us                                                                 | 315 us: 1.01x faster                                         |
| dulwich_log                | 58.6 ms                                                                | 58.3 ms: 1.00x faster                                        |
| sqlglot_v2_optimize        | 52.8 ms                                                                | 52.6 ms: 1.00x faster                                        |
| sympy_sum                  | 148 ms                                                                 | 147 ms: 1.00x faster                                         |
| crypto_pyaes               | 76.1 ms                                                                | 75.8 ms: 1.00x faster                                        |
| sqlglot_v2_normalize       | 106 ms                                                                 | 106 ms: 1.00x faster                                         |
| sympy_integrate            | 19.8 ms                                                                | 19.8 ms: 1.00x faster                                        |
| regex_v8                   | 24.3 ms                                                                | 24.2 ms: 1.00x faster                                        |
| gc_traversal               | 4.91 ms                                                                | 4.92 ms: 1.00x slower                                        |
| python_startup_no_site     | 8.20 ms                                                                | 8.21 ms: 1.00x slower                                        |
| bench_thread_pool          | 867 us                                                                 | 869 us: 1.00x slower                                         |
| create_gc_cycles           | 2.49 ms                                                                | 2.50 ms: 1.00x slower                                        |
| comprehensions             | 16.7 us                                                                | 16.7 us: 1.00x slower                                        |
| xml_etree_process          | 58.0 ms                                                                | 58.3 ms: 1.00x slower                                        |
| json_loads                 | 29.9 us                                                                | 30.1 us: 1.00x slower                                        |
| bpe_tokeniser              | 4.61 sec                                                               | 4.64 sec: 1.01x slower                                       |
| thrift                     | 770 us                                                                 | 776 us: 1.01x slower                                         |
| mako                       | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                        |
| deltablue                  | 3.08 ms                                                                | 3.11 ms: 1.01x slower                                        |
| xml_etree_generate         | 83.4 ms                                                                | 84.2 ms: 1.01x slower                                        |
| float                      | 69.3 ms                                                                | 70.0 ms: 1.01x slower                                        |
| fannkuch                   | 428 ms                                                                 | 432 ms: 1.01x slower                                         |
| shortest_path              | 492 ms                                                                 | 497 ms: 1.01x slower                                         |
| sqlglot_v2_parse           | 1.26 ms                                                                | 1.27 ms: 1.01x slower                                        |
| typing_runtime_protocols   | 164 us                                                                 | 166 us: 1.01x slower                                         |
| logging_format             | 6.16 us                                                                | 6.23 us: 1.01x slower                                        |
| sqlglot_v2_transpile       | 1.57 ms                                                                | 1.58 ms: 1.01x slower                                        |
| xml_etree_parse            | 140 ms                                                                 | 142 ms: 1.01x slower                                         |
| scimark_sor                | 117 ms                                                                 | 118 ms: 1.01x slower                                         |
| nbody                      | 96.0 ms                                                                | 98.1 ms: 1.02x slower                                        |
| hexiom                     | 6.16 ms                                                                | 6.31 ms: 1.03x slower                                        |
| coroutines                 | 23.4 ms                                                                | 24.2 ms: 1.03x slower                                        |
| mdp                        | 2.49 sec                                                               | 2.66 sec: 1.07x slower                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (36): sympy_expand, richards_super, subparsers, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, scimark_lu, generators, scimark_sparse_mat_mult, meteor_contest, bench_mp_pool, xml_etree_iterparse, pylint, raytrace, async_tree_memoization, connected_components, scimark_monte_carlo, sqlalchemy_declarative, sympy_str, python_startup, asyncio_websockets, json, pyflate, django_template, sqlalchemy_imperative, tomli_loads, docutils, sphinx, regex_compile, genshi_xml, logging_simple, chaos, sqlite_synth, k_core

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x