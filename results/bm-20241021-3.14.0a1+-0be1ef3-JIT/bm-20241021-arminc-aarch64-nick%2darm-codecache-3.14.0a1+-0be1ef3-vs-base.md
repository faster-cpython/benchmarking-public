# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.005x faster
- HPT reliability: 95.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 385 ms                                                                   | 375 ms: 1.03x faster                                              |
| docutils       | 3.64 sec                                                                 | 3.55 sec: 1.02x faster                                            |
| sphinx         | 1.47 sec                                                                 | 1.42 sec: 1.04x faster                                            |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg | 1.25 sec                                                                 | 1.27 sec: 1.01x slower                                            |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                      |

Benchmark hidden because not significant (10): async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, coroutines, async_tree_none, async_tree_memoization, asyncio_websockets, async_generators, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 96.8 ms                                                                  | 97.7 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                   | 172 ms: 1.03x faster                                              |
| regex_dna      | 253 ms                                                                   | 249 ms: 1.02x faster                                              |
| regex_effbot   | 4.94 ms                                                                  | 5.06 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_iterparse  | 153 ms                                                                   | 149 ms: 1.03x faster                                              |
| unpickle_pure_python | 272 us                                                                   | 266 us: 1.02x faster                                              |
| json_dumps           | 14.4 ms                                                                  | 14.2 ms: 1.01x faster                                             |
| xml_etree_parse      | 187 ms                                                                   | 189 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                    | 1.00x faster                                                      |

Benchmark hidden because not significant (5): xml_etree_generate, json_loads, pickle_pure_python, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.5 ms                                                                  | 14.6 ms: 1.01x slower                                             |
| python_startup_no_site | 8.70 ms                                                                  | 8.78 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 85.7 ms                                                                  | 82.5 ms: 1.04x faster                                             |
| mako           | 13.2 ms                                                                  | 13.2 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_reduce          | 4.06 us                                                                  | 3.87 us: 1.05x faster                                             |
| dulwich_log              | 81.5 ms                                                                  | 78.1 ms: 1.04x faster                                             |
| sqlglot_optimize         | 83.1 ms                                                                  | 79.9 ms: 1.04x faster                                             |
| genshi_xml               | 85.7 ms                                                                  | 82.5 ms: 1.04x faster                                             |
| sphinx                   | 1.47 sec                                                                 | 1.42 sec: 1.04x faster                                            |
| pyflate                  | 638 ms                                                                   | 616 ms: 1.04x faster                                              |
| richards                 | 63.2 ms                                                                  | 61.1 ms: 1.03x faster                                             |
| regex_compile            | 177 ms                                                                   | 172 ms: 1.03x faster                                              |
| 2to3                     | 385 ms                                                                   | 375 ms: 1.03x faster                                              |
| xml_etree_iterparse      | 153 ms                                                                   | 149 ms: 1.03x faster                                              |
| hexiom                   | 10.4 ms                                                                  | 10.1 ms: 1.03x faster                                             |
| sqlglot_normalize        | 157 ms                                                                   | 153 ms: 1.03x faster                                              |
| sympy_str                | 361 ms                                                                   | 353 ms: 1.03x faster                                              |
| sympy_sum                | 219 ms                                                                   | 214 ms: 1.02x faster                                              |
| pycparser                | 1.53 sec                                                                 | 1.49 sec: 1.02x faster                                            |
| unpickle_pure_python     | 272 us                                                                   | 266 us: 1.02x faster                                              |
| docutils                 | 3.64 sec                                                                 | 3.55 sec: 1.02x faster                                            |
| coverage                 | 101 ms                                                                   | 99.0 ms: 1.02x faster                                             |
| deepcopy                 | 382 us                                                                   | 374 us: 1.02x faster                                              |
| regex_dna                | 253 ms                                                                   | 249 ms: 1.02x faster                                              |
| sqlglot_transpile        | 2.19 ms                                                                  | 2.16 ms: 1.01x faster                                             |
| sympy_expand             | 595 ms                                                                   | 588 ms: 1.01x faster                                              |
| json_dumps               | 14.4 ms                                                                  | 14.2 ms: 1.01x faster                                             |
| spectral_norm            | 155 ms                                                                   | 154 ms: 1.01x faster                                              |
| typing_runtime_protocols | 214 us                                                                   | 212 us: 1.01x faster                                              |
| mdp                      | 3.49 sec                                                                 | 3.48 sec: 1.00x faster                                            |
| mako                     | 13.2 ms                                                                  | 13.2 ms: 1.00x slower                                             |
| bpe_tokeniser            | 5.97 sec                                                                 | 6.01 sec: 1.01x slower                                            |
| python_startup           | 14.5 ms                                                                  | 14.6 ms: 1.01x slower                                             |
| python_startup_no_site   | 8.70 ms                                                                  | 8.78 ms: 1.01x slower                                             |
| float                    | 96.8 ms                                                                  | 97.7 ms: 1.01x slower                                             |
| thrift                   | 964 us                                                                   | 974 us: 1.01x slower                                              |
| nqueens                  | 127 ms                                                                   | 128 ms: 1.01x slower                                              |
| bench_thread_pool        | 1.36 ms                                                                  | 1.38 ms: 1.01x slower                                             |
| async_tree_io_tg         | 1.25 sec                                                                 | 1.27 sec: 1.01x slower                                            |
| xml_etree_parse          | 187 ms                                                                   | 189 ms: 1.01x slower                                              |
| go                       | 185 ms                                                                   | 188 ms: 1.02x slower                                              |
| pprint_pformat           | 2.51 sec                                                                 | 2.55 sec: 1.02x slower                                            |
| scimark_monte_carlo      | 89.1 ms                                                                  | 90.6 ms: 1.02x slower                                             |
| chaos                    | 85.0 ms                                                                  | 86.8 ms: 1.02x slower                                             |
| regex_effbot             | 4.94 ms                                                                  | 5.06 ms: 1.02x slower                                             |
| Geometric mean           | (ref)                                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (48): bench_mp_pool, pylint, json, django_template, sympy_integrate, async_tree_io, richards_super, comprehensions, fannkuch, telco, crypto_pyaes, logging_silent, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pathlib, coroutines, async_tree_none, xml_etree_generate, logging_simple, pidigits, genshi_text, pprint_safe_repr, async_tree_memoization, asyncio_websockets, meteor_contest, json_loads, pickle_pure_python, async_generators, tomli_loads, nbody, scimark_fft, scimark_lu, create_gc_cycles, raytrace, regex_v8, html5lib, gc_traversal, logging_format, async_tree_memoization_tg, deepcopy_memo, xml_etree_process, async_tree_none_tg, tornado_http, sqlglot_parse, generators, scimark_sor, deltablue

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 95.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x