# Results vs. base

- fork: mdboom
- ref: tail_call_no_preserv
- machine: linux-x86_64
- commit hash: 09f3d0f
- commit date: 2025-01-16
- overall geometric mean: 1.029x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                       | 282 ms: 1.01x slower                                                         |
| docutils       | 2.85 sec                                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 630 ms                                                                       | 621 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 528 ms                                                                       | 522 ms: 1.01x faster                                                         |
| asyncio_websockets         | 384 ms                                                                       | 392 ms: 1.02x slower                                                         |
| coroutines                 | 21.5 ms                                                                      | 22.3 ms: 1.03x slower                                                        |
| async_generators           | 414 ms                                                                       | 429 ms: 1.04x slower                                                         |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                       | 89.2 ms: 1.18x faster                                                        |
| float          | 75.1 ms                                                                      | 71.9 ms: 1.05x faster                                                        |
| pidigits       | 285 ms                                                                       | 286 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                       | 138 ms: 1.05x faster                                                         |
| regex_effbot   | 3.03 ms                                                                      | 3.00 ms: 1.01x faster                                                        |
| regex_dna      | 222 ms                                                                       | 223 ms: 1.01x slower                                                         |
| regex_v8       | 26.4 ms                                                                      | 27.2 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.48 sec                                                                     | 2.06 sec: 1.21x faster                                                       |
| unpickle_pure_python | 239 us                                                                       | 216 us: 1.10x faster                                                         |
| pickle_pure_python   | 353 us                                                                       | 325 us: 1.08x faster                                                         |
| xml_etree_process    | 61.0 ms                                                                      | 57.6 ms: 1.06x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                                      | 80.9 ms: 1.06x faster                                                        |
| json_loads           | 25.6 us                                                                      | 25.2 us: 1.02x faster                                                        |
| json_dumps           | 11.9 ms                                                                      | 11.7 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 106 ms                                                                       | 105 ms: 1.01x faster                                                         |
| xml_etree_parse      | 163 ms                                                                       | 161 ms: 1.01x faster                                                         |
| Geometric mean       | (ref)                                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                      | 9.06 ms: 1.00x slower                                                        |
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                                      | 23.5 ms: 1.06x faster                                                        |
| mako            | 12.0 ms                                                                      | 11.3 ms: 1.06x faster                                                        |
| genshi_xml      | 54.9 ms                                                                      | 53.7 ms: 1.02x faster                                                        |
| django_template | 35.2 ms                                                                      | 37.2 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| scimark_monte_carlo        | 71.2 ms                                                                      | 57.5 ms: 1.24x faster                                                        |
| scimark_sor                | 126 ms                                                                       | 104 ms: 1.21x faster                                                         |
| tomli_loads                | 2.48 sec                                                                     | 2.06 sec: 1.21x faster                                                       |
| nbody                      | 105 ms                                                                       | 89.2 ms: 1.18x faster                                                        |
| fannkuch                   | 431 ms                                                                       | 366 ms: 1.18x faster                                                         |
| deepcopy_memo              | 33.4 us                                                                      | 28.9 us: 1.16x faster                                                        |
| scimark_fft                | 311 ms                                                                       | 272 ms: 1.14x faster                                                         |
| hexiom                     | 6.84 ms                                                                      | 6.12 ms: 1.12x faster                                                        |
| scimark_lu                 | 99.1 ms                                                                      | 89.2 ms: 1.11x faster                                                        |
| logging_silent             | 99.8 ns                                                                      | 89.9 ns: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 4.54 ms                                                                      | 4.10 ms: 1.11x faster                                                        |
| unpickle_pure_python       | 239 us                                                                       | 216 us: 1.10x faster                                                         |
| pyflate                    | 473 ms                                                                       | 431 ms: 1.10x faster                                                         |
| pickle_pure_python         | 353 us                                                                       | 325 us: 1.08x faster                                                         |
| generators                 | 33.1 ms                                                                      | 30.6 ms: 1.08x faster                                                        |
| richards                   | 46.8 ms                                                                      | 43.3 ms: 1.08x faster                                                        |
| go                         | 137 ms                                                                       | 128 ms: 1.07x faster                                                         |
| pprint_safe_repr           | 874 ms                                                                       | 817 ms: 1.07x faster                                                         |
| pprint_pformat             | 1.77 sec                                                                     | 1.65 sec: 1.07x faster                                                       |
| genshi_text                | 25.0 ms                                                                      | 23.5 ms: 1.06x faster                                                        |
| mako                       | 12.0 ms                                                                      | 11.3 ms: 1.06x faster                                                        |
| xml_etree_process          | 61.0 ms                                                                      | 57.6 ms: 1.06x faster                                                        |
| gc_traversal               | 5.64 ms                                                                      | 5.34 ms: 1.06x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                                      | 80.9 ms: 1.06x faster                                                        |
| spectral_norm              | 94.4 ms                                                                      | 90.0 ms: 1.05x faster                                                        |
| richards_super             | 52.3 ms                                                                      | 49.9 ms: 1.05x faster                                                        |
| float                      | 75.1 ms                                                                      | 71.9 ms: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                                       | 138 ms: 1.05x faster                                                         |
| sqlglot_parse              | 1.41 ms                                                                      | 1.35 ms: 1.05x faster                                                        |
| chaos                      | 63.9 ms                                                                      | 61.4 ms: 1.04x faster                                                        |
| comprehensions             | 18.1 us                                                                      | 17.4 us: 1.04x faster                                                        |
| deepcopy_reduce            | 2.93 us                                                                      | 2.82 us: 1.04x faster                                                        |
| thrift                     | 853 us                                                                       | 827 us: 1.03x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                                      | 1.74 ms: 1.03x faster                                                        |
| deepcopy                   | 286 us                                                                       | 279 us: 1.03x faster                                                         |
| genshi_xml                 | 54.9 ms                                                                      | 53.7 ms: 1.02x faster                                                        |
| crypto_pyaes               | 79.6 ms                                                                      | 78.1 ms: 1.02x faster                                                        |
| dulwich_log                | 66.6 ms                                                                      | 65.4 ms: 1.02x faster                                                        |
| json_loads                 | 25.6 us                                                                      | 25.2 us: 1.02x faster                                                        |
| nqueens                    | 95.5 ms                                                                      | 94.1 ms: 1.02x faster                                                        |
| json_dumps                 | 11.9 ms                                                                      | 11.7 ms: 1.02x faster                                                        |
| async_tree_io_tg           | 630 ms                                                                       | 621 ms: 1.01x faster                                                         |
| bpe_tokeniser              | 4.86 sec                                                                     | 4.79 sec: 1.01x faster                                                       |
| xml_etree_iterparse        | 106 ms                                                                       | 105 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 528 ms                                                                       | 522 ms: 1.01x faster                                                         |
| regex_effbot               | 3.03 ms                                                                      | 3.00 ms: 1.01x faster                                                        |
| xml_etree_parse            | 163 ms                                                                       | 161 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 17.9 ms                                                                      | 17.7 ms: 1.01x faster                                                        |
| pycparser                  | 1.27 sec                                                                     | 1.26 sec: 1.01x faster                                                       |
| meteor_contest             | 134 ms                                                                       | 133 ms: 1.00x faster                                                         |
| shortest_path              | 452 ms                                                                       | 452 ms: 1.00x slower                                                         |
| python_startup_no_site     | 9.05 ms                                                                      | 9.06 ms: 1.00x slower                                                        |
| python_startup             | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                        |
| pidigits                   | 285 ms                                                                       | 286 ms: 1.00x slower                                                         |
| sqlite_synth               | 2.82 us                                                                      | 2.84 us: 1.00x slower                                                        |
| regex_dna                  | 222 ms                                                                       | 223 ms: 1.01x slower                                                         |
| 2to3                       | 280 ms                                                                       | 282 ms: 1.01x slower                                                         |
| mdp                        | 2.63 sec                                                                     | 2.65 sec: 1.01x slower                                                       |
| sympy_str                  | 289 ms                                                                       | 292 ms: 1.01x slower                                                         |
| logging_format             | 6.75 us                                                                      | 6.83 us: 1.01x slower                                                        |
| sqlglot_normalize          | 118 ms                                                                       | 120 ms: 1.01x slower                                                         |
| deltablue                  | 3.28 ms                                                                      | 3.33 ms: 1.01x slower                                                        |
| docutils                   | 2.85 sec                                                                     | 2.89 sec: 1.01x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                                      | 59.6 ms: 1.02x slower                                                        |
| asyncio_websockets         | 384 ms                                                                       | 392 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 169 us                                                                       | 172 us: 1.02x slower                                                         |
| sympy_integrate            | 22.6 ms                                                                      | 23.0 ms: 1.02x slower                                                        |
| many_optionals             | 1.01 ms                                                                      | 1.03 ms: 1.02x slower                                                        |
| telco                      | 7.84 ms                                                                      | 8.03 ms: 1.02x slower                                                        |
| sympy_expand               | 487 ms                                                                       | 500 ms: 1.03x slower                                                         |
| regex_v8                   | 26.4 ms                                                                      | 27.2 ms: 1.03x slower                                                        |
| coroutines                 | 21.5 ms                                                                      | 22.3 ms: 1.03x slower                                                        |
| async_generators           | 414 ms                                                                       | 429 ms: 1.04x slower                                                         |
| coverage                   | 72.7 ms                                                                      | 75.9 ms: 1.04x slower                                                        |
| django_template            | 35.2 ms                                                                      | 37.2 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (21): bench_mp_pool, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, sympy_sum, html5lib, k_core, raytrace, async_tree_io, connected_components, json, logging_simple, async_tree_none, sqlalchemy_declarative, async_tree_memoization, subparsers, sphinx, bench_thread_pool, create_gc_cycles, pathlib, pylint

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x