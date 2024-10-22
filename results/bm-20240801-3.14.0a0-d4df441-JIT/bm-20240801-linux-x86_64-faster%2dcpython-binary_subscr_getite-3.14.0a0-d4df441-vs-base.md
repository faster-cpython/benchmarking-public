# Results vs. base

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: d4df441
- commit date: 2024-08-01
- overall geometric mean: 1.00x faster
- HPT reliability: 69.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 273 ms: 1.00x faster                                                            |
| html5lib       | 65.1 ms                                                               | 63.8 ms: 1.02x faster                                                           |
| tornado_http   | 92.7 ms                                                               | 92.3 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                                          |
| coroutines                 | 22.6 ms                                                               | 22.8 ms: 1.01x slower                                                           |
| async_generators           | 457 ms                                                                | 463 ms: 1.01x slower                                                            |
| asyncio_tcp                | 491 ms                                                                | 499 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 525 ms                                                                | 537 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none, async_tree_memoization_tg, asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.5 ms                                                               | 79.6 ms: 1.02x faster                                                           |
| float          | 70.7 ms                                                               | 69.8 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.6 ms                                                               | 25.2 ms: 1.01x faster                                                           |
| regex_compile  | 134 ms                                                                | 133 ms: 1.01x faster                                                            |
| regex_dna      | 221 ms                                                                | 230 ms: 1.04x slower                                                            |
| regex_effbot   | 3.74 ms                                                               | 3.89 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 56.5 ms                                                               | 55.5 ms: 1.02x faster                                                           |
| xml_etree_generate   | 80.1 ms                                                               | 79.3 ms: 1.01x faster                                                           |
| unpickle_pure_python | 214 us                                                                | 213 us: 1.01x faster                                                            |
| json_loads           | 28.1 us                                                               | 28.0 us: 1.01x faster                                                           |
| json_dumps           | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                           |
| pickle_pure_python   | 293 us                                                                | 300 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.18 ms                                                               | 7.17 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 53.4 ms                                                               | 52.7 ms: 1.01x faster                                                           |
| genshi_text    | 23.7 ms                                                               | 24.1 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_sor                | 131 ms                                                                | 114 ms: 1.15x faster                                                            |
| scimark_lu                 | 124 ms                                                                | 109 ms: 1.14x faster                                                            |
| logging_silent             | 104 ns                                                                | 101 ns: 1.03x faster                                                            |
| logging_simple             | 5.60 us                                                               | 5.46 us: 1.02x faster                                                           |
| nbody                      | 81.5 ms                                                               | 79.6 ms: 1.02x faster                                                           |
| deltablue                  | 3.57 ms                                                               | 3.49 ms: 1.02x faster                                                           |
| typing_runtime_protocols   | 176 us                                                                | 172 us: 1.02x faster                                                            |
| html5lib                   | 65.1 ms                                                               | 63.8 ms: 1.02x faster                                                           |
| richards                   | 40.8 ms                                                               | 39.9 ms: 1.02x faster                                                           |
| raytrace                   | 267 ms                                                                | 262 ms: 1.02x faster                                                            |
| deepcopy_reduce            | 2.79 us                                                               | 2.73 us: 1.02x faster                                                           |
| deepcopy                   | 276 us                                                                | 271 us: 1.02x faster                                                            |
| xml_etree_process          | 56.5 ms                                                               | 55.5 ms: 1.02x faster                                                           |
| regex_v8                   | 25.6 ms                                                               | 25.2 ms: 1.01x faster                                                           |
| genshi_xml                 | 53.4 ms                                                               | 52.7 ms: 1.01x faster                                                           |
| float                      | 70.7 ms                                                               | 69.8 ms: 1.01x faster                                                           |
| deepcopy_memo              | 28.9 us                                                               | 28.5 us: 1.01x faster                                                           |
| xml_etree_generate         | 80.1 ms                                                               | 79.3 ms: 1.01x faster                                                           |
| logging_format             | 6.12 us                                                               | 6.06 us: 1.01x faster                                                           |
| nqueens                    | 85.4 ms                                                               | 84.6 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 55.8 ms                                                               | 55.4 ms: 1.01x faster                                                           |
| go                         | 147 ms                                                                | 146 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                           |
| regex_compile              | 134 ms                                                                | 133 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 214 us                                                                | 213 us: 1.01x faster                                                            |
| create_gc_cycles           | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                           |
| json_loads                 | 28.1 us                                                               | 28.0 us: 1.01x faster                                                           |
| sympy_expand               | 505 ms                                                                | 503 ms: 1.01x faster                                                            |
| tornado_http               | 92.7 ms                                                               | 92.3 ms: 1.00x faster                                                           |
| sympy_integrate            | 22.5 ms                                                               | 22.4 ms: 1.00x faster                                                           |
| 2to3                       | 273 ms                                                                | 273 ms: 1.00x faster                                                            |
| python_startup             | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site     | 7.18 ms                                                               | 7.17 ms: 1.00x faster                                                           |
| hexiom                     | 6.67 ms                                                               | 6.70 ms: 1.00x slower                                                           |
| thrift                     | 785 us                                                                | 788 us: 1.00x slower                                                            |
| comprehensions             | 16.2 us                                                               | 16.3 us: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                                          |
| gc_traversal               | 3.65 ms                                                               | 3.68 ms: 1.01x slower                                                           |
| pathlib                    | 16.0 ms                                                               | 16.2 ms: 1.01x slower                                                           |
| coroutines                 | 22.6 ms                                                               | 22.8 ms: 1.01x slower                                                           |
| sqlglot_normalize          | 111 ms                                                                | 112 ms: 1.01x slower                                                            |
| json_dumps                 | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 4.32 ms                                                               | 4.38 ms: 1.01x slower                                                           |
| async_generators           | 457 ms                                                                | 463 ms: 1.01x slower                                                            |
| scimark_fft                | 301 ms                                                                | 306 ms: 1.02x slower                                                            |
| asyncio_tcp                | 491 ms                                                                | 499 ms: 1.02x slower                                                            |
| genshi_text                | 23.7 ms                                                               | 24.1 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 525 ms                                                                | 537 ms: 1.02x slower                                                            |
| pickle_pure_python         | 293 us                                                                | 300 us: 1.02x slower                                                            |
| meteor_contest             | 104 ms                                                                | 107 ms: 1.02x slower                                                            |
| spectral_norm              | 100 ms                                                                | 103 ms: 1.02x slower                                                            |
| regex_dna                  | 221 ms                                                                | 230 ms: 1.04x slower                                                            |
| json                       | 5.12 ms                                                               | 5.31 ms: 1.04x slower                                                           |
| regex_effbot               | 3.74 ms                                                               | 3.89 ms: 1.04x slower                                                           |
| mdp                        | 2.56 sec                                                              | 2.70 sec: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (35): pprint_safe_repr, pylint, async_tree_memoization, async_tree_none, dask, coverage, pycparser, tomli_loads, bench_thread_pool, async_tree_memoization_tg, docutils, xml_etree_parse, sqlglot_parse, pidigits, asyncio_websockets, pprint_pformat, bpe_tokeniser, sqlglot_transpile, sympy_str, generators, sympy_sum, bench_mp_pool, xml_etree_iterparse, django_template, async_tree_io, chaos, mako, telco, pyflate, async_tree_none_tg, crypto_pyaes, richards_super, async_tree_io_tg, fannkuch, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 69.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x