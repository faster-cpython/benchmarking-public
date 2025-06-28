# Results vs. base

- fork: brandtbucher
- ref: jit_nops
- machine: darwin-arm64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.000x slower
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 172 ms                                                                | 173 ms: 1.01x slower                                            |
| docutils       | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators       | 280 ms                                                                | 277 ms: 1.01x faster                                            |
| async_tree_memoization | 194 ms                                                                | 197 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (17): async_tree_io, async_tree_cpu_io_mixed, coroutines, async_tree_none, async_tree_memoization_tg, async_tree_eager, async_tree_eager_memoization, async_tree_eager_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 283 ms                                                                | 284 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.37 ms                                                               | 2.34 ms: 1.01x faster                                           |
| regex_v8       | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                           |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x faster                                            |
| regex_compile  | 71.1 ms                                                               | 71.5 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse    | 102 ms                                                                | 101 ms: 1.02x faster                                            |
| xml_etree_generate | 50.9 ms                                                               | 50.7 ms: 1.00x faster                                           |
| xml_etree_process  | 35.6 ms                                                               | 35.5 ms: 1.00x faster                                           |
| tomli_loads        | 1.23 sec                                                              | 1.24 sec: 1.01x slower                                          |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_loads, pickle_pure_python, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                               | 18.3 ms: 1.01x faster                                           |
| python_startup_no_site | 13.8 ms                                                               | 13.8 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.8 ms                                                               | 21.9 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pprint_safe_repr        | 537 ms                                                                | 527 ms: 1.02x faster                                            |
| xml_etree_parse         | 102 ms                                                                | 101 ms: 1.02x faster                                            |
| telco                   | 4.61 ms                                                               | 4.55 ms: 1.01x faster                                           |
| python_startup          | 18.5 ms                                                               | 18.3 ms: 1.01x faster                                           |
| regex_effbot            | 2.37 ms                                                               | 2.34 ms: 1.01x faster                                           |
| fannkuch                | 302 ms                                                                | 299 ms: 1.01x faster                                            |
| async_generators        | 280 ms                                                                | 277 ms: 1.01x faster                                            |
| json                    | 2.94 ms                                                               | 2.91 ms: 1.01x faster                                           |
| gc_traversal            | 3.22 ms                                                               | 3.19 ms: 1.01x faster                                           |
| regex_v8                | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                           |
| create_gc_cycles        | 1.37 ms                                                               | 1.36 ms: 1.01x faster                                           |
| chaos                   | 39.5 ms                                                               | 39.2 ms: 1.01x faster                                           |
| python_startup_no_site  | 13.8 ms                                                               | 13.8 ms: 1.00x faster                                           |
| xml_etree_generate      | 50.9 ms                                                               | 50.7 ms: 1.00x faster                                           |
| dulwich_log             | 25.1 ms                                                               | 25.0 ms: 1.00x faster                                           |
| regex_dna               | 143 ms                                                                | 143 ms: 1.00x faster                                            |
| logging_silent          | 72.5 ns                                                               | 72.3 ns: 1.00x faster                                           |
| thrift                  | 443 us                                                                | 442 us: 1.00x faster                                            |
| xml_etree_process       | 35.6 ms                                                               | 35.5 ms: 1.00x faster                                           |
| spectral_norm           | 67.9 ms                                                               | 67.8 ms: 1.00x faster                                           |
| scimark_sor             | 89.2 ms                                                               | 89.0 ms: 1.00x faster                                           |
| pidigits                | 283 ms                                                                | 284 ms: 1.00x slower                                            |
| deepcopy                | 155 us                                                                | 156 us: 1.00x slower                                            |
| sqlglot_v2_transpile    | 977 us                                                                | 980 us: 1.00x slower                                            |
| sqlglot_v2_parse        | 800 us                                                                | 802 us: 1.00x slower                                            |
| scimark_lu              | 82.0 ms                                                               | 82.3 ms: 1.00x slower                                           |
| scimark_fft             | 199 ms                                                                | 200 ms: 1.00x slower                                            |
| bpe_tokeniser           | 3.08 sec                                                              | 3.09 sec: 1.00x slower                                          |
| scimark_sparse_mat_mult | 3.54 ms                                                               | 3.55 ms: 1.00x slower                                           |
| nqueens                 | 61.5 ms                                                               | 61.9 ms: 1.01x slower                                           |
| shortest_path           | 337 ms                                                                | 338 ms: 1.01x slower                                            |
| sqlglot_v2_optimize     | 33.9 ms                                                               | 34.1 ms: 1.01x slower                                           |
| tomli_loads             | 1.23 sec                                                              | 1.24 sec: 1.01x slower                                          |
| regex_compile           | 71.1 ms                                                               | 71.5 ms: 1.01x slower                                           |
| django_template         | 21.8 ms                                                               | 21.9 ms: 1.01x slower                                           |
| sqlglot_v2_normalize    | 68.5 ms                                                               | 69.0 ms: 1.01x slower                                           |
| comprehensions          | 12.1 us                                                               | 12.1 us: 1.01x slower                                           |
| many_optionals          | 476 us                                                                | 479 us: 1.01x slower                                            |
| crypto_pyaes            | 55.6 ms                                                               | 56.0 ms: 1.01x slower                                           |
| 2to3                    | 172 ms                                                                | 173 ms: 1.01x slower                                            |
| docutils                | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                          |
| hexiom                  | 4.72 ms                                                               | 4.77 ms: 1.01x slower                                           |
| pathlib                 | 21.9 ms                                                               | 22.2 ms: 1.02x slower                                           |
| richards                | 35.8 ms                                                               | 36.5 ms: 1.02x slower                                           |
| async_tree_memoization  | 194 ms                                                                | 197 ms: 1.02x slower                                            |
| richards_super          | 39.9 ms                                                               | 41.2 ms: 1.03x slower                                           |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (55): pprint_pformat, sympy_sum, async_tree_io, xml_etree_iterparse, genshi_text, mdp, json_loads, sympy_integrate, async_tree_cpu_io_mixed, float, nbody, coroutines, meteor_contest, pyflate, connected_components, async_tree_none, dask, pylint, deltablue, async_tree_memoization_tg, deepcopy_memo, typing_runtime_protocols, async_tree_eager, mako, async_tree_eager_memoization, sympy_expand, async_tree_eager_io, async_tree_cpu_io_mixed_tg, go, deepcopy_reduce, raytrace, generators, k_core, coverage, asyncio_websockets, sympy_str, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, pickle_pure_python, logging_format, async_tree_eager_io_tg, scimark_monte_carlo, sqlite_synth, async_tree_eager_tg, json_dumps, unpickle_pure_python, logging_simple, async_tree_none_tg, genshi_xml, async_tree_eager_memoization_tg, sphinx, html5lib, async_tree_io_tg, subparsers, pycparser

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 99.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x