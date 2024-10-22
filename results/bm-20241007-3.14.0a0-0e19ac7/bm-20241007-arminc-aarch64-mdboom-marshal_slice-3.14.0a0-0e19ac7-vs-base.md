# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-aarch64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.00x faster
- HPT reliability: 66.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| html5lib       | 65.2 ms                                                                 | 63.1 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                     |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 716 ms                                                                  | 705 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                                  | 714 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 2.21 sec                                                                | 2.22 sec: 1.01x slower                                           |
| async_tree_io              | 1.15 sec                                                                | 1.17 sec: 1.02x slower                                           |
| async_tree_none            | 418 ms                                                                  | 429 ms: 1.03x slower                                             |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_io_tg, async_generators, asyncio_websockets, async_tree_memoization_tg, coroutines, asyncio_tcp, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 262 ms                                                                  | 254 ms: 1.03x faster                                             |
| regex_v8       | 30.4 ms                                                                 | 30.8 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_list     | 5.32 us                                                                 | 5.23 us: 1.02x faster                                            |
| json_dumps      | 13.4 ms                                                                 | 13.3 ms: 1.01x faster                                            |
| tomli_loads     | 2.64 sec                                                                | 2.65 sec: 1.01x slower                                           |
| pickle          | 13.6 us                                                                 | 13.9 us: 1.02x slower                                            |
| xml_etree_parse | 188 ms                                                                  | 193 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (9): pickle_pure_python, json_loads, xml_etree_process, unpickle_pure_python, xml_etree_generate, unpickle, unpickle_list, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                                 | 8.69 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 28.1 ms                                                                 | 27.2 ms: 1.03x faster                                            |
| django_template | 42.6 ms                                                                 | 42.1 ms: 1.01x faster                                            |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpack_sequence            | 57.0 ns                                                                 | 54.8 ns: 1.04x faster                                            |
| regex_dna                  | 262 ms                                                                  | 254 ms: 1.03x faster                                             |
| html5lib                   | 65.2 ms                                                                 | 63.1 ms: 1.03x faster                                            |
| genshi_text                | 28.1 ms                                                                 | 27.2 ms: 1.03x faster                                            |
| telco                      | 9.47 ms                                                                 | 9.25 ms: 1.02x faster                                            |
| bench_thread_pool          | 1.30 ms                                                                 | 1.27 ms: 1.02x faster                                            |
| deepcopy_reduce            | 3.52 us                                                                 | 3.45 us: 1.02x faster                                            |
| meteor_contest             | 113 ms                                                                  | 111 ms: 1.02x faster                                             |
| pprint_pformat             | 1.89 sec                                                                | 1.86 sec: 1.02x faster                                           |
| gc_traversal               | 5.16 ms                                                                 | 5.07 ms: 1.02x faster                                            |
| scimark_fft                | 434 ms                                                                  | 426 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 716 ms                                                                  | 705 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                                  | 714 ms: 1.02x faster                                             |
| hexiom                     | 7.14 ms                                                                 | 7.03 ms: 1.02x faster                                            |
| bpe_tokeniser              | 5.81 sec                                                                | 5.72 sec: 1.02x faster                                           |
| pickle_list                | 5.32 us                                                                 | 5.23 us: 1.02x faster                                            |
| scimark_sor                | 159 ms                                                                  | 157 ms: 1.02x faster                                             |
| nqueens                    | 99.8 ms                                                                 | 98.5 ms: 1.01x faster                                            |
| json_dumps                 | 13.4 ms                                                                 | 13.3 ms: 1.01x faster                                            |
| pprint_safe_repr           | 915 ms                                                                  | 904 ms: 1.01x faster                                             |
| django_template            | 42.6 ms                                                                 | 42.1 ms: 1.01x faster                                            |
| scimark_lu                 | 133 ms                                                                  | 132 ms: 1.01x faster                                             |
| tomli_loads                | 2.64 sec                                                                | 2.65 sec: 1.01x slower                                           |
| asyncio_tcp_ssl            | 2.21 sec                                                                | 2.22 sec: 1.01x slower                                           |
| python_startup_no_site     | 8.64 ms                                                                 | 8.69 ms: 1.01x slower                                            |
| mdp                        | 3.31 sec                                                                | 3.34 sec: 1.01x slower                                           |
| logging_simple             | 7.05 us                                                                 | 7.11 us: 1.01x slower                                            |
| regex_v8                   | 30.4 ms                                                                 | 30.8 ms: 1.01x slower                                            |
| pickle                     | 13.6 us                                                                 | 13.9 us: 1.02x slower                                            |
| fannkuch                   | 463 ms                                                                  | 471 ms: 1.02x slower                                             |
| async_tree_io              | 1.15 sec                                                                | 1.17 sec: 1.02x slower                                           |
| async_tree_none            | 418 ms                                                                  | 429 ms: 1.03x slower                                             |
| xml_etree_parse            | 188 ms                                                                  | 193 ms: 1.03x slower                                             |
| thrift                     | 931 us                                                                  | 962 us: 1.03x slower                                             |
| create_gc_cycles           | 2.26 ms                                                                 | 2.35 ms: 1.04x slower                                            |
| pyflate                    | 558 ms                                                                  | 583 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                                   | 1.00x faster                                                     |

Benchmark hidden because not significant (61): bench_mp_pool, sqlglot_optimize, pylint, comprehensions, pickle_pure_python, json, mako, async_tree_memoization, regex_effbot, deepcopy, genshi_xml, nbody, json_loads, crypto_pyaes, async_tree_io_tg, regex_compile, async_generators, asyncio_websockets, python_startup, sqlglot_normalize, dulwich_log, scimark_sparse_mat_mult, pidigits, go, richards_super, float, sympy_sum, sqlite_synth, richards, chaos, deltablue, typing_runtime_protocols, coverage, xml_etree_process, raytrace, async_tree_memoization_tg, sqlglot_transpile, unpickle_pure_python, 2to3, coroutines, sympy_str, asyncio_tcp, sympy_integrate, xml_etree_generate, scimark_monte_carlo, sympy_expand, docutils, unpickle, unpickle_list, pycparser, pathlib, deepcopy_memo, pickle_dict, generators, tornado_http, logging_silent, spectral_norm, sqlglot_parse, xml_etree_iterparse, logging_format, async_tree_none_tg

# HPT report

- Reliability score: 66.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x