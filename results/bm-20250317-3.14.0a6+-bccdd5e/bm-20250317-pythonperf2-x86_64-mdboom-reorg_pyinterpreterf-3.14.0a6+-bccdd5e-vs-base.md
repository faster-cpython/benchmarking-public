# Results vs. base

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: bccdd5e
- commit date: 2025-03-17
- overall geometric mean: 1.002x faster
- HPT reliability: 65.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                       | 285 ms: 1.00x faster                                                         |
| html5lib       | 70.2 ms                                                                      | 69.6 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 422 ms                                                                       | 416 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 278 ms                                                                       | 275 ms: 1.01x faster                                                         |
| async_tree_memoization_tg  | 342 ms                                                                       | 339 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 507 ms: 1.01x faster                                                         |
| asyncio_websockets         | 386 ms                                                                       | 383 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 520 ms                                                                       | 523 ms: 1.01x slower                                                         |
| async_tree_none            | 290 ms                                                                       | 292 ms: 1.01x slower                                                         |
| async_tree_memoization     | 347 ms                                                                       | 350 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                       | 254 ms: 1.00x faster                                                         |
| nbody          | 99.3 ms                                                                      | 108 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                      | 23.5 ms: 1.02x faster                                                        |
| regex_compile  | 138 ms                                                                       | 136 ms: 1.02x faster                                                         |
| regex_dna      | 229 ms                                                                       | 234 ms: 1.02x slower                                                         |
| regex_effbot   | 3.07 ms                                                                      | 3.14 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 342 us                                                                       | 335 us: 1.02x faster                                                         |
| json_loads           | 26.1 us                                                                      | 25.7 us: 1.02x faster                                                        |
| xml_etree_parse      | 143 ms                                                                       | 141 ms: 1.02x faster                                                         |
| json_dumps           | 11.5 ms                                                                      | 11.4 ms: 1.01x faster                                                        |
| unpickle_pure_python | 228 us                                                                       | 226 us: 1.01x faster                                                         |
| xml_etree_process    | 60.7 ms                                                                      | 60.2 ms: 1.01x faster                                                        |
| tomli_loads          | 2.18 sec                                                                     | 2.20 sec: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 10.5 ms                                                                      | 10.5 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 37.7 ms                                                                      | 37.0 ms: 1.02x faster                                                        |
| genshi_xml      | 56.7 ms                                                                      | 56.2 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| logging_simple             | 6.70 us                                                                      | 6.33 us: 1.06x faster                                                        |
| logging_format             | 7.36 us                                                                      | 7.05 us: 1.04x faster                                                        |
| subparsers                 | 24.1 ms                                                                      | 23.5 ms: 1.03x faster                                                        |
| comprehensions             | 18.1 us                                                                      | 17.7 us: 1.03x faster                                                        |
| richards                   | 48.8 ms                                                                      | 47.8 ms: 1.02x faster                                                        |
| pickle_pure_python         | 342 us                                                                       | 335 us: 1.02x faster                                                         |
| spectral_norm              | 92.0 ms                                                                      | 90.1 ms: 1.02x faster                                                        |
| django_template            | 37.7 ms                                                                      | 37.0 ms: 1.02x faster                                                        |
| mdp                        | 2.55 sec                                                                     | 2.50 sec: 1.02x faster                                                       |
| telco                      | 8.13 ms                                                                      | 7.98 ms: 1.02x faster                                                        |
| regex_v8                   | 24.0 ms                                                                      | 23.5 ms: 1.02x faster                                                        |
| richards_super             | 55.0 ms                                                                      | 54.0 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 67.1 ms                                                                      | 66.0 ms: 1.02x faster                                                        |
| json_loads                 | 26.1 us                                                                      | 25.7 us: 1.02x faster                                                        |
| regex_compile              | 138 ms                                                                       | 136 ms: 1.02x faster                                                         |
| chaos                      | 65.3 ms                                                                      | 64.3 ms: 1.02x faster                                                        |
| xml_etree_parse            | 143 ms                                                                       | 141 ms: 1.02x faster                                                         |
| async_generators           | 422 ms                                                                       | 416 ms: 1.02x faster                                                         |
| generators                 | 28.6 ms                                                                      | 28.2 ms: 1.02x faster                                                        |
| hexiom                     | 6.54 ms                                                                      | 6.44 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 177 us                                                                       | 174 us: 1.01x faster                                                         |
| sqlglot_v2_parse           | 1.43 ms                                                                      | 1.40 ms: 1.01x faster                                                        |
| sqlglot_v2_transpile       | 1.81 ms                                                                      | 1.79 ms: 1.01x faster                                                        |
| async_tree_none_tg         | 278 ms                                                                       | 275 ms: 1.01x faster                                                         |
| json_dumps                 | 11.5 ms                                                                      | 11.4 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 228 us                                                                       | 226 us: 1.01x faster                                                         |
| async_tree_memoization_tg  | 342 ms                                                                       | 339 ms: 1.01x faster                                                         |
| genshi_xml                 | 56.7 ms                                                                      | 56.2 ms: 1.01x faster                                                        |
| pyflate                    | 474 ms                                                                       | 470 ms: 1.01x faster                                                         |
| html5lib                   | 70.2 ms                                                                      | 69.6 ms: 1.01x faster                                                        |
| pathlib                    | 17.3 ms                                                                      | 17.2 ms: 1.01x faster                                                        |
| xml_etree_process          | 60.7 ms                                                                      | 60.2 ms: 1.01x faster                                                        |
| thrift                     | 866 us                                                                       | 860 us: 1.01x faster                                                         |
| deepcopy_reduce            | 3.03 us                                                                      | 3.01 us: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 507 ms: 1.01x faster                                                         |
| asyncio_websockets         | 386 ms                                                                       | 383 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult    | 4.74 ms                                                                      | 4.71 ms: 1.01x faster                                                        |
| deltablue                  | 3.40 ms                                                                      | 3.39 ms: 1.01x faster                                                        |
| many_optionals             | 1.04 ms                                                                      | 1.04 ms: 1.01x faster                                                        |
| deepcopy_memo              | 29.9 us                                                                      | 29.7 us: 1.00x faster                                                        |
| 2to3                       | 286 ms                                                                       | 285 ms: 1.00x faster                                                         |
| sqlalchemy_declarative     | 146 ms                                                                       | 146 ms: 1.00x faster                                                         |
| sympy_integrate            | 23.5 ms                                                                      | 23.5 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                                       | 254 ms: 1.00x faster                                                         |
| python_startup_no_site     | 10.5 ms                                                                      | 10.5 ms: 1.00x slower                                                        |
| meteor_contest             | 128 ms                                                                       | 128 ms: 1.00x slower                                                         |
| shortest_path              | 452 ms                                                                       | 453 ms: 1.00x slower                                                         |
| scimark_sor                | 110 ms                                                                       | 111 ms: 1.00x slower                                                         |
| scimark_fft                | 318 ms                                                                       | 319 ms: 1.00x slower                                                         |
| sqlite_synth               | 2.81 us                                                                      | 2.82 us: 1.01x slower                                                        |
| scimark_lu                 | 101 ms                                                                       | 102 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 520 ms                                                                       | 523 ms: 1.01x slower                                                         |
| tomli_loads                | 2.18 sec                                                                     | 2.20 sec: 1.01x slower                                                       |
| connected_components       | 429 ms                                                                       | 433 ms: 1.01x slower                                                         |
| async_tree_none            | 290 ms                                                                       | 292 ms: 1.01x slower                                                         |
| crypto_pyaes               | 82.9 ms                                                                      | 83.6 ms: 1.01x slower                                                        |
| async_tree_memoization     | 347 ms                                                                       | 350 ms: 1.01x slower                                                         |
| bpe_tokeniser              | 4.81 sec                                                                     | 4.86 sec: 1.01x slower                                                       |
| sqlalchemy_imperative      | 18.0 ms                                                                      | 18.3 ms: 1.01x slower                                                        |
| pycparser                  | 1.27 sec                                                                     | 1.29 sec: 1.02x slower                                                       |
| raytrace                   | 293 ms                                                                       | 297 ms: 1.02x slower                                                         |
| pprint_safe_repr           | 809 ms                                                                       | 822 ms: 1.02x slower                                                         |
| nqueens                    | 94.8 ms                                                                      | 96.3 ms: 1.02x slower                                                        |
| sqlglot_v2_optimize        | 58.4 ms                                                                      | 59.4 ms: 1.02x slower                                                        |
| go                         | 131 ms                                                                       | 133 ms: 1.02x slower                                                         |
| coverage                   | 81.1 ms                                                                      | 82.6 ms: 1.02x slower                                                        |
| fannkuch                   | 386 ms                                                                       | 393 ms: 1.02x slower                                                         |
| deepcopy                   | 289 us                                                                       | 295 us: 1.02x slower                                                         |
| regex_dna                  | 229 ms                                                                       | 234 ms: 1.02x slower                                                         |
| regex_effbot               | 3.07 ms                                                                      | 3.14 ms: 1.02x slower                                                        |
| sqlglot_v2_normalize       | 117 ms                                                                       | 120 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.64 sec                                                                     | 1.68 sec: 1.03x slower                                                       |
| nbody                      | 99.3 ms                                                                      | 108 ms: 1.09x slower                                                         |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (23): async_tree_io_tg, create_gc_cycles, bench_thread_pool, json, genshi_text, async_tree_io, xml_etree_generate, sympy_expand, python_startup, logging_silent, mako, gc_traversal, k_core, sympy_str, docutils, dulwich_log, sympy_sum, coroutines, pylint, float, xml_etree_iterparse, sphinx, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 65.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x