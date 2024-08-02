# Results vs. base

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.00x slower
- HPT reliability: 98.07%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                | 271 ms: 1.00x slower                                                            |
| chameleon      | 6.91 ms                                                               | 7.03 ms: 1.02x slower                                                           |
| html5lib       | 67.5 ms                                                               | 67.2 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.0 ms                                                               | 78.5 ms: 1.01x slower                                                           |
| pidigits       | 189 ms                                                                | 191 ms: 1.01x slower                                                            |
| nbody          | 85.6 ms                                                               | 97.1 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 221 ms: 1.03x faster                                                            |
| regex_v8       | 24.7 ms                                                               | 24.2 ms: 1.02x faster                                                           |
| regex_compile  | 135 ms                                                                | 133 ms: 1.01x faster                                                            |
| regex_effbot   | 3.89 ms                                                               | 3.85 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle             | 15.5 us                                                               | 15.2 us: 1.02x faster                                                           |
| pickle               | 12.1 us                                                               | 12.0 us: 1.01x faster                                                           |
| xml_etree_generate   | 86.5 ms                                                               | 85.8 ms: 1.01x faster                                                           |
| unpickle_list        | 5.38 us                                                               | 5.35 us: 1.01x faster                                                           |
| pickle_list          | 5.21 us                                                               | 5.19 us: 1.00x faster                                                           |
| pickle_dict          | 36.1 us                                                               | 35.9 us: 1.00x faster                                                           |
| json_dumps           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| pickle_pure_python   | 304 us                                                                | 309 us: 1.02x slower                                                            |
| tomli_loads          | 2.14 sec                                                              | 2.18 sec: 1.02x slower                                                          |
| unpickle_pure_python | 217 us                                                                | 222 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                               | 7.11 ms: 1.01x slower                                                           |
| python_startup         | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                               | 11.1 ms: 1.00x slower                                                           |
| django_template | 34.6 ms                                                               | 34.7 ms: 1.00x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| spectral_norm            | 116 ms                                                                | 108 ms: 1.08x faster                                                            |
| crypto_pyaes             | 76.1 ms                                                               | 72.4 ms: 1.05x faster                                                           |
| regex_dna                | 228 ms                                                                | 221 ms: 1.03x faster                                                            |
| pyflate                  | 484 ms                                                                | 472 ms: 1.03x faster                                                            |
| unpickle                 | 15.5 us                                                               | 15.2 us: 1.02x faster                                                           |
| regex_v8                 | 24.7 ms                                                               | 24.2 ms: 1.02x faster                                                           |
| thrift                   | 827 us                                                                | 814 us: 1.02x faster                                                            |
| scimark_sor              | 135 ms                                                                | 133 ms: 1.02x faster                                                            |
| pathlib                  | 16.8 ms                                                               | 16.6 ms: 1.01x faster                                                           |
| sqlite_synth             | 3.00 us                                                               | 2.96 us: 1.01x faster                                                           |
| regex_compile            | 135 ms                                                                | 133 ms: 1.01x faster                                                            |
| richards_super           | 54.8 ms                                                               | 54.1 ms: 1.01x faster                                                           |
| deltablue                | 3.27 ms                                                               | 3.23 ms: 1.01x faster                                                           |
| pickle                   | 12.1 us                                                               | 12.0 us: 1.01x faster                                                           |
| regex_effbot             | 3.89 ms                                                               | 3.85 ms: 1.01x faster                                                           |
| xml_etree_generate       | 86.5 ms                                                               | 85.8 ms: 1.01x faster                                                           |
| genshi_text              | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                                           |
| coverage                 | 93.2 ms                                                               | 92.4 ms: 1.01x faster                                                           |
| meteor_contest           | 110 ms                                                                | 109 ms: 1.01x faster                                                            |
| typing_runtime_protocols | 164 us                                                                | 163 us: 1.01x faster                                                            |
| go                       | 143 ms                                                                | 142 ms: 1.01x faster                                                            |
| unpickle_list            | 5.38 us                                                               | 5.35 us: 1.01x faster                                                           |
| comprehensions           | 16.6 us                                                               | 16.5 us: 1.01x faster                                                           |
| richards                 | 48.1 ms                                                               | 47.9 ms: 1.00x faster                                                           |
| pickle_list              | 5.21 us                                                               | 5.19 us: 1.00x faster                                                           |
| pickle_dict              | 36.1 us                                                               | 35.9 us: 1.00x faster                                                           |
| html5lib                 | 67.5 ms                                                               | 67.2 ms: 1.00x faster                                                           |
| json_dumps               | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                              | 1.85 sec: 1.00x slower                                                          |
| 2to3                     | 270 ms                                                                | 271 ms: 1.00x slower                                                            |
| mako                     | 11.1 ms                                                               | 11.1 ms: 1.00x slower                                                           |
| django_template          | 34.6 ms                                                               | 34.7 ms: 1.00x slower                                                           |
| sqlglot_normalize        | 108 ms                                                                | 109 ms: 1.01x slower                                                            |
| asyncio_websockets       | 566 ms                                                                | 569 ms: 1.01x slower                                                            |
| python_startup_no_site   | 7.07 ms                                                               | 7.11 ms: 1.01x slower                                                           |
| float                    | 78.0 ms                                                               | 78.5 ms: 1.01x slower                                                           |
| sqlglot_transpile        | 1.61 ms                                                               | 1.62 ms: 1.01x slower                                                           |
| python_startup           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| async_generators         | 441 ms                                                                | 444 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.30 ms                                                               | 1.31 ms: 1.01x slower                                                           |
| pidigits                 | 189 ms                                                                | 191 ms: 1.01x slower                                                            |
| deepcopy_reduce          | 3.24 us                                                               | 3.27 us: 1.01x slower                                                           |
| asyncio_tcp              | 505 ms                                                                | 509 ms: 1.01x slower                                                            |
| chaos                    | 61.0 ms                                                               | 61.7 ms: 1.01x slower                                                           |
| logging_simple           | 5.75 us                                                               | 5.82 us: 1.01x slower                                                           |
| pprint_pformat           | 1.51 sec                                                              | 1.53 sec: 1.01x slower                                                          |
| gc_traversal             | 3.72 ms                                                               | 3.78 ms: 1.01x slower                                                           |
| deepcopy                 | 359 us                                                                | 365 us: 1.01x slower                                                            |
| pickle_pure_python       | 304 us                                                                | 309 us: 1.02x slower                                                            |
| scimark_monte_carlo      | 68.5 ms                                                               | 69.6 ms: 1.02x slower                                                           |
| chameleon                | 6.91 ms                                                               | 7.03 ms: 1.02x slower                                                           |
| nqueens                  | 79.9 ms                                                               | 81.3 ms: 1.02x slower                                                           |
| telco                    | 8.41 ms                                                               | 8.57 ms: 1.02x slower                                                           |
| tomli_loads              | 2.14 sec                                                              | 2.18 sec: 1.02x slower                                                          |
| scimark_sparse_mat_mult  | 5.21 ms                                                               | 5.31 ms: 1.02x slower                                                           |
| coroutines               | 23.8 ms                                                               | 24.3 ms: 1.02x slower                                                           |
| pprint_safe_repr         | 732 ms                                                                | 748 ms: 1.02x slower                                                            |
| logging_silent           | 102 ns                                                                | 104 ns: 1.02x slower                                                            |
| unpickle_pure_python     | 217 us                                                                | 222 us: 1.02x slower                                                            |
| generators               | 28.9 ms                                                               | 29.7 ms: 1.03x slower                                                           |
| mdp                      | 2.57 sec                                                              | 2.64 sec: 1.03x slower                                                          |
| fannkuch                 | 397 ms                                                                | 410 ms: 1.03x slower                                                            |
| deepcopy_memo            | 38.7 us                                                               | 40.0 us: 1.03x slower                                                           |
| scimark_fft              | 376 ms                                                                | 390 ms: 1.04x slower                                                            |
| hexiom                   | 6.09 ms                                                               | 6.32 ms: 1.04x slower                                                           |
| raytrace                 | 267 ms                                                                | 277 ms: 1.04x slower                                                            |
| nbody                    | 85.6 ms                                                               | 97.1 ms: 1.13x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (31): async_tree_io, json_loads, json, async_tree_none_tg, flaskblogging, async_tree_memoization_tg, xml_etree_process, async_tree_none, docutils, async_tree_io_tg, sympy_integrate, logging_format, async_tree_cpu_io_mixed_tg, tornado_http, scimark_lu, dulwich_log, bench_thread_pool, async_tree_cpu_io_mixed, pycparser, create_gc_cycles, genshi_xml, sympy_sum, sympy_str, dask, sympy_expand, bench_mp_pool, sqlglot_optimize, pylint, async_tree_memoization, xml_etree_iterparse, xml_etree_parse

# HPT report

- Reliability score: 98.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x