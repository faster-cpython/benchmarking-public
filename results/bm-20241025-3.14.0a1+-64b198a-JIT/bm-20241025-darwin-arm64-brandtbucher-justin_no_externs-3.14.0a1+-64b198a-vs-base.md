# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 186 ms: 1.01x slower                                                      |
| docutils       | 1.56 sec                                                               | 1.57 sec: 1.01x slower                                                    |
| html5lib       | 32.8 ms                                                                | 32.6 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg               | 218 ms                                                                 | 213 ms: 1.02x faster                                                      |
| asyncio_websockets               | 243 ms                                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                 | 336 ms: 1.00x slower                                                      |
| coroutines                       | 16.4 ms                                                                | 16.5 ms: 1.00x slower                                                     |
| async_tree_eager_tg              | 42.4 ms                                                                | 42.8 ms: 1.01x slower                                                     |
| async_tree_eager                 | 63.5 ms                                                                | 64.2 ms: 1.01x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed_tg, async_generators, async_tree_eager_io_tg, async_tree_eager_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_eager_memoization, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 65.9 ms                                                                | 65.0 ms: 1.01x faster                                                     |
| float          | 48.3 ms                                                                | 48.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                     |
| regex_dna      | 142 ms                                                                 | 144 ms: 1.01x slower                                                      |
| regex_compile  | 74.9 ms                                                                | 76.6 ms: 1.02x slower                                                     |
| regex_effbot   | 2.45 ms                                                                | 2.56 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse    | 108 ms                                                                 | 105 ms: 1.03x faster                                                      |
| json_dumps         | 7.15 ms                                                                | 7.16 ms: 1.00x slower                                                     |
| xml_etree_generate | 49.4 ms                                                                | 49.6 ms: 1.00x slower                                                     |
| json_loads         | 16.6 us                                                                | 16.6 us: 1.00x slower                                                     |
| pickle_pure_python | 178 us                                                                 | 179 us: 1.01x slower                                                      |
| tomli_loads        | 1.25 sec                                                               | 1.27 sec: 1.02x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                                | 18.1 ms: 1.02x faster                                                     |
| python_startup_no_site | 14.4 ms                                                                | 14.3 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 17.1 ms                                                                | 16.6 ms: 1.03x faster                                                     |
| mako            | 6.44 ms                                                                | 6.58 ms: 1.02x slower                                                     |
| genshi_xml      | 42.6 ms                                                                | 44.1 ms: 1.04x slower                                                     |
| django_template | 23.0 ms                                                                | 24.1 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| comprehensions                   | 17.0 us                                                                | 13.5 us: 1.26x faster                                                     |
| genshi_text                      | 17.1 ms                                                                | 16.6 ms: 1.03x faster                                                     |
| xml_etree_parse                  | 108 ms                                                                 | 105 ms: 1.03x faster                                                      |
| async_tree_none_tg               | 218 ms                                                                 | 213 ms: 1.02x faster                                                      |
| python_startup                   | 18.5 ms                                                                | 18.1 ms: 1.02x faster                                                     |
| logging_simple                   | 3.17 us                                                                | 3.11 us: 1.02x faster                                                     |
| json                             | 2.91 ms                                                                | 2.86 ms: 1.02x faster                                                     |
| generators                       | 25.3 ms                                                                | 24.9 ms: 1.01x faster                                                     |
| nbody                            | 65.9 ms                                                                | 65.0 ms: 1.01x faster                                                     |
| thrift                           | 426 us                                                                 | 423 us: 1.01x faster                                                      |
| bench_mp_pool                    | 62.0 ms                                                                | 61.6 ms: 1.01x faster                                                     |
| python_startup_no_site           | 14.4 ms                                                                | 14.3 ms: 1.01x faster                                                     |
| scimark_lu                       | 64.5 ms                                                                | 64.1 ms: 1.01x faster                                                     |
| html5lib                         | 32.8 ms                                                                | 32.6 ms: 1.01x faster                                                     |
| logging_format                   | 3.44 us                                                                | 3.42 us: 1.01x faster                                                     |
| deepcopy_reduce                  | 1.53 us                                                                | 1.52 us: 1.01x faster                                                     |
| asyncio_websockets               | 243 ms                                                                 | 242 ms: 1.00x faster                                                      |
| bpe_tokeniser                    | 3.04 sec                                                               | 3.03 sec: 1.00x faster                                                    |
| bench_thread_pool                | 473 us                                                                 | 471 us: 1.00x faster                                                      |
| create_gc_cycles                 | 1.33 ms                                                                | 1.32 ms: 1.00x faster                                                     |
| regex_v8                         | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                     |
| scimark_sparse_mat_mult          | 3.16 ms                                                                | 3.17 ms: 1.00x slower                                                     |
| json_dumps                       | 7.15 ms                                                                | 7.16 ms: 1.00x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                 | 336 ms: 1.00x slower                                                      |
| deepcopy                         | 156 us                                                                 | 156 us: 1.00x slower                                                      |
| xml_etree_generate               | 49.4 ms                                                                | 49.6 ms: 1.00x slower                                                     |
| json_loads                       | 16.6 us                                                                | 16.6 us: 1.00x slower                                                     |
| sqlglot_transpile                | 1.08 ms                                                                | 1.08 ms: 1.00x slower                                                     |
| coroutines                       | 16.4 ms                                                                | 16.5 ms: 1.00x slower                                                     |
| coverage                         | 43.7 ms                                                                | 44.0 ms: 1.01x slower                                                     |
| float                            | 48.3 ms                                                                | 48.6 ms: 1.01x slower                                                     |
| docutils                         | 1.56 sec                                                               | 1.57 sec: 1.01x slower                                                    |
| pickle_pure_python               | 178 us                                                                 | 179 us: 1.01x slower                                                      |
| crypto_pyaes                     | 54.5 ms                                                                | 54.9 ms: 1.01x slower                                                     |
| sympy_sum                        | 79.8 ms                                                                | 80.4 ms: 1.01x slower                                                     |
| deltablue                        | 2.41 ms                                                                | 2.43 ms: 1.01x slower                                                     |
| pathlib                          | 22.4 ms                                                                | 22.6 ms: 1.01x slower                                                     |
| async_tree_eager_tg              | 42.4 ms                                                                | 42.8 ms: 1.01x slower                                                     |
| scimark_fft                      | 190 ms                                                                 | 192 ms: 1.01x slower                                                      |
| sqlglot_parse                    | 879 us                                                                 | 888 us: 1.01x slower                                                      |
| regex_dna                        | 142 ms                                                                 | 144 ms: 1.01x slower                                                      |
| scimark_monte_carlo              | 45.3 ms                                                                | 45.8 ms: 1.01x slower                                                     |
| scimark_sor                      | 85.9 ms                                                                | 86.8 ms: 1.01x slower                                                     |
| async_tree_eager                 | 63.5 ms                                                                | 64.2 ms: 1.01x slower                                                     |
| mdp                              | 1.55 sec                                                               | 1.56 sec: 1.01x slower                                                    |
| deepcopy_memo                    | 16.5 us                                                                | 16.7 us: 1.01x slower                                                     |
| sympy_str                        | 152 ms                                                                 | 154 ms: 1.01x slower                                                      |
| fannkuch                         | 265 ms                                                                 | 269 ms: 1.01x slower                                                      |
| raytrace                         | 170 ms                                                                 | 172 ms: 1.01x slower                                                      |
| 2to3                             | 183 ms                                                                 | 186 ms: 1.01x slower                                                      |
| pyflate                          | 326 ms                                                                 | 330 ms: 1.01x slower                                                      |
| richards_super                   | 37.9 ms                                                                | 38.4 ms: 1.01x slower                                                     |
| sympy_expand                     | 247 ms                                                                 | 250 ms: 1.01x slower                                                      |
| nqueens                          | 58.6 ms                                                                | 59.4 ms: 1.01x slower                                                     |
| pycparser                        | 683 ms                                                                 | 693 ms: 1.01x slower                                                      |
| go                               | 100 ms                                                                 | 102 ms: 1.01x slower                                                      |
| dulwich_log                      | 28.8 ms                                                                | 29.2 ms: 1.02x slower                                                     |
| sympy_integrate                  | 12.5 ms                                                                | 12.7 ms: 1.02x slower                                                     |
| chaos                            | 41.6 ms                                                                | 42.3 ms: 1.02x slower                                                     |
| sqlglot_optimize                 | 37.4 ms                                                                | 38.0 ms: 1.02x slower                                                     |
| sqlglot_normalize                | 187 ms                                                                 | 190 ms: 1.02x slower                                                      |
| tomli_loads                      | 1.25 sec                                                               | 1.27 sec: 1.02x slower                                                    |
| richards                         | 34.1 ms                                                                | 34.8 ms: 1.02x slower                                                     |
| telco                            | 4.48 ms                                                                | 4.57 ms: 1.02x slower                                                     |
| pprint_safe_repr                 | 500 ms                                                                 | 511 ms: 1.02x slower                                                      |
| mako                             | 6.44 ms                                                                | 6.58 ms: 1.02x slower                                                     |
| regex_compile                    | 74.9 ms                                                                | 76.6 ms: 1.02x slower                                                     |
| hexiom                           | 5.01 ms                                                                | 5.17 ms: 1.03x slower                                                     |
| genshi_xml                       | 42.6 ms                                                                | 44.1 ms: 1.04x slower                                                     |
| regex_effbot                     | 2.45 ms                                                                | 2.56 ms: 1.04x slower                                                     |
| django_template                  | 23.0 ms                                                                | 24.1 ms: 1.05x slower                                                     |
| pprint_pformat                   | 991 ms                                                                 | 1.04 sec: 1.05x slower                                                    |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (27): tornado_http, xml_etree_iterparse, typing_runtime_protocols, unpickle_pure_python, async_tree_cpu_io_mixed_tg, async_generators, async_tree_eager_io_tg, spectral_norm, async_tree_eager_io, async_tree_memoization_tg, async_tree_io_tg, xml_etree_process, pidigits, gc_traversal, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, sqlalchemy_declarative, async_tree_io, sqlalchemy_imperative, meteor_contest, logging_silent, async_tree_eager_memoization, async_tree_memoization, sphinx, pylint

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x