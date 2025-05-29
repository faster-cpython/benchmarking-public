# Results vs. base

- fork: mdboom
- ref: early_tail_call_load
- machine: darwin-arm64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.001x slower
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.35 sec                                                               | 1.35 sec: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets | 242 ms                                                                 | 242 ms: 1.00x faster                                                   |
| async_generators   | 247 ms                                                                 | 250 ms: 1.01x slower                                                   |
| coroutines         | 14.5 ms                                                                | 15.1 ms: 1.04x slower                                                  |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_io_tg, async_tree_eager, async_tree_eager_memoization, async_tree_none, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_eager_io, async_tree_none_tg, async_tree_io, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 280 ms                                                                 | 280 ms: 1.00x slower                                                   |
| float          | 43.4 ms                                                                | 43.6 ms: 1.00x slower                                                  |
| nbody          | 62.0 ms                                                                | 63.3 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 17.8 ms                                                                | 17.7 ms: 1.01x faster                                                  |
| regex_dna      | 146 ms                                                                 | 146 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 125 us                                                                 | 123 us: 1.02x faster                                                   |
| pickle_pure_python   | 181 us                                                                 | 182 us: 1.00x slower                                                   |
| xml_etree_process    | 33.9 ms                                                                | 34.0 ms: 1.00x slower                                                  |
| xml_etree_generate   | 48.2 ms                                                                | 48.5 ms: 1.01x slower                                                  |
| json_dumps           | 7.04 ms                                                                | 7.09 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (4): json_loads, tomli_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                                | 12.4 ms: 1.04x faster                                                  |
| python_startup         | 17.2 ms                                                                | 17.1 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 12.3 ms                                                                | 12.3 ms: 1.01x faster                                                  |
| genshi_xml     | 26.0 ms                                                                | 26.3 ms: 1.01x slower                                                  |
| mako           | 6.95 ms                                                                | 7.05 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site  | 12.8 ms                                                                | 12.4 ms: 1.04x faster                                                  |
| scimark_lu              | 66.0 ms                                                                | 64.8 ms: 1.02x faster                                                  |
| meteor_contest          | 69.6 ms                                                                | 68.4 ms: 1.02x faster                                                  |
| unpickle_pure_python    | 125 us                                                                 | 123 us: 1.02x faster                                                   |
| sqlalchemy_declarative  | 54.6 ms                                                                | 53.9 ms: 1.01x faster                                                  |
| crypto_pyaes            | 47.3 ms                                                                | 46.8 ms: 1.01x faster                                                  |
| chaos                   | 35.4 ms                                                                | 35.0 ms: 1.01x faster                                                  |
| sympy_integrate         | 10.1 ms                                                                | 10.1 ms: 1.01x faster                                                  |
| sqlite_synth            | 1.51 us                                                                | 1.50 us: 1.01x faster                                                  |
| telco                   | 4.45 ms                                                                | 4.42 ms: 1.01x faster                                                  |
| regex_v8                | 17.8 ms                                                                | 17.7 ms: 1.01x faster                                                  |
| genshi_text             | 12.3 ms                                                                | 12.3 ms: 1.01x faster                                                  |
| many_optionals          | 413 us                                                                 | 411 us: 1.01x faster                                                   |
| python_startup          | 17.2 ms                                                                | 17.1 ms: 1.01x faster                                                  |
| raytrace                | 155 ms                                                                 | 155 ms: 1.00x faster                                                   |
| docutils                | 1.35 sec                                                               | 1.35 sec: 1.00x faster                                                 |
| sqlglot_parse           | 680 us                                                                 | 678 us: 1.00x faster                                                   |
| asyncio_websockets      | 242 ms                                                                 | 242 ms: 1.00x faster                                                   |
| regex_dna               | 146 ms                                                                 | 146 ms: 1.00x slower                                                   |
| pidigits                | 280 ms                                                                 | 280 ms: 1.00x slower                                                   |
| pprint_pformat          | 878 ms                                                                 | 879 ms: 1.00x slower                                                   |
| pickle_pure_python      | 181 us                                                                 | 182 us: 1.00x slower                                                   |
| nqueens                 | 50.5 ms                                                                | 50.6 ms: 1.00x slower                                                  |
| richards                | 27.5 ms                                                                | 27.6 ms: 1.00x slower                                                  |
| xml_etree_process       | 33.9 ms                                                                | 34.0 ms: 1.00x slower                                                  |
| float                   | 43.4 ms                                                                | 43.6 ms: 1.00x slower                                                  |
| dulwich_log             | 26.2 ms                                                                | 26.4 ms: 1.00x slower                                                  |
| richards_super          | 30.9 ms                                                                | 31.0 ms: 1.00x slower                                                  |
| deepcopy_reduce         | 1.49 us                                                                | 1.50 us: 1.00x slower                                                  |
| scimark_monte_carlo     | 38.8 ms                                                                | 39.0 ms: 1.01x slower                                                  |
| scimark_sor             | 73.0 ms                                                                | 73.3 ms: 1.01x slower                                                  |
| deepcopy_memo           | 16.2 us                                                                | 16.3 us: 1.01x slower                                                  |
| xml_etree_generate      | 48.2 ms                                                                | 48.5 ms: 1.01x slower                                                  |
| mdp                     | 1.42 sec                                                               | 1.43 sec: 1.01x slower                                                 |
| thrift                  | 406 us                                                                 | 409 us: 1.01x slower                                                   |
| connected_components    | 295 ms                                                                 | 297 ms: 1.01x slower                                                   |
| bpe_tokeniser           | 2.74 sec                                                               | 2.75 sec: 1.01x slower                                                 |
| json_dumps              | 7.04 ms                                                                | 7.09 ms: 1.01x slower                                                  |
| scimark_fft             | 168 ms                                                                 | 169 ms: 1.01x slower                                                   |
| spectral_norm           | 58.1 ms                                                                | 58.6 ms: 1.01x slower                                                  |
| deltablue               | 2.02 ms                                                                | 2.04 ms: 1.01x slower                                                  |
| pprint_safe_repr        | 432 ms                                                                 | 436 ms: 1.01x slower                                                   |
| genshi_xml              | 26.0 ms                                                                | 26.3 ms: 1.01x slower                                                  |
| deepcopy                | 139 us                                                                 | 140 us: 1.01x slower                                                   |
| shortest_path           | 322 ms                                                                 | 325 ms: 1.01x slower                                                   |
| async_generators        | 247 ms                                                                 | 250 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult | 2.64 ms                                                                | 2.67 ms: 1.01x slower                                                  |
| mako                    | 6.95 ms                                                                | 7.05 ms: 1.01x slower                                                  |
| nbody                   | 62.0 ms                                                                | 63.3 ms: 1.02x slower                                                  |
| coroutines              | 14.5 ms                                                                | 15.1 ms: 1.04x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (55): pathlib, pylint, create_gc_cycles, sqlglot_transpile, typing_runtime_protocols, sqlalchemy_imperative, sphinx, pycparser, async_tree_cpu_io_mixed, fannkuch, regex_compile, sympy_sum, sqlglot_optimize, async_tree_cpu_io_mixed_tg, 2to3, sqlglot_normalize, json_loads, logging_format, hexiom, coverage, gc_traversal, logging_silent, tomli_loads, xml_etree_iterparse, async_tree_memoization, logging_simple, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, bench_thread_pool, regex_effbot, dask, django_template, comprehensions, async_tree_eager_cpu_io_mixed, html5lib, subparsers, go, generators, sympy_expand, async_tree_io_tg, async_tree_eager, async_tree_eager_memoization, async_tree_none, sympy_str, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_eager_io, async_tree_none_tg, async_tree_io, json, pyflate, async_tree_eager_memoization_tg, xml_etree_parse, k_core, bench_mp_pool

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x