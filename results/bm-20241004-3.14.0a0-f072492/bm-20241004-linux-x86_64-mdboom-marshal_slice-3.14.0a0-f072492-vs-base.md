# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.00x slower
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 257 ms: 1.01x slower                                           |
| html5lib       | 61.6 ms                                                               | 62.3 ms: 1.01x slower                                          |
| tornado_http   | 90.1 ms                                                               | 91.1 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 553 ms                                                                | 524 ms: 1.06x faster                                           |
| async_tree_none_tg         | 310 ms                                                                | 299 ms: 1.04x faster                                           |
| asyncio_websockets         | 557 ms                                                                | 552 ms: 1.01x faster                                           |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.78 sec: 1.00x slower                                         |
| asyncio_tcp                | 468 ms                                                                | 471 ms: 1.01x slower                                           |
| coroutines                 | 22.9 ms                                                               | 23.2 ms: 1.01x slower                                          |
| async_tree_io_tg           | 869 ms                                                                | 891 ms: 1.03x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none, async_generators, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                           |
| float          | 76.0 ms                                                               | 77.5 ms: 1.02x slower                                          |
| nbody          | 86.9 ms                                                               | 89.0 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                               | 3.54 ms: 1.05x faster                                          |
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                           |
| regex_v8       | 24.6 ms                                                               | 25.1 ms: 1.02x slower                                          |
| regex_dna      | 220 ms                                                                | 227 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_dict        | 35.5 us                                                               | 34.2 us: 1.04x faster                                          |
| unpickle_list      | 5.35 us                                                               | 5.21 us: 1.03x faster                                          |
| pickle             | 11.6 us                                                               | 11.4 us: 1.02x faster                                          |
| xml_etree_parse    | 159 ms                                                                | 156 ms: 1.02x faster                                           |
| json_dumps         | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                          |
| pickle_list        | 5.10 us                                                               | 5.08 us: 1.00x faster                                          |
| json_loads         | 26.8 us                                                               | 26.9 us: 1.00x slower                                          |
| xml_etree_generate | 85.8 ms                                                               | 86.3 ms: 1.01x slower                                          |
| xml_etree_process  | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                          |
| unpickle           | 14.3 us                                                               | 15.1 us: 1.05x slower                                          |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (4): unpickle_pure_python, tomli_loads, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.98 ms                                                               | 7.38 ms: 1.06x slower                                          |
| python_startup         | 10.5 ms                                                               | 11.2 ms: 1.06x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.4 ms                                                               | 11.2 ms: 1.02x faster                                          |
| django_template | 34.2 ms                                                               | 33.8 ms: 1.01x faster                                          |
| genshi_text     | 22.6 ms                                                               | 22.5 ms: 1.01x faster                                          |
| genshi_xml      | 49.3 ms                                                               | 50.1 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal               | 3.96 ms                                                               | 3.68 ms: 1.08x faster                                          |
| pycparser                  | 1.18 sec                                                              | 1.12 sec: 1.06x faster                                         |
| async_tree_cpu_io_mixed_tg | 553 ms                                                                | 524 ms: 1.06x faster                                           |
| regex_effbot               | 3.73 ms                                                               | 3.54 ms: 1.05x faster                                          |
| pickle_dict                | 35.5 us                                                               | 34.2 us: 1.04x faster                                          |
| async_tree_none_tg         | 310 ms                                                                | 299 ms: 1.04x faster                                           |
| spectral_norm              | 114 ms                                                                | 110 ms: 1.03x faster                                           |
| unpickle_list              | 5.35 us                                                               | 5.21 us: 1.03x faster                                          |
| mdp                        | 2.58 sec                                                              | 2.52 sec: 1.02x faster                                         |
| pickle                     | 11.6 us                                                               | 11.4 us: 1.02x faster                                          |
| deepcopy_memo              | 30.0 us                                                               | 29.5 us: 1.02x faster                                          |
| crypto_pyaes               | 71.1 ms                                                               | 69.9 ms: 1.02x faster                                          |
| xml_etree_parse            | 159 ms                                                                | 156 ms: 1.02x faster                                           |
| mako                       | 11.4 ms                                                               | 11.2 ms: 1.02x faster                                          |
| typing_runtime_protocols   | 160 us                                                                | 158 us: 1.02x faster                                           |
| django_template            | 34.2 ms                                                               | 33.8 ms: 1.01x faster                                          |
| go                         | 121 ms                                                                | 119 ms: 1.01x faster                                           |
| bpe_tokeniser              | 4.79 sec                                                              | 4.75 sec: 1.01x faster                                         |
| chaos                      | 59.7 ms                                                               | 59.1 ms: 1.01x faster                                          |
| dulwich_log                | 64.4 ms                                                               | 63.9 ms: 1.01x faster                                          |
| fannkuch                   | 399 ms                                                                | 396 ms: 1.01x faster                                           |
| asyncio_websockets         | 557 ms                                                                | 552 ms: 1.01x faster                                           |
| genshi_text                | 22.6 ms                                                               | 22.5 ms: 1.01x faster                                          |
| json_dumps                 | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                          |
| pickle_list                | 5.10 us                                                               | 5.08 us: 1.00x faster                                          |
| sqlglot_normalize          | 106 ms                                                                | 105 ms: 1.00x faster                                           |
| sqlglot_transpile          | 1.59 ms                                                               | 1.58 ms: 1.00x faster                                          |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                           |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.78 sec: 1.00x slower                                         |
| hexiom                     | 6.26 ms                                                               | 6.27 ms: 1.00x slower                                          |
| bench_thread_pool          | 849 us                                                                | 851 us: 1.00x slower                                           |
| sqlglot_optimize           | 53.0 ms                                                               | 53.2 ms: 1.00x slower                                          |
| json_loads                 | 26.8 us                                                               | 26.9 us: 1.00x slower                                          |
| nqueens                    | 78.9 ms                                                               | 79.2 ms: 1.00x slower                                          |
| richards                   | 46.1 ms                                                               | 46.3 ms: 1.00x slower                                          |
| create_gc_cycles           | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                          |
| xml_etree_generate         | 85.8 ms                                                               | 86.3 ms: 1.01x slower                                          |
| logging_simple             | 5.55 us                                                               | 5.58 us: 1.01x slower                                          |
| pathlib                    | 15.9 ms                                                               | 16.0 ms: 1.01x slower                                          |
| raytrace                   | 265 ms                                                                | 267 ms: 1.01x slower                                           |
| deepcopy                   | 260 us                                                                | 262 us: 1.01x slower                                           |
| asyncio_tcp                | 468 ms                                                                | 471 ms: 1.01x slower                                           |
| regex_compile              | 128 ms                                                                | 129 ms: 1.01x slower                                           |
| deepcopy_reduce            | 2.68 us                                                               | 2.70 us: 1.01x slower                                          |
| xml_etree_process          | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                          |
| logging_silent             | 103 ns                                                                | 104 ns: 1.01x slower                                           |
| scimark_monte_carlo        | 68.4 ms                                                               | 69.0 ms: 1.01x slower                                          |
| scimark_sor                | 124 ms                                                                | 125 ms: 1.01x slower                                           |
| sympy_integrate            | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                          |
| coroutines                 | 22.9 ms                                                               | 23.2 ms: 1.01x slower                                          |
| comprehensions             | 16.4 us                                                               | 16.6 us: 1.01x slower                                          |
| richards_super             | 52.1 ms                                                               | 52.6 ms: 1.01x slower                                          |
| tornado_http               | 90.1 ms                                                               | 91.1 ms: 1.01x slower                                          |
| pprint_pformat             | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                         |
| html5lib                   | 61.6 ms                                                               | 62.3 ms: 1.01x slower                                          |
| coverage                   | 84.1 ms                                                               | 85.2 ms: 1.01x slower                                          |
| 2to3                       | 254 ms                                                                | 257 ms: 1.01x slower                                           |
| pyflate                    | 473 ms                                                                | 479 ms: 1.01x slower                                           |
| deltablue                  | 3.24 ms                                                               | 3.28 ms: 1.01x slower                                          |
| logging_format             | 6.13 us                                                               | 6.22 us: 1.02x slower                                          |
| genshi_xml                 | 49.3 ms                                                               | 50.1 ms: 1.02x slower                                          |
| regex_v8                   | 24.6 ms                                                               | 25.1 ms: 1.02x slower                                          |
| float                      | 76.0 ms                                                               | 77.5 ms: 1.02x slower                                          |
| nbody                      | 86.9 ms                                                               | 89.0 ms: 1.02x slower                                          |
| scimark_fft                | 366 ms                                                                | 376 ms: 1.02x slower                                           |
| async_tree_io_tg           | 869 ms                                                                | 891 ms: 1.03x slower                                           |
| regex_dna                  | 220 ms                                                                | 227 ms: 1.03x slower                                           |
| unpickle                   | 14.3 us                                                               | 15.1 us: 1.05x slower                                          |
| python_startup_no_site     | 6.98 ms                                                               | 7.38 ms: 1.06x slower                                          |
| python_startup             | 10.5 ms                                                               | 11.2 ms: 1.06x slower                                          |
| scimark_sparse_mat_mult    | 4.59 ms                                                               | 4.92 ms: 1.07x slower                                          |
| bench_mp_pool              | 56.0 ms                                                               | 60.3 ms: 1.08x slower                                          |
| unpack_sequence            | 46.8 ns                                                               | 53.3 ns: 1.14x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (24): async_tree_memoization_tg, async_tree_none, sqlglot_parse, meteor_contest, scimark_lu, generators, unpickle_pure_python, sympy_expand, pylint, docutils, pprint_safe_repr, tomli_loads, pickle_pure_python, async_generators, sqlite_synth, sympy_sum, json, sympy_str, thrift, telco, xml_etree_iterparse, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 98.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x