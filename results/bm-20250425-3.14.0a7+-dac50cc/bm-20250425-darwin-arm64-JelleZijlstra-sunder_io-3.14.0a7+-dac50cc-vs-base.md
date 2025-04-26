# Results vs. base

- fork: JelleZijlstra
- ref: sunder_io
- machine: darwin-arm64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.000x slower
- HPT reliability: 73.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_generators | 247 ms                                                                 | 246 ms: 1.01x faster                                               |
| coroutines       | 16.3 ms                                                                | 16.3 ms: 1.00x faster                                              |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (17): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_memoization, async_tree_eager_io_tg, async_tree_none, async_tree_io_tg, async_tree_eager, async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 141 ms                                                                 | 140 ms: 1.00x faster                                               |
| regex_effbot   | 2.23 ms                                                                | 2.26 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 202 us                                                                 | 201 us: 1.01x faster                                               |
| json_loads           | 17.7 us                                                                | 17.6 us: 1.00x faster                                              |
| unpickle_pure_python | 143 us                                                                 | 143 us: 1.00x faster                                               |
| json_dumps           | 7.34 ms                                                                | 7.37 ms: 1.00x slower                                              |
| xml_etree_generate   | 53.0 ms                                                                | 53.5 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                                | 14.7 ms: 1.07x faster                                              |
| python_startup         | 20.0 ms                                                                | 19.9 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 28.6 ms                                                                | 28.4 ms: 1.01x faster                                              |
| genshi_text    | 13.7 ms                                                                | 13.6 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20250425-darwin-arm64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site  | 15.8 ms                                                                | 14.7 ms: 1.07x faster                                              |
| genshi_xml              | 28.6 ms                                                                | 28.4 ms: 1.01x faster                                              |
| pickle_pure_python      | 202 us                                                                 | 201 us: 1.01x faster                                               |
| async_generators        | 247 ms                                                                 | 246 ms: 1.01x faster                                               |
| logging_simple          | 3.29 us                                                                | 3.28 us: 1.01x faster                                              |
| json_loads              | 17.7 us                                                                | 17.6 us: 1.00x faster                                              |
| fannkuch                | 261 ms                                                                 | 260 ms: 1.00x faster                                               |
| genshi_text             | 13.7 ms                                                                | 13.6 ms: 1.00x faster                                              |
| python_startup          | 20.0 ms                                                                | 19.9 ms: 1.00x faster                                              |
| sqlalchemy_declarative  | 58.6 ms                                                                | 58.4 ms: 1.00x faster                                              |
| sqlglot_v2_parse        | 768 us                                                                 | 766 us: 1.00x faster                                               |
| sqlglot_v2_normalize    | 64.7 ms                                                                | 64.6 ms: 1.00x faster                                              |
| gc_traversal            | 3.11 ms                                                                | 3.10 ms: 1.00x faster                                              |
| unpickle_pure_python    | 143 us                                                                 | 143 us: 1.00x faster                                               |
| regex_dna               | 141 ms                                                                 | 140 ms: 1.00x faster                                               |
| coroutines              | 16.3 ms                                                                | 16.3 ms: 1.00x faster                                              |
| comprehensions          | 11.2 us                                                                | 11.2 us: 1.00x faster                                              |
| bpe_tokeniser           | 2.93 sec                                                               | 2.93 sec: 1.00x slower                                             |
| meteor_contest          | 71.7 ms                                                                | 71.9 ms: 1.00x slower                                              |
| scimark_sor             | 77.4 ms                                                                | 77.6 ms: 1.00x slower                                              |
| scimark_monte_carlo     | 41.9 ms                                                                | 42.0 ms: 1.00x slower                                              |
| scimark_lu              | 73.8 ms                                                                | 74.1 ms: 1.00x slower                                              |
| sqlite_synth            | 1.54 us                                                                | 1.55 us: 1.00x slower                                              |
| scimark_sparse_mat_mult | 3.08 ms                                                                | 3.09 ms: 1.00x slower                                              |
| json_dumps              | 7.34 ms                                                                | 7.37 ms: 1.00x slower                                              |
| generators              | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                              |
| deepcopy                | 146 us                                                                 | 147 us: 1.01x slower                                               |
| scimark_fft             | 182 ms                                                                 | 183 ms: 1.01x slower                                               |
| pprint_pformat          | 959 ms                                                                 | 964 ms: 1.01x slower                                               |
| subparsers              | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                              |
| richards_super          | 36.0 ms                                                                | 36.3 ms: 1.01x slower                                              |
| telco                   | 4.50 ms                                                                | 4.54 ms: 1.01x slower                                              |
| xml_etree_generate      | 53.0 ms                                                                | 53.5 ms: 1.01x slower                                              |
| many_optionals          | 434 us                                                                 | 439 us: 1.01x slower                                               |
| pprint_safe_repr        | 471 ms                                                                 | 477 ms: 1.01x slower                                               |
| regex_effbot            | 2.23 ms                                                                | 2.26 ms: 1.01x slower                                              |
| pathlib                 | 22.9 ms                                                                | 23.3 ms: 1.02x slower                                              |
| deepcopy_memo           | 17.5 us                                                                | 18.1 us: 1.03x slower                                              |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (65): xml_etree_parse, typing_runtime_protocols, pycparser, nqueens, create_gc_cycles, xml_etree_iterparse, async_tree_io, django_template, sympy_integrate, deltablue, richards, k_core, dulwich_log, async_tree_none_tg, async_tree_memoization_tg, logging_format, async_tree_eager_cpu_io_mixed, mdp, float, chaos, hexiom, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, logging_silent, pyflate, async_tree_cpu_io_mixed, sqlglot_v2_transpile, nbody, async_tree_eager_memoization_tg, crypto_pyaes, async_tree_eager_tg, deepcopy_reduce, sphinx, bench_thread_pool, async_tree_memoization, pylint, regex_compile, pidigits, raytrace, async_tree_eager_io_tg, bench_mp_pool, regex_v8, sqlalchemy_imperative, async_tree_none, connected_components, mako, async_tree_io_tg, async_tree_eager, sqlglot_v2_optimize, sympy_str, async_tree_eager_io, sympy_expand, async_tree_eager_memoization, spectral_norm, 2to3, sympy_sum, go, docutils, xml_etree_process, coverage, tomli_loads, shortest_path, html5lib, async_tree_cpu_io_mixed_tg, json

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 73.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x