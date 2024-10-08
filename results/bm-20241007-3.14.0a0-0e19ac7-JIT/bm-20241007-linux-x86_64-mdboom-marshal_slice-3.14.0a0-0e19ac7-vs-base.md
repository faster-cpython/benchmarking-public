# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.00x faster
- HPT reliability: 85.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 277 ms: 1.01x faster                                           |
| docutils       | 2.95 sec                                                              | 2.93 sec: 1.01x faster                                         |
| html5lib       | 65.0 ms                                                               | 64.5 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 410 ms                                                                | 401 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 582 ms                                                                | 570 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 561 ms                                                                | 549 ms: 1.02x faster                                           |
| coroutines                 | 22.8 ms                                                               | 22.7 ms: 1.01x faster                                          |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.81 sec: 1.01x slower                                         |
| async_generators           | 450 ms                                                                | 460 ms: 1.02x slower                                           |
| async_tree_none            | 318 ms                                                                | 331 ms: 1.04x slower                                           |
| async_tree_io_tg           | 867 ms                                                                | 915 ms: 1.06x slower                                           |
| async_tree_io              | 886 ms                                                                | 937 ms: 1.06x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (4): async_tree_none_tg, asyncio_websockets, asyncio_tcp, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 81.8 ms                                                               | 80.7 ms: 1.01x faster                                          |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 25.7 ms                                                               | 24.1 ms: 1.07x faster                                          |
| regex_dna      | 231 ms                                                                | 219 ms: 1.05x faster                                           |
| regex_effbot   | 3.79 ms                                                               | 3.77 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle               | 11.8 us                                                               | 11.5 us: 1.03x faster                                          |
| pickle_dict          | 34.6 us                                                               | 34.1 us: 1.01x faster                                          |
| xml_etree_generate   | 77.9 ms                                                               | 77.2 ms: 1.01x faster                                          |
| xml_etree_iterparse  | 98.2 ms                                                               | 99.1 ms: 1.01x slower                                          |
| pickle_list          | 5.14 us                                                               | 5.20 us: 1.01x slower                                          |
| pickle_pure_python   | 303 us                                                                | 307 us: 1.01x slower                                           |
| unpickle_pure_python | 214 us                                                                | 217 us: 1.02x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (7): xml_etree_parse, tomli_loads, xml_etree_process, json_dumps, json_loads, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                          |
| python_startup_no_site | 7.07 ms                                                               | 7.09 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 36.2 ms                                                               | 35.5 ms: 1.02x faster                                          |
| mako            | 9.89 ms                                                               | 10.0 ms: 1.01x slower                                          |
| genshi_xml      | 57.1 ms                                                               | 58.3 ms: 1.02x slower                                          |
| genshi_text     | 24.9 ms                                                               | 25.5 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mdp                        | 2.71 sec                                                              | 2.54 sec: 1.07x faster                                         |
| regex_v8                   | 25.7 ms                                                               | 24.1 ms: 1.07x faster                                          |
| regex_dna                  | 231 ms                                                                | 219 ms: 1.05x faster                                           |
| pycparser                  | 1.23 sec                                                              | 1.16 sec: 1.05x faster                                         |
| pyflate                    | 455 ms                                                                | 439 ms: 1.04x faster                                           |
| bpe_tokeniser              | 4.46 sec                                                              | 4.32 sec: 1.03x faster                                         |
| pickle                     | 11.8 us                                                               | 11.5 us: 1.03x faster                                          |
| async_tree_memoization     | 410 ms                                                                | 401 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 582 ms                                                                | 570 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 561 ms                                                                | 549 ms: 1.02x faster                                           |
| dulwich_log                | 68.7 ms                                                               | 67.3 ms: 1.02x faster                                          |
| django_template            | 36.2 ms                                                               | 35.5 ms: 1.02x faster                                          |
| chaos                      | 60.7 ms                                                               | 59.4 ms: 1.02x faster                                          |
| meteor_contest             | 107 ms                                                                | 105 ms: 1.02x faster                                           |
| sympy_sum                  | 178 ms                                                                | 175 ms: 1.02x faster                                           |
| pickle_dict                | 34.6 us                                                               | 34.1 us: 1.01x faster                                          |
| nbody                      | 81.8 ms                                                               | 80.7 ms: 1.01x faster                                          |
| 2to3                       | 280 ms                                                                | 277 ms: 1.01x faster                                           |
| comprehensions             | 17.1 us                                                               | 17.0 us: 1.01x faster                                          |
| xml_etree_generate         | 77.9 ms                                                               | 77.2 ms: 1.01x faster                                          |
| logging_simple             | 5.70 us                                                               | 5.66 us: 1.01x faster                                          |
| html5lib                   | 65.0 ms                                                               | 64.5 ms: 1.01x faster                                          |
| sqlite_synth               | 2.77 us                                                               | 2.75 us: 1.01x faster                                          |
| docutils                   | 2.95 sec                                                              | 2.93 sec: 1.01x faster                                         |
| fannkuch                   | 371 ms                                                                | 369 ms: 1.01x faster                                           |
| sympy_str                  | 303 ms                                                                | 301 ms: 1.01x faster                                           |
| richards                   | 42.9 ms                                                               | 42.6 ms: 1.01x faster                                          |
| sympy_integrate            | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                          |
| bench_thread_pool          | 895 us                                                                | 890 us: 1.01x faster                                           |
| go                         | 132 ms                                                                | 132 ms: 1.01x faster                                           |
| coroutines                 | 22.8 ms                                                               | 22.7 ms: 1.01x faster                                          |
| regex_effbot               | 3.79 ms                                                               | 3.77 ms: 1.00x faster                                          |
| sqlglot_normalize          | 116 ms                                                                | 116 ms: 1.00x faster                                           |
| sqlglot_transpile          | 1.70 ms                                                               | 1.69 ms: 1.00x faster                                          |
| pidigits                   | 185 ms                                                                | 185 ms: 1.00x slower                                           |
| unpack_sequence            | 108 ns                                                                | 108 ns: 1.00x slower                                           |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                          |
| python_startup_no_site     | 7.07 ms                                                               | 7.09 ms: 1.00x slower                                          |
| deepcopy_memo              | 26.8 us                                                               | 26.9 us: 1.00x slower                                          |
| scimark_sor                | 118 ms                                                                | 118 ms: 1.01x slower                                           |
| scimark_lu                 | 111 ms                                                                | 112 ms: 1.01x slower                                           |
| nqueens                    | 86.1 ms                                                               | 86.7 ms: 1.01x slower                                          |
| deepcopy_reduce            | 2.64 us                                                               | 2.66 us: 1.01x slower                                          |
| xml_etree_iterparse        | 98.2 ms                                                               | 99.1 ms: 1.01x slower                                          |
| generators                 | 34.7 ms                                                               | 35.0 ms: 1.01x slower                                          |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.81 sec: 1.01x slower                                         |
| pickle_list                | 5.14 us                                                               | 5.20 us: 1.01x slower                                          |
| mako                       | 9.89 ms                                                               | 10.0 ms: 1.01x slower                                          |
| pickle_pure_python         | 303 us                                                                | 307 us: 1.01x slower                                           |
| typing_runtime_protocols   | 164 us                                                                | 167 us: 1.01x slower                                           |
| sqlglot_parse              | 1.34 ms                                                               | 1.36 ms: 1.01x slower                                          |
| pathlib                    | 15.7 ms                                                               | 15.9 ms: 1.01x slower                                          |
| unpickle_pure_python       | 214 us                                                                | 217 us: 1.02x slower                                           |
| genshi_xml                 | 57.1 ms                                                               | 58.3 ms: 1.02x slower                                          |
| async_generators           | 450 ms                                                                | 460 ms: 1.02x slower                                           |
| genshi_text                | 24.9 ms                                                               | 25.5 ms: 1.02x slower                                          |
| json                       | 5.03 ms                                                               | 5.19 ms: 1.03x slower                                          |
| async_tree_none            | 318 ms                                                                | 331 ms: 1.04x slower                                           |
| create_gc_cycles           | 1.72 ms                                                               | 1.80 ms: 1.04x slower                                          |
| async_tree_io_tg           | 867 ms                                                                | 915 ms: 1.06x slower                                           |
| async_tree_io              | 886 ms                                                                | 937 ms: 1.06x slower                                           |
| gc_traversal               | 3.52 ms                                                               | 3.78 ms: 1.07x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (35): xml_etree_parse, scimark_fft, scimark_monte_carlo, logging_format, tomli_loads, richards_super, hexiom, async_tree_none_tg, tornado_http, bench_mp_pool, thrift, spectral_norm, pylint, coverage, crypto_pyaes, asyncio_websockets, xml_etree_process, raytrace, telco, pprint_pformat, sqlglot_optimize, deltablue, float, sympy_expand, asyncio_tcp, json_dumps, regex_compile, json_loads, unpickle_list, scimark_sparse_mat_mult, logging_silent, unpickle, deepcopy, pprint_safe_repr, async_tree_memoization_tg

# HPT report

- Reliability score: 85.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x