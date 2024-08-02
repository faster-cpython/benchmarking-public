# Results vs. base

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.01x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| chameleon      | 7.04 ms                                                               | 7.12 ms: 1.01x slower                                                           |
| docutils       | 2.94 sec                                                              | 2.96 sec: 1.01x slower                                                          |
| html5lib       | 68.2 ms                                                               | 67.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.7 ms                                                               | 81.0 ms: 1.01x faster                                                           |
| pidigits       | 189 ms                                                                | 189 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                | 136 ms: 1.01x faster                                                            |
| regex_effbot   | 3.79 ms                                                               | 3.87 ms: 1.02x slower                                                           |
| regex_dna      | 225 ms                                                                | 233 ms: 1.03x slower                                                            |
| regex_v8       | 25.5 ms                                                               | 26.5 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_dict          | 35.8 us                                                               | 35.6 us: 1.00x faster                                                           |
| pickle_list          | 5.13 us                                                               | 5.15 us: 1.00x slower                                                           |
| unpickle_pure_python | 221 us                                                                | 222 us: 1.00x slower                                                            |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| unpickle_list        | 5.16 us                                                               | 5.31 us: 1.03x slower                                                           |
| pickle_pure_python   | 293 us                                                                | 302 us: 1.03x slower                                                            |
| tomli_loads          | 1.95 sec                                                              | 2.11 sec: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): unpickle, pickle, xml_etree_parse, json_loads, xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.57 ms                                                               | 7.59 ms: 1.00x slower                                                           |
| python_startup         | 10.8 ms                                                               | 10.9 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.95 ms                                                               | 10.1 ms: 1.01x slower                                                           |
| genshi_text     | 25.1 ms                                                               | 25.6 ms: 1.02x slower                                                           |
| django_template | 35.8 ms                                                               | 36.7 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| chaos                    | 59.7 ms                                                               | 57.7 ms: 1.03x faster                                                           |
| logging_format           | 6.40 us                                                               | 6.24 us: 1.03x faster                                                           |
| scimark_sor              | 138 ms                                                                | 134 ms: 1.03x faster                                                            |
| logging_simple           | 5.80 us                                                               | 5.68 us: 1.02x faster                                                           |
| crypto_pyaes             | 67.9 ms                                                               | 66.6 ms: 1.02x faster                                                           |
| json                     | 5.34 ms                                                               | 5.25 ms: 1.02x faster                                                           |
| meteor_contest           | 110 ms                                                                | 108 ms: 1.02x faster                                                            |
| pathlib                  | 16.6 ms                                                               | 16.4 ms: 1.01x faster                                                           |
| html5lib                 | 68.2 ms                                                               | 67.3 ms: 1.01x faster                                                           |
| regex_compile            | 138 ms                                                                | 136 ms: 1.01x faster                                                            |
| comprehensions           | 16.6 us                                                               | 16.5 us: 1.01x faster                                                           |
| nbody                    | 81.7 ms                                                               | 81.0 ms: 1.01x faster                                                           |
| deepcopy                 | 373 us                                                                | 370 us: 1.01x faster                                                            |
| pickle_dict              | 35.8 us                                                               | 35.6 us: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.87 sec                                                              | 1.86 sec: 1.00x faster                                                          |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x slower                                                            |
| python_startup_no_site   | 7.57 ms                                                               | 7.59 ms: 1.00x slower                                                           |
| python_startup           | 10.8 ms                                                               | 10.9 ms: 1.00x slower                                                           |
| pickle_list              | 5.13 us                                                               | 5.15 us: 1.00x slower                                                           |
| async_generators         | 461 ms                                                                | 463 ms: 1.00x slower                                                            |
| unpickle_pure_python     | 221 us                                                                | 222 us: 1.00x slower                                                            |
| asyncio_websockets       | 567 ms                                                                | 570 ms: 1.00x slower                                                            |
| sqlglot_optimize         | 56.5 ms                                                               | 56.8 ms: 1.01x slower                                                           |
| bench_thread_pool        | 860 us                                                                | 865 us: 1.01x slower                                                            |
| docutils                 | 2.94 sec                                                              | 2.96 sec: 1.01x slower                                                          |
| dulwich_log              | 68.9 ms                                                               | 69.4 ms: 1.01x slower                                                           |
| telco                    | 8.28 ms                                                               | 8.34 ms: 1.01x slower                                                           |
| create_gc_cycles         | 1.80 ms                                                               | 1.82 ms: 1.01x slower                                                           |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| raytrace                 | 279 ms                                                                | 281 ms: 1.01x slower                                                            |
| typing_runtime_protocols | 170 us                                                                | 171 us: 1.01x slower                                                            |
| richards_super           | 47.8 ms                                                               | 48.2 ms: 1.01x slower                                                           |
| go                       | 149 ms                                                                | 151 ms: 1.01x slower                                                            |
| deepcopy_memo            | 38.0 us                                                               | 38.5 us: 1.01x slower                                                           |
| sympy_expand             | 508 ms                                                                | 514 ms: 1.01x slower                                                            |
| chameleon                | 7.04 ms                                                               | 7.12 ms: 1.01x slower                                                           |
| logging_silent           | 105 ns                                                                | 107 ns: 1.01x slower                                                            |
| mako                     | 9.95 ms                                                               | 10.1 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 112 ms                                                                | 114 ms: 1.01x slower                                                            |
| fannkuch                 | 355 ms                                                                | 360 ms: 1.01x slower                                                            |
| pyflate                  | 444 ms                                                                | 450 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.30 ms                                                               | 1.32 ms: 1.01x slower                                                           |
| scimark_lu               | 124 ms                                                                | 125 ms: 1.01x slower                                                            |
| sqlite_synth             | 2.85 us                                                               | 2.89 us: 1.02x slower                                                           |
| pprint_pformat           | 1.43 sec                                                              | 1.45 sec: 1.02x slower                                                          |
| sqlglot_transpile        | 1.64 ms                                                               | 1.67 ms: 1.02x slower                                                           |
| richards                 | 41.5 ms                                                               | 42.2 ms: 1.02x slower                                                           |
| coverage                 | 91.9 ms                                                               | 93.8 ms: 1.02x slower                                                           |
| nqueens                  | 85.4 ms                                                               | 87.2 ms: 1.02x slower                                                           |
| deepcopy_reduce          | 3.29 us                                                               | 3.36 us: 1.02x slower                                                           |
| deltablue                | 3.71 ms                                                               | 3.79 ms: 1.02x slower                                                           |
| coroutines               | 22.8 ms                                                               | 23.3 ms: 1.02x slower                                                           |
| genshi_text              | 25.1 ms                                                               | 25.6 ms: 1.02x slower                                                           |
| regex_effbot             | 3.79 ms                                                               | 3.87 ms: 1.02x slower                                                           |
| mdp                      | 2.58 sec                                                              | 2.64 sec: 1.02x slower                                                          |
| django_template          | 35.8 ms                                                               | 36.7 ms: 1.03x slower                                                           |
| unpickle_list            | 5.16 us                                                               | 5.31 us: 1.03x slower                                                           |
| generators               | 30.3 ms                                                               | 31.2 ms: 1.03x slower                                                           |
| pickle_pure_python       | 293 us                                                                | 302 us: 1.03x slower                                                            |
| regex_dna                | 225 ms                                                                | 233 ms: 1.03x slower                                                            |
| regex_v8                 | 25.5 ms                                                               | 26.5 ms: 1.04x slower                                                           |
| gc_traversal             | 3.84 ms                                                               | 4.08 ms: 1.06x slower                                                           |
| scimark_fft              | 312 ms                                                                | 334 ms: 1.07x slower                                                            |
| tomli_loads              | 1.95 sec                                                              | 2.11 sec: 1.08x slower                                                          |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.82 ms: 1.12x slower                                                           |
| spectral_norm            | 101 ms                                                                | 116 ms: 1.14x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (32): async_tree_memoization, unpickle, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, pickle, async_tree_memoization_tg, xml_etree_parse, thrift, async_tree_io_tg, async_tree_io, asyncio_tcp, async_tree_none, flaskblogging, json_loads, 2to3, sympy_sum, sympy_integrate, scimark_monte_carlo, xml_etree_iterparse, pprint_safe_repr, hexiom, sympy_str, float, pylint, xml_etree_process, bench_mp_pool, pycparser, tornado_http, xml_etree_generate, genshi_xml, dask

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x