# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 69.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 282 ms: 1.00x faster                                                        |
| docutils       | 2.92 sec                                                                    | 2.91 sec: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators          | 363 ms                                                                      | 355 ms: 1.02x faster                                                        |
| async_tree_memoization_tg | 391 ms                                                                      | 385 ms: 1.01x faster                                                        |
| async_tree_memoization    | 399 ms                                                                      | 395 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| coroutines                | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, asyncio_tcp, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                      | 255 ms: 1.00x slower                                                        |
| float          | 79.4 ms                                                                     | 80.1 ms: 1.01x slower                                                       |
| nbody          | 85.3 ms                                                                     | 86.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                      | 238 ms: 1.07x faster                                                        |
| regex_effbot   | 3.58 ms                                                                     | 3.46 ms: 1.03x faster                                                       |
| regex_v8       | 27.4 ms                                                                     | 26.9 ms: 1.02x faster                                                       |
| regex_compile  | 140 ms                                                                      | 141 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 314 us                                                                      | 312 us: 1.01x faster                                                        |
| json_dumps           | 10.9 ms                                                                     | 10.9 ms: 1.00x faster                                                       |
| xml_etree_generate   | 84.8 ms                                                                     | 85.1 ms: 1.00x slower                                                       |
| xml_etree_process    | 59.2 ms                                                                     | 59.7 ms: 1.01x slower                                                       |
| tomli_loads          | 2.53 sec                                                                    | 2.55 sec: 1.01x slower                                                      |
| unpickle_pure_python | 210 us                                                                      | 214 us: 1.02x slower                                                        |
| json_loads           | 24.7 us                                                                     | 25.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.06 ms                                                                     | 9.09 ms: 1.00x slower                                                       |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 40.0 ms                                                                     | 39.6 ms: 1.01x faster                                                       |
| genshi_xml      | 54.8 ms                                                                     | 55.5 ms: 1.01x slower                                                       |
| mako            | 10.3 ms                                                                     | 10.5 ms: 1.02x slower                                                       |
| genshi_text     | 24.7 ms                                                                     | 26.0 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna                 | 254 ms                                                                      | 238 ms: 1.07x faster                                                        |
| logging_format            | 6.99 us                                                                     | 6.68 us: 1.05x faster                                                       |
| regex_effbot              | 3.58 ms                                                                     | 3.46 ms: 1.03x faster                                                       |
| logging_simple            | 6.43 us                                                                     | 6.23 us: 1.03x faster                                                       |
| gc_traversal              | 4.58 ms                                                                     | 4.44 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult   | 4.22 ms                                                                     | 4.11 ms: 1.03x faster                                                       |
| async_generators          | 363 ms                                                                      | 355 ms: 1.02x faster                                                        |
| comprehensions            | 17.7 us                                                                     | 17.3 us: 1.02x faster                                                       |
| regex_v8                  | 27.4 ms                                                                     | 26.9 ms: 1.02x faster                                                       |
| typing_runtime_protocols  | 175 us                                                                      | 172 us: 1.02x faster                                                        |
| spectral_norm             | 96.9 ms                                                                     | 95.4 ms: 1.02x faster                                                       |
| async_tree_memoization_tg | 391 ms                                                                      | 385 ms: 1.01x faster                                                        |
| scimark_fft               | 307 ms                                                                      | 303 ms: 1.01x faster                                                        |
| bpe_tokeniser             | 4.93 sec                                                                    | 4.88 sec: 1.01x faster                                                      |
| django_template           | 40.0 ms                                                                     | 39.6 ms: 1.01x faster                                                       |
| pprint_safe_repr          | 799 ms                                                                      | 792 ms: 1.01x faster                                                        |
| async_tree_memoization    | 399 ms                                                                      | 395 ms: 1.01x faster                                                        |
| richards_super            | 56.8 ms                                                                     | 56.3 ms: 1.01x faster                                                       |
| sqlglot_parse             | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                       |
| pycparser                 | 1.21 sec                                                                    | 1.20 sec: 1.01x faster                                                      |
| pickle_pure_python        | 314 us                                                                      | 312 us: 1.01x faster                                                        |
| docutils                  | 2.92 sec                                                                    | 2.91 sec: 1.00x faster                                                      |
| json_dumps                | 10.9 ms                                                                     | 10.9 ms: 1.00x faster                                                       |
| scimark_lu                | 95.8 ms                                                                     | 95.4 ms: 1.00x faster                                                       |
| sympy_integrate           | 23.0 ms                                                                     | 22.9 ms: 1.00x faster                                                       |
| sqlglot_optimize          | 58.5 ms                                                                     | 58.3 ms: 1.00x faster                                                       |
| sqlglot_transpile         | 1.79 ms                                                                     | 1.78 ms: 1.00x faster                                                       |
| 2to3                      | 282 ms                                                                      | 282 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| pidigits                  | 254 ms                                                                      | 255 ms: 1.00x slower                                                        |
| python_startup_no_site    | 9.06 ms                                                                     | 9.09 ms: 1.00x slower                                                       |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| richards                  | 50.0 ms                                                                     | 50.2 ms: 1.00x slower                                                       |
| xml_etree_generate        | 84.8 ms                                                                     | 85.1 ms: 1.00x slower                                                       |
| meteor_contest            | 127 ms                                                                      | 127 ms: 1.00x slower                                                        |
| regex_compile             | 140 ms                                                                      | 141 ms: 1.01x slower                                                        |
| sympy_expand              | 496 ms                                                                      | 499 ms: 1.01x slower                                                        |
| mdp                       | 2.48 sec                                                                    | 2.49 sec: 1.01x slower                                                      |
| pathlib                   | 15.7 ms                                                                     | 15.8 ms: 1.01x slower                                                       |
| xml_etree_process         | 59.2 ms                                                                     | 59.7 ms: 1.01x slower                                                       |
| scimark_sor               | 118 ms                                                                      | 119 ms: 1.01x slower                                                        |
| tomli_loads               | 2.53 sec                                                                    | 2.55 sec: 1.01x slower                                                      |
| coroutines                | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                       |
| float                     | 79.4 ms                                                                     | 80.1 ms: 1.01x slower                                                       |
| genshi_xml                | 54.8 ms                                                                     | 55.5 ms: 1.01x slower                                                       |
| nqueens                   | 89.2 ms                                                                     | 90.4 ms: 1.01x slower                                                       |
| chaos                     | 61.0 ms                                                                     | 61.8 ms: 1.01x slower                                                       |
| nbody                     | 85.3 ms                                                                     | 86.4 ms: 1.01x slower                                                       |
| go                        | 133 ms                                                                      | 135 ms: 1.01x slower                                                        |
| hexiom                    | 6.17 ms                                                                     | 6.26 ms: 1.02x slower                                                       |
| crypto_pyaes              | 72.2 ms                                                                     | 73.4 ms: 1.02x slower                                                       |
| deepcopy_memo             | 28.5 us                                                                     | 29.0 us: 1.02x slower                                                       |
| unpickle_pure_python      | 210 us                                                                      | 214 us: 1.02x slower                                                        |
| json_loads                | 24.7 us                                                                     | 25.2 us: 1.02x slower                                                       |
| mako                      | 10.3 ms                                                                     | 10.5 ms: 1.02x slower                                                       |
| fannkuch                  | 354 ms                                                                      | 362 ms: 1.02x slower                                                        |
| logging_silent            | 97.7 ns                                                                     | 100 ns: 1.03x slower                                                        |
| thrift                    | 848 us                                                                      | 874 us: 1.03x slower                                                        |
| create_gc_cycles          | 1.93 ms                                                                     | 2.00 ms: 1.03x slower                                                       |
| genshi_text               | 24.7 ms                                                                     | 26.0 ms: 1.05x slower                                                       |
| pyflate                   | 470 ms                                                                      | 497 ms: 1.06x slower                                                        |
| coverage                  | 76.2 ms                                                                     | 85.2 ms: 1.12x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (27): bench_mp_pool, async_tree_none_tg, async_tree_cpu_io_mixed_tg, bench_thread_pool, html5lib, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, json, telco, scimark_monte_carlo, deltablue, asyncio_tcp, pprint_pformat, sympy_sum, sqlglot_normalize, asyncio_websockets, sympy_str, generators, deepcopy_reduce, deepcopy, pylint, tornado_http, raytrace, xml_etree_iterparse, xml_etree_parse, async_tree_io

# HPT report

- Reliability score: 69.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x