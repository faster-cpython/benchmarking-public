# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.005x slower
- HPT reliability: 96.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 253 ms: 1.00x slower                                           |
| html5lib       | 61.6 ms                                                               | 61.4 ms: 1.00x faster                                          |
| tornado_http   | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| coroutines                 | 23.6 ms                                                               | 22.8 ms: 1.04x faster                                          |
| async_tree_cpu_io_mixed_tg | 550 ms                                                                | 536 ms: 1.03x faster                                           |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.77 sec: 1.01x faster                                         |
| asyncio_tcp                | 471 ms                                                                | 470 ms: 1.00x faster                                           |
| async_generators           | 431 ms                                                                | 433 ms: 1.01x slower                                           |
| async_tree_io_tg           | 875 ms                                                                | 915 ms: 1.05x slower                                           |
| async_tree_io              | 882 ms                                                                | 924 ms: 1.05x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 76.4 ms                                                               | 76.1 ms: 1.00x faster                                          |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                | 127 ms: 1.01x faster                                           |
| regex_v8       | 24.9 ms                                                               | 25.2 ms: 1.01x slower                                          |
| regex_dna      | 215 ms                                                                | 220 ms: 1.02x slower                                           |
| regex_effbot   | 3.55 ms                                                               | 3.70 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_list          | 5.11 us                                                               | 5.01 us: 1.02x faster                                          |
| tomli_loads          | 2.09 sec                                                              | 2.07 sec: 1.01x faster                                         |
| pickle               | 11.5 us                                                               | 11.5 us: 1.00x slower                                          |
| json_loads           | 26.8 us                                                               | 27.1 us: 1.01x slower                                          |
| pickle_dict          | 34.5 us                                                               | 34.9 us: 1.01x slower                                          |
| pickle_pure_python   | 300 us                                                                | 305 us: 1.02x slower                                           |
| unpickle_pure_python | 211 us                                                                | 215 us: 1.02x slower                                           |
| unpickle_list        | 5.28 us                                                               | 5.41 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (6): json_dumps, xml_etree_process, xml_etree_iterparse, xml_etree_generate, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                          |
| python_startup_no_site | 6.99 ms                                                               | 7.01 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                               | 49.3 ms: 1.05x faster                                          |
| genshi_text     | 22.5 ms                                                               | 21.9 ms: 1.03x faster                                          |
| django_template | 33.9 ms                                                               | 34.2 ms: 1.01x slower                                          |
| mako            | 11.1 ms                                                               | 11.4 ms: 1.04x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml                 | 51.8 ms                                                               | 49.3 ms: 1.05x faster                                          |
| coroutines                 | 23.6 ms                                                               | 22.8 ms: 1.04x faster                                          |
| genshi_text                | 22.5 ms                                                               | 21.9 ms: 1.03x faster                                          |
| async_tree_cpu_io_mixed_tg | 550 ms                                                                | 536 ms: 1.03x faster                                           |
| coverage                   | 86.3 ms                                                               | 84.5 ms: 1.02x faster                                          |
| typing_runtime_protocols   | 162 us                                                                | 159 us: 1.02x faster                                           |
| pprint_pformat             | 1.47 sec                                                              | 1.44 sec: 1.02x faster                                         |
| pprint_safe_repr           | 717 ms                                                                | 703 ms: 1.02x faster                                           |
| pickle_list                | 5.11 us                                                               | 5.01 us: 1.02x faster                                          |
| deepcopy_reduce            | 2.75 us                                                               | 2.71 us: 1.01x faster                                          |
| deepcopy                   | 263 us                                                                | 260 us: 1.01x faster                                           |
| tomli_loads                | 2.09 sec                                                              | 2.07 sec: 1.01x faster                                         |
| scimark_lu                 | 113 ms                                                                | 112 ms: 1.01x faster                                           |
| sqlite_synth               | 2.83 us                                                               | 2.80 us: 1.01x faster                                          |
| pathlib                    | 15.9 ms                                                               | 15.8 ms: 1.01x faster                                          |
| crypto_pyaes               | 72.3 ms                                                               | 71.7 ms: 1.01x faster                                          |
| dulwich_log                | 64.9 ms                                                               | 64.4 ms: 1.01x faster                                          |
| sympy_expand               | 454 ms                                                                | 450 ms: 1.01x faster                                           |
| scimark_sor                | 125 ms                                                                | 124 ms: 1.01x faster                                           |
| tornado_http               | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                          |
| regex_compile              | 128 ms                                                                | 127 ms: 1.01x faster                                           |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.77 sec: 1.01x faster                                         |
| float                      | 76.4 ms                                                               | 76.1 ms: 1.00x faster                                          |
| html5lib                   | 61.6 ms                                                               | 61.4 ms: 1.00x faster                                          |
| sqlglot_normalize          | 107 ms                                                                | 107 ms: 1.00x faster                                           |
| fannkuch                   | 400 ms                                                                | 399 ms: 1.00x faster                                           |
| asyncio_tcp                | 471 ms                                                                | 470 ms: 1.00x faster                                           |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x faster                                           |
| 2to3                       | 253 ms                                                                | 253 ms: 1.00x slower                                           |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                          |
| pickle                     | 11.5 us                                                               | 11.5 us: 1.00x slower                                          |
| python_startup_no_site     | 6.99 ms                                                               | 7.01 ms: 1.00x slower                                          |
| sqlglot_transpile          | 1.58 ms                                                               | 1.58 ms: 1.00x slower                                          |
| generators                 | 27.6 ms                                                               | 27.7 ms: 1.00x slower                                          |
| sympy_integrate            | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                          |
| deepcopy_memo              | 29.6 us                                                               | 29.7 us: 1.01x slower                                          |
| async_generators           | 431 ms                                                                | 433 ms: 1.01x slower                                           |
| logging_format             | 6.11 us                                                               | 6.15 us: 1.01x slower                                          |
| unpack_sequence            | 47.9 ns                                                               | 48.3 ns: 1.01x slower                                          |
| django_template            | 33.9 ms                                                               | 34.2 ms: 1.01x slower                                          |
| chaos                      | 59.3 ms                                                               | 59.8 ms: 1.01x slower                                          |
| comprehensions             | 16.4 us                                                               | 16.5 us: 1.01x slower                                          |
| json_loads                 | 26.8 us                                                               | 27.1 us: 1.01x slower                                          |
| regex_v8                   | 24.9 ms                                                               | 25.2 ms: 1.01x slower                                          |
| pickle_dict                | 34.5 us                                                               | 34.9 us: 1.01x slower                                          |
| scimark_monte_carlo        | 66.9 ms                                                               | 67.8 ms: 1.01x slower                                          |
| richards_super             | 51.4 ms                                                               | 52.1 ms: 1.01x slower                                          |
| meteor_contest             | 105 ms                                                                | 107 ms: 1.01x slower                                           |
| telco                      | 7.88 ms                                                               | 8.01 ms: 1.02x slower                                          |
| scimark_fft                | 359 ms                                                                | 364 ms: 1.02x slower                                           |
| pickle_pure_python         | 300 us                                                                | 305 us: 1.02x slower                                           |
| go                         | 117 ms                                                                | 119 ms: 1.02x slower                                           |
| raytrace                   | 260 ms                                                                | 264 ms: 1.02x slower                                           |
| richards                   | 45.2 ms                                                               | 46.0 ms: 1.02x slower                                          |
| unpickle_pure_python       | 211 us                                                                | 215 us: 1.02x slower                                           |
| pyflate                    | 461 ms                                                                | 472 ms: 1.02x slower                                           |
| regex_dna                  | 215 ms                                                                | 220 ms: 1.02x slower                                           |
| unpickle_list              | 5.28 us                                                               | 5.41 us: 1.02x slower                                          |
| hexiom                     | 6.08 ms                                                               | 6.24 ms: 1.03x slower                                          |
| deltablue                  | 3.17 ms                                                               | 3.26 ms: 1.03x slower                                          |
| mako                       | 11.1 ms                                                               | 11.4 ms: 1.04x slower                                          |
| create_gc_cycles           | 1.72 ms                                                               | 1.79 ms: 1.04x slower                                          |
| pycparser                  | 1.12 sec                                                              | 1.17 sec: 1.04x slower                                         |
| regex_effbot               | 3.55 ms                                                               | 3.70 ms: 1.04x slower                                          |
| async_tree_io_tg           | 875 ms                                                                | 915 ms: 1.05x slower                                           |
| nqueens                    | 78.5 ms                                                               | 82.2 ms: 1.05x slower                                          |
| async_tree_io              | 882 ms                                                                | 924 ms: 1.05x slower                                           |
| logging_silent             | 98.8 ns                                                               | 104 ns: 1.05x slower                                           |
| gc_traversal               | 3.56 ms                                                               | 3.95 ms: 1.11x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (28): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, scimark_sparse_mat_mult, sqlglot_parse, bpe_tokeniser, bench_mp_pool, thrift, sympy_sum, pylint, json_dumps, asyncio_websockets, nbody, sqlglot_optimize, json, bench_thread_pool, mdp, docutils, xml_etree_process, sympy_str, xml_etree_iterparse, spectral_norm, xml_etree_generate, logging_simple, xml_etree_parse, unpickle, async_tree_none, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 96.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x