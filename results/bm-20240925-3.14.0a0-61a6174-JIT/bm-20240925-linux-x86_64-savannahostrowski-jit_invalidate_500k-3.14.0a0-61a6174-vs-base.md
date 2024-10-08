# Results vs. base

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.00x slower
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                                | 276 ms: 1.01x slower                                                            |
| html5lib       | 64.3 ms                                                               | 62.0 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 557 ms                                                                | 551 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                          |
| async_generators           | 454 ms                                                                | 460 ms: 1.01x slower                                                            |
| asyncio_tcp                | 487 ms                                                                | 497 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg, coroutines, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 82.1 ms                                                               | 81.4 ms: 1.01x faster                                                           |
| float          | 70.1 ms                                                               | 69.8 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 212 ms: 1.04x faster                                                            |
| regex_v8       | 25.5 ms                                                               | 24.8 ms: 1.03x faster                                                           |
| regex_effbot   | 3.65 ms                                                               | 3.70 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate  | 79.4 ms                                                               | 77.3 ms: 1.03x faster                                                           |
| unpickle_list       | 5.36 us                                                               | 5.27 us: 1.02x faster                                                           |
| xml_etree_process   | 55.7 ms                                                               | 54.8 ms: 1.02x faster                                                           |
| pickle_pure_python  | 307 us                                                                | 303 us: 1.01x faster                                                            |
| json_dumps          | 9.93 ms                                                               | 9.81 ms: 1.01x faster                                                           |
| tomli_loads         | 1.94 sec                                                              | 1.92 sec: 1.01x faster                                                          |
| xml_etree_iterparse | 98.4 ms                                                               | 98.7 ms: 1.00x slower                                                           |
| json_loads          | 26.9 us                                                               | 27.2 us: 1.01x slower                                                           |
| pickle_list         | 4.94 us                                                               | 5.11 us: 1.03x slower                                                           |
| pickle              | 11.3 us                                                               | 11.7 us: 1.03x slower                                                           |
| pickle_dict         | 33.3 us                                                               | 35.0 us: 1.05x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): unpickle_pure_python, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.06 ms: 1.00x faster                                                           |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.93 ms                                                               | 9.74 ms: 1.02x faster                                                           |
| django_template | 36.4 ms                                                               | 36.0 ms: 1.01x faster                                                           |
| genshi_text     | 24.5 ms                                                               | 24.8 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal               | 3.99 ms                                                               | 3.77 ms: 1.06x faster                                                           |
| regex_dna                  | 220 ms                                                                | 212 ms: 1.04x faster                                                            |
| html5lib                   | 64.3 ms                                                               | 62.0 ms: 1.04x faster                                                           |
| regex_v8                   | 25.5 ms                                                               | 24.8 ms: 1.03x faster                                                           |
| xml_etree_generate         | 79.4 ms                                                               | 77.3 ms: 1.03x faster                                                           |
| pycparser                  | 1.21 sec                                                              | 1.18 sec: 1.02x faster                                                          |
| mako                       | 9.93 ms                                                               | 9.74 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 4.48 ms                                                               | 4.40 ms: 1.02x faster                                                           |
| mdp                        | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                          |
| unpickle_list              | 5.36 us                                                               | 5.27 us: 1.02x faster                                                           |
| xml_etree_process          | 55.7 ms                                                               | 54.8 ms: 1.02x faster                                                           |
| pickle_pure_python         | 307 us                                                                | 303 us: 1.01x faster                                                            |
| json_dumps                 | 9.93 ms                                                               | 9.81 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 557 ms                                                                | 551 ms: 1.01x faster                                                            |
| django_template            | 36.4 ms                                                               | 36.0 ms: 1.01x faster                                                           |
| nbody                      | 82.1 ms                                                               | 81.4 ms: 1.01x faster                                                           |
| tomli_loads                | 1.94 sec                                                              | 1.92 sec: 1.01x faster                                                          |
| sqlite_synth               | 2.77 us                                                               | 2.75 us: 1.01x faster                                                           |
| float                      | 70.1 ms                                                               | 69.8 ms: 1.00x faster                                                           |
| create_gc_cycles           | 1.75 ms                                                               | 1.75 ms: 1.00x faster                                                           |
| python_startup_no_site     | 7.09 ms                                                               | 7.06 ms: 1.00x faster                                                           |
| python_startup             | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                          |
| xml_etree_iterparse        | 98.4 ms                                                               | 98.7 ms: 1.00x slower                                                           |
| pathlib                    | 15.9 ms                                                               | 15.9 ms: 1.00x slower                                                           |
| bench_thread_pool          | 840 us                                                                | 844 us: 1.00x slower                                                            |
| bpe_tokeniser              | 4.42 sec                                                              | 4.45 sec: 1.01x slower                                                          |
| telco                      | 7.91 ms                                                               | 7.96 ms: 1.01x slower                                                           |
| 2to3                       | 274 ms                                                                | 276 ms: 1.01x slower                                                            |
| pyflate                    | 436 ms                                                                | 439 ms: 1.01x slower                                                            |
| sympy_integrate            | 22.7 ms                                                               | 22.9 ms: 1.01x slower                                                           |
| dulwich_log                | 68.0 ms                                                               | 68.6 ms: 1.01x slower                                                           |
| coverage                   | 84.6 ms                                                               | 85.4 ms: 1.01x slower                                                           |
| scimark_lu                 | 110 ms                                                                | 111 ms: 1.01x slower                                                            |
| chaos                      | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 57.7 ms                                                               | 58.4 ms: 1.01x slower                                                           |
| json_loads                 | 26.9 us                                                               | 27.2 us: 1.01x slower                                                           |
| deltablue                  | 3.17 ms                                                               | 3.20 ms: 1.01x slower                                                           |
| hexiom                     | 6.89 ms                                                               | 6.97 ms: 1.01x slower                                                           |
| go                         | 131 ms                                                                | 133 ms: 1.01x slower                                                            |
| unpack_sequence            | 111 ns                                                                | 112 ns: 1.01x slower                                                            |
| logging_simple             | 5.58 us                                                               | 5.65 us: 1.01x slower                                                           |
| sympy_sum                  | 171 ms                                                                | 174 ms: 1.01x slower                                                            |
| sympy_expand               | 500 ms                                                                | 506 ms: 1.01x slower                                                            |
| genshi_text                | 24.5 ms                                                               | 24.8 ms: 1.01x slower                                                           |
| async_generators           | 454 ms                                                                | 460 ms: 1.01x slower                                                            |
| sympy_str                  | 296 ms                                                                | 300 ms: 1.01x slower                                                            |
| thrift                     | 776 us                                                                | 788 us: 1.01x slower                                                            |
| regex_effbot               | 3.65 ms                                                               | 3.70 ms: 1.01x slower                                                           |
| fannkuch                   | 371 ms                                                                | 377 ms: 1.02x slower                                                            |
| meteor_contest             | 106 ms                                                                | 108 ms: 1.02x slower                                                            |
| deepcopy_reduce            | 2.62 us                                                               | 2.67 us: 1.02x slower                                                           |
| crypto_pyaes               | 66.2 ms                                                               | 67.5 ms: 1.02x slower                                                           |
| asyncio_tcp                | 487 ms                                                                | 497 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 160 us                                                                | 164 us: 1.02x slower                                                            |
| spectral_norm              | 101 ms                                                                | 104 ms: 1.02x slower                                                            |
| richards_super             | 45.7 ms                                                               | 46.9 ms: 1.02x slower                                                           |
| richards                   | 40.1 ms                                                               | 41.1 ms: 1.03x slower                                                           |
| deepcopy_memo              | 26.6 us                                                               | 27.4 us: 1.03x slower                                                           |
| pickle_list                | 4.94 us                                                               | 5.11 us: 1.03x slower                                                           |
| comprehensions             | 16.5 us                                                               | 17.0 us: 1.03x slower                                                           |
| pickle                     | 11.3 us                                                               | 11.7 us: 1.03x slower                                                           |
| nqueens                    | 85.2 ms                                                               | 88.5 ms: 1.04x slower                                                           |
| json                       | 4.96 ms                                                               | 5.17 ms: 1.04x slower                                                           |
| pickle_dict                | 33.3 us                                                               | 35.0 us: 1.05x slower                                                           |
| generators                 | 32.9 ms                                                               | 34.9 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (31): async_tree_cpu_io_mixed, scimark_sor, unpickle_pure_python, unpickle, async_tree_memoization_tg, pprint_safe_repr, regex_compile, sqlglot_normalize, scimark_fft, logging_silent, docutils, tornado_http, scimark_monte_carlo, asyncio_websockets, pidigits, xml_etree_parse, bench_mp_pool, async_tree_io_tg, raytrace, sqlglot_parse, coroutines, logging_format, sqlglot_transpile, pprint_pformat, async_tree_io, async_tree_none_tg, genshi_xml, async_tree_memoization, deepcopy, async_tree_none, pylint

# HPT report

- Reliability score: 99.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x