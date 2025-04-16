# Results vs. base

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 1196dc5
- commit date: 2025-04-16
- overall geometric mean: 1.005x slower
- HPT reliability: 84.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 250 ms: 1.01x faster                                                      |
| docutils       | 2.61 sec                                                               | 2.59 sec: 1.01x faster                                                    |
| html5lib       | 61.0 ms                                                                | 62.6 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators          | 398 ms                                                                 | 400 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed   | 480 ms                                                                 | 485 ms: 1.01x slower                                                      |
| async_tree_none           | 258 ms                                                                 | 263 ms: 1.02x slower                                                      |
| async_tree_io             | 610 ms                                                                 | 624 ms: 1.02x slower                                                      |
| async_tree_memoization    | 310 ms                                                                 | 318 ms: 1.03x slower                                                      |
| async_tree_none_tg        | 246 ms                                                                 | 253 ms: 1.03x slower                                                      |
| async_tree_memoization_tg | 311 ms                                                                 | 320 ms: 1.03x slower                                                      |
| Geometric mean            | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (4): asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 194 ms: 1.02x slower                                                      |
| nbody          | 93.7 ms                                                                | 96.6 ms: 1.03x slower                                                     |
| float          | 69.1 ms                                                                | 73.0 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.9 ms                                                                | 22.6 ms: 1.01x faster                                                     |
| regex_effbot   | 3.29 ms                                                                | 3.25 ms: 1.01x faster                                                     |
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                      |
| regex_dna      | 206 ms                                                                 | 212 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 86.2 ms                                                                | 84.1 ms: 1.02x faster                                                     |
| xml_etree_process    | 59.7 ms                                                                | 58.7 ms: 1.02x faster                                                     |
| json_loads           | 29.7 us                                                                | 29.4 us: 1.01x faster                                                     |
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                     |
| xml_etree_parse      | 142 ms                                                                 | 141 ms: 1.01x faster                                                      |
| unpickle_pure_python | 219 us                                                                 | 231 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_iterparse, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                     |
| python_startup_no_site | 8.22 ms                                                                | 8.24 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 11.5 ms                                                                | 11.0 ms: 1.05x faster                                                     |
| genshi_text    | 21.1 ms                                                                | 21.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators                | 30.6 ms                                                                | 29.3 ms: 1.05x faster                                                     |
| mako                      | 11.5 ms                                                                | 11.0 ms: 1.05x faster                                                     |
| logging_silent            | 102 ns                                                                 | 98.5 ns: 1.03x faster                                                     |
| scimark_sparse_mat_mult   | 4.88 ms                                                                | 4.74 ms: 1.03x faster                                                     |
| xml_etree_generate        | 86.2 ms                                                                | 84.1 ms: 1.02x faster                                                     |
| coverage                  | 88.4 ms                                                                | 86.3 ms: 1.02x faster                                                     |
| deepcopy_reduce           | 2.69 us                                                                | 2.63 us: 1.02x faster                                                     |
| richards_super            | 49.3 ms                                                                | 48.3 ms: 1.02x faster                                                     |
| mdp                       | 1.22 sec                                                               | 1.20 sec: 1.02x faster                                                    |
| xml_etree_process         | 59.7 ms                                                                | 58.7 ms: 1.02x faster                                                     |
| richards                  | 42.9 ms                                                                | 42.2 ms: 1.02x faster                                                     |
| subparsers                | 20.8 ms                                                                | 20.4 ms: 1.02x faster                                                     |
| scimark_lu                | 120 ms                                                                 | 118 ms: 1.01x faster                                                      |
| regex_v8                  | 22.9 ms                                                                | 22.6 ms: 1.01x faster                                                     |
| json                      | 5.33 ms                                                                | 5.25 ms: 1.01x faster                                                     |
| scimark_monte_carlo       | 66.3 ms                                                                | 65.6 ms: 1.01x faster                                                     |
| regex_effbot              | 3.29 ms                                                                | 3.25 ms: 1.01x faster                                                     |
| json_loads                | 29.7 us                                                                | 29.4 us: 1.01x faster                                                     |
| 2to3                      | 252 ms                                                                 | 250 ms: 1.01x faster                                                      |
| docutils                  | 2.61 sec                                                               | 2.59 sec: 1.01x faster                                                    |
| deepcopy_memo             | 28.6 us                                                                | 28.4 us: 1.01x faster                                                     |
| json_dumps                | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                     |
| bpe_tokeniser             | 4.60 sec                                                               | 4.57 sec: 1.01x faster                                                    |
| xml_etree_parse           | 142 ms                                                                 | 141 ms: 1.01x faster                                                      |
| sympy_expand              | 451 ms                                                                 | 448 ms: 1.01x faster                                                      |
| sympy_sum                 | 149 ms                                                                 | 148 ms: 1.00x faster                                                      |
| sqlalchemy_imperative     | 16.9 ms                                                                | 16.8 ms: 1.00x faster                                                     |
| fannkuch                  | 416 ms                                                                 | 415 ms: 1.00x faster                                                      |
| sqlalchemy_declarative    | 132 ms                                                                 | 132 ms: 1.00x faster                                                      |
| python_startup            | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                     |
| sqlglot_v2_optimize       | 52.1 ms                                                                | 52.2 ms: 1.00x slower                                                     |
| python_startup_no_site    | 8.22 ms                                                                | 8.24 ms: 1.00x slower                                                     |
| many_optionals            | 929 us                                                                 | 932 us: 1.00x slower                                                      |
| dulwich_log               | 59.8 ms                                                                | 60.0 ms: 1.00x slower                                                     |
| gc_traversal              | 5.03 ms                                                                | 5.05 ms: 1.00x slower                                                     |
| hexiom                    | 6.22 ms                                                                | 6.24 ms: 1.00x slower                                                     |
| create_gc_cycles          | 2.47 ms                                                                | 2.48 ms: 1.00x slower                                                     |
| async_generators          | 398 ms                                                                 | 400 ms: 1.01x slower                                                      |
| regex_compile             | 126 ms                                                                 | 127 ms: 1.01x slower                                                      |
| sqlglot_v2_parse          | 1.24 ms                                                                | 1.25 ms: 1.01x slower                                                     |
| sqlglot_v2_transpile      | 1.56 ms                                                                | 1.57 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed   | 480 ms                                                                 | 485 ms: 1.01x slower                                                      |
| connected_components      | 450 ms                                                                 | 455 ms: 1.01x slower                                                      |
| shortest_path             | 494 ms                                                                 | 499 ms: 1.01x slower                                                      |
| typing_runtime_protocols  | 164 us                                                                 | 166 us: 1.01x slower                                                      |
| pprint_pformat            | 1.45 sec                                                               | 1.47 sec: 1.02x slower                                                    |
| telco                     | 7.67 ms                                                                | 7.79 ms: 1.02x slower                                                     |
| go                        | 111 ms                                                                 | 113 ms: 1.02x slower                                                      |
| pprint_safe_repr          | 714 ms                                                                 | 726 ms: 1.02x slower                                                      |
| pathlib                   | 16.6 ms                                                                | 16.9 ms: 1.02x slower                                                     |
| pidigits                  | 190 ms                                                                 | 194 ms: 1.02x slower                                                      |
| async_tree_none           | 258 ms                                                                 | 263 ms: 1.02x slower                                                      |
| sympy_integrate           | 19.0 ms                                                                | 19.4 ms: 1.02x slower                                                     |
| async_tree_io             | 610 ms                                                                 | 624 ms: 1.02x slower                                                      |
| html5lib                  | 61.0 ms                                                                | 62.6 ms: 1.03x slower                                                     |
| regex_dna                 | 206 ms                                                                 | 212 ms: 1.03x slower                                                      |
| async_tree_memoization    | 310 ms                                                                 | 318 ms: 1.03x slower                                                      |
| logging_format            | 5.95 us                                                                | 6.12 us: 1.03x slower                                                     |
| async_tree_none_tg        | 246 ms                                                                 | 253 ms: 1.03x slower                                                      |
| async_tree_memoization_tg | 311 ms                                                                 | 320 ms: 1.03x slower                                                      |
| nbody                     | 93.7 ms                                                                | 96.6 ms: 1.03x slower                                                     |
| genshi_text               | 21.1 ms                                                                | 21.8 ms: 1.03x slower                                                     |
| logging_simple            | 5.41 us                                                                | 5.62 us: 1.04x slower                                                     |
| pyflate                   | 435 ms                                                                 | 452 ms: 1.04x slower                                                      |
| unpickle_pure_python      | 219 us                                                                 | 231 us: 1.06x slower                                                      |
| float                     | 69.1 ms                                                                | 73.0 ms: 1.06x slower                                                     |
| chaos                     | 55.6 ms                                                                | 60.7 ms: 1.09x slower                                                     |
| raytrace                  | 263 ms                                                                 | 293 ms: 1.11x slower                                                      |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (27): bench_mp_pool, xml_etree_iterparse, deepcopy, tomli_loads, k_core, django_template, genshi_xml, scimark_fft, bench_thread_pool, sphinx, meteor_contest, pickle_pure_python, pycparser, deltablue, sympy_str, nqueens, comprehensions, asyncio_websockets, crypto_pyaes, scimark_sor, coroutines, sqlglot_v2_normalize, pylint, sqlite_synth, async_tree_cpu_io_mixed_tg, spectral_norm, async_tree_io_tg

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 84.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x