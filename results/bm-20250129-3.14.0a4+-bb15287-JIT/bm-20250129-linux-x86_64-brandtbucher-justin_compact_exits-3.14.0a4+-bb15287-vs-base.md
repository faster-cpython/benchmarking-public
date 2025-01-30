# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: bb15287
- commit date: 2025-01-29
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 259 ms: 1.00x faster                                                         |
| docutils       | 2.67 sec                                                               | 2.65 sec: 1.01x faster                                                       |
| html5lib       | 63.3 ms                                                                | 66.1 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 415 ms                                                                 | 407 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 504 ms                                                                 | 494 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 492 ms                                                                 | 483 ms: 1.02x faster                                                         |
| async_tree_memoization     | 332 ms                                                                 | 329 ms: 1.01x faster                                                         |
| coroutines                 | 23.4 ms                                                                | 24.0 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 86.0 ms                                                                | 86.7 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                         |
| regex_v8       | 24.1 ms                                                                | 23.9 ms: 1.01x faster                                                        |
| regex_effbot   | 3.22 ms                                                                | 3.23 ms: 1.00x slower                                                        |
| regex_dna      | 209 ms                                                                 | 213 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 196 us                                                                 | 188 us: 1.04x faster                                                         |
| tomli_loads          | 1.82 sec                                                               | 1.79 sec: 1.02x faster                                                       |
| json_loads           | 29.1 us                                                                | 28.8 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 95.8 ms                                                                | 94.9 ms: 1.01x faster                                                        |
| json_dumps           | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.06 ms                                                                | 7.11 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 59.7 ms                                                                | 57.7 ms: 1.03x faster                                                        |
| django_template | 32.9 ms                                                                | 31.9 ms: 1.03x faster                                                        |
| mako            | 9.93 ms                                                                | 9.95 ms: 1.00x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250130-linux-x86_64-python-a4722449caccc42ad644-3.14.0a4+-a472244 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| richards                   | 43.4 ms                                                                | 40.0 ms: 1.08x faster                                                        |
| richards_super             | 49.6 ms                                                                | 46.3 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 196 us                                                                 | 188 us: 1.04x faster                                                         |
| pyflate                    | 437 ms                                                                 | 420 ms: 1.04x faster                                                         |
| logging_format             | 6.36 us                                                                | 6.11 us: 1.04x faster                                                        |
| hexiom                     | 7.37 ms                                                                | 7.10 ms: 1.04x faster                                                        |
| fannkuch                   | 395 ms                                                                 | 382 ms: 1.04x faster                                                         |
| comprehensions             | 17.0 us                                                                | 16.4 us: 1.03x faster                                                        |
| genshi_xml                 | 59.7 ms                                                                | 57.7 ms: 1.03x faster                                                        |
| logging_simple             | 5.79 us                                                                | 5.61 us: 1.03x faster                                                        |
| django_template            | 32.9 ms                                                                | 31.9 ms: 1.03x faster                                                        |
| generators                 | 37.6 ms                                                                | 36.5 ms: 1.03x faster                                                        |
| go                         | 125 ms                                                                 | 121 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 727 ms                                                                 | 707 ms: 1.03x faster                                                         |
| sqlglot_normalize          | 110 ms                                                                 | 107 ms: 1.02x faster                                                         |
| scimark_fft                | 314 ms                                                                 | 307 ms: 1.02x faster                                                         |
| deepcopy_reduce            | 2.75 us                                                                | 2.69 us: 1.02x faster                                                        |
| deepcopy                   | 272 us                                                                 | 266 us: 1.02x faster                                                         |
| tomli_loads                | 1.82 sec                                                               | 1.79 sec: 1.02x faster                                                       |
| async_generators           | 415 ms                                                                 | 407 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 504 ms                                                                 | 494 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 492 ms                                                                 | 483 ms: 1.02x faster                                                         |
| scimark_lu                 | 117 ms                                                                 | 115 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 54.6 ms                                                                | 53.6 ms: 1.02x faster                                                        |
| nqueens                    | 90.8 ms                                                                | 89.2 ms: 1.02x faster                                                        |
| bpe_tokeniser              | 4.31 sec                                                               | 4.24 sec: 1.02x faster                                                       |
| deepcopy_memo              | 30.1 us                                                                | 29.6 us: 1.02x faster                                                        |
| shortest_path              | 480 ms                                                                 | 472 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.47 sec                                                               | 1.45 sec: 1.02x faster                                                       |
| pathlib                    | 16.1 ms                                                                | 15.9 ms: 1.02x faster                                                        |
| pycparser                  | 1.14 sec                                                               | 1.12 sec: 1.02x faster                                                       |
| thrift                     | 773 us                                                                 | 762 us: 1.02x faster                                                         |
| sympy_expand               | 474 ms                                                                 | 467 ms: 1.02x faster                                                         |
| json                       | 5.25 ms                                                                | 5.18 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.28 ms                                                                | 1.26 ms: 1.01x faster                                                        |
| regex_compile              | 130 ms                                                                 | 128 ms: 1.01x faster                                                         |
| scimark_sor                | 115 ms                                                                 | 114 ms: 1.01x faster                                                         |
| sympy_integrate            | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                        |
| logging_silent             | 109 ns                                                                 | 107 ns: 1.01x faster                                                         |
| regex_v8                   | 24.1 ms                                                                | 23.9 ms: 1.01x faster                                                        |
| deltablue                  | 3.46 ms                                                                | 3.43 ms: 1.01x faster                                                        |
| crypto_pyaes               | 69.8 ms                                                                | 69.1 ms: 1.01x faster                                                        |
| json_loads                 | 29.1 us                                                                | 28.8 us: 1.01x faster                                                        |
| xml_etree_iterparse        | 95.8 ms                                                                | 94.9 ms: 1.01x faster                                                        |
| raytrace                   | 289 ms                                                                 | 286 ms: 1.01x faster                                                         |
| mdp                        | 2.56 sec                                                               | 2.55 sec: 1.01x faster                                                       |
| sqlglot_transpile          | 1.59 ms                                                                | 1.58 ms: 1.01x faster                                                        |
| async_tree_memoization     | 332 ms                                                                 | 329 ms: 1.01x faster                                                         |
| docutils                   | 2.67 sec                                                               | 2.65 sec: 1.01x faster                                                       |
| sympy_sum                  | 155 ms                                                                 | 154 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.7 ms: 1.00x faster                                                        |
| connected_components       | 437 ms                                                                 | 435 ms: 1.00x faster                                                         |
| 2to3                       | 260 ms                                                                 | 259 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| mako                       | 9.93 ms                                                                | 9.95 ms: 1.00x slower                                                        |
| regex_effbot               | 3.22 ms                                                                | 3.23 ms: 1.00x slower                                                        |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| many_optionals             | 957 us                                                                 | 961 us: 1.00x slower                                                         |
| scimark_sparse_mat_mult    | 4.45 ms                                                                | 4.47 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.06 ms                                                                | 7.11 ms: 1.01x slower                                                        |
| nbody                      | 86.0 ms                                                                | 86.7 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                         |
| dulwich_log                | 66.7 ms                                                                | 67.3 ms: 1.01x slower                                                        |
| telco                      | 7.56 ms                                                                | 7.64 ms: 1.01x slower                                                        |
| bench_mp_pool              | 80.8 ms                                                                | 81.7 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.44 ms                                                                | 2.47 ms: 1.01x slower                                                        |
| json_dumps                 | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                        |
| regex_dna                  | 209 ms                                                                 | 213 ms: 1.02x slower                                                         |
| coroutines                 | 23.4 ms                                                                | 24.0 ms: 1.03x slower                                                        |
| gc_traversal               | 4.75 ms                                                                | 4.88 ms: 1.03x slower                                                        |
| html5lib                   | 63.3 ms                                                                | 66.1 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (25): pylint, async_tree_io_tg, spectral_norm, async_tree_none, scimark_monte_carlo, async_tree_memoization_tg, xml_etree_parse, chaos, xml_etree_process, genshi_text, float, sqlalchemy_declarative, k_core, async_tree_io, sphinx, sympy_str, asyncio_websockets, subparsers, bench_thread_pool, typing_runtime_protocols, xml_etree_generate, pickle_pure_python, coverage, sqlite_synth, async_tree_none_tg

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x