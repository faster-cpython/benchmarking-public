# Results vs. base

- fork: kumaraditya303
- ref: future_iter
- machine: darwin-arm64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.002x faster
- HPT reliability: 74.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 159 ms                                                                 | 186 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|---------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io             | 361 ms                                                                 | 336 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg          | 368 ms                                                                 | 348 ms: 1.06x faster                                                  |
| async_tree_memoization          | 200 ms                                                                 | 193 ms: 1.04x faster                                                  |
| async_tree_io                   | 361 ms                                                                 | 348 ms: 1.04x faster                                                  |
| async_tree_none                 | 160 ms                                                                 | 156 ms: 1.03x faster                                                  |
| async_tree_io_tg                | 351 ms                                                                 | 344 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg      | 410 ms                                                                 | 405 ms: 1.01x faster                                                  |
| async_tree_eager_memoization    | 141 ms                                                                 | 139 ms: 1.01x faster                                                  |
| async_tree_eager_memoization_tg | 123 ms                                                                 | 122 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed         | 413 ms                                                                 | 409 ms: 1.01x faster                                                  |
| coroutines                      | 16.0 ms                                                                | 16.0 ms: 1.00x faster                                                 |
| async_tree_eager                | 61.7 ms                                                                | 61.6 ms: 1.00x faster                                                 |
| async_tree_eager_tg             | 43.2 ms                                                                | 43.5 ms: 1.01x slower                                                 |
| asyncio_websockets              | 241 ms                                                                 | 244 ms: 1.01x slower                                                  |
| Geometric mean                  | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_generators, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 67.8 ms                                                                | 67.6 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 138 ms                                                                 | 135 ms: 1.03x faster                                                  |
| regex_v8       | 15.9 ms                                                                | 15.9 ms: 1.00x faster                                                 |
| regex_compile  | 66.6 ms                                                                | 66.7 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 37.9 ms                                                                | 38.0 ms: 1.00x slower                                                 |
| json_dumps          | 7.24 ms                                                                | 7.27 ms: 1.00x slower                                                 |
| json_loads          | 16.4 us                                                                | 16.5 us: 1.00x slower                                                 |
| xml_etree_iterparse | 71.0 ms                                                                | 71.4 ms: 1.01x slower                                                 |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (5): tomli_loads, unpickle_pure_python, pickle_pure_python, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                                | 13.5 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 13.5 ms                                                                | 13.4 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|---------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io             | 361 ms                                                                 | 336 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg          | 368 ms                                                                 | 348 ms: 1.06x faster                                                  |
| async_tree_memoization          | 200 ms                                                                 | 193 ms: 1.04x faster                                                  |
| async_tree_io                   | 361 ms                                                                 | 348 ms: 1.04x faster                                                  |
| async_tree_none                 | 160 ms                                                                 | 156 ms: 1.03x faster                                                  |
| regex_dna                       | 138 ms                                                                 | 135 ms: 1.03x faster                                                  |
| async_tree_io_tg                | 351 ms                                                                 | 344 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg      | 410 ms                                                                 | 405 ms: 1.01x faster                                                  |
| async_tree_eager_memoization    | 141 ms                                                                 | 139 ms: 1.01x faster                                                  |
| async_tree_eager_memoization_tg | 123 ms                                                                 | 122 ms: 1.01x faster                                                  |
| nqueens                         | 56.5 ms                                                                | 55.8 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed         | 413 ms                                                                 | 409 ms: 1.01x faster                                                  |
| python_startup_no_site          | 13.6 ms                                                                | 13.5 ms: 1.01x faster                                                 |
| json                            | 2.87 ms                                                                | 2.85 ms: 1.01x faster                                                 |
| telco                           | 4.54 ms                                                                | 4.51 ms: 1.01x faster                                                 |
| meteor_contest                  | 71.9 ms                                                                | 71.5 ms: 1.01x faster                                                 |
| genshi_text                     | 13.5 ms                                                                | 13.4 ms: 1.01x faster                                                 |
| deepcopy                        | 149 us                                                                 | 148 us: 1.01x faster                                                  |
| subparsers                      | 11.9 ms                                                                | 11.8 ms: 1.00x faster                                                 |
| regex_v8                        | 15.9 ms                                                                | 15.9 ms: 1.00x faster                                                 |
| mdp                             | 1.48 sec                                                               | 1.48 sec: 1.00x faster                                                |
| deepcopy_reduce                 | 1.55 us                                                                | 1.54 us: 1.00x faster                                                 |
| raytrace                        | 169 ms                                                                 | 169 ms: 1.00x faster                                                  |
| coroutines                      | 16.0 ms                                                                | 16.0 ms: 1.00x faster                                                 |
| chaos                           | 37.9 ms                                                                | 37.8 ms: 1.00x faster                                                 |
| hexiom                          | 4.16 ms                                                                | 4.15 ms: 1.00x faster                                                 |
| pprint_safe_repr                | 456 ms                                                                 | 455 ms: 1.00x faster                                                  |
| nbody                           | 67.8 ms                                                                | 67.6 ms: 1.00x faster                                                 |
| async_tree_eager                | 61.7 ms                                                                | 61.6 ms: 1.00x faster                                                 |
| pprint_pformat                  | 920 ms                                                                 | 918 ms: 1.00x faster                                                  |
| sqlglot_normalize               | 179 ms                                                                 | 178 ms: 1.00x faster                                                  |
| regex_compile                   | 66.6 ms                                                                | 66.7 ms: 1.00x slower                                                 |
| scimark_sor                     | 78.3 ms                                                                | 78.5 ms: 1.00x slower                                                 |
| sympy_str                       | 138 ms                                                                 | 138 ms: 1.00x slower                                                  |
| xml_etree_process               | 37.9 ms                                                                | 38.0 ms: 1.00x slower                                                 |
| gc_traversal                    | 3.06 ms                                                                | 3.08 ms: 1.00x slower                                                 |
| json_dumps                      | 7.24 ms                                                                | 7.27 ms: 1.00x slower                                                 |
| sqlglot_transpile               | 923 us                                                                 | 927 us: 1.00x slower                                                  |
| scimark_fft                     | 172 ms                                                                 | 173 ms: 1.00x slower                                                  |
| json_loads                      | 16.4 us                                                                | 16.5 us: 1.00x slower                                                 |
| dulwich_log                     | 26.9 ms                                                                | 27.0 ms: 1.00x slower                                                 |
| xml_etree_iterparse             | 71.0 ms                                                                | 71.4 ms: 1.01x slower                                                 |
| async_tree_eager_tg             | 43.2 ms                                                                | 43.5 ms: 1.01x slower                                                 |
| fannkuch                        | 245 ms                                                                 | 246 ms: 1.01x slower                                                  |
| scimark_lu                      | 71.9 ms                                                                | 72.7 ms: 1.01x slower                                                 |
| generators                      | 22.3 ms                                                                | 22.6 ms: 1.01x slower                                                 |
| asyncio_websockets              | 241 ms                                                                 | 244 ms: 1.01x slower                                                  |
| 2to3                            | 159 ms                                                                 | 186 ms: 1.17x slower                                                  |
| Geometric mean                  | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (57): async_tree_memoization_tg, tomli_loads, django_template, typing_runtime_protocols, async_generators, python_startup, async_tree_eager_cpu_io_mixed, deltablue, sympy_integrate, spectral_norm, sympy_expand, comprehensions, sqlglot_parse, thrift, html5lib, coverage, k_core, deepcopy_memo, logging_format, richards_super, genshi_xml, scimark_sparse_mat_mult, pyflate, async_tree_eager_cpu_io_mixed_tg, sqlglot_optimize, docutils, unpickle_pure_python, pidigits, regex_effbot, pickle_pure_python, go, sqlalchemy_declarative, connected_components, shortest_path, mako, pycparser, richards, logging_simple, scimark_monte_carlo, bpe_tokeniser, sqlite_synth, bench_mp_pool, logging_silent, float, crypto_pyaes, sympy_sum, xml_etree_generate, mypy2, bench_thread_pool, create_gc_cycles, pylint, sqlalchemy_imperative, sphinx, many_optionals, async_tree_none_tg, xml_etree_parse, pathlib

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 74.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x