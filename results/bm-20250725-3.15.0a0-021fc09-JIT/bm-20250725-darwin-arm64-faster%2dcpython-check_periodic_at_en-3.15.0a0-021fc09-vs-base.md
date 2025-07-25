# Results vs. base

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: darwin-arm64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.002x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.45 sec                                                              | 1.45 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines       | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                           |
| async_tree_eager | 64.7 ms                                                               | 64.6 ms: 1.00x faster                                                           |
| async_generators | 283 ms                                                                | 286 ms: 1.01x slower                                                            |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (16): asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 71.7 ms                                                               | 71.6 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.14 ms                                                               | 2.15 ms: 1.00x slower                                                           |
| regex_compile  | 72.8 ms                                                               | 73.3 ms: 1.01x slower                                                           |
| regex_v8       | 15.2 ms                                                               | 15.5 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 49.6 ms                                                               | 49.2 ms: 1.01x faster                                                           |
| xml_etree_parse      | 98.1 ms                                                               | 97.5 ms: 1.01x faster                                                           |
| xml_etree_process    | 34.7 ms                                                               | 34.5 ms: 1.00x faster                                                           |
| json_loads           | 17.4 us                                                               | 17.4 us: 1.00x slower                                                           |
| unpickle_pure_python | 128 us                                                                | 129 us: 1.01x slower                                                            |
| pickle_pure_python   | 207 us                                                                | 209 us: 1.01x slower                                                            |
| json_dumps           | 6.63 ms                                                               | 6.69 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.3 ms                                                               | 17.0 ms: 1.02x faster                                                           |
| python_startup_no_site | 12.8 ms                                                               | 12.7 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 23.1 ms                                                               | 23.3 ms: 1.01x slower                                                           |
| genshi_xml      | 33.1 ms                                                               | 33.5 ms: 1.01x slower                                                           |
| genshi_text     | 15.4 ms                                                               | 15.7 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_sor              | 86.0 ms                                                               | 84.2 ms: 1.02x faster                                                           |
| telco                    | 4.48 ms                                                               | 4.40 ms: 1.02x faster                                                           |
| python_startup           | 17.3 ms                                                               | 17.0 ms: 1.02x faster                                                           |
| typing_runtime_protocols | 97.1 us                                                               | 95.8 us: 1.01x faster                                                           |
| create_gc_cycles         | 1.36 ms                                                               | 1.35 ms: 1.01x faster                                                           |
| python_startup_no_site   | 12.8 ms                                                               | 12.7 ms: 1.01x faster                                                           |
| deepcopy_reduce          | 1.80 us                                                               | 1.78 us: 1.01x faster                                                           |
| sqlglot_v2_parse         | 787 us                                                                | 781 us: 1.01x faster                                                            |
| xml_etree_generate       | 49.6 ms                                                               | 49.2 ms: 1.01x faster                                                           |
| xml_etree_parse          | 98.1 ms                                                               | 97.5 ms: 1.01x faster                                                           |
| coroutines               | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                           |
| bpe_tokeniser            | 2.93 sec                                                              | 2.92 sec: 1.00x faster                                                          |
| xml_etree_process        | 34.7 ms                                                               | 34.5 ms: 1.00x faster                                                           |
| sqlglot_v2_normalize     | 68.8 ms                                                               | 68.6 ms: 1.00x faster                                                           |
| generators               | 24.6 ms                                                               | 24.5 ms: 1.00x faster                                                           |
| meteor_contest           | 74.1 ms                                                               | 73.9 ms: 1.00x faster                                                           |
| async_tree_eager         | 64.7 ms                                                               | 64.6 ms: 1.00x faster                                                           |
| scimark_fft              | 191 ms                                                                | 191 ms: 1.00x faster                                                            |
| nbody                    | 71.7 ms                                                               | 71.6 ms: 1.00x faster                                                           |
| comprehensions           | 11.3 us                                                               | 11.3 us: 1.00x slower                                                           |
| richards                 | 33.7 ms                                                               | 33.8 ms: 1.00x slower                                                           |
| deepcopy_memo            | 22.0 us                                                               | 22.0 us: 1.00x slower                                                           |
| pyflate                  | 287 ms                                                                | 288 ms: 1.00x slower                                                            |
| logging_silent           | 73.9 ns                                                               | 74.2 ns: 1.00x slower                                                           |
| logging_simple           | 3.39 us                                                               | 3.41 us: 1.00x slower                                                           |
| raytrace                 | 176 ms                                                                | 177 ms: 1.00x slower                                                            |
| sympy_expand             | 248 ms                                                                | 249 ms: 1.00x slower                                                            |
| nqueens                  | 62.0 ms                                                               | 62.2 ms: 1.00x slower                                                           |
| hexiom                   | 4.61 ms                                                               | 4.62 ms: 1.00x slower                                                           |
| regex_effbot             | 2.14 ms                                                               | 2.15 ms: 1.00x slower                                                           |
| sympy_str                | 146 ms                                                                | 147 ms: 1.00x slower                                                            |
| json_loads               | 17.4 us                                                               | 17.4 us: 1.00x slower                                                           |
| sqlite_synth             | 1.57 us                                                               | 1.58 us: 1.00x slower                                                           |
| thrift                   | 455 us                                                                | 457 us: 1.00x slower                                                            |
| sympy_integrate          | 10.9 ms                                                               | 10.9 ms: 1.01x slower                                                           |
| docutils                 | 1.45 sec                                                              | 1.45 sec: 1.01x slower                                                          |
| many_optionals           | 592 us                                                                | 595 us: 1.01x slower                                                            |
| unpickle_pure_python     | 128 us                                                                | 129 us: 1.01x slower                                                            |
| logging_format           | 3.67 us                                                               | 3.69 us: 1.01x slower                                                           |
| regex_compile            | 72.8 ms                                                               | 73.3 ms: 1.01x slower                                                           |
| pickle_pure_python       | 207 us                                                                | 209 us: 1.01x slower                                                            |
| django_template          | 23.1 ms                                                               | 23.3 ms: 1.01x slower                                                           |
| json_dumps               | 6.63 ms                                                               | 6.69 ms: 1.01x slower                                                           |
| go                       | 88.2 ms                                                               | 89.1 ms: 1.01x slower                                                           |
| async_generators         | 283 ms                                                                | 286 ms: 1.01x slower                                                            |
| deltablue                | 2.51 ms                                                               | 2.54 ms: 1.01x slower                                                           |
| pprint_safe_repr         | 444 ms                                                                | 450 ms: 1.01x slower                                                            |
| genshi_xml               | 33.1 ms                                                               | 33.5 ms: 1.01x slower                                                           |
| regex_v8                 | 15.2 ms                                                               | 15.5 ms: 1.02x slower                                                           |
| genshi_text              | 15.4 ms                                                               | 15.7 ms: 1.02x slower                                                           |
| pycparser                | 688 ms                                                                | 702 ms: 1.02x slower                                                            |
| scimark_monte_carlo      | 45.9 ms                                                               | 49.0 ms: 1.07x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (49): pprint_pformat, k_core, dask, dulwich_log, chaos, mako, connected_components, coverage, asyncio_websockets, async_tree_io, sqlglot_v2_optimize, xml_etree_iterparse, gc_traversal, pidigits, scimark_sparse_mat_mult, spectral_norm, 2to3, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, scimark_lu, regex_dna, fannkuch, html5lib, mdp, async_tree_eager_io, shortest_path, richards_super, crypto_pyaes, subparsers, sphinx, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, deepcopy, async_tree_eager_memoization, async_tree_none_tg, sqlglot_v2_transpile, async_tree_none, pylint, async_tree_memoization, sympy_sum, float, async_tree_eager_tg, tomli_loads, pathlib, async_tree_eager_memoization_tg, json, async_tree_eager_io_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x