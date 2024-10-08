# Results vs. base

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-aarch64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.00x slower
- HPT reliability: 70.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io  | 1.17 sec                                                                | 1.14 sec: 1.03x faster                                              |
| asyncio_tcp    | 551 ms                                                                  | 566 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                        |

Benchmark hidden because not significant (11): async_generators, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_tcp_ssl, coroutines, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 110 ms                                                                  | 109 ms: 1.01x faster                                                |
| float          | 91.8 ms                                                                 | 94.2 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                  | 124 ms: 1.01x faster                                                |
| regex_effbot   | 4.89 ms                                                                 | 5.01 ms: 1.02x slower                                               |
| regex_dna      | 247 ms                                                                  | 253 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps      | 13.5 ms                                                                 | 13.3 ms: 1.02x faster                                               |
| pickle_list     | 5.23 us                                                                 | 5.19 us: 1.01x faster                                               |
| tomli_loads     | 2.63 sec                                                                | 2.61 sec: 1.01x faster                                              |
| xml_etree_parse | 185 ms                                                                  | 191 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                        |

Benchmark hidden because not significant (10): unpickle_pure_python, json_loads, unpickle, xml_etree_generate, pickle_pure_python, unpickle_list, pickle, pickle_dict, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                 | 13.0 ms: 1.01x slower                                               |
| python_startup_no_site | 8.58 ms                                                                 | 8.65 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 13.3 ms                                                                 | 13.3 ms: 1.01x slower                                               |
| django_template | 41.4 ms                                                                 | 42.6 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| scimark_fft             | 471 ms                                                                  | 440 ms: 1.07x faster                                                |
| sqlite_synth            | 3.93 us                                                                 | 3.82 us: 1.03x faster                                               |
| async_tree_io           | 1.17 sec                                                                | 1.14 sec: 1.03x faster                                              |
| scimark_lu              | 136 ms                                                                  | 134 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 82.1 ms                                                                 | 80.7 ms: 1.02x faster                                               |
| spectral_norm           | 143 ms                                                                  | 141 ms: 1.02x faster                                                |
| json_dumps              | 13.5 ms                                                                 | 13.3 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult | 6.49 ms                                                                 | 6.39 ms: 1.01x faster                                               |
| regex_compile           | 126 ms                                                                  | 124 ms: 1.01x faster                                                |
| nbody                   | 110 ms                                                                  | 109 ms: 1.01x faster                                                |
| chaos                   | 68.7 ms                                                                 | 68.1 ms: 1.01x faster                                               |
| pickle_list             | 5.23 us                                                                 | 5.19 us: 1.01x faster                                               |
| tomli_loads             | 2.63 sec                                                                | 2.61 sec: 1.01x faster                                              |
| mako                    | 13.3 ms                                                                 | 13.3 ms: 1.01x slower                                               |
| sqlglot_transpile       | 1.73 ms                                                                 | 1.74 ms: 1.01x slower                                               |
| python_startup          | 13.0 ms                                                                 | 13.0 ms: 1.01x slower                                               |
| python_startup_no_site  | 8.58 ms                                                                 | 8.65 ms: 1.01x slower                                               |
| bench_mp_pool           | 7.03 ms                                                                 | 7.11 ms: 1.01x slower                                               |
| pprint_safe_repr        | 911 ms                                                                  | 923 ms: 1.01x slower                                                |
| crypto_pyaes            | 81.8 ms                                                                 | 82.9 ms: 1.01x slower                                               |
| pprint_pformat          | 1.88 sec                                                                | 1.91 sec: 1.02x slower                                              |
| unpack_sequence         | 58.9 ns                                                                 | 59.9 ns: 1.02x slower                                               |
| deepcopy                | 331 us                                                                  | 337 us: 1.02x slower                                                |
| thrift                  | 924 us                                                                  | 943 us: 1.02x slower                                                |
| regex_effbot            | 4.89 ms                                                                 | 5.01 ms: 1.02x slower                                               |
| regex_dna               | 247 ms                                                                  | 253 ms: 1.02x slower                                                |
| fannkuch                | 459 ms                                                                  | 471 ms: 1.03x slower                                                |
| float                   | 91.8 ms                                                                 | 94.2 ms: 1.03x slower                                               |
| asyncio_tcp             | 551 ms                                                                  | 566 ms: 1.03x slower                                                |
| django_template         | 41.4 ms                                                                 | 42.6 ms: 1.03x slower                                               |
| xml_etree_parse         | 185 ms                                                                  | 191 ms: 1.03x slower                                                |
| pyflate                 | 557 ms                                                                  | 579 ms: 1.04x slower                                                |
| create_gc_cycles        | 2.28 ms                                                                 | 2.37 ms: 1.04x slower                                               |
| Geometric mean          | (ref)                                                                   | 1.00x slower                                                        |

Benchmark hidden because not significant (64): async_generators, async_tree_none_tg, regex_v8, tornado_http, genshi_xml, scimark_sor, deepcopy_memo, unpickle_pure_python, json_loads, coverage, asyncio_websockets, logging_silent, async_tree_memoization_tg, hexiom, meteor_contest, go, html5lib, async_tree_cpu_io_mixed_tg, sympy_integrate, async_tree_io_tg, bpe_tokeniser, richards, sympy_sum, richards_super, mdp, json, raytrace, sympy_expand, pidigits, unpickle, xml_etree_generate, pathlib, pickle_pure_python, unpickle_list, deltablue, pickle, asyncio_tcp_ssl, pickle_dict, sympy_str, xml_etree_process, coroutines, pycparser, comprehensions, gc_traversal, async_tree_memoization, docutils, logging_format, sqlglot_parse, generators, async_tree_none, telco, pylint, typing_runtime_protocols, sqlglot_optimize, deepcopy_reduce, bench_thread_pool, 2to3, nqueens, genshi_text, async_tree_cpu_io_mixed, dulwich_log, logging_simple, sqlglot_normalize, xml_etree_iterparse

# HPT report

- Reliability score: 70.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x