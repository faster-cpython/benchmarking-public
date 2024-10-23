# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.00x faster
- HPT reliability: 98.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 384 ms                                                                   | 375 ms: 1.03x faster                                              |
| docutils       | 3.61 sec                                                                 | 3.55 sec: 1.01x faster                                            |
| sphinx         | 1.47 sec                                                                 | 1.42 sec: 1.03x faster                                            |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization | 597 ms                                                                   | 607 ms: 1.02x slower                                              |
| async_tree_io_tg       | 1.23 sec                                                                 | 1.27 sec: 1.03x slower                                            |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                      |

Benchmark hidden because not significant (9): coroutines, async_tree_io, async_generators, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 97.0 ms                                                                  | 97.7 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                   | 249 ms: 1.03x faster                                              |
| regex_v8       | 31.8 ms                                                                  | 31.2 ms: 1.02x faster                                             |
| regex_compile  | 175 ms                                                                   | 172 ms: 1.02x faster                                              |
| regex_effbot   | 5.00 ms                                                                  | 5.06 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 270 us                                                                   | 266 us: 1.02x faster                                              |
| json_loads           | 31.5 us                                                                  | 31.8 us: 1.01x slower                                             |
| xml_etree_parse      | 187 ms                                                                   | 189 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                    | 1.00x faster                                                      |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, tomli_loads, xml_etree_iterparse, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 14.5 ms                                                                  | 14.6 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 53.5 ms                                                                  | 52.3 ms: 1.02x faster                                             |
| genshi_xml      | 84.1 ms                                                                  | 82.5 ms: 1.02x faster                                             |
| Geometric mean  | (ref)                                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| spectral_norm            | 160 ms                                                                   | 154 ms: 1.04x faster                                              |
| sphinx                   | 1.47 sec                                                                 | 1.42 sec: 1.03x faster                                            |
| regex_dna                | 257 ms                                                                   | 249 ms: 1.03x faster                                              |
| sqlglot_optimize         | 82.4 ms                                                                  | 79.9 ms: 1.03x faster                                             |
| richards                 | 63.1 ms                                                                  | 61.1 ms: 1.03x faster                                             |
| pycparser                | 1.54 sec                                                                 | 1.49 sec: 1.03x faster                                            |
| sqlglot_normalize        | 157 ms                                                                   | 153 ms: 1.03x faster                                              |
| richards_super           | 69.3 ms                                                                  | 67.5 ms: 1.03x faster                                             |
| 2to3                     | 384 ms                                                                   | 375 ms: 1.03x faster                                              |
| django_template          | 53.5 ms                                                                  | 52.3 ms: 1.02x faster                                             |
| typing_runtime_protocols | 217 us                                                                   | 212 us: 1.02x faster                                              |
| fannkuch                 | 526 ms                                                                   | 515 ms: 1.02x faster                                              |
| regex_v8                 | 31.8 ms                                                                  | 31.2 ms: 1.02x faster                                             |
| genshi_xml               | 84.1 ms                                                                  | 82.5 ms: 1.02x faster                                             |
| regex_compile            | 175 ms                                                                   | 172 ms: 1.02x faster                                              |
| hexiom                   | 10.3 ms                                                                  | 10.1 ms: 1.02x faster                                             |
| unpickle_pure_python     | 270 us                                                                   | 266 us: 1.02x faster                                              |
| docutils                 | 3.61 sec                                                                 | 3.55 sec: 1.01x faster                                            |
| sympy_str                | 357 ms                                                                   | 353 ms: 1.01x faster                                              |
| deepcopy_reduce          | 3.92 us                                                                  | 3.87 us: 1.01x faster                                             |
| sympy_expand             | 596 ms                                                                   | 588 ms: 1.01x faster                                              |
| pyflate                  | 623 ms                                                                   | 616 ms: 1.01x faster                                              |
| mdp                      | 3.51 sec                                                                 | 3.48 sec: 1.01x faster                                            |
| scimark_sparse_mat_mult  | 7.11 ms                                                                  | 7.13 ms: 1.00x slower                                             |
| python_startup           | 14.5 ms                                                                  | 14.6 ms: 1.00x slower                                             |
| float                    | 97.0 ms                                                                  | 97.7 ms: 1.01x slower                                             |
| pprint_pformat           | 2.53 sec                                                                 | 2.55 sec: 1.01x slower                                            |
| json_loads               | 31.5 us                                                                  | 31.8 us: 1.01x slower                                             |
| regex_effbot             | 5.00 ms                                                                  | 5.06 ms: 1.01x slower                                             |
| scimark_monte_carlo      | 89.6 ms                                                                  | 90.6 ms: 1.01x slower                                             |
| chaos                    | 85.8 ms                                                                  | 86.8 ms: 1.01x slower                                             |
| deepcopy_memo            | 38.7 us                                                                  | 39.2 us: 1.01x slower                                             |
| xml_etree_parse          | 187 ms                                                                   | 189 ms: 1.01x slower                                              |
| telco                    | 9.41 ms                                                                  | 9.56 ms: 1.02x slower                                             |
| logging_format           | 8.13 us                                                                  | 8.26 us: 1.02x slower                                             |
| async_tree_memoization   | 597 ms                                                                   | 607 ms: 1.02x slower                                              |
| dulwich_log              | 76.2 ms                                                                  | 78.1 ms: 1.02x slower                                             |
| async_tree_io_tg         | 1.23 sec                                                                 | 1.27 sec: 1.03x slower                                            |
| nqueens                  | 123 ms                                                                   | 128 ms: 1.04x slower                                              |
| Geometric mean           | (ref)                                                                    | 1.00x faster                                                      |

Benchmark hidden because not significant (50): pylint, sqlglot_transpile, deepcopy, crypto_pyaes, sympy_sum, coroutines, async_tree_io, create_gc_cycles, json_dumps, xml_etree_generate, sympy_integrate, pidigits, logging_silent, async_generators, tomli_loads, scimark_fft, xml_etree_iterparse, gc_traversal, async_tree_cpu_io_mixed_tg, pickle_pure_python, mako, pprint_safe_repr, bpe_tokeniser, comprehensions, pathlib, python_startup_no_site, raytrace, thrift, xml_etree_process, json, meteor_contest, nbody, async_tree_cpu_io_mixed, html5lib, go, async_tree_none, scimark_lu, asyncio_websockets, bench_thread_pool, coverage, async_tree_none_tg, tornado_http, logging_simple, async_tree_memoization_tg, sqlglot_parse, generators, genshi_text, deltablue, scimark_sor, bench_mp_pool

# HPT report

- Reliability score: 98.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x