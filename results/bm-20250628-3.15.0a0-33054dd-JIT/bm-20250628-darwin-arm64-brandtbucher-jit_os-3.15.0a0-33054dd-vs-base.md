# Results vs. base

- fork: brandtbucher
- ref: jit_os
- machine: darwin-arm64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.001x faster
- HPT reliability: 97.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 175 ms                                                                | 174 ms: 1.01x faster                                          |
| html5lib       | 32.5 ms                                                               | 31.7 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_generators | 281 ms                                                                | 278 ms: 1.01x faster                                          |
| async_tree_eager | 64.1 ms                                                               | 64.5 ms: 1.00x slower                                         |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (17): async_tree_none, async_tree_io, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, coroutines, async_tree_eager_io, async_tree_eager_memoization, async_tree_eager_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 75.2 ms                                                               | 75.7 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                | 143 ms: 1.02x faster                                          |
| regex_effbot   | 2.37 ms                                                               | 2.34 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                  |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                        |
| pickle_pure_python   | 210 us                                                                | 211 us: 1.00x slower                                          |
| unpickle_pure_python | 134 us                                                                | 134 us: 1.00x slower                                          |
| xml_etree_generate   | 50.8 ms                                                               | 51.0 ms: 1.00x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (5): json_dumps, json_loads, xml_etree_iterparse, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 15.6 ms                                                               | 14.2 ms: 1.10x faster                                         |
| python_startup         | 20.2 ms                                                               | 18.7 ms: 1.08x faster                                         |
| Geometric mean         | (ref)                                                                 | 1.09x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako           | 6.95 ms                                                               | 6.99 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site  | 15.6 ms                                                               | 14.2 ms: 1.10x faster                                         |
| python_startup          | 20.2 ms                                                               | 18.7 ms: 1.08x faster                                         |
| html5lib                | 32.5 ms                                                               | 31.7 ms: 1.03x faster                                         |
| regex_dna               | 145 ms                                                                | 143 ms: 1.02x faster                                          |
| scimark_sparse_mat_mult | 3.56 ms                                                               | 3.51 ms: 1.01x faster                                         |
| async_generators        | 281 ms                                                                | 278 ms: 1.01x faster                                          |
| fannkuch                | 302 ms                                                                | 299 ms: 1.01x faster                                          |
| regex_effbot            | 2.37 ms                                                               | 2.34 ms: 1.01x faster                                         |
| telco                   | 4.60 ms                                                               | 4.55 ms: 1.01x faster                                         |
| pyflate                 | 295 ms                                                                | 292 ms: 1.01x faster                                          |
| tomli_loads             | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                        |
| coverage                | 48.3 ms                                                               | 47.9 ms: 1.01x faster                                         |
| 2to3                    | 175 ms                                                                | 174 ms: 1.01x faster                                          |
| scimark_fft             | 199 ms                                                                | 198 ms: 1.01x faster                                          |
| deepcopy                | 156 us                                                                | 156 us: 1.01x faster                                          |
| deepcopy_memo           | 19.6 us                                                               | 19.5 us: 1.00x faster                                         |
| spectral_norm           | 67.8 ms                                                               | 67.8 ms: 1.00x faster                                         |
| generators              | 24.0 ms                                                               | 24.1 ms: 1.00x slower                                         |
| scimark_sor             | 88.8 ms                                                               | 88.9 ms: 1.00x slower                                         |
| thrift                  | 442 us                                                                | 443 us: 1.00x slower                                          |
| sympy_expand            | 244 ms                                                                | 245 ms: 1.00x slower                                          |
| pickle_pure_python      | 210 us                                                                | 211 us: 1.00x slower                                          |
| unpickle_pure_python    | 134 us                                                                | 134 us: 1.00x slower                                          |
| xml_etree_generate      | 50.8 ms                                                               | 51.0 ms: 1.00x slower                                         |
| richards                | 36.4 ms                                                               | 36.5 ms: 1.00x slower                                         |
| create_gc_cycles        | 1.35 ms                                                               | 1.36 ms: 1.00x slower                                         |
| bpe_tokeniser           | 3.09 sec                                                              | 3.10 sec: 1.00x slower                                        |
| raytrace                | 179 ms                                                                | 179 ms: 1.00x slower                                          |
| async_tree_eager        | 64.1 ms                                                               | 64.5 ms: 1.00x slower                                         |
| nqueens                 | 61.4 ms                                                               | 61.7 ms: 1.01x slower                                         |
| gc_traversal            | 3.19 ms                                                               | 3.21 ms: 1.01x slower                                         |
| mako                    | 6.95 ms                                                               | 6.99 ms: 1.01x slower                                         |
| sympy_sum               | 75.6 ms                                                               | 76.0 ms: 1.01x slower                                         |
| sqlglot_v2_normalize    | 68.3 ms                                                               | 68.7 ms: 1.01x slower                                         |
| go                      | 87.5 ms                                                               | 88.1 ms: 1.01x slower                                         |
| sqlglot_v2_optimize     | 33.8 ms                                                               | 34.0 ms: 1.01x slower                                         |
| nbody                   | 75.2 ms                                                               | 75.7 ms: 1.01x slower                                         |
| hexiom                  | 4.72 ms                                                               | 4.75 ms: 1.01x slower                                         |
| scimark_lu              | 82.2 ms                                                               | 82.8 ms: 1.01x slower                                         |
| chaos                   | 39.4 ms                                                               | 39.7 ms: 1.01x slower                                         |
| crypto_pyaes            | 55.6 ms                                                               | 56.1 ms: 1.01x slower                                         |
| logging_format          | 3.75 us                                                               | 3.79 us: 1.01x slower                                         |
| comprehensions          | 12.1 us                                                               | 12.2 us: 1.01x slower                                         |
| sqlglot_v2_transpile    | 976 us                                                                | 989 us: 1.01x slower                                          |
| sqlglot_v2_parse        | 800 us                                                                | 811 us: 1.01x slower                                          |
| pprint_safe_repr        | 528 ms                                                                | 537 ms: 1.02x slower                                          |
| pathlib                 | 22.1 ms                                                               | 22.5 ms: 1.02x slower                                         |
| pprint_pformat          | 1.07 sec                                                              | 1.10 sec: 1.03x slower                                        |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (53): dulwich_log, logging_silent, json_dumps, docutils, pidigits, async_tree_none, sphinx, json_loads, pylint, shortest_path, scimark_monte_carlo, async_tree_io, async_tree_memoization, connected_components, async_tree_none_tg, regex_v8, asyncio_websockets, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, dask, xml_etree_iterparse, sympy_str, mdp, pycparser, genshi_text, deltablue, logging_simple, richards_super, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, django_template, async_tree_io_tg, sympy_integrate, regex_compile, sqlite_synth, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, deepcopy_reduce, coroutines, async_tree_eager_io, float, async_tree_eager_memoization, meteor_contest, many_optionals, xml_etree_parse, xml_etree_process, async_tree_eager_tg, genshi_xml, async_tree_eager_memoization_tg, json, typing_runtime_protocols, subparsers, k_core

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 97.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x