# Results vs. base

- fork: faster-cpython
- ref: spill_stack_pointer_
- machine: linux-x86_64
- commit hash: fb5ef8e
- commit date: 2024-06-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                | 271 ms: 1.01x slower                                                            |
| docutils       | 2.78 sec                                                              | 2.80 sec: 1.01x slower                                                          |
| html5lib       | 68.2 ms                                                               | 67.7 ms: 1.01x faster                                                           |
| tornado_http   | 93.4 ms                                                               | 94.9 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.2 ms                                                               | 79.3 ms: 1.01x slower                                                           |
| nbody          | 88.8 ms                                                               | 92.1 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 232 ms                                                                | 223 ms: 1.04x faster                                                            |
| regex_effbot   | 3.70 ms                                                               | 3.67 ms: 1.01x faster                                                           |
| regex_compile  | 135 ms                                                                | 136 ms: 1.01x slower                                                            |
| regex_v8       | 24.4 ms                                                               | 24.8 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle               | 12.1 us                                                               | 11.7 us: 1.04x faster                                                           |
| pickle_list          | 5.18 us                                                               | 5.04 us: 1.03x faster                                                           |
| pickle_dict          | 36.3 us                                                               | 35.3 us: 1.03x faster                                                           |
| xml_etree_process    | 61.6 ms                                                               | 60.3 ms: 1.02x faster                                                           |
| unpickle_list        | 5.50 us                                                               | 5.40 us: 1.02x faster                                                           |
| xml_etree_generate   | 88.6 ms                                                               | 87.0 ms: 1.02x faster                                                           |
| json_dumps           | 10.7 ms                                                               | 10.6 ms: 1.02x faster                                                           |
| xml_etree_parse      | 161 ms                                                                | 158 ms: 1.02x faster                                                            |
| pickle_pure_python   | 305 us                                                                | 302 us: 1.01x faster                                                            |
| json_loads           | 29.0 us                                                               | 28.8 us: 1.01x faster                                                           |
| tomli_loads          | 2.15 sec                                                              | 2.19 sec: 1.02x slower                                                          |
| unpickle_pure_python | 216 us                                                                | 223 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.12 ms                                                               | 7.13 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                               | 10.9 ms: 1.02x faster                                                           |
| genshi_xml      | 51.4 ms                                                               | 50.5 ms: 1.02x faster                                                           |
| genshi_text     | 23.9 ms                                                               | 23.6 ms: 1.01x faster                                                           |
| django_template | 35.1 ms                                                               | 36.1 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators               | 29.3 ms                                                               | 27.9 ms: 1.05x faster                                                           |
| regex_dna                | 232 ms                                                                | 223 ms: 1.04x faster                                                            |
| pickle                   | 12.1 us                                                               | 11.7 us: 1.04x faster                                                           |
| coroutines               | 23.9 ms                                                               | 23.1 ms: 1.04x faster                                                           |
| mdp                      | 2.79 sec                                                              | 2.71 sec: 1.03x faster                                                          |
| pickle_list              | 5.18 us                                                               | 5.04 us: 1.03x faster                                                           |
| pickle_dict              | 36.3 us                                                               | 35.3 us: 1.03x faster                                                           |
| xml_etree_process        | 61.6 ms                                                               | 60.3 ms: 1.02x faster                                                           |
| mako                     | 11.2 ms                                                               | 10.9 ms: 1.02x faster                                                           |
| unpickle_list            | 5.50 us                                                               | 5.40 us: 1.02x faster                                                           |
| xml_etree_generate       | 88.6 ms                                                               | 87.0 ms: 1.02x faster                                                           |
| genshi_xml               | 51.4 ms                                                               | 50.5 ms: 1.02x faster                                                           |
| json_dumps               | 10.7 ms                                                               | 10.6 ms: 1.02x faster                                                           |
| xml_etree_parse          | 161 ms                                                                | 158 ms: 1.02x faster                                                            |
| genshi_text              | 23.9 ms                                                               | 23.6 ms: 1.01x faster                                                           |
| typing_runtime_protocols | 170 us                                                                | 168 us: 1.01x faster                                                            |
| pickle_pure_python       | 305 us                                                                | 302 us: 1.01x faster                                                            |
| html5lib                 | 68.2 ms                                                               | 67.7 ms: 1.01x faster                                                           |
| json_loads               | 29.0 us                                                               | 28.8 us: 1.01x faster                                                           |
| regex_effbot             | 3.70 ms                                                               | 3.67 ms: 1.01x faster                                                           |
| scimark_monte_carlo      | 69.0 ms                                                               | 68.5 ms: 1.01x faster                                                           |
| pathlib                  | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                           |
| richards                 | 48.5 ms                                                               | 48.3 ms: 1.01x faster                                                           |
| deepcopy_memo            | 39.7 us                                                               | 39.5 us: 1.01x faster                                                           |
| asyncio_websockets       | 566 ms                                                                | 564 ms: 1.00x faster                                                            |
| deepcopy                 | 367 us                                                                | 366 us: 1.00x faster                                                            |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site   | 7.12 ms                                                               | 7.13 ms: 1.00x slower                                                           |
| raytrace                 | 263 ms                                                                | 264 ms: 1.00x slower                                                            |
| chaos                    | 60.5 ms                                                               | 60.8 ms: 1.00x slower                                                           |
| pprint_pformat           | 1.52 sec                                                              | 1.53 sec: 1.01x slower                                                          |
| hexiom                   | 6.13 ms                                                               | 6.16 ms: 1.01x slower                                                           |
| bench_thread_pool        | 824 us                                                                | 828 us: 1.01x slower                                                            |
| pprint_safe_repr         | 740 ms                                                                | 745 ms: 1.01x slower                                                            |
| docutils                 | 2.78 sec                                                              | 2.80 sec: 1.01x slower                                                          |
| gc_traversal             | 3.97 ms                                                               | 4.00 ms: 1.01x slower                                                           |
| sqlite_synth             | 2.94 us                                                               | 2.97 us: 1.01x slower                                                           |
| regex_compile            | 135 ms                                                                | 136 ms: 1.01x slower                                                            |
| deltablue                | 3.23 ms                                                               | 3.26 ms: 1.01x slower                                                           |
| create_gc_cycles         | 1.78 ms                                                               | 1.80 ms: 1.01x slower                                                           |
| comprehensions           | 16.8 us                                                               | 16.9 us: 1.01x slower                                                           |
| dulwich_log              | 65.2 ms                                                               | 65.8 ms: 1.01x slower                                                           |
| go                       | 143 ms                                                                | 145 ms: 1.01x slower                                                            |
| sympy_sum                | 155 ms                                                                | 157 ms: 1.01x slower                                                            |
| sympy_integrate          | 20.3 ms                                                               | 20.5 ms: 1.01x slower                                                           |
| sympy_str                | 279 ms                                                                | 282 ms: 1.01x slower                                                            |
| pycparser                | 1.16 sec                                                              | 1.17 sec: 1.01x slower                                                          |
| sqlglot_optimize         | 54.7 ms                                                               | 55.4 ms: 1.01x slower                                                           |
| 2to3                     | 268 ms                                                                | 271 ms: 1.01x slower                                                            |
| sympy_expand             | 470 ms                                                                | 476 ms: 1.01x slower                                                            |
| meteor_contest           | 109 ms                                                                | 110 ms: 1.01x slower                                                            |
| json                     | 5.32 ms                                                               | 5.39 ms: 1.01x slower                                                           |
| float                    | 78.2 ms                                                               | 79.3 ms: 1.01x slower                                                           |
| scimark_fft              | 374 ms                                                                | 379 ms: 1.01x slower                                                            |
| coverage                 | 92.7 ms                                                               | 94.2 ms: 1.02x slower                                                           |
| tornado_http             | 93.4 ms                                                               | 94.9 ms: 1.02x slower                                                           |
| fannkuch                 | 393 ms                                                                | 399 ms: 1.02x slower                                                            |
| regex_v8                 | 24.4 ms                                                               | 24.8 ms: 1.02x slower                                                           |
| tomli_loads              | 2.15 sec                                                              | 2.19 sec: 1.02x slower                                                          |
| sqlglot_transpile        | 1.61 ms                                                               | 1.64 ms: 1.02x slower                                                           |
| sqlglot_normalize        | 109 ms                                                                | 111 ms: 1.02x slower                                                            |
| nqueens                  | 79.7 ms                                                               | 81.3 ms: 1.02x slower                                                           |
| scimark_sor              | 123 ms                                                                | 126 ms: 1.02x slower                                                            |
| sqlglot_parse            | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                           |
| asyncio_tcp              | 497 ms                                                                | 509 ms: 1.02x slower                                                            |
| crypto_pyaes             | 74.3 ms                                                               | 76.4 ms: 1.03x slower                                                           |
| spectral_norm            | 113 ms                                                                | 116 ms: 1.03x slower                                                            |
| django_template          | 35.1 ms                                                               | 36.1 ms: 1.03x slower                                                           |
| unpickle_pure_python     | 216 us                                                                | 223 us: 1.03x slower                                                            |
| logging_silent           | 100 ns                                                                | 104 ns: 1.03x slower                                                            |
| logging_simple           | 5.68 us                                                               | 5.89 us: 1.04x slower                                                           |
| nbody                    | 88.8 ms                                                               | 92.1 ms: 1.04x slower                                                           |
| async_generators         | 439 ms                                                                | 458 ms: 1.04x slower                                                            |
| logging_format           | 6.27 us                                                               | 6.55 us: 1.04x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (22): async_tree_cpu_io_mixed_tg, unpickle, xml_etree_iterparse, thrift, async_tree_memoization_tg, richards_super, async_tree_io_tg, scimark_sparse_mat_mult, async_tree_none_tg, asyncio_tcp_ssl, scimark_lu, pyflate, pylint, bench_mp_pool, pidigits, deepcopy_reduce, async_tree_cpu_io_mixed, telco, dask, async_tree_io, async_tree_none, async_tree_memoization

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x