# Results vs. base

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: darwin-arm64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.000x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                                 | 156 ms: 1.15x faster                                                             |
| docutils       | 1.39 sec                                                               | 1.45 sec: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 269 ms                                                                 | 263 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 410 ms                                                                 | 404 ms: 1.02x faster                                                             |
| async_tree_none            | 154 ms                                                                 | 152 ms: 1.01x faster                                                             |
| async_tree_eager           | 61.2 ms                                                                | 60.3 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 407 ms                                                                 | 402 ms: 1.01x faster                                                             |
| coroutines                 | 15.0 ms                                                                | 14.9 ms: 1.01x faster                                                            |
| async_tree_memoization     | 185 ms                                                                 | 184 ms: 1.00x faster                                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (12): async_tree_eager_tg, async_tree_io_tg, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 44.2 ms                                                                | 44.4 ms: 1.00x slower                                                            |
| nbody          | 63.6 ms                                                                | 63.8 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                            |
| regex_dna      | 147 ms                                                                 | 149 ms: 1.01x slower                                                             |
| regex_v8       | 18.0 ms                                                                | 18.3 ms: 1.02x slower                                                            |
| regex_effbot   | 2.39 ms                                                                | 2.45 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 128 us                                                                 | 127 us: 1.01x faster                                                             |
| pickle_pure_python   | 186 us                                                                 | 185 us: 1.01x faster                                                             |
| xml_etree_process    | 33.2 ms                                                                | 33.0 ms: 1.01x faster                                                            |
| xml_etree_generate   | 48.1 ms                                                                | 47.8 ms: 1.00x faster                                                            |
| tomli_loads          | 1.16 sec                                                               | 1.17 sec: 1.01x slower                                                           |
| json_dumps           | 7.12 ms                                                                | 7.24 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 16.7 ms                                                                | 17.2 ms: 1.03x slower                                                            |
| python_startup_no_site | 12.0 ms                                                                | 12.7 ms: 1.06x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml     | 27.4 ms                                                                | 27.0 ms: 1.01x faster                                                            |
| genshi_text    | 12.7 ms                                                                | 12.7 ms: 1.01x faster                                                            |
| mako           | 6.47 ms                                                                | 6.46 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3                       | 179 ms                                                                 | 156 ms: 1.15x faster                                                             |
| async_generators           | 269 ms                                                                 | 263 ms: 1.02x faster                                                             |
| typing_runtime_protocols   | 89.4 us                                                                | 87.9 us: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 410 ms                                                                 | 404 ms: 1.02x faster                                                             |
| async_tree_none            | 154 ms                                                                 | 152 ms: 1.01x faster                                                             |
| async_tree_eager           | 61.2 ms                                                                | 60.3 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 407 ms                                                                 | 402 ms: 1.01x faster                                                             |
| genshi_xml                 | 27.4 ms                                                                | 27.0 ms: 1.01x faster                                                            |
| sympy_sum                  | 70.3 ms                                                                | 69.5 ms: 1.01x faster                                                            |
| comprehensions             | 11.6 us                                                                | 11.5 us: 1.01x faster                                                            |
| create_gc_cycles           | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                                            |
| sympy_str                  | 132 ms                                                                 | 131 ms: 1.01x faster                                                             |
| many_optionals             | 430 us                                                                 | 427 us: 1.01x faster                                                             |
| unpickle_pure_python       | 128 us                                                                 | 127 us: 1.01x faster                                                             |
| scimark_monte_carlo        | 39.5 ms                                                                | 39.2 ms: 1.01x faster                                                            |
| genshi_text                | 12.7 ms                                                                | 12.7 ms: 1.01x faster                                                            |
| pickle_pure_python         | 186 us                                                                 | 185 us: 1.01x faster                                                             |
| deepcopy                   | 139 us                                                                 | 138 us: 1.01x faster                                                             |
| xml_etree_process          | 33.2 ms                                                                | 33.0 ms: 1.01x faster                                                            |
| bench_thread_pool          | 459 us                                                                 | 457 us: 1.01x faster                                                             |
| coroutines                 | 15.0 ms                                                                | 14.9 ms: 1.01x faster                                                            |
| regex_compile              | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                            |
| deltablue                  | 2.07 ms                                                                | 2.06 ms: 1.01x faster                                                            |
| logging_silent             | 58.4 ns                                                                | 58.1 ns: 1.01x faster                                                            |
| xml_etree_generate         | 48.1 ms                                                                | 47.8 ms: 1.00x faster                                                            |
| sqlalchemy_imperative      | 6.37 ms                                                                | 6.34 ms: 1.00x faster                                                            |
| async_tree_memoization     | 185 ms                                                                 | 184 ms: 1.00x faster                                                             |
| sqlalchemy_declarative     | 55.5 ms                                                                | 55.3 ms: 1.00x faster                                                            |
| dask                       | 770 ms                                                                 | 766 ms: 1.00x faster                                                             |
| sqlglot_parse              | 814 us                                                                 | 811 us: 1.00x faster                                                             |
| sympy_expand               | 222 ms                                                                 | 221 ms: 1.00x faster                                                             |
| deepcopy_memo              | 16.7 us                                                                | 16.6 us: 1.00x faster                                                            |
| go                         | 72.8 ms                                                                | 72.6 ms: 1.00x faster                                                            |
| nqueens                    | 53.0 ms                                                                | 52.8 ms: 1.00x faster                                                            |
| scimark_sor                | 74.3 ms                                                                | 74.2 ms: 1.00x faster                                                            |
| spectral_norm              | 68.1 ms                                                                | 68.0 ms: 1.00x faster                                                            |
| meteor_contest             | 74.6 ms                                                                | 74.5 ms: 1.00x faster                                                            |
| mako                       | 6.47 ms                                                                | 6.46 ms: 1.00x faster                                                            |
| dulwich_log                | 27.0 ms                                                                | 27.1 ms: 1.00x slower                                                            |
| float                      | 44.2 ms                                                                | 44.4 ms: 1.00x slower                                                            |
| nbody                      | 63.6 ms                                                                | 63.8 ms: 1.00x slower                                                            |
| sqlite_synth               | 1.53 us                                                                | 1.54 us: 1.01x slower                                                            |
| scimark_fft                | 181 ms                                                                 | 183 ms: 1.01x slower                                                             |
| tomli_loads                | 1.16 sec                                                               | 1.17 sec: 1.01x slower                                                           |
| crypto_pyaes               | 51.5 ms                                                                | 52.0 ms: 1.01x slower                                                            |
| regex_dna                  | 147 ms                                                                 | 149 ms: 1.01x slower                                                             |
| pprint_pformat             | 993 ms                                                                 | 1.01 sec: 1.02x slower                                                           |
| json_dumps                 | 7.12 ms                                                                | 7.24 ms: 1.02x slower                                                            |
| regex_v8                   | 18.0 ms                                                                | 18.3 ms: 1.02x slower                                                            |
| regex_effbot               | 2.39 ms                                                                | 2.45 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 2.94 ms                                                                | 3.01 ms: 1.03x slower                                                            |
| python_startup             | 16.7 ms                                                                | 17.2 ms: 1.03x slower                                                            |
| pprint_safe_repr           | 487 ms                                                                 | 504 ms: 1.03x slower                                                             |
| bench_mp_pool              | 58.0 ms                                                                | 60.2 ms: 1.04x slower                                                            |
| docutils                   | 1.39 sec                                                               | 1.45 sec: 1.04x slower                                                           |
| generators                 | 17.4 ms                                                                | 18.1 ms: 1.05x slower                                                            |
| python_startup_no_site     | 12.0 ms                                                                | 12.7 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (48): async_tree_eager_tg, async_tree_io_tg, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_eager_io, pylint, connected_components, async_tree_eager_cpu_io_mixed_tg, xml_etree_iterparse, async_tree_eager_memoization, shortest_path, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, pycparser, coverage, scimark_lu, django_template, sqlglot_optimize, sqlglot_normalize, deepcopy_reduce, asyncio_websockets, fannkuch, bpe_tokeniser, xml_etree_parse, raytrace, chaos, logging_simple, json, sqlglot_transpile, pidigits, richards, pyflate, richards_super, sympy_integrate, hexiom, html5lib, gc_traversal, json_loads, sphinx, logging_format, thrift, mdp, pathlib, telco, k_core, subparsers

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x