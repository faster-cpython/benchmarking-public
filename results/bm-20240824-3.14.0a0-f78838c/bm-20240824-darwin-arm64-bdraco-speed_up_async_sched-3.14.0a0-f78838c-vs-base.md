# Results vs. base

- fork: bdraco
- ref: speed_up_async_sched
- machine: darwin-arm64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.00x slower
- HPT reliability: 61.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 158 ms                                                                | 160 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_memoization    | 155 ms                                                                | 151 ms: 1.03x faster                                                  |
| async_generators                | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| coroutines                      | 16.1 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| async_tree_eager                | 60.0 ms                                                               | 60.8 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg      | 457 ms                                                                | 465 ms: 1.02x slower                                                  |
| async_tree_eager_tg             | 41.5 ms                                                               | 42.2 ms: 1.02x slower                                                 |
| async_tree_eager_io_tg          | 714 ms                                                                | 742 ms: 1.04x slower                                                  |
| async_tree_eager_memoization_tg | 124 ms                                                                | 129 ms: 1.04x slower                                                  |
| async_tree_io_tg                | 566 ms                                                                | 606 ms: 1.07x slower                                                  |
| Geometric mean                  | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (12): async_tree_memoization_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_none, asyncio_tcp_ssl, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_eager_io, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.7 ms                                                               | 48.9 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 67.5 ms                                                               | 66.9 ms: 1.01x faster                                                 |
| regex_v8       | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| regex_dna      | 145 ms                                                                | 145 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python | 182 us                                                                | 181 us: 1.01x faster                                                  |
| xml_etree_generate | 53.1 ms                                                               | 53.2 ms: 1.00x slower                                                 |
| xml_etree_process  | 37.5 ms                                                               | 37.7 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (6): xml_etree_iterparse, xml_etree_parse, json_dumps, tomli_loads, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                               | 13.5 ms: 1.01x faster                                                 |
| python_startup         | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                 |
| genshi_xml     | 30.2 ms                                                               | 30.1 ms: 1.00x faster                                                 |
| mako           | 6.91 ms                                                               | 6.94 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                       | bm-20240824-darwin-arm64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_memoization    | 155 ms                                                                | 151 ms: 1.03x faster                                                  |
| python_startup_no_site          | 13.6 ms                                                               | 13.5 ms: 1.01x faster                                                 |
| deepcopy_memo                   | 17.0 us                                                               | 16.9 us: 1.01x faster                                                 |
| regex_compile                   | 67.5 ms                                                               | 66.9 ms: 1.01x faster                                                 |
| typing_runtime_protocols        | 91.6 us                                                               | 90.9 us: 1.01x faster                                                 |
| regex_v8                        | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| mdp                             | 1.44 sec                                                              | 1.43 sec: 1.01x faster                                                |
| logging_simple                  | 3.09 us                                                               | 3.07 us: 1.01x faster                                                 |
| fannkuch                        | 262 ms                                                                | 260 ms: 1.01x faster                                                  |
| pickle_pure_python              | 182 us                                                                | 181 us: 1.01x faster                                                  |
| genshi_text                     | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                 |
| python_startup                  | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| coverage                        | 44.5 ms                                                               | 44.3 ms: 1.00x faster                                                 |
| comprehensions                  | 9.97 us                                                               | 9.93 us: 1.00x faster                                                 |
| sympy_expand                    | 227 ms                                                                | 226 ms: 1.00x faster                                                  |
| sympy_integrate                 | 10.4 ms                                                               | 10.3 ms: 1.00x faster                                                 |
| genshi_xml                      | 30.2 ms                                                               | 30.1 ms: 1.00x faster                                                 |
| go                              | 106 ms                                                                | 106 ms: 1.00x faster                                                  |
| async_generators                | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| logging_format                  | 3.41 us                                                               | 3.40 us: 1.00x faster                                                 |
| sqlglot_parse                   | 741 us                                                                | 739 us: 1.00x faster                                                  |
| coroutines                      | 16.1 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| nqueens                         | 53.4 ms                                                               | 53.3 ms: 1.00x faster                                                 |
| regex_dna                       | 145 ms                                                                | 145 ms: 1.00x faster                                                  |
| xml_etree_generate              | 53.1 ms                                                               | 53.2 ms: 1.00x slower                                                 |
| crypto_pyaes                    | 50.8 ms                                                               | 50.9 ms: 1.00x slower                                                 |
| chaos                           | 35.6 ms                                                               | 35.7 ms: 1.00x slower                                                 |
| logging_silent                  | 61.1 ns                                                               | 61.2 ns: 1.00x slower                                                 |
| richards                        | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult         | 2.77 ms                                                               | 2.78 ms: 1.00x slower                                                 |
| scimark_monte_carlo             | 43.2 ms                                                               | 43.3 ms: 1.00x slower                                                 |
| bpe_tokeniser                   | 3.12 sec                                                              | 3.13 sec: 1.00x slower                                                |
| deltablue                       | 2.13 ms                                                               | 2.13 ms: 1.00x slower                                                 |
| scimark_fft                     | 184 ms                                                                | 185 ms: 1.00x slower                                                  |
| bench_thread_pool               | 448 us                                                                | 449 us: 1.00x slower                                                  |
| richards_super                  | 33.3 ms                                                               | 33.4 ms: 1.00x slower                                                 |
| float                           | 48.7 ms                                                               | 48.9 ms: 1.00x slower                                                 |
| mako                            | 6.91 ms                                                               | 6.94 ms: 1.00x slower                                                 |
| deepcopy_reduce                 | 1.50 us                                                               | 1.51 us: 1.01x slower                                                 |
| scimark_sor                     | 92.8 ms                                                               | 93.3 ms: 1.01x slower                                                 |
| dulwich_log                     | 26.9 ms                                                               | 27.1 ms: 1.01x slower                                                 |
| sympy_sum                       | 68.6 ms                                                               | 69.1 ms: 1.01x slower                                                 |
| xml_etree_process               | 37.5 ms                                                               | 37.7 ms: 1.01x slower                                                 |
| meteor_contest                  | 71.9 ms                                                               | 72.5 ms: 1.01x slower                                                 |
| 2to3                            | 158 ms                                                                | 160 ms: 1.01x slower                                                  |
| spectral_norm                   | 67.0 ms                                                               | 67.7 ms: 1.01x slower                                                 |
| pprint_pformat                  | 919 ms                                                                | 930 ms: 1.01x slower                                                  |
| async_tree_eager                | 60.0 ms                                                               | 60.8 ms: 1.01x slower                                                 |
| pprint_safe_repr                | 450 ms                                                                | 457 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg      | 457 ms                                                                | 465 ms: 1.02x slower                                                  |
| async_tree_eager_tg             | 41.5 ms                                                               | 42.2 ms: 1.02x slower                                                 |
| json                            | 2.95 ms                                                               | 3.01 ms: 1.02x slower                                                 |
| async_tree_eager_io_tg          | 714 ms                                                                | 742 ms: 1.04x slower                                                  |
| async_tree_eager_memoization_tg | 124 ms                                                                | 129 ms: 1.04x slower                                                  |
| async_tree_io_tg                | 566 ms                                                                | 606 ms: 1.07x slower                                                  |
| Geometric mean                  | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (43): async_tree_memoization_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, xml_etree_iterparse, thrift, async_tree_none, xml_etree_parse, django_template, asyncio_tcp_ssl, sqlglot_transpile, nbody, json_dumps, deepcopy, raytrace, bench_mp_pool, docutils, generators, gc_traversal, sqlglot_optimize, pycparser, pidigits, hexiom, sqlglot_normalize, regex_effbot, sympy_str, scimark_lu, html5lib, tomli_loads, json_loads, telco, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, pyflate, pathlib, pylint, create_gc_cycles, unpickle_pure_python, async_tree_none_tg, async_tree_io, async_tree_eager_io, asyncio_tcp, tornado_http

# HPT report

- Reliability score: 61.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x