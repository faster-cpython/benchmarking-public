# Results vs. base

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: 37fd664
- commit date: 2025-03-17
- overall geometric mean: 1.004x faster
- HPT reliability: 63.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                       | 285 ms: 1.01x faster                                                         |
| docutils       | 2.93 sec                                                                     | 2.91 sec: 1.01x faster                                                       |
| html5lib       | 70.2 ms                                                                      | 69.4 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|-------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators        | 422 ms                                                                       | 413 ms: 1.02x faster                                                         |
| async_tree_none_tg      | 278 ms                                                                       | 275 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed | 520 ms                                                                       | 523 ms: 1.01x slower                                                         |
| async_tree_none         | 290 ms                                                                       | 292 ms: 1.01x slower                                                         |
| async_tree_memoization  | 347 ms                                                                       | 351 ms: 1.01x slower                                                         |
| Geometric mean          | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 99.3 ms                                                                      | 101 ms: 1.01x slower                                                         |
| float          | 71.3 ms                                                                      | 72.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                      | 23.7 ms: 1.01x faster                                                        |
| regex_compile  | 138 ms                                                                       | 138 ms: 1.00x faster                                                         |
| regex_effbot   | 3.07 ms                                                                      | 3.13 ms: 1.02x slower                                                        |
| regex_dna      | 229 ms                                                                       | 237 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 143 ms                                                                       | 136 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 100 ms                                                                       | 97.4 ms: 1.03x faster                                                        |
| json_loads           | 26.1 us                                                                      | 25.5 us: 1.02x faster                                                        |
| unpickle_pure_python | 228 us                                                                       | 225 us: 1.01x faster                                                         |
| json_dumps           | 11.5 ms                                                                      | 11.4 ms: 1.01x faster                                                        |
| pickle_pure_python   | 342 us                                                                       | 338 us: 1.01x faster                                                         |
| xml_etree_process    | 60.7 ms                                                                      | 60.4 ms: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                      | 16.3 ms: 1.00x faster                                                        |
| python_startup_no_site | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 37.7 ms                                                                      | 36.8 ms: 1.02x faster                                                        |
| genshi_text     | 24.4 ms                                                                      | 23.8 ms: 1.02x faster                                                        |
| genshi_xml      | 56.7 ms                                                                      | 55.5 ms: 1.02x faster                                                        |
| mako            | 11.1 ms                                                                      | 11.0 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|--------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse          | 143 ms                                                                       | 136 ms: 1.05x faster                                                         |
| typing_runtime_protocols | 177 us                                                                       | 168 us: 1.05x faster                                                         |
| pyflate                  | 474 ms                                                                       | 452 ms: 1.05x faster                                                         |
| logging_simple           | 6.70 us                                                                      | 6.41 us: 1.04x faster                                                        |
| logging_format           | 7.36 us                                                                      | 7.13 us: 1.03x faster                                                        |
| xml_etree_iterparse      | 100 ms                                                                       | 97.4 ms: 1.03x faster                                                        |
| create_gc_cycles         | 2.84 ms                                                                      | 2.77 ms: 1.03x faster                                                        |
| richards_super           | 55.0 ms                                                                      | 53.6 ms: 1.02x faster                                                        |
| django_template          | 37.7 ms                                                                      | 36.8 ms: 1.02x faster                                                        |
| genshi_text              | 24.4 ms                                                                      | 23.8 ms: 1.02x faster                                                        |
| json_loads               | 26.1 us                                                                      | 25.5 us: 1.02x faster                                                        |
| async_generators         | 422 ms                                                                       | 413 ms: 1.02x faster                                                         |
| genshi_xml               | 56.7 ms                                                                      | 55.5 ms: 1.02x faster                                                        |
| comprehensions           | 18.1 us                                                                      | 17.8 us: 1.02x faster                                                        |
| subparsers               | 24.1 ms                                                                      | 23.6 ms: 1.02x faster                                                        |
| fannkuch                 | 386 ms                                                                       | 378 ms: 1.02x faster                                                         |
| scimark_lu               | 101 ms                                                                       | 99.1 ms: 1.02x faster                                                        |
| pycparser                | 1.27 sec                                                                     | 1.25 sec: 1.02x faster                                                       |
| telco                    | 8.13 ms                                                                      | 7.99 ms: 1.02x faster                                                        |
| sqlglot_v2_parse         | 1.43 ms                                                                      | 1.40 ms: 1.02x faster                                                        |
| sqlglot_v2_transpile     | 1.81 ms                                                                      | 1.79 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 228 us                                                                       | 225 us: 1.01x faster                                                         |
| json_dumps               | 11.5 ms                                                                      | 11.4 ms: 1.01x faster                                                        |
| json                     | 5.30 ms                                                                      | 5.24 ms: 1.01x faster                                                        |
| mako                     | 11.1 ms                                                                      | 11.0 ms: 1.01x faster                                                        |
| chaos                    | 65.3 ms                                                                      | 64.5 ms: 1.01x faster                                                        |
| pickle_pure_python       | 342 us                                                                       | 338 us: 1.01x faster                                                         |
| html5lib                 | 70.2 ms                                                                      | 69.4 ms: 1.01x faster                                                        |
| regex_v8                 | 24.0 ms                                                                      | 23.7 ms: 1.01x faster                                                        |
| scimark_fft              | 318 ms                                                                       | 314 ms: 1.01x faster                                                         |
| async_tree_none_tg       | 278 ms                                                                       | 275 ms: 1.01x faster                                                         |
| hexiom                   | 6.54 ms                                                                      | 6.48 ms: 1.01x faster                                                        |
| thrift                   | 866 us                                                                       | 859 us: 1.01x faster                                                         |
| deepcopy_memo            | 29.9 us                                                                      | 29.6 us: 1.01x faster                                                        |
| many_optionals           | 1.04 ms                                                                      | 1.04 ms: 1.01x faster                                                        |
| logging_silent           | 95.7 ns                                                                      | 95.0 ns: 1.01x faster                                                        |
| docutils                 | 2.93 sec                                                                     | 2.91 sec: 1.01x faster                                                       |
| xml_etree_process        | 60.7 ms                                                                      | 60.4 ms: 1.01x faster                                                        |
| 2to3                     | 286 ms                                                                       | 285 ms: 1.01x faster                                                         |
| sympy_integrate          | 23.5 ms                                                                      | 23.4 ms: 1.00x faster                                                        |
| regex_compile            | 138 ms                                                                       | 138 ms: 1.00x faster                                                         |
| spectral_norm            | 92.0 ms                                                                      | 91.7 ms: 1.00x faster                                                        |
| python_startup           | 16.4 ms                                                                      | 16.3 ms: 1.00x faster                                                        |
| python_startup_no_site   | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                                        |
| meteor_contest           | 128 ms                                                                       | 128 ms: 1.00x slower                                                         |
| sympy_str                | 296 ms                                                                       | 297 ms: 1.00x slower                                                         |
| sympy_sum                | 155 ms                                                                       | 156 ms: 1.00x slower                                                         |
| sqlite_synth             | 2.81 us                                                                      | 2.82 us: 1.00x slower                                                        |
| mdp                      | 2.55 sec                                                                     | 2.56 sec: 1.01x slower                                                       |
| sqlalchemy_declarative   | 146 ms                                                                       | 147 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed  | 520 ms                                                                       | 523 ms: 1.01x slower                                                         |
| crypto_pyaes             | 82.9 ms                                                                      | 83.4 ms: 1.01x slower                                                        |
| sympy_expand             | 504 ms                                                                       | 508 ms: 1.01x slower                                                         |
| async_tree_none          | 290 ms                                                                       | 292 ms: 1.01x slower                                                         |
| connected_components     | 429 ms                                                                       | 433 ms: 1.01x slower                                                         |
| deepcopy                 | 289 us                                                                       | 292 us: 1.01x slower                                                         |
| coverage                 | 81.1 ms                                                                      | 82.0 ms: 1.01x slower                                                        |
| async_tree_memoization   | 347 ms                                                                       | 351 ms: 1.01x slower                                                         |
| shortest_path            | 452 ms                                                                       | 457 ms: 1.01x slower                                                         |
| nqueens                  | 94.8 ms                                                                      | 95.9 ms: 1.01x slower                                                        |
| bpe_tokeniser            | 4.81 sec                                                                     | 4.86 sec: 1.01x slower                                                       |
| sqlglot_v2_optimize      | 58.4 ms                                                                      | 59.2 ms: 1.01x slower                                                        |
| nbody                    | 99.3 ms                                                                      | 101 ms: 1.01x slower                                                         |
| scimark_monte_carlo      | 67.1 ms                                                                      | 68.1 ms: 1.01x slower                                                        |
| raytrace                 | 293 ms                                                                       | 298 ms: 1.02x slower                                                         |
| regex_effbot             | 3.07 ms                                                                      | 3.13 ms: 1.02x slower                                                        |
| float                    | 71.3 ms                                                                      | 72.9 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult  | 4.74 ms                                                                      | 4.86 ms: 1.02x slower                                                        |
| generators               | 28.6 ms                                                                      | 29.4 ms: 1.03x slower                                                        |
| sqlglot_v2_normalize     | 117 ms                                                                       | 120 ms: 1.03x slower                                                         |
| pprint_pformat           | 1.64 sec                                                                     | 1.69 sec: 1.03x slower                                                       |
| regex_dna                | 229 ms                                                                       | 237 ms: 1.03x slower                                                         |
| pprint_safe_repr         | 809 ms                                                                       | 838 ms: 1.04x slower                                                         |
| Geometric mean           | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (23): async_tree_io_tg, sphinx, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, go, richards, pylint, pathlib, sqlalchemy_imperative, scimark_sor, deltablue, gc_traversal, dulwich_log, xml_etree_generate, k_core, pidigits, async_tree_io, coroutines, tomli_loads, deepcopy_reduce, bench_thread_pool, bench_mp_pool

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 63.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x