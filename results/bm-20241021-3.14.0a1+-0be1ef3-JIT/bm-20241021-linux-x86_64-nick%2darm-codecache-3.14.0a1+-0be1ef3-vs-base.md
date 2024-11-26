# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.006x faster
- HPT reliability: 85.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 277 ms                                                                 | 276 ms: 1.01x faster                                            |
| docutils       | 2.94 sec                                                               | 2.91 sec: 1.01x faster                                          |
| html5lib       | 66.5 ms                                                                | 67.1 ms: 1.01x slower                                           |
| sphinx         | 1.17 sec                                                               | 1.16 sec: 1.01x faster                                          |
| tornado_http   | 94.3 ms                                                                | 94.8 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 556 ms: 1.01x faster                                            |
| async_generators           | 456 ms                                                                 | 457 ms: 1.00x slower                                            |
| coroutines                 | 23.1 ms                                                                | 23.7 ms: 1.02x slower                                           |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 83.8 ms                                                                | 82.3 ms: 1.02x faster                                           |
| float          | 75.9 ms                                                                | 75.6 ms: 1.00x faster                                           |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 214 ms: 1.05x faster                                            |
| regex_v8       | 25.5 ms                                                                | 24.7 ms: 1.03x faster                                           |
| regex_effbot   | 3.83 ms                                                                | 3.72 ms: 1.03x faster                                           |
| regex_compile  | 138 ms                                                                 | 139 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps          | 11.1 ms                                                                | 10.8 ms: 1.03x faster                                           |
| pickle_pure_python  | 317 us                                                                 | 311 us: 1.02x faster                                            |
| json_loads          | 27.0 us                                                                | 26.8 us: 1.01x faster                                           |
| xml_etree_generate  | 77.8 ms                                                                | 78.2 ms: 1.01x slower                                           |
| xml_etree_iterparse | 100 ms                                                                 | 101 ms: 1.01x slower                                            |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_pure_python, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                                | 7.07 ms: 1.00x faster                                           |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                                | 25.8 ms: 1.02x faster                                           |
| mako           | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| richards                   | 43.2 ms                                                                | 40.8 ms: 1.06x faster                                           |
| gc_traversal               | 4.62 ms                                                                | 4.37 ms: 1.06x faster                                           |
| regex_dna                  | 225 ms                                                                 | 214 ms: 1.05x faster                                            |
| pprint_safe_repr           | 729 ms                                                                 | 696 ms: 1.05x faster                                            |
| pycparser                  | 1.19 sec                                                               | 1.14 sec: 1.05x faster                                          |
| regex_v8                   | 25.5 ms                                                                | 24.7 ms: 1.03x faster                                           |
| json_dumps                 | 11.1 ms                                                                | 10.8 ms: 1.03x faster                                           |
| regex_effbot               | 3.83 ms                                                                | 3.72 ms: 1.03x faster                                           |
| pprint_pformat             | 1.50 sec                                                               | 1.46 sec: 1.03x faster                                          |
| telco                      | 7.73 ms                                                                | 7.58 ms: 1.02x faster                                           |
| pyflate                    | 456 ms                                                                 | 447 ms: 1.02x faster                                            |
| pickle_pure_python         | 317 us                                                                 | 311 us: 1.02x faster                                            |
| nbody                      | 83.8 ms                                                                | 82.3 ms: 1.02x faster                                           |
| deepcopy_memo              | 29.6 us                                                                | 29.1 us: 1.02x faster                                           |
| genshi_text                | 26.2 ms                                                                | 25.8 ms: 1.02x faster                                           |
| sphinx                     | 1.17 sec                                                               | 1.16 sec: 1.01x faster                                          |
| richards_super             | 48.2 ms                                                                | 47.6 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 556 ms: 1.01x faster                                            |
| docutils                   | 2.94 sec                                                               | 2.91 sec: 1.01x faster                                          |
| deepcopy                   | 269 us                                                                 | 266 us: 1.01x faster                                            |
| scimark_fft                | 318 ms                                                                 | 315 ms: 1.01x faster                                            |
| create_gc_cycles           | 2.68 ms                                                                | 2.66 ms: 1.01x faster                                           |
| sqlglot_optimize           | 59.8 ms                                                                | 59.3 ms: 1.01x faster                                           |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                            |
| json_loads                 | 27.0 us                                                                | 26.8 us: 1.01x faster                                           |
| raytrace                   | 275 ms                                                                 | 273 ms: 1.01x faster                                            |
| bench_mp_pool              | 84.3 ms                                                                | 83.8 ms: 1.01x faster                                           |
| sympy_str                  | 301 ms                                                                 | 299 ms: 1.01x faster                                            |
| 2to3                       | 277 ms                                                                 | 276 ms: 1.01x faster                                            |
| sqlglot_normalize          | 114 ms                                                                 | 113 ms: 1.00x faster                                            |
| float                      | 75.9 ms                                                                | 75.6 ms: 1.00x faster                                           |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                            |
| python_startup_no_site     | 7.10 ms                                                                | 7.07 ms: 1.00x faster                                           |
| mdp                        | 2.55 sec                                                               | 2.54 sec: 1.00x faster                                          |
| sympy_integrate            | 23.4 ms                                                                | 23.3 ms: 1.00x faster                                           |
| sympy_expand               | 500 ms                                                                 | 498 ms: 1.00x faster                                            |
| python_startup             | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                           |
| async_generators           | 456 ms                                                                 | 457 ms: 1.00x slower                                            |
| regex_compile              | 138 ms                                                                 | 139 ms: 1.00x slower                                            |
| tornado_http               | 94.3 ms                                                                | 94.8 ms: 1.00x slower                                           |
| sqlglot_transpile          | 1.69 ms                                                                | 1.70 ms: 1.01x slower                                           |
| bench_thread_pool          | 876 us                                                                 | 881 us: 1.01x slower                                            |
| xml_etree_generate         | 77.8 ms                                                                | 78.2 ms: 1.01x slower                                           |
| coverage                   | 83.9 ms                                                                | 84.4 ms: 1.01x slower                                           |
| bpe_tokeniser              | 4.43 sec                                                               | 4.46 sec: 1.01x slower                                          |
| hexiom                     | 6.96 ms                                                                | 7.01 ms: 1.01x slower                                           |
| scimark_sor                | 118 ms                                                                 | 119 ms: 1.01x slower                                            |
| html5lib                   | 66.5 ms                                                                | 67.1 ms: 1.01x slower                                           |
| go                         | 132 ms                                                                 | 133 ms: 1.01x slower                                            |
| xml_etree_iterparse        | 100 ms                                                                 | 101 ms: 1.01x slower                                            |
| mako                       | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                           |
| pathlib                    | 15.8 ms                                                                | 16.0 ms: 1.01x slower                                           |
| nqueens                    | 86.2 ms                                                                | 87.6 ms: 1.02x slower                                           |
| logging_simple             | 5.46 us                                                                | 5.57 us: 1.02x slower                                           |
| coroutines                 | 23.1 ms                                                                | 23.7 ms: 1.02x slower                                           |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (34): scimark_monte_carlo, pylint, async_tree_cpu_io_mixed, django_template, genshi_xml, fannkuch, thrift, xml_etree_parse, comprehensions, logging_silent, chaos, json, scimark_lu, deltablue, generators, asyncio_websockets, sympy_sum, deepcopy_reduce, async_tree_memoization_tg, sqlglot_parse, unpickle_pure_python, logging_format, tomli_loads, xml_etree_process, dulwich_log, spectral_norm, async_tree_none_tg, async_tree_io_tg, async_tree_io, typing_runtime_protocols, async_tree_memoization, crypto_pyaes, async_tree_none, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 85.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x