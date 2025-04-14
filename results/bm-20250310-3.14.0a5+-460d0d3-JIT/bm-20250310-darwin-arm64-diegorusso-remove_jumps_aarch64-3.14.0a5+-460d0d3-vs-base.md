# Results vs. base

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: darwin-arm64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.001x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 165 ms                                                                 | 193 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                    | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                   | 16.6 ms                                                                | 16.5 ms: 1.00x faster                                                      |
| async_tree_eager_memoization | 139 ms                                                                 | 140 ms: 1.01x slower                                                       |
| async_tree_eager             | 60.8 ms                                                                | 61.3 ms: 1.01x slower                                                      |
| async_generators             | 272 ms                                                                 | 275 ms: 1.01x slower                                                       |
| async_tree_io                | 371 ms                                                                 | 378 ms: 1.02x slower                                                       |
| Geometric mean               | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (14): async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                                | 64.5 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 2.25 ms                                                                | 2.24 ms: 1.00x faster                                                      |
| regex_compile  | 68.4 ms                                                                | 68.7 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python | 196 us                                                                 | 197 us: 1.00x slower                                                       |
| xml_etree_process  | 35.7 ms                                                                | 35.9 ms: 1.01x slower                                                      |
| xml_etree_generate | 50.7 ms                                                                | 51.1 ms: 1.01x slower                                                      |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (6): tomli_loads, unpickle_pure_python, xml_etree_parse, json_dumps, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 19.7 ms                                                                | 19.6 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 13.7 ms                                                                | 13.8 ms: 1.00x slower                                                      |
| mako           | 6.50 ms                                                                | 6.54 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                    | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| sqlite_synth                 | 1.67 us                                                                | 1.55 us: 1.08x faster                                                      |
| sqlglot_v2_optimize          | 35.4 ms                                                                | 33.1 ms: 1.07x faster                                                      |
| sqlglot_v2_parse             | 888 us                                                                 | 846 us: 1.05x faster                                                       |
| sympy_integrate              | 11.5 ms                                                                | 11.3 ms: 1.01x faster                                                      |
| scimark_monte_carlo          | 44.5 ms                                                                | 44.0 ms: 1.01x faster                                                      |
| many_optionals               | 456 us                                                                 | 451 us: 1.01x faster                                                       |
| sqlglot_v2_transpile         | 1.03 ms                                                                | 1.02 ms: 1.01x faster                                                      |
| subparsers                   | 12.1 ms                                                                | 12.0 ms: 1.01x faster                                                      |
| spectral_norm                | 63.4 ms                                                                | 62.8 ms: 1.01x faster                                                      |
| connected_components         | 299 ms                                                                 | 298 ms: 1.01x faster                                                       |
| bench_mp_pool                | 61.9 ms                                                                | 61.6 ms: 1.01x faster                                                      |
| python_startup               | 19.7 ms                                                                | 19.6 ms: 1.00x faster                                                      |
| regex_effbot                 | 2.25 ms                                                                | 2.24 ms: 1.00x faster                                                      |
| coroutines                   | 16.6 ms                                                                | 16.5 ms: 1.00x faster                                                      |
| nbody                        | 64.5 ms                                                                | 64.5 ms: 1.00x faster                                                      |
| chaos                        | 39.3 ms                                                                | 39.3 ms: 1.00x slower                                                      |
| logging_simple               | 3.19 us                                                                | 3.20 us: 1.00x slower                                                      |
| pyflate                      | 306 ms                                                                 | 307 ms: 1.00x slower                                                       |
| bench_thread_pool            | 486 us                                                                 | 488 us: 1.00x slower                                                       |
| generators                   | 23.3 ms                                                                | 23.5 ms: 1.00x slower                                                      |
| pickle_pure_python           | 196 us                                                                 | 197 us: 1.00x slower                                                       |
| genshi_text                  | 13.7 ms                                                                | 13.8 ms: 1.00x slower                                                      |
| regex_compile                | 68.4 ms                                                                | 68.7 ms: 1.00x slower                                                      |
| logging_format               | 3.50 us                                                                | 3.51 us: 1.00x slower                                                      |
| telco                        | 4.49 ms                                                                | 4.52 ms: 1.01x slower                                                      |
| sqlalchemy_declarative       | 58.7 ms                                                                | 59.0 ms: 1.01x slower                                                      |
| mako                         | 6.50 ms                                                                | 6.54 ms: 1.01x slower                                                      |
| dulwich_log                  | 24.5 ms                                                                | 24.7 ms: 1.01x slower                                                      |
| deepcopy                     | 150 us                                                                 | 151 us: 1.01x slower                                                       |
| async_tree_eager_memoization | 139 ms                                                                 | 140 ms: 1.01x slower                                                       |
| go                           | 92.7 ms                                                                | 93.4 ms: 1.01x slower                                                      |
| xml_etree_process            | 35.7 ms                                                                | 35.9 ms: 1.01x slower                                                      |
| xml_etree_generate           | 50.7 ms                                                                | 51.1 ms: 1.01x slower                                                      |
| async_tree_eager             | 60.8 ms                                                                | 61.3 ms: 1.01x slower                                                      |
| bpe_tokeniser                | 2.93 sec                                                               | 2.96 sec: 1.01x slower                                                     |
| thrift                       | 435 us                                                                 | 439 us: 1.01x slower                                                       |
| pprint_pformat               | 995 ms                                                                 | 1.01 sec: 1.01x slower                                                     |
| json                         | 3.02 ms                                                                | 3.06 ms: 1.01x slower                                                      |
| async_generators             | 272 ms                                                                 | 275 ms: 1.01x slower                                                       |
| fannkuch                     | 279 ms                                                                 | 282 ms: 1.01x slower                                                       |
| meteor_contest               | 74.5 ms                                                                | 75.7 ms: 1.02x slower                                                      |
| async_tree_io                | 371 ms                                                                 | 378 ms: 1.02x slower                                                       |
| 2to3                         | 165 ms                                                                 | 193 ms: 1.17x slower                                                       |
| Geometric mean               | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (62): typing_runtime_protocols, tomli_loads, html5lib, docutils, logging_silent, unpickle_pure_python, nqueens, sympy_str, richards, sqlalchemy_imperative, crypto_pyaes, scimark_fft, dask, deepcopy_memo, sqlglot_v2_normalize, pathlib, float, gc_traversal, sphinx, async_tree_eager_cpu_io_mixed, python_startup_no_site, genshi_xml, scimark_sparse_mat_mult, hexiom, async_tree_cpu_io_mixed, k_core, regex_v8, regex_dna, django_template, pylint, async_tree_none, scimark_sor, xml_etree_parse, json_dumps, richards_super, raytrace, pidigits, deepcopy_reduce, sympy_sum, comprehensions, asyncio_websockets, mdp, json_loads, scimark_lu, async_tree_memoization, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, sympy_expand, deltablue, shortest_path, coverage, create_gc_cycles, async_tree_memoization_tg, pycparser, async_tree_eager_cpu_io_mixed_tg, pprint_safe_repr, async_tree_none_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x