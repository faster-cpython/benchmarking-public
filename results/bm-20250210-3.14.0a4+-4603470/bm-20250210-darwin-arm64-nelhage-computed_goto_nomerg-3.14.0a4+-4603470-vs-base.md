# Results vs. base

- fork: nelhage
- ref: computed_goto_nomerg
- machine: darwin-arm64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.001x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io      | 377 ms                                                                 | 372 ms: 1.01x faster                                                    |
| asyncio_websockets | 242 ms                                                                 | 242 ms: 1.00x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (17): async_tree_eager_io_tg, async_tree_none, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_generators, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_eager, coroutines, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 17.2 ms                                                                | 16.9 ms: 1.02x faster                                                   |
| regex_compile  | 66.9 ms                                                                | 66.8 ms: 1.00x faster                                                   |
| regex_dna      | 141 ms                                                                 | 142 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 7.28 ms                                                                | 7.24 ms: 1.01x faster                                                   |
| xml_etree_process    | 38.6 ms                                                                | 38.4 ms: 1.00x faster                                                   |
| unpickle_pure_python | 142 us                                                                 | 142 us: 1.00x faster                                                    |
| pickle_pure_python   | 200 us                                                                 | 199 us: 1.00x faster                                                    |
| json_loads           | 17.8 us                                                                | 17.8 us: 1.00x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_generate, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                   |
| genshi_text     | 13.5 ms                                                                | 13.5 ms: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250208-darwin-arm64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8                 | 17.2 ms                                                                | 16.9 ms: 1.02x faster                                                   |
| async_tree_io            | 377 ms                                                                 | 372 ms: 1.01x faster                                                    |
| nqueens                  | 58.4 ms                                                                | 57.9 ms: 1.01x faster                                                   |
| deepcopy_reduce          | 1.58 us                                                                | 1.57 us: 1.01x faster                                                   |
| bpe_tokeniser            | 2.91 sec                                                               | 2.88 sec: 1.01x faster                                                  |
| generators               | 23.0 ms                                                                | 22.9 ms: 1.01x faster                                                   |
| typing_runtime_protocols | 93.8 us                                                                | 93.2 us: 1.01x faster                                                   |
| connected_components     | 299 ms                                                                 | 297 ms: 1.01x faster                                                    |
| django_template          | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                   |
| json_dumps               | 7.28 ms                                                                | 7.24 ms: 1.01x faster                                                   |
| bench_thread_pool        | 488 us                                                                 | 485 us: 1.01x faster                                                    |
| hexiom                   | 4.31 ms                                                                | 4.29 ms: 1.01x faster                                                   |
| xml_etree_process        | 38.6 ms                                                                | 38.4 ms: 1.00x faster                                                   |
| subparsers               | 11.8 ms                                                                | 11.7 ms: 1.00x faster                                                   |
| genshi_text              | 13.5 ms                                                                | 13.5 ms: 1.00x faster                                                   |
| raytrace                 | 171 ms                                                                 | 170 ms: 1.00x faster                                                    |
| sqlglot_normalize        | 177 ms                                                                 | 177 ms: 1.00x faster                                                    |
| scimark_sor              | 78.2 ms                                                                | 77.9 ms: 1.00x faster                                                   |
| crypto_pyaes             | 52.4 ms                                                                | 52.2 ms: 1.00x faster                                                   |
| sqlalchemy_declarative   | 58.0 ms                                                                | 57.9 ms: 1.00x faster                                                   |
| sympy_expand             | 232 ms                                                                 | 231 ms: 1.00x faster                                                    |
| many_optionals           | 432 us                                                                 | 430 us: 1.00x faster                                                    |
| unpickle_pure_python     | 142 us                                                                 | 142 us: 1.00x faster                                                    |
| thrift                   | 436 us                                                                 | 435 us: 1.00x faster                                                    |
| chaos                    | 39.0 ms                                                                | 38.9 ms: 1.00x faster                                                   |
| regex_compile            | 66.9 ms                                                                | 66.8 ms: 1.00x faster                                                   |
| pickle_pure_python       | 200 us                                                                 | 199 us: 1.00x faster                                                    |
| pprint_pformat           | 936 ms                                                                 | 934 ms: 1.00x faster                                                    |
| scimark_monte_carlo      | 42.6 ms                                                                | 42.7 ms: 1.00x slower                                                   |
| asyncio_websockets       | 242 ms                                                                 | 242 ms: 1.00x slower                                                    |
| richards_super           | 35.9 ms                                                                | 36.0 ms: 1.00x slower                                                   |
| logging_silent           | 65.8 ns                                                                | 65.9 ns: 1.00x slower                                                   |
| sqlite_synth             | 1.52 us                                                                | 1.52 us: 1.00x slower                                                   |
| deepcopy_memo            | 18.2 us                                                                | 18.2 us: 1.00x slower                                                   |
| json_loads               | 17.8 us                                                                | 17.8 us: 1.00x slower                                                   |
| spectral_norm            | 61.1 ms                                                                | 61.3 ms: 1.00x slower                                                   |
| fannkuch                 | 253 ms                                                                 | 254 ms: 1.00x slower                                                    |
| create_gc_cycles         | 1.28 ms                                                                | 1.29 ms: 1.00x slower                                                   |
| regex_dna                | 141 ms                                                                 | 142 ms: 1.01x slower                                                    |
| pathlib                  | 22.7 ms                                                                | 22.9 ms: 1.01x slower                                                   |
| dulwich_log              | 27.3 ms                                                                | 27.5 ms: 1.01x slower                                                   |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (64): async_tree_eager_io_tg, pylint, async_tree_none, sympy_sum, sphinx, xml_etree_iterparse, async_tree_eager_io, deepcopy, async_tree_eager_memoization_tg, sqlalchemy_imperative, python_startup_no_site, async_tree_none_tg, python_startup, sympy_str, async_tree_eager_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, pycparser, async_tree_eager_cpu_io_mixed_tg, richards, mdp, logging_simple, float, sqlglot_optimize, async_generators, comprehensions, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, sympy_integrate, 2to3, async_tree_memoization, logging_format, mako, html5lib, async_tree_memoization_tg, async_tree_eager, scimark_sparse_mat_mult, docutils, coroutines, regex_effbot, scimark_fft, nbody, pyflate, shortest_path, sqlglot_parse, xml_etree_generate, pidigits, async_tree_eager_memoization, gc_traversal, sqlglot_transpile, dask, go, tomli_loads, deltablue, k_core, json, xml_etree_parse, meteor_contest, pprint_safe_repr, telco, scimark_lu, genshi_xml, coverage, bench_mp_pool

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x