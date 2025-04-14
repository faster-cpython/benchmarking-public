# Results vs. base

- fork: mdboom
- ref: unicode_hash_eq
- machine: linux-x86_64
- commit hash: ff745e5
- commit date: 2025-04-08
- overall geometric mean: 1.003x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 256 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                 | 23.5 ms                                                                | 23.0 ms: 1.02x faster                                             |
| async_generators           | 394 ms                                                                 | 396 ms: 1.00x slower                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                                 | 487 ms: 1.01x slower                                              |
| async_tree_memoization     | 310 ms                                                                 | 312 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 477 ms: 1.01x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.8 ms                                                                | 95.9 ms: 1.02x faster                                             |
| float          | 71.1 ms                                                                | 70.6 ms: 1.01x faster                                             |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 125 ms: 1.00x faster                                              |
| regex_v8       | 22.8 ms                                                                | 23.0 ms: 1.01x slower                                             |
| regex_dna      | 205 ms                                                                 | 216 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                             |
| tomli_loads          | 1.95 sec                                                               | 1.93 sec: 1.01x faster                                            |
| pickle_pure_python   | 322 us                                                                 | 320 us: 1.01x faster                                              |
| xml_etree_generate   | 84.4 ms                                                                | 85.1 ms: 1.01x slower                                             |
| json_loads           | 29.6 us                                                                | 29.8 us: 1.01x slower                                             |
| unpickle_pure_python | 215 us                                                                 | 218 us: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                             |
| python_startup_no_site | 8.16 ms                                                                | 8.20 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.4 ms                                                                | 11.3 ms: 1.01x faster                                             |
| django_template | 31.7 ms                                                                | 31.6 ms: 1.00x faster                                             |
| genshi_xml      | 48.7 ms                                                                | 49.4 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6+-3b3720f | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                 | 23.5 ms                                                                | 23.0 ms: 1.02x faster                                             |
| nbody                      | 97.8 ms                                                                | 95.9 ms: 1.02x faster                                             |
| gc_traversal               | 4.98 ms                                                                | 4.89 ms: 1.02x faster                                             |
| spectral_norm              | 100 ms                                                                 | 98.7 ms: 1.02x faster                                             |
| coverage                   | 84.4 ms                                                                | 83.4 ms: 1.01x faster                                             |
| json_dumps                 | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                             |
| dulwich_log                | 58.6 ms                                                                | 58.0 ms: 1.01x faster                                             |
| richards                   | 44.4 ms                                                                | 44.0 ms: 1.01x faster                                             |
| tomli_loads                | 1.95 sec                                                               | 1.93 sec: 1.01x faster                                            |
| pyflate                    | 455 ms                                                                 | 451 ms: 1.01x faster                                              |
| chaos                      | 58.1 ms                                                                | 57.6 ms: 1.01x faster                                             |
| pickle_pure_python         | 322 us                                                                 | 320 us: 1.01x faster                                              |
| pathlib                    | 16.5 ms                                                                | 16.4 ms: 1.01x faster                                             |
| mako                       | 11.4 ms                                                                | 11.3 ms: 1.01x faster                                             |
| float                      | 71.1 ms                                                                | 70.6 ms: 1.01x faster                                             |
| comprehensions             | 16.8 us                                                                | 16.7 us: 1.01x faster                                             |
| django_template            | 31.7 ms                                                                | 31.6 ms: 1.00x faster                                             |
| sqlglot_v2_normalize       | 107 ms                                                                 | 106 ms: 1.00x faster                                              |
| richards_super             | 50.3 ms                                                                | 50.1 ms: 1.00x faster                                             |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                              |
| sympy_str                  | 266 ms                                                                 | 267 ms: 1.00x slower                                              |
| sympy_expand               | 455 ms                                                                 | 457 ms: 1.00x slower                                              |
| sqlglot_v2_transpile       | 1.57 ms                                                                | 1.58 ms: 1.00x slower                                             |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.00x slower                                              |
| create_gc_cycles           | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                             |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                             |
| async_generators           | 394 ms                                                                 | 396 ms: 1.00x slower                                              |
| deepcopy                   | 255 us                                                                 | 256 us: 1.00x slower                                              |
| mdp                        | 1.23 sec                                                               | 1.23 sec: 1.00x slower                                            |
| python_startup_no_site     | 8.16 ms                                                                | 8.20 ms: 1.00x slower                                             |
| sqlalchemy_declarative     | 130 ms                                                                 | 131 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                                 | 487 ms: 1.01x slower                                              |
| async_tree_memoization     | 310 ms                                                                 | 312 ms: 1.01x slower                                              |
| sympy_integrate            | 19.1 ms                                                                | 19.2 ms: 1.01x slower                                             |
| 2to3                       | 254 ms                                                                 | 256 ms: 1.01x slower                                              |
| go                         | 114 ms                                                                 | 115 ms: 1.01x slower                                              |
| crypto_pyaes               | 73.5 ms                                                                | 74.0 ms: 1.01x slower                                             |
| pprint_pformat             | 1.47 sec                                                               | 1.48 sec: 1.01x slower                                            |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 477 ms: 1.01x slower                                              |
| regex_v8                   | 22.8 ms                                                                | 23.0 ms: 1.01x slower                                             |
| sqlite_synth               | 2.77 us                                                                | 2.79 us: 1.01x slower                                             |
| telco                      | 7.83 ms                                                                | 7.90 ms: 1.01x slower                                             |
| xml_etree_generate         | 84.4 ms                                                                | 85.1 ms: 1.01x slower                                             |
| bpe_tokeniser              | 4.53 sec                                                               | 4.57 sec: 1.01x slower                                            |
| json_loads                 | 29.6 us                                                                | 29.8 us: 1.01x slower                                             |
| sqlalchemy_imperative      | 16.6 ms                                                                | 16.7 ms: 1.01x slower                                             |
| scimark_monte_carlo        | 67.0 ms                                                                | 67.7 ms: 1.01x slower                                             |
| deepcopy_memo              | 29.3 us                                                                | 29.7 us: 1.01x slower                                             |
| unpickle_pure_python       | 215 us                                                                 | 218 us: 1.01x slower                                              |
| genshi_xml                 | 48.7 ms                                                                | 49.4 ms: 1.01x slower                                             |
| hexiom                     | 6.19 ms                                                                | 6.29 ms: 1.02x slower                                             |
| deltablue                  | 3.14 ms                                                                | 3.19 ms: 1.02x slower                                             |
| deepcopy_reduce            | 2.63 us                                                                | 2.69 us: 1.02x slower                                             |
| scimark_sor                | 117 ms                                                                 | 120 ms: 1.02x slower                                              |
| pycparser                  | 1.12 sec                                                               | 1.17 sec: 1.04x slower                                            |
| logging_silent             | 96.8 ns                                                                | 102 ns: 1.05x slower                                              |
| regex_dna                  | 205 ms                                                                 | 216 ms: 1.06x slower                                              |
| shortest_path              | 494 ms                                                                 | 522 ms: 1.06x slower                                              |
| connected_components       | 450 ms                                                                 | 477 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (35): async_tree_memoization_tg, typing_runtime_protocols, xml_etree_parse, k_core, scimark_sparse_mat_mult, scimark_fft, nqueens, xml_etree_iterparse, logging_format, generators, sqlglot_v2_optimize, bench_thread_pool, async_tree_io_tg, raytrace, fannkuch, asyncio_websockets, sqlglot_v2_parse, many_optionals, genshi_text, sympy_sum, docutils, logging_simple, xml_etree_process, pylint, async_tree_none_tg, async_tree_none, subparsers, json, bench_mp_pool, pprint_safe_repr, html5lib, sphinx, scimark_lu, async_tree_io, regex_effbot

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x