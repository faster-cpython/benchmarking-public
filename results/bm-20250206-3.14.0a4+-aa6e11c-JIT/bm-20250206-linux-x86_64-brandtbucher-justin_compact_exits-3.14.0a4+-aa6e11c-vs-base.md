# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: aa6e11c
- commit date: 2025-02-06
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 262 ms: 1.01x slower                                                         |
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.01x slower                                                       |
| html5lib       | 64.1 ms                                                                | 63.5 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 501 ms                                                                 | 494 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 487 ms                                                                 | 481 ms: 1.01x faster                                                         |
| async_tree_memoization     | 329 ms                                                                 | 325 ms: 1.01x faster                                                         |
| async_generators           | 411 ms                                                                 | 408 ms: 1.01x faster                                                         |
| coroutines                 | 22.7 ms                                                                | 23.0 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| nbody          | 93.6 ms                                                                | 94.6 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                 | 212 ms: 1.01x faster                                                         |
| regex_v8       | 24.1 ms                                                                | 24.0 ms: 1.00x faster                                                        |
| regex_compile  | 129 ms                                                                 | 128 ms: 1.00x faster                                                         |
| regex_effbot   | 3.31 ms                                                                | 3.31 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 83.3 ms                                                                | 77.5 ms: 1.07x faster                                                        |
| xml_etree_process    | 56.7 ms                                                                | 54.7 ms: 1.04x faster                                                        |
| unpickle_pure_python | 201 us                                                                 | 194 us: 1.03x faster                                                         |
| tomli_loads          | 1.84 sec                                                               | 1.79 sec: 1.03x faster                                                       |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                         |
| xml_etree_iterparse  | 95.9 ms                                                                | 95.2 ms: 1.01x faster                                                        |
| pickle_pure_python   | 314 us                                                                 | 318 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.04 ms                                                                | 7.01 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.0 ms                                                                | 55.1 ms: 1.04x faster                                                        |
| django_template | 33.0 ms                                                                | 32.3 ms: 1.02x faster                                                        |
| mako            | 9.86 ms                                                                | 10.0 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate         | 83.3 ms                                                                | 77.5 ms: 1.07x faster                                                        |
| richards_super             | 50.1 ms                                                                | 47.2 ms: 1.06x faster                                                        |
| gc_traversal               | 4.89 ms                                                                | 4.61 ms: 1.06x faster                                                        |
| richards                   | 43.7 ms                                                                | 41.2 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.56 sec                                                               | 1.49 sec: 1.05x faster                                                       |
| deepcopy_reduce            | 2.81 us                                                                | 2.69 us: 1.04x faster                                                        |
| nqueens                    | 90.5 ms                                                                | 87.1 ms: 1.04x faster                                                        |
| connected_components       | 441 ms                                                                 | 425 ms: 1.04x faster                                                         |
| xml_etree_process          | 56.7 ms                                                                | 54.7 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.0 ms                                                                | 55.1 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 763 ms                                                                 | 737 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 201 us                                                                 | 194 us: 1.03x faster                                                         |
| generators                 | 37.5 ms                                                                | 36.4 ms: 1.03x faster                                                        |
| hexiom                     | 7.43 ms                                                                | 7.22 ms: 1.03x faster                                                        |
| tomli_loads                | 1.84 sec                                                               | 1.79 sec: 1.03x faster                                                       |
| bpe_tokeniser              | 4.37 sec                                                               | 4.26 sec: 1.03x faster                                                       |
| comprehensions             | 17.1 us                                                                | 16.7 us: 1.02x faster                                                        |
| pycparser                  | 1.18 sec                                                               | 1.16 sec: 1.02x faster                                                       |
| deepcopy                   | 272 us                                                                 | 265 us: 1.02x faster                                                         |
| pyflate                    | 448 ms                                                                 | 438 ms: 1.02x faster                                                         |
| django_template            | 33.0 ms                                                                | 32.3 ms: 1.02x faster                                                        |
| logging_silent             | 112 ns                                                                 | 109 ns: 1.02x faster                                                         |
| thrift                     | 773 us                                                                 | 758 us: 1.02x faster                                                         |
| raytrace                   | 292 ms                                                                 | 287 ms: 1.02x faster                                                         |
| logging_format             | 6.32 us                                                                | 6.21 us: 1.02x faster                                                        |
| shortest_path              | 484 ms                                                                 | 476 ms: 1.02x faster                                                         |
| scimark_fft                | 315 ms                                                                 | 310 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 54.3 ms                                                                | 53.5 ms: 1.01x faster                                                        |
| pathlib                    | 16.2 ms                                                                | 16.0 ms: 1.01x faster                                                        |
| coverage                   | 90.6 ms                                                                | 89.3 ms: 1.01x faster                                                        |
| regex_dna                  | 215 ms                                                                 | 212 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 501 ms                                                                 | 494 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 487 ms                                                                 | 481 ms: 1.01x faster                                                         |
| sympy_integrate            | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                        |
| async_tree_memoization     | 329 ms                                                                 | 325 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 108 ms                                                                 | 107 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                                        |
| xml_etree_parse            | 138 ms                                                                 | 137 ms: 1.01x faster                                                         |
| logging_simple             | 5.77 us                                                                | 5.71 us: 1.01x faster                                                        |
| mdp                        | 2.56 sec                                                               | 2.54 sec: 1.01x faster                                                       |
| fannkuch                   | 386 ms                                                                 | 382 ms: 1.01x faster                                                         |
| html5lib                   | 64.1 ms                                                                | 63.5 ms: 1.01x faster                                                        |
| subparsers                 | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 95.9 ms                                                                | 95.2 ms: 1.01x faster                                                        |
| async_generators           | 411 ms                                                                 | 408 ms: 1.01x faster                                                         |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| sympy_sum                  | 155 ms                                                                 | 154 ms: 1.00x faster                                                         |
| regex_v8                   | 24.1 ms                                                                | 24.0 ms: 1.00x faster                                                        |
| bench_thread_pool          | 897 us                                                                 | 893 us: 1.00x faster                                                         |
| dulwich_log                | 66.9 ms                                                                | 66.7 ms: 1.00x faster                                                        |
| regex_compile              | 129 ms                                                                 | 128 ms: 1.00x faster                                                         |
| python_startup_no_site     | 7.04 ms                                                                | 7.01 ms: 1.00x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                                | 2.45 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| regex_effbot               | 3.31 ms                                                                | 3.31 ms: 1.00x slower                                                        |
| 2to3                       | 261 ms                                                                 | 262 ms: 1.01x slower                                                         |
| docutils                   | 2.68 sec                                                               | 2.69 sec: 1.01x slower                                                       |
| nbody                      | 93.6 ms                                                                | 94.6 ms: 1.01x slower                                                        |
| pickle_pure_python         | 314 us                                                                 | 318 us: 1.01x slower                                                         |
| sympy_expand               | 469 ms                                                                 | 476 ms: 1.01x slower                                                         |
| coroutines                 | 22.7 ms                                                                | 23.0 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 162 us                                                                 | 164 us: 1.02x slower                                                         |
| telco                      | 7.53 ms                                                                | 7.65 ms: 1.02x slower                                                        |
| mako                       | 9.86 ms                                                                | 10.0 ms: 1.02x slower                                                        |
| crypto_pyaes               | 69.9 ms                                                                | 71.3 ms: 1.02x slower                                                        |
| meteor_contest             | 106 ms                                                                 | 113 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (29): async_tree_io, chaos, genshi_text, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, json, json_loads, float, many_optionals, sqlalchemy_declarative, bench_mp_pool, pylint, json_dumps, async_tree_none, scimark_monte_carlo, spectral_norm, deepcopy_memo, asyncio_websockets, go, k_core, sqlalchemy_imperative, sympy_str, sqlite_synth, deltablue, sphinx, scimark_sparse_mat_mult, scimark_sor, scimark_lu

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x