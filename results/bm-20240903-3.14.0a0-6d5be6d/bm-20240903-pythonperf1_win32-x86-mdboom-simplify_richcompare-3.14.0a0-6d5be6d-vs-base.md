# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                                       | 1.86 sec: 1.02x faster                                                         |
| html5lib       | 46.5 ms                                                                        | 46.1 ms: 1.01x faster                                                          |
| tornado_http   | 106 ms                                                                         | 104 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 556 ms                                                                         | 531 ms: 1.05x faster                                                           |
| async_tree_none            | 226 ms                                                                         | 216 ms: 1.05x faster                                                           |
| async_tree_io_tg           | 531 ms                                                                         | 509 ms: 1.04x faster                                                           |
| async_tree_memoization     | 284 ms                                                                         | 272 ms: 1.04x faster                                                           |
| async_tree_memoization_tg  | 257 ms                                                                         | 247 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 204 ms                                                                         | 198 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 479 ms                                                                         | 465 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                         | 463 ms: 1.02x faster                                                           |
| async_generators           | 294 ms                                                                         | 297 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.03x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_tcp_ssl, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 97.8 ms                                                                        | 96.0 ms: 1.02x faster                                                          |
| float          | 62.1 ms                                                                        | 61.5 ms: 1.01x faster                                                          |
| pidigits       | 198 ms                                                                         | 202 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 110 ms                                                                         | 107 ms: 1.02x faster                                                           |
| regex_v8       | 16.2 ms                                                                        | 16.4 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python  | 258 us                                                                         | 251 us: 1.03x faster                                                           |
| tomli_loads         | 1.91 sec                                                                       | 1.86 sec: 1.03x faster                                                         |
| xml_etree_process   | 51.2 ms                                                                        | 50.0 ms: 1.02x faster                                                          |
| json_dumps          | 7.52 ms                                                                        | 7.46 ms: 1.01x faster                                                          |
| xml_etree_generate  | 67.8 ms                                                                        | 67.3 ms: 1.01x faster                                                          |
| xml_etree_iterparse | 68.1 ms                                                                        | 67.7 ms: 1.01x faster                                                          |
| json_loads          | 20.7 us                                                                        | 21.1 us: 1.02x slower                                                          |
| Geometric mean      | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.1 ms                                                                        | 23.8 ms: 1.01x faster                                                          |
| python_startup_no_site | 19.9 ms                                                                        | 19.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                                          | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 8.45 ms                                                                        | 8.20 ms: 1.03x faster                                                          |
| genshi_text     | 22.3 ms                                                                        | 21.9 ms: 1.02x faster                                                          |
| django_template | 33.2 ms                                                                        | 32.9 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                                         | 149 us: 1.06x faster                                                           |
| raytrace                   | 245 ms                                                                         | 231 ms: 1.06x faster                                                           |
| async_tree_io              | 556 ms                                                                         | 531 ms: 1.05x faster                                                           |
| async_tree_none            | 226 ms                                                                         | 216 ms: 1.05x faster                                                           |
| deepcopy                   | 249 us                                                                         | 238 us: 1.05x faster                                                           |
| async_tree_io_tg           | 531 ms                                                                         | 509 ms: 1.04x faster                                                           |
| async_tree_memoization     | 284 ms                                                                         | 272 ms: 1.04x faster                                                           |
| sqlglot_parse              | 1.12 ms                                                                        | 1.07 ms: 1.04x faster                                                          |
| async_tree_memoization_tg  | 257 ms                                                                         | 247 ms: 1.04x faster                                                           |
| dulwich_log                | 50.9 ms                                                                        | 49.2 ms: 1.03x faster                                                          |
| async_tree_none_tg         | 204 ms                                                                         | 198 ms: 1.03x faster                                                           |
| logging_format             | 8.94 us                                                                        | 8.65 us: 1.03x faster                                                          |
| telco                      | 6.99 ms                                                                        | 6.77 ms: 1.03x faster                                                          |
| comprehensions             | 14.0 us                                                                        | 13.6 us: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 479 ms                                                                         | 465 ms: 1.03x faster                                                           |
| sqlglot_transpile          | 1.38 ms                                                                        | 1.33 ms: 1.03x faster                                                          |
| pickle_pure_python         | 258 us                                                                         | 251 us: 1.03x faster                                                           |
| mako                       | 8.45 ms                                                                        | 8.20 ms: 1.03x faster                                                          |
| sqlglot_optimize           | 44.2 ms                                                                        | 42.9 ms: 1.03x faster                                                          |
| sqlglot_normalize          | 230 ms                                                                         | 223 ms: 1.03x faster                                                           |
| tomli_loads                | 1.91 sec                                                                       | 1.86 sec: 1.03x faster                                                         |
| logging_simple             | 8.15 us                                                                        | 7.92 us: 1.03x faster                                                          |
| scimark_sparse_mat_mult    | 3.23 ms                                                                        | 3.15 ms: 1.03x faster                                                          |
| chaos                      | 55.5 ms                                                                        | 54.1 ms: 1.03x faster                                                          |
| xml_etree_process          | 51.2 ms                                                                        | 50.0 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 658 ms                                                                         | 643 ms: 1.02x faster                                                           |
| regex_compile              | 110 ms                                                                         | 107 ms: 1.02x faster                                                           |
| sympy_sum                  | 109 ms                                                                         | 107 ms: 1.02x faster                                                           |
| pprint_pformat             | 1.35 sec                                                                       | 1.32 sec: 1.02x faster                                                         |
| coverage                   | 52.8 ms                                                                        | 51.8 ms: 1.02x faster                                                          |
| json                       | 4.36 ms                                                                        | 4.28 ms: 1.02x faster                                                          |
| genshi_text                | 22.3 ms                                                                        | 21.9 ms: 1.02x faster                                                          |
| docutils                   | 1.89 sec                                                                       | 1.86 sec: 1.02x faster                                                         |
| nbody                      | 97.8 ms                                                                        | 96.0 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                         | 463 ms: 1.02x faster                                                           |
| mdp                        | 1.73 sec                                                                       | 1.70 sec: 1.02x faster                                                         |
| tornado_http               | 106 ms                                                                         | 104 ms: 1.02x faster                                                           |
| thrift                     | 752 us                                                                         | 741 us: 1.02x faster                                                           |
| scimark_sor                | 104 ms                                                                         | 102 ms: 1.01x faster                                                           |
| sympy_integrate            | 15.7 ms                                                                        | 15.5 ms: 1.01x faster                                                          |
| sympy_str                  | 219 ms                                                                         | 216 ms: 1.01x faster                                                           |
| go                         | 105 ms                                                                         | 104 ms: 1.01x faster                                                           |
| python_startup             | 24.1 ms                                                                        | 23.8 ms: 1.01x faster                                                          |
| django_template            | 33.2 ms                                                                        | 32.9 ms: 1.01x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                                        | 19.7 ms: 1.01x faster                                                          |
| scimark_fft                | 239 ms                                                                         | 237 ms: 1.01x faster                                                           |
| float                      | 62.1 ms                                                                        | 61.5 ms: 1.01x faster                                                          |
| deepcopy_reduce            | 2.48 us                                                                        | 2.46 us: 1.01x faster                                                          |
| meteor_contest             | 82.7 ms                                                                        | 82.0 ms: 1.01x faster                                                          |
| json_dumps                 | 7.52 ms                                                                        | 7.46 ms: 1.01x faster                                                          |
| html5lib                   | 46.5 ms                                                                        | 46.1 ms: 1.01x faster                                                          |
| deepcopy_memo              | 22.2 us                                                                        | 22.0 us: 1.01x faster                                                          |
| xml_etree_generate         | 67.8 ms                                                                        | 67.3 ms: 1.01x faster                                                          |
| pyflate                    | 360 ms                                                                         | 358 ms: 1.01x faster                                                           |
| xml_etree_iterparse        | 68.1 ms                                                                        | 67.7 ms: 1.01x faster                                                          |
| sympy_expand               | 386 ms                                                                         | 384 ms: 1.00x faster                                                           |
| scimark_monte_carlo        | 56.0 ms                                                                        | 56.4 ms: 1.01x slower                                                          |
| scimark_lu                 | 69.6 ms                                                                        | 70.0 ms: 1.01x slower                                                          |
| create_gc_cycles           | 747 us                                                                         | 754 us: 1.01x slower                                                           |
| crypto_pyaes               | 58.9 ms                                                                        | 59.5 ms: 1.01x slower                                                          |
| regex_v8                   | 16.2 ms                                                                        | 16.4 ms: 1.01x slower                                                          |
| spectral_norm              | 76.2 ms                                                                        | 76.9 ms: 1.01x slower                                                          |
| async_generators           | 294 ms                                                                         | 297 ms: 1.01x slower                                                           |
| hexiom                     | 5.27 ms                                                                        | 5.36 ms: 1.02x slower                                                          |
| json_loads                 | 20.7 us                                                                        | 21.1 us: 1.02x slower                                                          |
| nqueens                    | 78.0 ms                                                                        | 79.3 ms: 1.02x slower                                                          |
| pycparser                  | 873 ms                                                                         | 888 ms: 1.02x slower                                                           |
| pidigits                   | 198 ms                                                                         | 202 ms: 1.02x slower                                                           |
| fannkuch                   | 334 ms                                                                         | 342 ms: 1.02x slower                                                           |
| richards_super             | 45.7 ms                                                                        | 46.9 ms: 1.03x slower                                                          |
| richards                   | 40.8 ms                                                                        | 41.9 ms: 1.03x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (17): asyncio_tcp, pylint, xml_etree_parse, bench_thread_pool, pathlib, regex_dna, 2to3, unpickle_pure_python, regex_effbot, asyncio_tcp_ssl, bench_mp_pool, coroutines, logging_silent, genshi_xml, gc_traversal, generators, deltablue

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown