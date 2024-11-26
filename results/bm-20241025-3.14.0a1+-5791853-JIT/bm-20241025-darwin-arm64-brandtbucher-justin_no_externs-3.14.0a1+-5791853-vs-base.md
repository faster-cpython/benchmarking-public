# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 185 ms: 1.01x slower                                                      |
| docutils       | 1.56 sec                                                               | 1.57 sec: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg               | 218 ms                                                                 | 214 ms: 1.02x faster                                                      |
| asyncio_websockets               | 243 ms                                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                 | 336 ms: 1.00x slower                                                      |
| async_tree_io_tg                 | 611 ms                                                                 | 612 ms: 1.00x slower                                                      |
| async_tree_eager_tg              | 42.4 ms                                                                | 42.6 ms: 1.00x slower                                                     |
| async_tree_none                  | 198 ms                                                                 | 200 ms: 1.01x slower                                                      |
| async_generators                 | 292 ms                                                                 | 295 ms: 1.01x slower                                                      |
| coroutines                       | 16.4 ms                                                                | 16.7 ms: 1.01x slower                                                     |
| async_tree_eager                 | 63.5 ms                                                                | 64.9 ms: 1.02x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 65.9 ms                                                                | 65.2 ms: 1.01x faster                                                     |
| pidigits       | 283 ms                                                                 | 284 ms: 1.00x slower                                                      |
| float          | 48.3 ms                                                                | 48.9 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 142 ms                                                                 | 141 ms: 1.01x faster                                                      |
| regex_effbot   | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                     |
| regex_compile  | 74.9 ms                                                                | 76.6 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads         | 16.6 us                                                                | 16.5 us: 1.00x faster                                                     |
| xml_etree_generate | 49.4 ms                                                                | 49.7 ms: 1.01x slower                                                     |
| pickle_pure_python | 178 us                                                                 | 180 us: 1.01x slower                                                      |
| tomli_loads        | 1.25 sec                                                               | 1.27 sec: 1.02x slower                                                    |
| xml_etree_process  | 34.6 ms                                                                | 35.2 ms: 1.02x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                                | 18.2 ms: 1.01x faster                                                     |
| python_startup_no_site | 14.4 ms                                                                | 14.3 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                     |
| mako            | 6.44 ms                                                                | 6.56 ms: 1.02x slower                                                     |
| genshi_xml      | 42.6 ms                                                                | 43.9 ms: 1.03x slower                                                     |
| genshi_text     | 17.1 ms                                                                | 17.6 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| comprehensions                   | 17.0 us                                                                | 13.6 us: 1.25x faster                                                     |
| async_tree_none_tg               | 218 ms                                                                 | 214 ms: 1.02x faster                                                      |
| json                             | 2.91 ms                                                                | 2.85 ms: 1.02x faster                                                     |
| generators                       | 25.3 ms                                                                | 24.9 ms: 1.02x faster                                                     |
| python_startup                   | 18.5 ms                                                                | 18.2 ms: 1.01x faster                                                     |
| logging_simple                   | 3.17 us                                                                | 3.13 us: 1.01x faster                                                     |
| thrift                           | 426 us                                                                 | 422 us: 1.01x faster                                                      |
| nbody                            | 65.9 ms                                                                | 65.2 ms: 1.01x faster                                                     |
| regex_dna                        | 142 ms                                                                 | 141 ms: 1.01x faster                                                      |
| logging_format                   | 3.44 us                                                                | 3.42 us: 1.01x faster                                                     |
| python_startup_no_site           | 14.4 ms                                                                | 14.3 ms: 1.01x faster                                                     |
| logging_silent                   | 70.0 ns                                                                | 69.7 ns: 1.00x faster                                                     |
| json_loads                       | 16.6 us                                                                | 16.5 us: 1.00x faster                                                     |
| asyncio_websockets               | 243 ms                                                                 | 242 ms: 1.00x faster                                                      |
| scimark_sparse_mat_mult          | 3.16 ms                                                                | 3.17 ms: 1.00x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                 | 336 ms: 1.00x slower                                                      |
| async_tree_io_tg                 | 611 ms                                                                 | 612 ms: 1.00x slower                                                      |
| async_tree_eager_tg              | 42.4 ms                                                                | 42.6 ms: 1.00x slower                                                     |
| pidigits                         | 283 ms                                                                 | 284 ms: 1.00x slower                                                      |
| scimark_fft                      | 190 ms                                                                 | 191 ms: 1.00x slower                                                      |
| docutils                         | 1.56 sec                                                               | 1.57 sec: 1.00x slower                                                    |
| coverage                         | 43.7 ms                                                                | 44.0 ms: 1.00x slower                                                     |
| spectral_norm                    | 69.7 ms                                                                | 70.1 ms: 1.01x slower                                                     |
| gc_traversal                     | 2.94 ms                                                                | 2.96 ms: 1.01x slower                                                     |
| xml_etree_generate               | 49.4 ms                                                                | 49.7 ms: 1.01x slower                                                     |
| go                               | 100 ms                                                                 | 101 ms: 1.01x slower                                                      |
| async_tree_none                  | 198 ms                                                                 | 200 ms: 1.01x slower                                                      |
| 2to3                             | 183 ms                                                                 | 185 ms: 1.01x slower                                                      |
| sqlglot_transpile                | 1.08 ms                                                                | 1.08 ms: 1.01x slower                                                     |
| mdp                              | 1.55 sec                                                               | 1.56 sec: 1.01x slower                                                    |
| pickle_pure_python               | 178 us                                                                 | 180 us: 1.01x slower                                                      |
| bench_thread_pool                | 473 us                                                                 | 477 us: 1.01x slower                                                      |
| meteor_contest                   | 74.4 ms                                                                | 75.1 ms: 1.01x slower                                                     |
| create_gc_cycles                 | 1.33 ms                                                                | 1.34 ms: 1.01x slower                                                     |
| dulwich_log                      | 28.8 ms                                                                | 29.1 ms: 1.01x slower                                                     |
| regex_effbot                     | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                     |
| async_generators                 | 292 ms                                                                 | 295 ms: 1.01x slower                                                      |
| django_template                  | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                     |
| sqlalchemy_declarative           | 61.8 ms                                                                | 62.5 ms: 1.01x slower                                                     |
| sqlglot_parse                    | 879 us                                                                 | 889 us: 1.01x slower                                                      |
| sympy_str                        | 152 ms                                                                 | 153 ms: 1.01x slower                                                      |
| bpe_tokeniser                    | 3.04 sec                                                               | 3.07 sec: 1.01x slower                                                    |
| float                            | 48.3 ms                                                                | 48.9 ms: 1.01x slower                                                     |
| crypto_pyaes                     | 54.5 ms                                                                | 55.2 ms: 1.01x slower                                                     |
| deepcopy_memo                    | 16.5 us                                                                | 16.7 us: 1.01x slower                                                     |
| richards_super                   | 37.9 ms                                                                | 38.4 ms: 1.01x slower                                                     |
| sqlalchemy_imperative            | 6.55 ms                                                                | 6.64 ms: 1.01x slower                                                     |
| coroutines                       | 16.4 ms                                                                | 16.7 ms: 1.01x slower                                                     |
| sympy_sum                        | 79.8 ms                                                                | 81.0 ms: 1.01x slower                                                     |
| richards                         | 34.1 ms                                                                | 34.7 ms: 1.02x slower                                                     |
| pycparser                        | 683 ms                                                                 | 694 ms: 1.02x slower                                                      |
| scimark_sor                      | 85.9 ms                                                                | 87.3 ms: 1.02x slower                                                     |
| sqlglot_normalize                | 187 ms                                                                 | 190 ms: 1.02x slower                                                      |
| sqlglot_optimize                 | 37.4 ms                                                                | 38.0 ms: 1.02x slower                                                     |
| tomli_loads                      | 1.25 sec                                                               | 1.27 sec: 1.02x slower                                                    |
| xml_etree_process                | 34.6 ms                                                                | 35.2 ms: 1.02x slower                                                     |
| deltablue                        | 2.41 ms                                                                | 2.46 ms: 1.02x slower                                                     |
| scimark_lu                       | 64.5 ms                                                                | 65.6 ms: 1.02x slower                                                     |
| sympy_integrate                  | 12.5 ms                                                                | 12.7 ms: 1.02x slower                                                     |
| mako                             | 6.44 ms                                                                | 6.56 ms: 1.02x slower                                                     |
| pyflate                          | 326 ms                                                                 | 332 ms: 1.02x slower                                                      |
| telco                            | 4.48 ms                                                                | 4.57 ms: 1.02x slower                                                     |
| async_tree_eager                 | 63.5 ms                                                                | 64.9 ms: 1.02x slower                                                     |
| regex_compile                    | 74.9 ms                                                                | 76.6 ms: 1.02x slower                                                     |
| chaos                            | 41.6 ms                                                                | 42.6 ms: 1.02x slower                                                     |
| sympy_expand                     | 247 ms                                                                 | 253 ms: 1.03x slower                                                      |
| nqueens                          | 58.6 ms                                                                | 60.1 ms: 1.03x slower                                                     |
| scimark_monte_carlo              | 45.3 ms                                                                | 46.5 ms: 1.03x slower                                                     |
| hexiom                           | 5.01 ms                                                                | 5.15 ms: 1.03x slower                                                     |
| genshi_xml                       | 42.6 ms                                                                | 43.9 ms: 1.03x slower                                                     |
| genshi_text                      | 17.1 ms                                                                | 17.6 ms: 1.03x slower                                                     |
| raytrace                         | 170 ms                                                                 | 177 ms: 1.04x slower                                                      |
| pprint_safe_repr                 | 500 ms                                                                 | 521 ms: 1.04x slower                                                      |
| fannkuch                         | 265 ms                                                                 | 282 ms: 1.06x slower                                                      |
| pprint_pformat                   | 991 ms                                                                 | 1.06 sec: 1.07x slower                                                    |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (24): tornado_http, typing_runtime_protocols, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, bench_mp_pool, deepcopy_reduce, unpickle_pure_python, deepcopy, async_tree_cpu_io_mixed, html5lib, xml_etree_parse, async_tree_memoization_tg, regex_v8, async_tree_eager_io, json_dumps, async_tree_eager_io_tg, pathlib, async_tree_io, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, sphinx, async_tree_eager_memoization, pylint

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x