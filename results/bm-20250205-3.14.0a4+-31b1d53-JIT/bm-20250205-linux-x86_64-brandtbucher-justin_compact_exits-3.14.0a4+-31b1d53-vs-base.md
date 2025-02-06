# Results vs. base

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 31b1d53
- commit date: 2025-02-05
- overall geometric mean: 1.010x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 258 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.61 sec: 1.02x faster                                                       |
| html5lib       | 64.1 ms                                                                | 61.4 ms: 1.04x faster                                                        |
| sphinx         | 1.04 sec                                                               | 1.01 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators       | 411 ms                                                                 | 406 ms: 1.01x faster                                                         |
| async_tree_memoization | 329 ms                                                                 | 331 ms: 1.01x slower                                                         |
| coroutines             | 22.7 ms                                                                | 23.4 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 188 ms: 1.01x slower                                                         |
| nbody          | 93.6 ms                                                                | 94.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.31 ms                                                                | 3.12 ms: 1.06x faster                                                        |
| regex_dna      | 215 ms                                                                 | 210 ms: 1.02x faster                                                         |
| regex_compile  | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_v8       | 24.1 ms                                                                | 24.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 83.3 ms                                                                | 79.6 ms: 1.05x faster                                                        |
| unpickle_pure_python | 201 us                                                                 | 194 us: 1.04x faster                                                         |
| tomli_loads          | 1.84 sec                                                               | 1.81 sec: 1.01x faster                                                       |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                         |
| pickle_pure_python   | 314 us                                                                 | 318 us: 1.02x slower                                                         |
| json_dumps           | 11.3 ms                                                                | 11.7 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.04 ms                                                                | 7.02 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 9.86 ms                                                                | 10.1 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| richards                 | 43.7 ms                                                                | 39.9 ms: 1.09x faster                                                        |
| richards_super           | 50.1 ms                                                                | 46.1 ms: 1.09x faster                                                        |
| regex_effbot             | 3.31 ms                                                                | 3.12 ms: 1.06x faster                                                        |
| xml_etree_generate       | 83.3 ms                                                                | 79.6 ms: 1.05x faster                                                        |
| deepcopy_reduce          | 2.81 us                                                                | 2.69 us: 1.04x faster                                                        |
| logging_simple           | 5.77 us                                                                | 5.52 us: 1.04x faster                                                        |
| html5lib                 | 64.1 ms                                                                | 61.4 ms: 1.04x faster                                                        |
| pycparser                | 1.18 sec                                                               | 1.14 sec: 1.04x faster                                                       |
| generators               | 37.5 ms                                                                | 36.2 ms: 1.04x faster                                                        |
| unpickle_pure_python     | 201 us                                                                 | 194 us: 1.04x faster                                                         |
| logging_format           | 6.32 us                                                                | 6.12 us: 1.03x faster                                                        |
| sympy_str                | 280 ms                                                                 | 271 ms: 1.03x faster                                                         |
| pylint                   | 286 ms                                                                 | 277 ms: 1.03x faster                                                         |
| sympy_integrate          | 20.7 ms                                                                | 20.1 ms: 1.03x faster                                                        |
| sympy_expand             | 469 ms                                                                 | 456 ms: 1.03x faster                                                         |
| sympy_sum                | 155 ms                                                                 | 151 ms: 1.03x faster                                                         |
| scimark_lu               | 115 ms                                                                 | 113 ms: 1.03x faster                                                         |
| sphinx                   | 1.04 sec                                                               | 1.01 sec: 1.02x faster                                                       |
| comprehensions           | 17.1 us                                                                | 16.7 us: 1.02x faster                                                        |
| docutils                 | 2.68 sec                                                               | 2.61 sec: 1.02x faster                                                       |
| shortest_path            | 484 ms                                                                 | 473 ms: 1.02x faster                                                         |
| sqlglot_optimize         | 54.3 ms                                                                | 53.1 ms: 1.02x faster                                                        |
| regex_dna                | 215 ms                                                                 | 210 ms: 1.02x faster                                                         |
| deltablue                | 3.48 ms                                                                | 3.40 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 763 ms                                                                 | 746 ms: 1.02x faster                                                         |
| gc_traversal             | 4.89 ms                                                                | 4.79 ms: 1.02x faster                                                        |
| raytrace                 | 292 ms                                                                 | 286 ms: 1.02x faster                                                         |
| hexiom                   | 7.43 ms                                                                | 7.28 ms: 1.02x faster                                                        |
| sqlglot_parse            | 1.28 ms                                                                | 1.26 ms: 1.02x faster                                                        |
| pathlib                  | 16.2 ms                                                                | 15.9 ms: 1.02x faster                                                        |
| sqlglot_transpile        | 1.60 ms                                                                | 1.57 ms: 1.02x faster                                                        |
| logging_silent           | 112 ns                                                                 | 110 ns: 1.02x faster                                                         |
| connected_components     | 441 ms                                                                 | 434 ms: 1.02x faster                                                         |
| pprint_pformat           | 1.56 sec                                                               | 1.54 sec: 1.02x faster                                                       |
| subparsers               | 20.7 ms                                                                | 20.4 ms: 1.02x faster                                                        |
| tomli_loads              | 1.84 sec                                                               | 1.81 sec: 1.01x faster                                                       |
| deepcopy_memo            | 30.3 us                                                                | 29.9 us: 1.01x faster                                                        |
| 2to3                     | 261 ms                                                                 | 258 ms: 1.01x faster                                                         |
| async_generators         | 411 ms                                                                 | 406 ms: 1.01x faster                                                         |
| deepcopy                 | 272 us                                                                 | 269 us: 1.01x faster                                                         |
| chaos                    | 60.0 ms                                                                | 59.4 ms: 1.01x faster                                                        |
| thrift                   | 773 us                                                                 | 765 us: 1.01x faster                                                         |
| go                       | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| coverage                 | 90.6 ms                                                                | 89.8 ms: 1.01x faster                                                        |
| typing_runtime_protocols | 162 us                                                                 | 160 us: 1.01x faster                                                         |
| scimark_monte_carlo      | 63.5 ms                                                                | 63.0 ms: 1.01x faster                                                        |
| sqlalchemy_imperative    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                        |
| mdp                      | 2.56 sec                                                               | 2.54 sec: 1.01x faster                                                       |
| scimark_sor              | 114 ms                                                                 | 113 ms: 1.01x faster                                                         |
| bench_thread_pool        | 897 us                                                                 | 891 us: 1.01x faster                                                         |
| xml_etree_parse          | 138 ms                                                                 | 137 ms: 1.01x faster                                                         |
| telco                    | 7.53 ms                                                                | 7.49 ms: 1.01x faster                                                        |
| sqlalchemy_declarative   | 131 ms                                                                 | 130 ms: 1.01x faster                                                         |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.04 ms                                                                | 7.02 ms: 1.00x faster                                                        |
| async_tree_memoization   | 329 ms                                                                 | 331 ms: 1.01x slower                                                         |
| regex_compile            | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_v8                 | 24.1 ms                                                                | 24.3 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult  | 4.51 ms                                                                | 4.56 ms: 1.01x slower                                                        |
| pidigits                 | 186 ms                                                                 | 188 ms: 1.01x slower                                                         |
| nbody                    | 93.6 ms                                                                | 94.8 ms: 1.01x slower                                                        |
| sqlite_synth             | 2.71 us                                                                | 2.74 us: 1.01x slower                                                        |
| pickle_pure_python       | 314 us                                                                 | 318 us: 1.02x slower                                                         |
| bpe_tokeniser            | 4.37 sec                                                               | 4.45 sec: 1.02x slower                                                       |
| mako                     | 9.86 ms                                                                | 10.1 ms: 1.03x slower                                                        |
| spectral_norm            | 95.4 ms                                                                | 98.0 ms: 1.03x slower                                                        |
| coroutines               | 22.7 ms                                                                | 23.4 ms: 1.03x slower                                                        |
| json_dumps               | 11.3 ms                                                                | 11.7 ms: 1.04x slower                                                        |
| meteor_contest           | 106 ms                                                                 | 112 ms: 1.05x slower                                                         |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (27): genshi_xml, sqlglot_normalize, django_template, k_core, xml_etree_iterparse, async_tree_io, async_tree_io_tg, json_loads, dulwich_log, async_tree_memoization_tg, pyflate, create_gc_cycles, fannkuch, async_tree_cpu_io_mixed, genshi_text, bench_mp_pool, many_optionals, asyncio_websockets, crypto_pyaes, nqueens, async_tree_cpu_io_mixed_tg, async_tree_none, xml_etree_process, json, float, async_tree_none_tg, scimark_fft

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x