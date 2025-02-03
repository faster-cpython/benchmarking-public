# Results vs. base

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: 1cbd7aa
- commit date: 2025-02-03
- overall geometric mean: 1.001x faster
- HPT reliability: 64.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                       | 279 ms: 1.00x faster                                                         |
| docutils       | 2.84 sec                                                                     | 2.85 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|--------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_websockets | 387 ms                                                                       | 384 ms: 1.01x faster                                                         |
| async_generators   | 410 ms                                                                       | 408 ms: 1.00x faster                                                         |
| coroutines         | 20.8 ms                                                                      | 20.7 ms: 1.00x faster                                                        |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 86.5 ms                                                                      | 87.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 236 ms                                                                       | 233 ms: 1.01x faster                                                         |
| regex_v8       | 25.9 ms                                                                      | 25.6 ms: 1.01x faster                                                        |
| regex_compile  | 134 ms                                                                       | 135 ms: 1.01x slower                                                         |
| regex_effbot   | 3.04 ms                                                                      | 3.14 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|---------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 136 ms                                                                       | 132 ms: 1.02x faster                                                         |
| json_loads          | 26.9 us                                                                      | 26.3 us: 1.02x faster                                                        |
| xml_etree_iterparse | 97.6 ms                                                                      | 95.6 ms: 1.02x faster                                                        |
| tomli_loads         | 2.08 sec                                                                     | 2.05 sec: 1.01x faster                                                       |
| pickle_pure_python  | 323 us                                                                       | 324 us: 1.01x slower                                                         |
| xml_etree_process   | 58.5 ms                                                                      | 59.0 ms: 1.01x slower                                                        |
| Geometric mean      | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 8.97 ms: 1.01x faster                                                        |
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 24.5 ms                                                                      | 22.9 ms: 1.07x faster                                                        |
| genshi_xml      | 55.0 ms                                                                      | 51.8 ms: 1.06x faster                                                        |
| django_template | 35.1 ms                                                                      | 35.4 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|--------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text              | 24.5 ms                                                                      | 22.9 ms: 1.07x faster                                                        |
| genshi_xml               | 55.0 ms                                                                      | 51.8 ms: 1.06x faster                                                        |
| spectral_norm            | 83.4 ms                                                                      | 79.9 ms: 1.04x faster                                                        |
| xml_etree_parse          | 136 ms                                                                       | 132 ms: 1.02x faster                                                         |
| bench_thread_pool        | 940 us                                                                       | 920 us: 1.02x faster                                                         |
| json_loads               | 26.9 us                                                                      | 26.3 us: 1.02x faster                                                        |
| xml_etree_iterparse      | 97.6 ms                                                                      | 95.6 ms: 1.02x faster                                                        |
| scimark_sor              | 108 ms                                                                       | 107 ms: 1.02x faster                                                         |
| scimark_monte_carlo      | 62.8 ms                                                                      | 62.0 ms: 1.01x faster                                                        |
| tomli_loads              | 2.08 sec                                                                     | 2.05 sec: 1.01x faster                                                       |
| pprint_pformat           | 1.61 sec                                                                     | 1.59 sec: 1.01x faster                                                       |
| regex_dna                | 236 ms                                                                       | 233 ms: 1.01x faster                                                         |
| regex_v8                 | 25.9 ms                                                                      | 25.6 ms: 1.01x faster                                                        |
| typing_runtime_protocols | 169 us                                                                       | 167 us: 1.01x faster                                                         |
| sqlalchemy_imperative    | 17.7 ms                                                                      | 17.6 ms: 1.01x faster                                                        |
| crypto_pyaes             | 72.7 ms                                                                      | 72.0 ms: 1.01x faster                                                        |
| sqlglot_parse            | 1.33 ms                                                                      | 1.32 ms: 1.01x faster                                                        |
| mdp                      | 2.47 sec                                                                     | 2.45 sec: 1.01x faster                                                       |
| telco                    | 7.93 ms                                                                      | 7.86 ms: 1.01x faster                                                        |
| hexiom                   | 6.06 ms                                                                      | 6.01 ms: 1.01x faster                                                        |
| deltablue                | 3.25 ms                                                                      | 3.23 ms: 1.01x faster                                                        |
| asyncio_websockets       | 387 ms                                                                       | 384 ms: 1.01x faster                                                         |
| coverage                 | 79.3 ms                                                                      | 78.8 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult  | 4.66 ms                                                                      | 4.64 ms: 1.01x faster                                                        |
| pprint_safe_repr         | 785 ms                                                                       | 781 ms: 1.01x faster                                                         |
| python_startup_no_site   | 9.02 ms                                                                      | 8.97 ms: 1.01x faster                                                        |
| async_generators         | 410 ms                                                                       | 408 ms: 1.00x faster                                                         |
| go                       | 123 ms                                                                       | 123 ms: 1.00x faster                                                         |
| sqlglot_normalize        | 114 ms                                                                       | 114 ms: 1.00x faster                                                         |
| python_startup           | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                        |
| richards                 | 45.3 ms                                                                      | 45.1 ms: 1.00x faster                                                        |
| pathlib                  | 15.7 ms                                                                      | 15.6 ms: 1.00x faster                                                        |
| sympy_expand             | 487 ms                                                                       | 485 ms: 1.00x faster                                                         |
| scimark_fft              | 305 ms                                                                       | 305 ms: 1.00x faster                                                         |
| coroutines               | 20.8 ms                                                                      | 20.7 ms: 1.00x faster                                                        |
| 2to3                     | 279 ms                                                                       | 279 ms: 1.00x faster                                                         |
| meteor_contest           | 124 ms                                                                       | 124 ms: 1.00x slower                                                         |
| scimark_lu               | 93.7 ms                                                                      | 94.0 ms: 1.00x slower                                                        |
| docutils                 | 2.84 sec                                                                     | 2.85 sec: 1.00x slower                                                       |
| sympy_integrate          | 22.9 ms                                                                      | 23.0 ms: 1.00x slower                                                        |
| subparsers               | 22.6 ms                                                                      | 22.7 ms: 1.00x slower                                                        |
| pickle_pure_python       | 323 us                                                                       | 324 us: 1.01x slower                                                         |
| django_template          | 35.1 ms                                                                      | 35.4 ms: 1.01x slower                                                        |
| xml_etree_process        | 58.5 ms                                                                      | 59.0 ms: 1.01x slower                                                        |
| connected_components     | 413 ms                                                                       | 417 ms: 1.01x slower                                                         |
| many_optionals           | 999 us                                                                       | 1.01 ms: 1.01x slower                                                        |
| regex_compile            | 134 ms                                                                       | 135 ms: 1.01x slower                                                         |
| generators               | 28.4 ms                                                                      | 28.7 ms: 1.01x slower                                                        |
| dulwich_log              | 65.4 ms                                                                      | 66.2 ms: 1.01x slower                                                        |
| sqlalchemy_declarative   | 141 ms                                                                       | 142 ms: 1.01x slower                                                         |
| pycparser                | 1.22 sec                                                                     | 1.23 sec: 1.01x slower                                                       |
| create_gc_cycles         | 2.68 ms                                                                      | 2.71 ms: 1.01x slower                                                        |
| nbody                    | 86.5 ms                                                                      | 87.9 ms: 1.02x slower                                                        |
| fannkuch                 | 355 ms                                                                       | 361 ms: 1.02x slower                                                         |
| bpe_tokeniser            | 4.48 sec                                                                     | 4.56 sec: 1.02x slower                                                       |
| chaos                    | 58.5 ms                                                                      | 60.0 ms: 1.03x slower                                                        |
| pyflate                  | 430 ms                                                                       | 442 ms: 1.03x slower                                                         |
| logging_simple           | 6.17 us                                                                      | 6.35 us: 1.03x slower                                                        |
| logging_format           | 6.75 us                                                                      | 6.97 us: 1.03x slower                                                        |
| regex_effbot             | 3.04 ms                                                                      | 3.14 ms: 1.03x slower                                                        |
| gc_traversal             | 6.10 ms                                                                      | 6.33 ms: 1.04x slower                                                        |
| Geometric mean           | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (35): bench_mp_pool, k_core, json, raytrace, async_tree_none_tg, async_tree_cpu_io_mixed_tg, json_dumps, sqlglot_optimize, pidigits, deepcopy_reduce, logging_silent, sqlite_synth, richards_super, async_tree_memoization_tg, html5lib, deepcopy, async_tree_none, sympy_sum, comprehensions, float, nqueens, pylint, async_tree_memoization, async_tree_cpu_io_mixed, sympy_str, sqlglot_transpile, mako, unpickle_pure_python, deepcopy_memo, shortest_path, xml_etree_generate, async_tree_io, sphinx, thrift, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 64.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x