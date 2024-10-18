# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.01x slower
- HPT reliability: 63.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 385 ms                                                                  | 375 ms: 1.03x faster                                             |
| docutils       | 3.74 sec                                                                | 3.67 sec: 1.02x faster                                           |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 557 ms                                                                  | 544 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 732 ms                                                                  | 718 ms: 1.02x faster                                             |
| async_generators           | 503 ms                                                                  | 510 ms: 1.01x slower                                             |
| async_tree_none            | 444 ms                                                                  | 455 ms: 1.02x slower                                             |
| async_tree_io              | 1.14 sec                                                                | 1.20 sec: 1.05x slower                                           |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (8): async_tree_memoization, coroutines, asyncio_websockets, async_tree_none_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 111 ms                                                                  | 110 ms: 1.01x faster                                             |
| float          | 89.5 ms                                                                 | 93.8 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 185 ms                                                                  | 176 ms: 1.05x faster                                             |
| regex_dna      | 253 ms                                                                  | 247 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                     |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process  | 81.3 ms                                                                 | 80.5 ms: 1.01x faster                                            |
| pickle_list        | 5.22 us                                                                 | 5.21 us: 1.00x faster                                            |
| xml_etree_generate | 111 ms                                                                  | 112 ms: 1.01x slower                                             |
| tomli_loads        | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                           |
| pickle_dict        | 37.7 us                                                                 | 38.2 us: 1.01x slower                                            |
| unpickle_list      | 6.43 us                                                                 | 6.60 us: 1.03x slower                                            |
| json_dumps         | 12.9 ms                                                                 | 13.4 ms: 1.03x slower                                            |
| Geometric mean     | (ref)                                                                   | 1.01x slower                                                     |

Benchmark hidden because not significant (7): xml_etree_parse, unpickle_pure_python, pickle_pure_python, xml_etree_iterparse, json_loads, unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 13.0 ms                                                                 | 14.7 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                                   | 1.06x slower                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.0 ms                                                                 | 12.9 ms: 1.01x faster                                            |
| django_template | 51.2 ms                                                                 | 52.3 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                                   | 1.01x slower                                                     |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| chaos                      | 90.8 ms                                                                 | 86.0 ms: 1.06x faster                                            |
| regex_compile              | 185 ms                                                                  | 176 ms: 1.05x faster                                             |
| sympy_sum                  | 218 ms                                                                  | 210 ms: 1.04x faster                                             |
| sqlglot_optimize           | 82.0 ms                                                                 | 79.2 ms: 1.04x faster                                            |
| sympy_str                  | 368 ms                                                                  | 355 ms: 1.03x faster                                             |
| typing_runtime_protocols   | 213 us                                                                  | 207 us: 1.03x faster                                             |
| regex_dna                  | 253 ms                                                                  | 247 ms: 1.03x faster                                             |
| 2to3                       | 385 ms                                                                  | 375 ms: 1.03x faster                                             |
| pprint_safe_repr           | 1.25 sec                                                                | 1.22 sec: 1.02x faster                                           |
| async_tree_memoization_tg  | 557 ms                                                                  | 544 ms: 1.02x faster                                             |
| pathlib                    | 22.0 ms                                                                 | 21.6 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed_tg | 732 ms                                                                  | 718 ms: 1.02x faster                                             |
| docutils                   | 3.74 sec                                                                | 3.67 sec: 1.02x faster                                           |
| crypto_pyaes               | 90.1 ms                                                                 | 88.5 ms: 1.02x faster                                            |
| deepcopy_reduce            | 3.89 us                                                                 | 3.83 us: 1.02x faster                                            |
| deepcopy_memo              | 38.3 us                                                                 | 37.7 us: 1.02x faster                                            |
| sqlglot_parse              | 1.71 ms                                                                 | 1.69 ms: 1.02x faster                                            |
| sympy_integrate            | 29.3 ms                                                                 | 28.9 ms: 1.01x faster                                            |
| pprint_pformat             | 2.64 sec                                                                | 2.60 sec: 1.01x faster                                           |
| unpack_sequence            | 149 ns                                                                  | 147 ns: 1.01x faster                                             |
| xml_etree_process          | 81.3 ms                                                                 | 80.5 ms: 1.01x faster                                            |
| nbody                      | 111 ms                                                                  | 110 ms: 1.01x faster                                             |
| nqueens                    | 122 ms                                                                  | 121 ms: 1.01x faster                                             |
| mako                       | 13.0 ms                                                                 | 12.9 ms: 1.01x faster                                            |
| sqlglot_normalize          | 155 ms                                                                  | 154 ms: 1.01x faster                                             |
| pickle_list                | 5.22 us                                                                 | 5.21 us: 1.00x faster                                            |
| xml_etree_generate         | 111 ms                                                                  | 112 ms: 1.01x slower                                             |
| tomli_loads                | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                           |
| pickle_dict                | 37.7 us                                                                 | 38.2 us: 1.01x slower                                            |
| comprehensions             | 24.6 us                                                                 | 24.9 us: 1.01x slower                                            |
| async_generators           | 503 ms                                                                  | 510 ms: 1.01x slower                                             |
| go                         | 186 ms                                                                  | 189 ms: 1.02x slower                                             |
| logging_silent             | 133 ns                                                                  | 135 ns: 1.02x slower                                             |
| django_template            | 51.2 ms                                                                 | 52.3 ms: 1.02x slower                                            |
| scimark_monte_carlo        | 88.8 ms                                                                 | 90.9 ms: 1.02x slower                                            |
| async_tree_none            | 444 ms                                                                  | 455 ms: 1.02x slower                                             |
| unpickle_list              | 6.43 us                                                                 | 6.60 us: 1.03x slower                                            |
| bpe_tokeniser              | 5.97 sec                                                                | 6.13 sec: 1.03x slower                                           |
| fannkuch                   | 502 ms                                                                  | 519 ms: 1.03x slower                                             |
| json_dumps                 | 12.9 ms                                                                 | 13.4 ms: 1.03x slower                                            |
| spectral_norm              | 146 ms                                                                  | 152 ms: 1.04x slower                                             |
| async_tree_io              | 1.14 sec                                                                | 1.20 sec: 1.05x slower                                           |
| coverage                   | 98.4 ms                                                                 | 103 ms: 1.05x slower                                             |
| float                      | 89.5 ms                                                                 | 93.8 ms: 1.05x slower                                            |
| richards                   | 65.2 ms                                                                 | 68.8 ms: 1.06x slower                                            |
| richards_super             | 71.7 ms                                                                 | 76.3 ms: 1.06x slower                                            |
| python_startup             | 13.0 ms                                                                 | 14.7 ms: 1.13x slower                                            |
| gc_traversal               | 5.06 ms                                                                 | 6.17 ms: 1.22x slower                                            |
| create_gc_cycles           | 2.28 ms                                                                 | 3.58 ms: 1.57x slower                                            |
| bench_mp_pool              | 2.04 sec                                                                | 3.29 sec: 1.61x slower                                           |
| Geometric mean             | (ref)                                                                   | 1.01x slower                                                     |

Benchmark hidden because not significant (47): dulwich_log, tornado_http, pylint, deepcopy, async_tree_memoization, coroutines, raytrace, regex_effbot, html5lib, telco, json, xml_etree_parse, scimark_sparse_mat_mult, pycparser, unpickle_pure_python, sqlglot_transpile, scimark_lu, thrift, pickle_pure_python, pyflate, scimark_sor, asyncio_websockets, mdp, sympy_expand, scimark_fft, xml_etree_iterparse, python_startup_no_site, async_tree_none_tg, generators, meteor_contest, asyncio_tcp_ssl, json_loads, unpickle, genshi_text, async_tree_cpu_io_mixed, logging_format, regex_v8, pidigits, sqlite_synth, asyncio_tcp, pickle, async_tree_io_tg, logging_simple, deltablue, hexiom, genshi_xml, bench_thread_pool
Ignored benchmarks (1) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx

# HPT report

- Reliability score: 63.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x