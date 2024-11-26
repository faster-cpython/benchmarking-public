# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.011x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 278 ms: 1.00x faster                                           |
| docutils       | 2.96 sec                                                              | 2.94 sec: 1.01x faster                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 424 ms                                                                | 406 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed_tg | 570 ms                                                                | 551 ms: 1.03x faster                                           |
| async_tree_none            | 329 ms                                                                | 319 ms: 1.03x faster                                           |
| asyncio_tcp                | 498 ms                                                                | 493 ms: 1.01x faster                                           |
| async_generators           | 454 ms                                                                | 457 ms: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                               | 23.0 ms: 1.02x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, asyncio_tcp_ssl, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 74.2 ms                                                               | 71.9 ms: 1.03x faster                                          |
| nbody          | 81.6 ms                                                               | 80.1 ms: 1.02x faster                                          |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                | 227 ms: 1.03x faster                                           |
| regex_v8       | 27.0 ms                                                               | 26.4 ms: 1.02x faster                                          |
| regex_effbot   | 3.75 ms                                                               | 3.68 ms: 1.02x faster                                          |
| regex_compile  | 138 ms                                                                | 143 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.7 us: 1.05x faster                                          |
| xml_etree_parse      | 148 ms                                                                | 145 ms: 1.02x faster                                           |
| xml_etree_iterparse  | 99.9 ms                                                               | 98.2 ms: 1.02x faster                                          |
| pickle_pure_python   | 307 us                                                                | 302 us: 1.01x faster                                           |
| tomli_loads          | 1.96 sec                                                              | 1.93 sec: 1.01x faster                                         |
| xml_etree_process    | 55.1 ms                                                               | 54.7 ms: 1.01x faster                                          |
| pickle_list          | 5.09 us                                                               | 5.13 us: 1.01x slower                                          |
| unpickle_pure_python | 213 us                                                                | 216 us: 1.02x slower                                           |
| unpickle_list        | 5.19 us                                                               | 5.29 us: 1.02x slower                                          |
| json_loads           | 26.5 us                                                               | 27.0 us: 1.02x slower                                          |
| pickle_dict          | 34.7 us                                                               | 35.5 us: 1.02x slower                                          |
| json_dumps           | 9.85 ms                                                               | 10.2 ms: 1.04x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (2): pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                               | 10.6 ms: 1.13x faster                                          |
| python_startup_no_site | 7.08 ms                                                               | 7.10 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.06x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 58.8 ms                                                               | 58.2 ms: 1.01x faster                                          |
| mako           | 9.92 ms                                                               | 9.94 ms: 1.00x slower                                          |
| genshi_text    | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| create_gc_cycles           | 2.60 ms                                                               | 1.73 ms: 1.50x faster                                          |
| bench_mp_pool              | 84.5 ms                                                               | 61.3 ms: 1.38x faster                                          |
| gc_traversal               | 4.47 ms                                                               | 3.75 ms: 1.19x faster                                          |
| python_startup             | 11.9 ms                                                               | 10.6 ms: 1.13x faster                                          |
| spectral_norm              | 111 ms                                                                | 102 ms: 1.09x faster                                           |
| unpickle                   | 15.4 us                                                               | 14.7 us: 1.05x faster                                          |
| async_tree_memoization     | 424 ms                                                                | 406 ms: 1.04x faster                                           |
| richards                   | 42.8 ms                                                               | 41.0 ms: 1.04x faster                                          |
| richards_super             | 47.4 ms                                                               | 45.8 ms: 1.04x faster                                          |
| deepcopy                   | 272 us                                                                | 263 us: 1.04x faster                                           |
| async_tree_cpu_io_mixed_tg | 570 ms                                                                | 551 ms: 1.03x faster                                           |
| async_tree_none            | 329 ms                                                                | 319 ms: 1.03x faster                                           |
| float                      | 74.2 ms                                                               | 71.9 ms: 1.03x faster                                          |
| regex_dna                  | 234 ms                                                                | 227 ms: 1.03x faster                                           |
| nqueens                    | 88.0 ms                                                               | 85.8 ms: 1.03x faster                                          |
| regex_v8                   | 27.0 ms                                                               | 26.4 ms: 1.02x faster                                          |
| nbody                      | 81.6 ms                                                               | 80.1 ms: 1.02x faster                                          |
| regex_effbot               | 3.75 ms                                                               | 3.68 ms: 1.02x faster                                          |
| scimark_fft                | 311 ms                                                                | 305 ms: 1.02x faster                                           |
| typing_runtime_protocols   | 166 us                                                                | 163 us: 1.02x faster                                           |
| raytrace                   | 281 ms                                                                | 276 ms: 1.02x faster                                           |
| xml_etree_parse            | 148 ms                                                                | 145 ms: 1.02x faster                                           |
| xml_etree_iterparse        | 99.9 ms                                                               | 98.2 ms: 1.02x faster                                          |
| sqlglot_optimize           | 60.9 ms                                                               | 59.9 ms: 1.02x faster                                          |
| json                       | 5.03 ms                                                               | 4.96 ms: 1.01x faster                                          |
| pickle_pure_python         | 307 us                                                                | 302 us: 1.01x faster                                           |
| tomli_loads                | 1.96 sec                                                              | 1.93 sec: 1.01x faster                                         |
| genshi_xml                 | 58.8 ms                                                               | 58.2 ms: 1.01x faster                                          |
| pycparser                  | 1.23 sec                                                              | 1.21 sec: 1.01x faster                                         |
| logging_simple             | 5.72 us                                                               | 5.67 us: 1.01x faster                                          |
| asyncio_tcp                | 498 ms                                                                | 493 ms: 1.01x faster                                           |
| docutils                   | 2.96 sec                                                              | 2.94 sec: 1.01x faster                                         |
| sqlite_synth               | 2.76 us                                                               | 2.73 us: 1.01x faster                                          |
| logging_format             | 6.25 us                                                               | 6.19 us: 1.01x faster                                          |
| fannkuch                   | 377 ms                                                                | 374 ms: 1.01x faster                                           |
| sqlglot_normalize          | 116 ms                                                                | 115 ms: 1.01x faster                                           |
| scimark_lu                 | 111 ms                                                                | 110 ms: 1.01x faster                                           |
| xml_etree_process          | 55.1 ms                                                               | 54.7 ms: 1.01x faster                                          |
| pathlib                    | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                          |
| pidigits                   | 186 ms                                                                | 185 ms: 1.00x faster                                           |
| sympy_str                  | 302 ms                                                                | 300 ms: 1.00x faster                                           |
| 2to3                       | 280 ms                                                                | 278 ms: 1.00x faster                                           |
| bpe_tokeniser              | 4.48 sec                                                              | 4.47 sec: 1.00x faster                                         |
| sympy_expand               | 500 ms                                                                | 499 ms: 1.00x faster                                           |
| mako                       | 9.92 ms                                                               | 9.94 ms: 1.00x slower                                          |
| python_startup_no_site     | 7.08 ms                                                               | 7.10 ms: 1.00x slower                                          |
| meteor_contest             | 107 ms                                                                | 108 ms: 1.01x slower                                           |
| async_generators           | 454 ms                                                                | 457 ms: 1.01x slower                                           |
| sympy_sum                  | 176 ms                                                                | 177 ms: 1.01x slower                                           |
| pickle_list                | 5.09 us                                                               | 5.13 us: 1.01x slower                                          |
| deepcopy_reduce            | 2.63 us                                                               | 2.66 us: 1.01x slower                                          |
| crypto_pyaes               | 66.6 ms                                                               | 67.4 ms: 1.01x slower                                          |
| comprehensions             | 16.8 us                                                               | 17.0 us: 1.01x slower                                          |
| coverage                   | 84.6 ms                                                               | 85.8 ms: 1.01x slower                                          |
| scimark_sor                | 117 ms                                                                | 118 ms: 1.01x slower                                           |
| thrift                     | 780 us                                                                | 790 us: 1.01x slower                                           |
| deepcopy_memo              | 26.7 us                                                               | 27.1 us: 1.02x slower                                          |
| unpickle_pure_python       | 213 us                                                                | 216 us: 1.02x slower                                           |
| unpickle_list              | 5.19 us                                                               | 5.29 us: 1.02x slower                                          |
| json_loads                 | 26.5 us                                                               | 27.0 us: 1.02x slower                                          |
| go                         | 131 ms                                                                | 134 ms: 1.02x slower                                           |
| pickle_dict                | 34.7 us                                                               | 35.5 us: 1.02x slower                                          |
| coroutines                 | 22.5 ms                                                               | 23.0 ms: 1.02x slower                                          |
| dulwich_log                | 66.8 ms                                                               | 68.5 ms: 1.03x slower                                          |
| scimark_monte_carlo        | 62.4 ms                                                               | 64.0 ms: 1.03x slower                                          |
| genshi_text                | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                          |
| regex_compile              | 138 ms                                                                | 143 ms: 1.03x slower                                           |
| chaos                      | 58.7 ms                                                               | 60.7 ms: 1.03x slower                                          |
| json_dumps                 | 9.85 ms                                                               | 10.2 ms: 1.04x slower                                          |
| unpack_sequence            | 105 ns                                                                | 110 ns: 1.05x slower                                           |
| pyflate                    | 434 ms                                                                | 457 ms: 1.05x slower                                           |
| mdp                        | 2.55 sec                                                              | 2.71 sec: 1.06x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (25): pylint, pprint_pformat, html5lib, pickle, telco, async_tree_io_tg, deltablue, pprint_safe_repr, xml_etree_generate, async_tree_memoization_tg, sympy_integrate, asyncio_websockets, asyncio_tcp_ssl, sqlglot_transpile, sqlglot_parse, generators, async_tree_io, bench_thread_pool, tornado_http, scimark_sparse_mat_mult, hexiom, django_template, logging_silent, async_tree_none_tg, async_tree_cpu_io_mixed
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x