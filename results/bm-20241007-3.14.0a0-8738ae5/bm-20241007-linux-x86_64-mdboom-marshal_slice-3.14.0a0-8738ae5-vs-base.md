# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 255 ms: 1.01x slower                                           |
| docutils       | 2.62 sec                                                              | 2.64 sec: 1.01x slower                                         |
| html5lib       | 61.6 ms                                                               | 61.4 ms: 1.00x faster                                          |
| tornado_http   | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| coroutines       | 23.6 ms                                                               | 23.0 ms: 1.03x faster                                          |
| asyncio_tcp_ssl  | 1.78 sec                                                              | 1.77 sec: 1.01x faster                                         |
| asyncio_tcp      | 471 ms                                                                | 472 ms: 1.00x slower                                           |
| async_generators | 431 ms                                                                | 434 ms: 1.01x slower                                           |
| async_tree_none  | 314 ms                                                                | 322 ms: 1.02x slower                                           |
| async_tree_io_tg | 875 ms                                                                | 916 ms: 1.05x slower                                           |
| async_tree_io    | 882 ms                                                                | 929 ms: 1.05x slower                                           |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                           |
| float          | 76.4 ms                                                               | 76.8 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                           |
| regex_v8       | 24.9 ms                                                               | 25.4 ms: 1.02x slower                                          |
| regex_dna      | 215 ms                                                                | 219 ms: 1.02x slower                                           |
| regex_effbot   | 3.55 ms                                                               | 3.69 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_dict          | 34.5 us                                                               | 33.4 us: 1.03x faster                                          |
| pickle_list          | 5.11 us                                                               | 4.96 us: 1.03x faster                                          |
| json_loads           | 26.8 us                                                               | 26.9 us: 1.00x slower                                          |
| xml_etree_process    | 58.9 ms                                                               | 59.2 ms: 1.01x slower                                          |
| xml_etree_generate   | 85.7 ms                                                               | 86.8 ms: 1.01x slower                                          |
| pickle_pure_python   | 300 us                                                                | 305 us: 1.02x slower                                           |
| pickle               | 11.5 us                                                               | 11.7 us: 1.02x slower                                          |
| unpickle_pure_python | 211 us                                                                | 216 us: 1.03x slower                                           |
| unpickle             | 14.9 us                                                               | 15.6 us: 1.05x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (5): json_dumps, tomli_loads, xml_etree_parse, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 7.01 ms: 1.00x slower                                          |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                               | 49.6 ms: 1.05x faster                                          |
| genshi_text    | 22.5 ms                                                               | 22.4 ms: 1.01x faster                                          |
| mako           | 11.1 ms                                                               | 11.0 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml               | 51.8 ms                                                               | 49.6 ms: 1.05x faster                                          |
| scimark_sparse_mat_mult  | 4.84 ms                                                               | 4.66 ms: 1.04x faster                                          |
| pickle_dict              | 34.5 us                                                               | 33.4 us: 1.03x faster                                          |
| pickle_list              | 5.11 us                                                               | 4.96 us: 1.03x faster                                          |
| coroutines               | 23.6 ms                                                               | 23.0 ms: 1.03x faster                                          |
| coverage                 | 86.3 ms                                                               | 84.8 ms: 1.02x faster                                          |
| scimark_sor              | 125 ms                                                                | 123 ms: 1.02x faster                                           |
| deepcopy_reduce          | 2.75 us                                                               | 2.71 us: 1.01x faster                                          |
| crypto_pyaes             | 72.3 ms                                                               | 71.5 ms: 1.01x faster                                          |
| scimark_lu               | 113 ms                                                                | 112 ms: 1.01x faster                                           |
| typing_runtime_protocols | 162 us                                                                | 161 us: 1.01x faster                                           |
| bpe_tokeniser            | 4.75 sec                                                              | 4.71 sec: 1.01x faster                                         |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.77 sec: 1.01x faster                                         |
| genshi_text              | 22.5 ms                                                               | 22.4 ms: 1.01x faster                                          |
| tornado_http             | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                          |
| dulwich_log              | 64.9 ms                                                               | 64.6 ms: 1.01x faster                                          |
| fannkuch                 | 400 ms                                                                | 398 ms: 1.01x faster                                           |
| mako                     | 11.1 ms                                                               | 11.0 ms: 1.00x faster                                          |
| html5lib                 | 61.6 ms                                                               | 61.4 ms: 1.00x faster                                          |
| bench_thread_pool        | 855 us                                                                | 853 us: 1.00x faster                                           |
| sqlglot_optimize         | 53.2 ms                                                               | 53.4 ms: 1.00x slower                                          |
| asyncio_tcp              | 471 ms                                                                | 472 ms: 1.00x slower                                           |
| python_startup_no_site   | 6.99 ms                                                               | 7.01 ms: 1.00x slower                                          |
| json_loads               | 26.8 us                                                               | 26.9 us: 1.00x slower                                          |
| generators               | 27.6 ms                                                               | 27.7 ms: 1.00x slower                                          |
| pprint_pformat           | 1.47 sec                                                              | 1.48 sec: 1.00x slower                                         |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                          |
| scimark_fft              | 359 ms                                                                | 360 ms: 1.00x slower                                           |
| pprint_safe_repr         | 717 ms                                                                | 721 ms: 1.00x slower                                           |
| sympy_integrate          | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                          |
| pidigits                 | 187 ms                                                                | 188 ms: 1.00x slower                                           |
| float                    | 76.4 ms                                                               | 76.8 ms: 1.01x slower                                          |
| xml_etree_process        | 58.9 ms                                                               | 59.2 ms: 1.01x slower                                          |
| spectral_norm            | 112 ms                                                                | 113 ms: 1.01x slower                                           |
| 2to3                     | 253 ms                                                                | 255 ms: 1.01x slower                                           |
| async_generators         | 431 ms                                                                | 434 ms: 1.01x slower                                           |
| docutils                 | 2.62 sec                                                              | 2.64 sec: 1.01x slower                                         |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                           |
| json                     | 5.07 ms                                                               | 5.12 ms: 1.01x slower                                          |
| chaos                    | 59.3 ms                                                               | 59.8 ms: 1.01x slower                                          |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                          |
| regex_compile            | 128 ms                                                                | 129 ms: 1.01x slower                                           |
| sqlglot_transpile        | 1.58 ms                                                               | 1.59 ms: 1.01x slower                                          |
| xml_etree_generate       | 85.7 ms                                                               | 86.8 ms: 1.01x slower                                          |
| comprehensions           | 16.4 us                                                               | 16.6 us: 1.01x slower                                          |
| gc_traversal             | 3.56 ms                                                               | 3.61 ms: 1.01x slower                                          |
| nqueens                  | 78.5 ms                                                               | 79.7 ms: 1.01x slower                                          |
| regex_v8                 | 24.9 ms                                                               | 25.4 ms: 1.02x slower                                          |
| pickle_pure_python       | 300 us                                                                | 305 us: 1.02x slower                                           |
| regex_dna                | 215 ms                                                                | 219 ms: 1.02x slower                                           |
| raytrace                 | 260 ms                                                                | 265 ms: 1.02x slower                                           |
| scimark_monte_carlo      | 66.9 ms                                                               | 68.2 ms: 1.02x slower                                          |
| pickle                   | 11.5 us                                                               | 11.7 us: 1.02x slower                                          |
| logging_simple           | 5.53 us                                                               | 5.65 us: 1.02x slower                                          |
| meteor_contest           | 105 ms                                                                | 107 ms: 1.02x slower                                           |
| hexiom                   | 6.08 ms                                                               | 6.22 ms: 1.02x slower                                          |
| logging_format           | 6.11 us                                                               | 6.26 us: 1.02x slower                                          |
| logging_silent           | 98.8 ns                                                               | 101 ns: 1.02x slower                                           |
| async_tree_none          | 314 ms                                                                | 322 ms: 1.02x slower                                           |
| unpickle_pure_python     | 211 us                                                                | 216 us: 1.03x slower                                           |
| deltablue                | 3.17 ms                                                               | 3.26 ms: 1.03x slower                                          |
| go                       | 117 ms                                                                | 120 ms: 1.03x slower                                           |
| pyflate                  | 461 ms                                                                | 476 ms: 1.03x slower                                           |
| deepcopy_memo            | 29.6 us                                                               | 30.5 us: 1.03x slower                                          |
| create_gc_cycles         | 1.72 ms                                                               | 1.77 ms: 1.03x slower                                          |
| telco                    | 7.88 ms                                                               | 8.16 ms: 1.04x slower                                          |
| regex_effbot             | 3.55 ms                                                               | 3.69 ms: 1.04x slower                                          |
| richards_super           | 51.4 ms                                                               | 53.5 ms: 1.04x slower                                          |
| async_tree_io_tg         | 875 ms                                                                | 916 ms: 1.05x slower                                           |
| unpickle                 | 14.9 us                                                               | 15.6 us: 1.05x slower                                          |
| richards                 | 45.2 ms                                                               | 47.4 ms: 1.05x slower                                          |
| async_tree_io            | 882 ms                                                                | 929 ms: 1.05x slower                                           |
| mdp                      | 2.51 sec                                                              | 2.71 sec: 1.08x slower                                         |
| unpack_sequence          | 47.9 ns                                                               | 57.9 ns: 1.21x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (23): async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, thrift, sympy_sum, json_dumps, pathlib, sqlite_synth, async_tree_none_tg, django_template, bench_mp_pool, deepcopy, tomli_loads, xml_etree_parse, nbody, xml_etree_iterparse, sympy_expand, unpickle_list, sympy_str, pylint, pycparser, async_tree_cpu_io_mixed, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x