# Results vs. base

- fork: diegorusso
- ref: aarch64_trampolines
- machine: darwin-arm64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.008x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 165 ms                                                                 | 163 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 360 ms                                                                 | 358 ms: 1.01x faster                                                      |
| async_tree_eager              | 60.8 ms                                                                | 61.1 ms: 1.01x slower                                                     |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (17): async_generators, async_tree_io_tg, coroutines, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                                | 64.0 ms: 1.01x faster                                                     |
| float          | 44.8 ms                                                                | 44.5 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                                | 15.7 ms: 1.01x slower                                                     |
| regex_effbot   | 2.25 ms                                                                | 2.27 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.19 sec                                                               | 1.18 sec: 1.01x faster                                                    |
| unpickle_pure_python | 134 us                                                                 | 132 us: 1.01x faster                                                      |
| json_dumps           | 7.33 ms                                                                | 7.29 ms: 1.01x faster                                                     |
| xml_etree_generate   | 50.7 ms                                                                | 50.4 ms: 1.00x faster                                                     |
| xml_etree_parse      | 101 ms                                                                 | 103 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_process, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.2 ms                                                                | 12.4 ms: 1.23x faster                                                     |
| python_startup         | 19.7 ms                                                                | 16.5 ms: 1.19x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.21x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 6.50 ms                                                                | 6.47 ms: 1.01x faster                                                     |
| genshi_xml     | 28.9 ms                                                                | 29.1 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site        | 15.2 ms                                                                | 12.4 ms: 1.23x faster                                                     |
| python_startup                | 19.7 ms                                                                | 16.5 ms: 1.19x faster                                                     |
| sqlite_synth                  | 1.67 us                                                                | 1.54 us: 1.08x faster                                                     |
| sqlglot_v2_optimize           | 35.4 ms                                                                | 33.0 ms: 1.07x faster                                                     |
| sqlglot_v2_parse              | 888 us                                                                 | 845 us: 1.05x faster                                                      |
| bench_mp_pool                 | 61.9 ms                                                                | 59.7 ms: 1.04x faster                                                     |
| scimark_fft                   | 182 ms                                                                 | 177 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult       | 2.96 ms                                                                | 2.89 ms: 1.02x faster                                                     |
| subparsers                    | 12.1 ms                                                                | 11.9 ms: 1.02x faster                                                     |
| scimark_monte_carlo           | 44.5 ms                                                                | 43.6 ms: 1.02x faster                                                     |
| many_optionals                | 456 us                                                                 | 447 us: 1.02x faster                                                      |
| deltablue                     | 2.15 ms                                                                | 2.11 ms: 1.02x faster                                                     |
| spectral_norm                 | 63.4 ms                                                                | 62.2 ms: 1.02x faster                                                     |
| sqlglot_v2_transpile          | 1.03 ms                                                                | 1.01 ms: 1.01x faster                                                     |
| tomli_loads                   | 1.19 sec                                                               | 1.18 sec: 1.01x faster                                                    |
| unpickle_pure_python          | 134 us                                                                 | 132 us: 1.01x faster                                                      |
| pprint_safe_repr              | 495 ms                                                                 | 488 ms: 1.01x faster                                                      |
| sympy_integrate               | 11.5 ms                                                                | 11.3 ms: 1.01x faster                                                     |
| nqueens                       | 59.3 ms                                                                | 58.7 ms: 1.01x faster                                                     |
| sqlalchemy_imperative         | 6.67 ms                                                                | 6.61 ms: 1.01x faster                                                     |
| nbody                         | 64.5 ms                                                                | 64.0 ms: 1.01x faster                                                     |
| float                         | 44.8 ms                                                                | 44.5 ms: 1.01x faster                                                     |
| telco                         | 4.49 ms                                                                | 4.46 ms: 1.01x faster                                                     |
| comprehensions                | 12.1 us                                                                | 12.1 us: 1.01x faster                                                     |
| 2to3                          | 165 ms                                                                 | 163 ms: 1.01x faster                                                      |
| connected_components          | 299 ms                                                                 | 297 ms: 1.01x faster                                                      |
| json_dumps                    | 7.33 ms                                                                | 7.29 ms: 1.01x faster                                                     |
| sqlalchemy_declarative        | 58.7 ms                                                                | 58.4 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                 | 358 ms: 1.01x faster                                                      |
| mako                          | 6.50 ms                                                                | 6.47 ms: 1.01x faster                                                     |
| gc_traversal                  | 3.14 ms                                                                | 3.12 ms: 1.00x faster                                                     |
| xml_etree_generate            | 50.7 ms                                                                | 50.4 ms: 1.00x faster                                                     |
| crypto_pyaes                  | 55.0 ms                                                                | 54.8 ms: 1.00x faster                                                     |
| bpe_tokeniser                 | 2.93 sec                                                               | 2.91 sec: 1.00x faster                                                    |
| dulwich_log                   | 24.5 ms                                                                | 24.4 ms: 1.00x faster                                                     |
| logging_silent                | 65.0 ns                                                                | 64.7 ns: 1.00x faster                                                     |
| go                            | 92.7 ms                                                                | 92.6 ms: 1.00x faster                                                     |
| raytrace                      | 178 ms                                                                 | 178 ms: 1.00x faster                                                      |
| thrift                        | 435 us                                                                 | 436 us: 1.00x slower                                                      |
| deepcopy                      | 150 us                                                                 | 151 us: 1.00x slower                                                      |
| logging_format                | 3.50 us                                                                | 3.51 us: 1.00x slower                                                     |
| genshi_xml                    | 28.9 ms                                                                | 29.1 ms: 1.00x slower                                                     |
| regex_v8                      | 15.6 ms                                                                | 15.7 ms: 1.01x slower                                                     |
| async_tree_eager              | 60.8 ms                                                                | 61.1 ms: 1.01x slower                                                     |
| deepcopy_memo                 | 18.2 us                                                                | 18.3 us: 1.01x slower                                                     |
| regex_effbot                  | 2.25 ms                                                                | 2.27 ms: 1.01x slower                                                     |
| xml_etree_parse               | 101 ms                                                                 | 103 ms: 1.01x slower                                                      |
| Geometric mean                | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (58): pycparser, html5lib, pathlib, sympy_str, async_generators, async_tree_io_tg, regex_compile, create_gc_cycles, fannkuch, django_template, sympy_expand, coroutines, pprint_pformat, mdp, async_tree_none, hexiom, sympy_sum, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, dask, async_tree_io, shortest_path, pickle_pure_python, regex_dna, docutils, xml_etree_process, genshi_text, k_core, pylint, deepcopy_reduce, async_tree_eager_io_tg, json_loads, scimark_sor, sphinx, pidigits, pyflate, scimark_lu, logging_simple, generators, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, richards_super, async_tree_eager_io, sqlglot_v2_normalize, meteor_contest, bench_thread_pool, chaos, async_tree_eager_memoization_tg, coverage, async_tree_eager_tg, typing_runtime_protocols, xml_etree_iterparse, async_tree_eager_memoization, json, richards

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x