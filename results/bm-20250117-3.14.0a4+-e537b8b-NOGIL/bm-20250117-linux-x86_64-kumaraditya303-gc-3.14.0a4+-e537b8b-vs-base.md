# Results vs. base

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.003x slower
- HPT reliability: 85.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                 | 309 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 466 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed    | 531 ms                                                                 | 522 ms: 1.02x faster                                         |
| async_tree_io_tg           | 550 ms                                                                 | 542 ms: 1.01x faster                                         |
| async_tree_io              | 605 ms                                                                 | 597 ms: 1.01x faster                                         |
| async_tree_none_tg         | 237 ms                                                                 | 235 ms: 1.01x faster                                         |
| coroutines                 | 25.7 ms                                                                | 25.5 ms: 1.01x faster                                        |
| async_generators           | 433 ms                                                                 | 445 ms: 1.03x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_memoization, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 80.2 ms                                                                | 78.2 ms: 1.03x faster                                        |
| nbody          | 142 ms                                                                 | 141 ms: 1.00x faster                                         |
| pidigits       | 182 ms                                                                 | 190 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 149 ms                                                                 | 149 ms: 1.00x slower                                         |
| regex_dna      | 221 ms                                                                 | 222 ms: 1.00x slower                                         |
| regex_v8       | 23.9 ms                                                                | 24.8 ms: 1.04x slower                                        |
| regex_effbot   | 3.24 ms                                                                | 3.36 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python  | 373 us                                                                 | 368 us: 1.01x faster                                         |
| xml_etree_generate  | 95.7 ms                                                                | 96.1 ms: 1.00x slower                                        |
| json_dumps          | 12.6 ms                                                                | 12.7 ms: 1.01x slower                                        |
| xml_etree_iterparse | 95.4 ms                                                                | 96.2 ms: 1.01x slower                                        |
| xml_etree_parse     | 147 ms                                                                 | 149 ms: 1.01x slower                                         |
| tomli_loads         | 2.36 sec                                                               | 2.41 sec: 1.02x slower                                       |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (3): json_loads, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 9.33 ms                                                                | 9.35 ms: 1.00x slower                                        |
| python_startup         | 15.0 ms                                                                | 15.0 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 61.2 ms                                                                | 60.1 ms: 1.02x faster                                        |
| mako            | 16.3 ms                                                                | 16.2 ms: 1.01x faster                                        |
| django_template | 41.9 ms                                                                | 41.7 ms: 1.00x faster                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4+-d95ba9f | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 2.86 sec                                                               | 2.74 sec: 1.04x faster                                       |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 466 ms: 1.03x faster                                         |
| float                      | 80.2 ms                                                                | 78.2 ms: 1.03x faster                                        |
| genshi_xml                 | 61.2 ms                                                                | 60.1 ms: 1.02x faster                                        |
| pathlib                    | 16.7 ms                                                                | 16.4 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed    | 531 ms                                                                 | 522 ms: 1.02x faster                                         |
| go                         | 143 ms                                                                 | 141 ms: 1.02x faster                                         |
| pickle_pure_python         | 373 us                                                                 | 368 us: 1.01x faster                                         |
| async_tree_io_tg           | 550 ms                                                                 | 542 ms: 1.01x faster                                         |
| deepcopy_reduce            | 3.30 us                                                                | 3.26 us: 1.01x faster                                        |
| async_tree_io              | 605 ms                                                                 | 597 ms: 1.01x faster                                         |
| async_tree_none_tg         | 237 ms                                                                 | 235 ms: 1.01x faster                                         |
| richards                   | 54.5 ms                                                                | 54.0 ms: 1.01x faster                                        |
| deepcopy                   | 314 us                                                                 | 311 us: 1.01x faster                                         |
| telco                      | 9.16 ms                                                                | 9.09 ms: 1.01x faster                                        |
| sqlite_synth               | 2.75 us                                                                | 2.73 us: 1.01x faster                                        |
| coroutines                 | 25.7 ms                                                                | 25.5 ms: 1.01x faster                                        |
| thrift                     | 954 us                                                                 | 948 us: 1.01x faster                                         |
| mako                       | 16.3 ms                                                                | 16.2 ms: 1.01x faster                                        |
| dulwich_log                | 69.1 ms                                                                | 68.7 ms: 1.01x faster                                        |
| sqlglot_parse              | 1.59 ms                                                                | 1.59 ms: 1.01x faster                                        |
| logging_silent             | 121 ns                                                                 | 120 ns: 1.01x faster                                         |
| crypto_pyaes               | 90.8 ms                                                                | 90.4 ms: 1.01x faster                                        |
| pprint_safe_repr           | 856 ms                                                                 | 852 ms: 1.00x faster                                         |
| pprint_pformat             | 1.76 sec                                                               | 1.75 sec: 1.00x faster                                       |
| nbody                      | 142 ms                                                                 | 141 ms: 1.00x faster                                         |
| k_core                     | 2.47 sec                                                               | 2.46 sec: 1.00x faster                                       |
| django_template            | 41.9 ms                                                                | 41.7 ms: 1.00x faster                                        |
| deepcopy_memo              | 39.9 us                                                                | 39.7 us: 1.00x faster                                        |
| comprehensions             | 20.8 us                                                                | 20.8 us: 1.00x faster                                        |
| regex_compile              | 149 ms                                                                 | 149 ms: 1.00x slower                                         |
| python_startup_no_site     | 9.33 ms                                                                | 9.35 ms: 1.00x slower                                        |
| sqlglot_normalize          | 120 ms                                                                 | 120 ms: 1.00x slower                                         |
| python_startup             | 15.0 ms                                                                | 15.0 ms: 1.00x slower                                        |
| shortest_path              | 571 ms                                                                 | 572 ms: 1.00x slower                                         |
| regex_dna                  | 221 ms                                                                 | 222 ms: 1.00x slower                                         |
| 2to3                       | 308 ms                                                                 | 309 ms: 1.00x slower                                         |
| raytrace                   | 354 ms                                                                 | 356 ms: 1.00x slower                                         |
| xml_etree_generate         | 95.7 ms                                                                | 96.1 ms: 1.00x slower                                        |
| connected_components       | 528 ms                                                                 | 531 ms: 1.01x slower                                         |
| bench_thread_pool          | 3.47 ms                                                                | 3.49 ms: 1.01x slower                                        |
| subparsers                 | 24.6 ms                                                                | 24.7 ms: 1.01x slower                                        |
| bpe_tokeniser              | 5.00 sec                                                               | 5.04 sec: 1.01x slower                                       |
| json_dumps                 | 12.6 ms                                                                | 12.7 ms: 1.01x slower                                        |
| hexiom                     | 7.70 ms                                                                | 7.76 ms: 1.01x slower                                        |
| deltablue                  | 4.69 ms                                                                | 4.72 ms: 1.01x slower                                        |
| xml_etree_iterparse        | 95.4 ms                                                                | 96.2 ms: 1.01x slower                                        |
| typing_runtime_protocols   | 209 us                                                                 | 211 us: 1.01x slower                                         |
| chaos                      | 73.8 ms                                                                | 74.5 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 86.4 ms                                                                | 87.2 ms: 1.01x slower                                        |
| xml_etree_parse            | 147 ms                                                                 | 149 ms: 1.01x slower                                         |
| sympy_sum                  | 175 ms                                                                 | 177 ms: 1.01x slower                                         |
| logging_simple             | 6.66 us                                                                | 6.73 us: 1.01x slower                                        |
| pycparser                  | 1.17 sec                                                               | 1.18 sec: 1.01x slower                                       |
| nqueens                    | 98.5 ms                                                                | 100 ms: 1.02x slower                                         |
| fannkuch                   | 508 ms                                                                 | 516 ms: 1.02x slower                                         |
| logging_format             | 7.47 us                                                                | 7.58 us: 1.02x slower                                        |
| richards_super             | 63.2 ms                                                                | 64.3 ms: 1.02x slower                                        |
| scimark_lu                 | 140 ms                                                                 | 142 ms: 1.02x slower                                         |
| tomli_loads                | 2.36 sec                                                               | 2.41 sec: 1.02x slower                                       |
| pyflate                    | 518 ms                                                                 | 532 ms: 1.03x slower                                         |
| async_generators           | 433 ms                                                                 | 445 ms: 1.03x slower                                         |
| spectral_norm              | 115 ms                                                                 | 119 ms: 1.03x slower                                         |
| regex_v8                   | 23.9 ms                                                                | 24.8 ms: 1.04x slower                                        |
| scimark_sparse_mat_mult    | 6.22 ms                                                                | 6.45 ms: 1.04x slower                                        |
| regex_effbot               | 3.24 ms                                                                | 3.36 ms: 1.04x slower                                        |
| pidigits                   | 182 ms                                                                 | 190 ms: 1.04x slower                                         |
| gc_traversal               | 4.18 ms                                                                | 4.56 ms: 1.09x slower                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (28): sqlglot_transpile, async_tree_memoization_tg, async_tree_memoization, async_tree_none, sympy_expand, scimark_sor, json_loads, meteor_contest, sqlglot_optimize, sqlalchemy_imperative, sympy_integrate, pylint, generators, xml_etree_process, sqlalchemy_declarative, html5lib, create_gc_cycles, sympy_str, unpickle_pure_python, sphinx, many_optionals, genshi_text, asyncio_websockets, json, coverage, scimark_fft, docutils, bench_mp_pool

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 85.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x