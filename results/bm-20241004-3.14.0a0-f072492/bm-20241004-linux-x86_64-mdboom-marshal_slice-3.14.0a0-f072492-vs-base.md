# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.006x slower
- HPT reliability: 98.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 257 ms: 1.02x slower                                           |
| docutils       | 2.62 sec                                                              | 2.63 sec: 1.01x slower                                         |
| html5lib       | 61.6 ms                                                               | 62.3 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 550 ms                                                                | 524 ms: 1.05x faster                                           |
| coroutines                 | 23.6 ms                                                               | 23.2 ms: 1.02x faster                                          |
| asyncio_websockets         | 558 ms                                                                | 552 ms: 1.01x faster                                           |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.78 sec: 1.00x faster                                         |
| async_generators           | 431 ms                                                                | 435 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed    | 559 ms                                                                | 570 ms: 1.02x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, asyncio_tcp, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                           |
| float          | 76.4 ms                                                               | 77.5 ms: 1.01x slower                                          |
| nbody          | 86.9 ms                                                               | 89.0 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.55 ms                                                               | 3.54 ms: 1.00x faster                                          |
| regex_compile  | 128 ms                                                                | 129 ms: 1.00x slower                                           |
| regex_v8       | 24.9 ms                                                               | 25.1 ms: 1.00x slower                                          |
| regex_dna      | 215 ms                                                                | 227 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle_list        | 5.28 us                                                               | 5.21 us: 1.01x faster                                          |
| pickle               | 11.5 us                                                               | 11.4 us: 1.01x faster                                          |
| tomli_loads          | 2.09 sec                                                              | 2.07 sec: 1.01x faster                                         |
| pickle_list          | 5.11 us                                                               | 5.08 us: 1.01x faster                                          |
| xml_etree_process    | 58.9 ms                                                               | 59.0 ms: 1.00x slower                                          |
| xml_etree_generate   | 85.7 ms                                                               | 86.3 ms: 1.01x slower                                          |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                           |
| pickle_pure_python   | 300 us                                                                | 306 us: 1.02x slower                                           |
| unpickle_pure_python | 211 us                                                                | 216 us: 1.02x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (5): pickle_dict, xml_etree_parse, json_dumps, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 7.38 ms: 1.06x slower                                          |
| python_startup         | 10.5 ms                                                               | 11.2 ms: 1.06x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                               | 50.1 ms: 1.03x faster                                          |
| mako           | 11.1 ms                                                               | 11.2 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 550 ms                                                                | 524 ms: 1.05x faster                                           |
| crypto_pyaes               | 72.3 ms                                                               | 69.9 ms: 1.03x faster                                          |
| genshi_xml                 | 51.8 ms                                                               | 50.1 ms: 1.03x faster                                          |
| typing_runtime_protocols   | 162 us                                                                | 158 us: 1.03x faster                                           |
| coroutines                 | 23.6 ms                                                               | 23.2 ms: 1.02x faster                                          |
| spectral_norm              | 112 ms                                                                | 110 ms: 1.02x faster                                           |
| deepcopy_reduce            | 2.75 us                                                               | 2.70 us: 1.02x faster                                          |
| dulwich_log                | 64.9 ms                                                               | 63.9 ms: 1.02x faster                                          |
| sqlglot_normalize          | 107 ms                                                                | 105 ms: 1.02x faster                                           |
| coverage                   | 86.3 ms                                                               | 85.2 ms: 1.01x faster                                          |
| unpickle_list              | 5.28 us                                                               | 5.21 us: 1.01x faster                                          |
| fannkuch                   | 400 ms                                                                | 396 ms: 1.01x faster                                           |
| asyncio_websockets         | 558 ms                                                                | 552 ms: 1.01x faster                                           |
| pickle                     | 11.5 us                                                               | 11.4 us: 1.01x faster                                          |
| sqlite_synth               | 2.83 us                                                               | 2.80 us: 1.01x faster                                          |
| json                       | 5.07 ms                                                               | 5.03 ms: 1.01x faster                                          |
| pprint_safe_repr           | 717 ms                                                                | 712 ms: 1.01x faster                                           |
| tomli_loads                | 2.09 sec                                                              | 2.07 sec: 1.01x faster                                         |
| pickle_list                | 5.11 us                                                               | 5.08 us: 1.01x faster                                          |
| deepcopy                   | 263 us                                                                | 262 us: 1.00x faster                                           |
| bench_thread_pool          | 855 us                                                                | 851 us: 1.00x faster                                           |
| regex_effbot               | 3.55 ms                                                               | 3.54 ms: 1.00x faster                                          |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.78 sec: 1.00x faster                                         |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                           |
| sqlglot_transpile          | 1.58 ms                                                               | 1.58 ms: 1.00x slower                                          |
| xml_etree_process          | 58.9 ms                                                               | 59.0 ms: 1.00x slower                                          |
| mdp                        | 2.51 sec                                                              | 2.52 sec: 1.00x slower                                         |
| regex_compile              | 128 ms                                                                | 129 ms: 1.00x slower                                           |
| regex_v8                   | 24.9 ms                                                               | 25.1 ms: 1.00x slower                                          |
| docutils                   | 2.62 sec                                                              | 2.63 sec: 1.01x slower                                         |
| sympy_sum                  | 147 ms                                                                | 148 ms: 1.01x slower                                           |
| sympy_str                  | 266 ms                                                                | 268 ms: 1.01x slower                                           |
| meteor_contest             | 105 ms                                                                | 106 ms: 1.01x slower                                           |
| xml_etree_generate         | 85.7 ms                                                               | 86.3 ms: 1.01x slower                                          |
| nqueens                    | 78.5 ms                                                               | 79.2 ms: 1.01x slower                                          |
| logging_simple             | 5.53 us                                                               | 5.58 us: 1.01x slower                                          |
| sympy_integrate            | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                          |
| html5lib                   | 61.6 ms                                                               | 62.3 ms: 1.01x slower                                          |
| async_generators           | 431 ms                                                                | 435 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 104 ms                                                                | 105 ms: 1.01x slower                                           |
| comprehensions             | 16.4 us                                                               | 16.6 us: 1.01x slower                                          |
| float                      | 76.4 ms                                                               | 77.5 ms: 1.01x slower                                          |
| scimark_sparse_mat_mult    | 4.84 ms                                                               | 4.92 ms: 1.02x slower                                          |
| mako                       | 11.1 ms                                                               | 11.2 ms: 1.02x slower                                          |
| 2to3                       | 253 ms                                                                | 257 ms: 1.02x slower                                           |
| logging_format             | 6.11 us                                                               | 6.22 us: 1.02x slower                                          |
| generators                 | 27.6 ms                                                               | 28.1 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed    | 559 ms                                                                | 570 ms: 1.02x slower                                           |
| pickle_pure_python         | 300 us                                                                | 306 us: 1.02x slower                                           |
| telco                      | 7.88 ms                                                               | 8.04 ms: 1.02x slower                                          |
| create_gc_cycles           | 1.72 ms                                                               | 1.75 ms: 1.02x slower                                          |
| go                         | 117 ms                                                                | 119 ms: 1.02x slower                                           |
| richards_super             | 51.4 ms                                                               | 52.6 ms: 1.02x slower                                          |
| unpickle_pure_python       | 211 us                                                                | 216 us: 1.02x slower                                           |
| nbody                      | 86.9 ms                                                               | 89.0 ms: 1.02x slower                                          |
| richards                   | 45.2 ms                                                               | 46.3 ms: 1.03x slower                                          |
| raytrace                   | 260 ms                                                                | 267 ms: 1.03x slower                                           |
| scimark_monte_carlo        | 66.9 ms                                                               | 69.0 ms: 1.03x slower                                          |
| hexiom                     | 6.08 ms                                                               | 6.27 ms: 1.03x slower                                          |
| gc_traversal               | 3.56 ms                                                               | 3.68 ms: 1.03x slower                                          |
| deltablue                  | 3.17 ms                                                               | 3.28 ms: 1.03x slower                                          |
| pyflate                    | 461 ms                                                                | 479 ms: 1.04x slower                                           |
| scimark_fft                | 359 ms                                                                | 376 ms: 1.05x slower                                           |
| regex_dna                  | 215 ms                                                                | 227 ms: 1.05x slower                                           |
| logging_silent             | 98.8 ns                                                               | 104 ns: 1.05x slower                                           |
| python_startup_no_site     | 6.99 ms                                                               | 7.38 ms: 1.06x slower                                          |
| python_startup             | 10.5 ms                                                               | 11.2 ms: 1.06x slower                                          |
| bench_mp_pool              | 56.1 ms                                                               | 60.3 ms: 1.08x slower                                          |
| unpack_sequence            | 47.9 ns                                                               | 53.3 ns: 1.11x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (28): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, pickle_dict, pycparser, genshi_text, django_template, scimark_lu, chaos, thrift, xml_etree_parse, deepcopy_memo, pylint, json_dumps, sqlglot_optimize, pprint_pformat, bpe_tokeniser, scimark_sor, asyncio_tcp, sqlglot_parse, json_loads, sympy_expand, tornado_http, pathlib, async_tree_io, async_tree_memoization, unpickle, async_tree_io_tg

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 98.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x