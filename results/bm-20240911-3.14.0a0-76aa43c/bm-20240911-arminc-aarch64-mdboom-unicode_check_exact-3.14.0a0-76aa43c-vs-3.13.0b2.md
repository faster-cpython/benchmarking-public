# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-aarch64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.00 sec: 1.03x faster                                                 |
| html5lib       | 66.1 ms                                                      | 64.1 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                           |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 555 ms: 1.16x faster                                                   |
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                 |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 722 ms: 1.06x faster                                                   |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.05x faster                                                   |
| float          | 91.4 ms                                                      | 92.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                   |
| regex_compile  | 128 ms                                                       | 124 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate | 114 ms                                                       | 111 ms: 1.02x faster                                                   |
| unpickle_list      | 6.52 us                                                      | 6.39 us: 1.02x faster                                                  |
| unpickle           | 19.8 us                                                      | 19.4 us: 1.02x faster                                                  |
| xml_etree_process  | 80.8 ms                                                      | 79.4 ms: 1.02x faster                                                  |
| json_loads         | 32.1 us                                                      | 31.6 us: 1.01x faster                                                  |
| pickle_dict        | 37.6 us                                                      | 37.9 us: 1.01x slower                                                  |
| tomli_loads        | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                 |
| pickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                                  |
| json_dumps         | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                  |
| Geometric mean     | (ref)                                                        | 1.00x faster                                                           |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_list, unpickle_pure_python, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 59.4 ms: 1.02x faster                                                  |
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 328 us: 1.37x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 37.3 us: 1.36x faster                                                  |
| go                         | 161 ms                                                       | 136 ms: 1.18x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 555 ms: 1.16x faster                                                   |
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.49 us: 1.16x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                 |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                 |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 722 ms: 1.06x faster                                                   |
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.4 ms: 1.05x faster                                                  |
| nbody                      | 114 ms                                                       | 109 ms: 1.05x faster                                                   |
| thrift                     | 962 us                                                       | 921 us: 1.04x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.04x faster                                                   |
| logging_simple             | 7.21 us                                                      | 6.92 us: 1.04x faster                                                  |
| pprint_pformat             | 1.93 sec                                                     | 1.86 sec: 1.04x faster                                                 |
| sympy_sum                  | 144 ms                                                       | 139 ms: 1.03x faster                                                   |
| regex_compile              | 128 ms                                                       | 124 ms: 1.03x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.00 sec: 1.03x faster                                                 |
| pprint_safe_repr           | 933 ms                                                       | 904 ms: 1.03x faster                                                   |
| scimark_sor                | 159 ms                                                       | 155 ms: 1.03x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 64.1 ms: 1.03x faster                                                  |
| gc_traversal               | 5.17 ms                                                      | 5.02 ms: 1.03x faster                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 1.22 ms: 1.03x faster                                                  |
| create_gc_cycles           | 2.33 ms                                                      | 2.27 ms: 1.03x faster                                                  |
| logging_format             | 7.82 us                                                      | 7.62 us: 1.03x faster                                                  |
| asyncio_tcp                | 584 ms                                                       | 568 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.3 ms: 1.02x faster                                                  |
| async_generators           | 488 ms                                                       | 476 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.02x faster                                                  |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                   |
| nqueens                    | 98.9 ms                                                      | 97.0 ms: 1.02x faster                                                  |
| unpickle_list              | 6.52 us                                                      | 6.39 us: 1.02x faster                                                  |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                  |
| json                       | 5.64 ms                                                      | 5.54 ms: 1.02x faster                                                  |
| pycparser                  | 1.22 sec                                                     | 1.20 sec: 1.02x faster                                                 |
| xml_etree_process          | 80.8 ms                                                      | 79.4 ms: 1.02x faster                                                  |
| genshi_xml                 | 60.4 ms                                                      | 59.4 ms: 1.02x faster                                                  |
| sympy_str                  | 265 ms                                                       | 261 ms: 1.02x faster                                                   |
| typing_runtime_protocols   | 193 us                                                       | 191 us: 1.02x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.6 us: 1.01x faster                                                  |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.01x faster                                                   |
| scimark_fft                | 445 ms                                                       | 439 ms: 1.01x faster                                                   |
| mdp                        | 3.33 sec                                                     | 3.29 sec: 1.01x faster                                                 |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                   |
| float                      | 91.4 ms                                                      | 92.1 ms: 1.01x slower                                                  |
| pickle_dict                | 37.6 us                                                      | 37.9 us: 1.01x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                  |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                  |
| telco                      | 10.0 ms                                                      | 10.2 ms: 1.01x slower                                                  |
| fannkuch                   | 451 ms                                                       | 459 ms: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                 |
| raytrace                   | 297 ms                                                       | 302 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                           |

Benchmark hidden because not significant (35): xml_etree_parse, 2to3, sqlglot_normalize, sympy_integrate, tornado_http, dulwich_log, regex_effbot, sqlite_synth, coverage, pickle_list, unpickle_pure_python, sqlglot_parse, comprehensions, genshi_text, sqlglot_optimize, regex_v8, asyncio_tcp_ssl, pickle_pure_python, crypto_pyaes, pidigits, sympy_expand, asyncio_websockets, scimark_monte_carlo, bpe_tokeniser, python_startup, deltablue, python_startup_no_site, chaos, bench_mp_pool, spectral_norm, pyflate, hexiom, django_template, xml_etree_iterparse, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x