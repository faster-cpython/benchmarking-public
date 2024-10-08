# Results vs. base

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: 71920f1
- commit date: 2024-07-30
- overall geometric mean: 1.00x faster
- HPT reliability: 93.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 65.7 ms: 1.01x slower                                                           |
| tornado_http   | 92.7 ms                                                               | 92.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators | 457 ms                                                                | 450 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                          |
| asyncio_tcp      | 491 ms                                                                | 505 ms: 1.03x slower                                                            |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_none, async_tree_memoization_tg, coroutines, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.5 ms                                                               | 79.5 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.74 ms                                                               | 3.69 ms: 1.01x faster                                                           |
| regex_v8       | 25.6 ms                                                               | 25.4 ms: 1.01x faster                                                           |
| regex_compile  | 134 ms                                                                | 133 ms: 1.00x faster                                                            |
| regex_dna      | 221 ms                                                                | 221 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python  | 293 us                                                                | 294 us: 1.00x slower                                                            |
| xml_etree_iterparse | 99.1 ms                                                               | 99.5 ms: 1.00x slower                                                           |
| tomli_loads         | 1.91 sec                                                              | 1.93 sec: 1.01x slower                                                          |
| json_dumps          | 10.1 ms                                                               | 10.4 ms: 1.03x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (5): xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.18 ms                                                               | 7.16 ms: 1.00x faster                                                           |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 53.4 ms                                                               | 53.9 ms: 1.01x slower                                                           |
| genshi_text    | 23.7 ms                                                               | 24.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_sor              | 131 ms                                                                | 114 ms: 1.15x faster                                                            |
| scimark_lu               | 124 ms                                                                | 108 ms: 1.15x faster                                                            |
| typing_runtime_protocols | 176 us                                                                | 170 us: 1.03x faster                                                            |
| scimark_sparse_mat_mult  | 4.32 ms                                                               | 4.19 ms: 1.03x faster                                                           |
| logging_simple           | 5.60 us                                                               | 5.45 us: 1.03x faster                                                           |
| nbody                    | 81.5 ms                                                               | 79.5 ms: 1.02x faster                                                           |
| deepcopy_reduce          | 2.79 us                                                               | 2.73 us: 1.02x faster                                                           |
| logging_format           | 6.12 us                                                               | 6.00 us: 1.02x faster                                                           |
| crypto_pyaes             | 67.0 ms                                                               | 65.8 ms: 1.02x faster                                                           |
| deepcopy_memo            | 28.9 us                                                               | 28.4 us: 1.02x faster                                                           |
| async_generators         | 457 ms                                                                | 450 ms: 1.01x faster                                                            |
| regex_effbot             | 3.74 ms                                                               | 3.69 ms: 1.01x faster                                                           |
| go                       | 147 ms                                                                | 146 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                                           |
| regex_v8                 | 25.6 ms                                                               | 25.4 ms: 1.01x faster                                                           |
| sqlglot_parse            | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                           |
| tornado_http             | 92.7 ms                                                               | 92.2 ms: 1.01x faster                                                           |
| regex_compile            | 134 ms                                                                | 133 ms: 1.00x faster                                                            |
| sqlglot_optimize         | 55.8 ms                                                               | 55.7 ms: 1.00x faster                                                           |
| python_startup_no_site   | 7.18 ms                                                               | 7.16 ms: 1.00x faster                                                           |
| bpe_tokeniser            | 4.51 sec                                                              | 4.49 sec: 1.00x faster                                                          |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| regex_dna                | 221 ms                                                                | 221 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                          |
| bench_thread_pool        | 817 us                                                                | 819 us: 1.00x slower                                                            |
| pickle_pure_python       | 293 us                                                                | 294 us: 1.00x slower                                                            |
| sympy_expand             | 505 ms                                                                | 507 ms: 1.00x slower                                                            |
| xml_etree_iterparse      | 99.1 ms                                                               | 99.5 ms: 1.00x slower                                                           |
| hexiom                   | 6.67 ms                                                               | 6.70 ms: 1.00x slower                                                           |
| logging_silent           | 104 ns                                                                | 105 ns: 1.01x slower                                                            |
| gc_traversal             | 3.65 ms                                                               | 3.67 ms: 1.01x slower                                                           |
| fannkuch                 | 368 ms                                                                | 370 ms: 1.01x slower                                                            |
| tomli_loads              | 1.91 sec                                                              | 1.93 sec: 1.01x slower                                                          |
| genshi_xml               | 53.4 ms                                                               | 53.9 ms: 1.01x slower                                                           |
| html5lib                 | 65.1 ms                                                               | 65.7 ms: 1.01x slower                                                           |
| richards                 | 40.8 ms                                                               | 41.2 ms: 1.01x slower                                                           |
| chaos                    | 57.2 ms                                                               | 57.8 ms: 1.01x slower                                                           |
| richards_super           | 46.6 ms                                                               | 47.1 ms: 1.01x slower                                                           |
| comprehensions           | 16.2 us                                                               | 16.4 us: 1.01x slower                                                           |
| sqlglot_normalize        | 111 ms                                                                | 113 ms: 1.01x slower                                                            |
| asyncio_tcp              | 491 ms                                                                | 505 ms: 1.03x slower                                                            |
| json_dumps               | 10.1 ms                                                               | 10.4 ms: 1.03x slower                                                           |
| spectral_norm            | 100 ms                                                                | 104 ms: 1.03x slower                                                            |
| thrift                   | 785 us                                                                | 811 us: 1.03x slower                                                            |
| pyflate                  | 433 ms                                                                | 449 ms: 1.04x slower                                                            |
| genshi_text              | 23.7 ms                                                               | 24.7 ms: 1.04x slower                                                           |
| mdp                      | 2.56 sec                                                              | 2.71 sec: 1.06x slower                                                          |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (43): async_tree_memoization, async_tree_none, pylint, async_tree_memoization_tg, xml_etree_generate, coroutines, coverage, sqlglot_transpile, pprint_pformat, deltablue, 2to3, dask, async_tree_none_tg, asyncio_websockets, pidigits, sympy_sum, bench_mp_pool, json_loads, raytrace, sympy_integrate, float, json, docutils, django_template, xml_etree_process, pycparser, sympy_str, async_tree_cpu_io_mixed, meteor_contest, generators, async_tree_cpu_io_mixed_tg, pathlib, pprint_safe_repr, mako, telco, scimark_monte_carlo, nqueens, scimark_fft, unpickle_pure_python, async_tree_io_tg, async_tree_io, xml_etree_parse, deepcopy

# HPT report

- Reliability score: 93.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x