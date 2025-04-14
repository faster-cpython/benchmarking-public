# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-aarch64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 290 ms                                                                   | 311 ms: 1.07x slower                                                               |
| docutils       | 2.90 sec                                                                 | 3.06 sec: 1.06x slower                                                             |
| html5lib       | 60.4 ms                                                                  | 66.4 ms: 1.10x slower                                                              |
| sphinx         | 1.13 sec                                                                 | 1.19 sec: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                    | 1.07x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                                   | 678 ms: 1.03x slower                                                               |
| async_tree_memoization     | 463 ms                                                                   | 486 ms: 1.05x slower                                                               |
| async_tree_none            | 375 ms                                                                   | 394 ms: 1.05x slower                                                               |
| async_tree_io              | 878 ms                                                                   | 933 ms: 1.06x slower                                                               |
| async_tree_cpu_io_mixed    | 653 ms                                                                   | 695 ms: 1.07x slower                                                               |
| async_tree_memoization_tg  | 455 ms                                                                   | 486 ms: 1.07x slower                                                               |
| async_tree_cpu_io_mixed_tg | 633 ms                                                                   | 679 ms: 1.07x slower                                                               |
| async_tree_none_tg         | 363 ms                                                                   | 393 ms: 1.08x slower                                                               |
| async_generators           | 431 ms                                                                   | 467 ms: 1.08x slower                                                               |
| coroutines                 | 28.3 ms                                                                  | 30.9 ms: 1.09x slower                                                              |
| async_tree_io_tg           | 857 ms                                                                   | 941 ms: 1.10x slower                                                               |
| Geometric mean             | (ref)                                                                    | 1.07x slower                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 84.4 ms                                                                  | 91.7 ms: 1.09x slower                                                              |
| nbody          | 118 ms                                                                   | 128 ms: 1.09x slower                                                               |
| Geometric mean | (ref)                                                                    | 1.06x slower                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 30.9 ms                                                                  | 32.6 ms: 1.05x slower                                                              |
| regex_dna      | 245 ms                                                                   | 260 ms: 1.06x slower                                                               |
| regex_compile  | 120 ms                                                                   | 133 ms: 1.11x slower                                                               |
| Geometric mean | (ref)                                                                    | 1.06x slower                                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 141 ms                                                                   | 147 ms: 1.04x slower                                                               |
| json_dumps           | 13.9 ms                                                                  | 14.6 ms: 1.05x slower                                                              |
| pickle_pure_python   | 381 us                                                                   | 405 us: 1.06x slower                                                               |
| tomli_loads          | 2.42 sec                                                                 | 2.58 sec: 1.07x slower                                                             |
| xml_etree_process    | 77.5 ms                                                                  | 83.9 ms: 1.08x slower                                                              |
| xml_etree_generate   | 108 ms                                                                   | 118 ms: 1.09x slower                                                               |
| unpickle_pure_python | 252 us                                                                   | 284 us: 1.13x slower                                                               |
| Geometric mean       | (ref)                                                                    | 1.06x slower                                                                       |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                                  | 9.10 ms: 1.03x slower                                                              |
| python_startup         | 15.9 ms                                                                  | 16.5 ms: 1.04x slower                                                              |
| Geometric mean         | (ref)                                                                    | 1.04x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml     | 59.1 ms                                                                  | 63.4 ms: 1.07x slower                                                              |
| genshi_text    | 26.4 ms                                                                  | 28.6 ms: 1.08x slower                                                              |
| mako           | 13.6 ms                                                                  | 14.9 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                                    | 1.07x slower                                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| sympy_sum                  | 139 ms                                                                   | 144 ms: 1.03x slower                                                               |
| asyncio_websockets         | 656 ms                                                                   | 678 ms: 1.03x slower                                                               |
| python_startup_no_site     | 8.79 ms                                                                  | 9.10 ms: 1.03x slower                                                              |
| python_startup             | 15.9 ms                                                                  | 16.5 ms: 1.04x slower                                                              |
| telco                      | 9.40 ms                                                                  | 9.79 ms: 1.04x slower                                                              |
| mdp                        | 3.29 sec                                                                 | 3.43 sec: 1.04x slower                                                             |
| xml_etree_iterparse        | 141 ms                                                                   | 147 ms: 1.04x slower                                                               |
| sqlglot_optimize           | 60.2 ms                                                                  | 63.2 ms: 1.05x slower                                                              |
| async_tree_memoization     | 463 ms                                                                   | 486 ms: 1.05x slower                                                               |
| k_core                     | 2.79 sec                                                                 | 2.93 sec: 1.05x slower                                                             |
| async_tree_none            | 375 ms                                                                   | 394 ms: 1.05x slower                                                               |
| sympy_expand               | 451 ms                                                                   | 474 ms: 1.05x slower                                                               |
| deepcopy                   | 330 us                                                                   | 347 us: 1.05x slower                                                               |
| json_dumps                 | 13.9 ms                                                                  | 14.6 ms: 1.05x slower                                                              |
| regex_v8                   | 30.9 ms                                                                  | 32.6 ms: 1.05x slower                                                              |
| docutils                   | 2.90 sec                                                                 | 3.06 sec: 1.06x slower                                                             |
| sphinx                     | 1.13 sec                                                                 | 1.19 sec: 1.06x slower                                                             |
| bench_thread_pool          | 1.31 ms                                                                  | 1.38 ms: 1.06x slower                                                              |
| regex_dna                  | 245 ms                                                                   | 260 ms: 1.06x slower                                                               |
| scimark_fft                | 410 ms                                                                   | 435 ms: 1.06x slower                                                               |
| async_tree_io              | 878 ms                                                                   | 933 ms: 1.06x slower                                                               |
| shortest_path              | 564 ms                                                                   | 600 ms: 1.06x slower                                                               |
| pickle_pure_python         | 381 us                                                                   | 405 us: 1.06x slower                                                               |
| sympy_integrate            | 20.9 ms                                                                  | 22.3 ms: 1.06x slower                                                              |
| generators                 | 35.1 ms                                                                  | 37.4 ms: 1.06x slower                                                              |
| async_tree_cpu_io_mixed    | 653 ms                                                                   | 695 ms: 1.07x slower                                                               |
| pylint                     | 306 ms                                                                   | 326 ms: 1.07x slower                                                               |
| logging_silent             | 130 ns                                                                   | 138 ns: 1.07x slower                                                               |
| tomli_loads                | 2.42 sec                                                                 | 2.58 sec: 1.07x slower                                                             |
| connected_components       | 540 ms                                                                   | 577 ms: 1.07x slower                                                               |
| async_tree_memoization_tg  | 455 ms                                                                   | 486 ms: 1.07x slower                                                               |
| typing_runtime_protocols   | 190 us                                                                   | 203 us: 1.07x slower                                                               |
| sqlglot_transpile          | 1.73 ms                                                                  | 1.85 ms: 1.07x slower                                                              |
| pathlib                    | 21.6 ms                                                                  | 23.2 ms: 1.07x slower                                                              |
| raytrace                   | 307 ms                                                                   | 329 ms: 1.07x slower                                                               |
| 2to3                       | 290 ms                                                                   | 311 ms: 1.07x slower                                                               |
| genshi_xml                 | 59.1 ms                                                                  | 63.4 ms: 1.07x slower                                                              |
| async_tree_cpu_io_mixed_tg | 633 ms                                                                   | 679 ms: 1.07x slower                                                               |
| thrift                     | 926 us                                                                   | 995 us: 1.07x slower                                                               |
| logging_format             | 7.47 us                                                                  | 8.03 us: 1.07x slower                                                              |
| genshi_text                | 26.4 ms                                                                  | 28.6 ms: 1.08x slower                                                              |
| xml_etree_process          | 77.5 ms                                                                  | 83.9 ms: 1.08x slower                                                              |
| bpe_tokeniser              | 5.38 sec                                                                 | 5.82 sec: 1.08x slower                                                             |
| async_tree_none_tg         | 363 ms                                                                   | 393 ms: 1.08x slower                                                               |
| deepcopy_memo              | 37.3 us                                                                  | 40.4 us: 1.08x slower                                                              |
| async_generators           | 431 ms                                                                   | 467 ms: 1.08x slower                                                               |
| meteor_contest             | 112 ms                                                                   | 121 ms: 1.09x slower                                                               |
| spectral_norm              | 115 ms                                                                   | 125 ms: 1.09x slower                                                               |
| nqueens                    | 98.2 ms                                                                  | 107 ms: 1.09x slower                                                               |
| float                      | 84.4 ms                                                                  | 91.7 ms: 1.09x slower                                                              |
| nbody                      | 118 ms                                                                   | 128 ms: 1.09x slower                                                               |
| sqlite_synth               | 3.83 us                                                                  | 4.16 us: 1.09x slower                                                              |
| sqlalchemy_declarative     | 139 ms                                                                   | 152 ms: 1.09x slower                                                               |
| xml_etree_generate         | 108 ms                                                                   | 118 ms: 1.09x slower                                                               |
| scimark_sparse_mat_mult    | 6.13 ms                                                                  | 6.69 ms: 1.09x slower                                                              |
| sympy_str                  | 255 ms                                                                   | 278 ms: 1.09x slower                                                               |
| richards                   | 50.2 ms                                                                  | 54.8 ms: 1.09x slower                                                              |
| coroutines                 | 28.3 ms                                                                  | 30.9 ms: 1.09x slower                                                              |
| mako                       | 13.6 ms                                                                  | 14.9 ms: 1.09x slower                                                              |
| pyflate                    | 554 ms                                                                   | 607 ms: 1.10x slower                                                               |
| pycparser                  | 1.22 sec                                                                 | 1.33 sec: 1.10x slower                                                             |
| async_tree_io_tg           | 857 ms                                                                   | 941 ms: 1.10x slower                                                               |
| comprehensions             | 20.4 us                                                                  | 22.4 us: 1.10x slower                                                              |
| crypto_pyaes               | 85.1 ms                                                                  | 93.4 ms: 1.10x slower                                                              |
| gc_traversal               | 6.49 ms                                                                  | 7.13 ms: 1.10x slower                                                              |
| pprint_pformat             | 1.87 sec                                                                 | 2.05 sec: 1.10x slower                                                             |
| html5lib                   | 60.4 ms                                                                  | 66.4 ms: 1.10x slower                                                              |
| dulwich_log                | 57.4 ms                                                                  | 63.1 ms: 1.10x slower                                                              |
| many_optionals             | 813 us                                                                   | 895 us: 1.10x slower                                                               |
| go                         | 134 ms                                                                   | 147 ms: 1.10x slower                                                               |
| scimark_monte_carlo        | 79.6 ms                                                                  | 88.0 ms: 1.10x slower                                                              |
| richards_super             | 57.1 ms                                                                  | 63.1 ms: 1.11x slower                                                              |
| scimark_sor                | 147 ms                                                                   | 162 ms: 1.11x slower                                                               |
| hexiom                     | 6.93 ms                                                                  | 7.68 ms: 1.11x slower                                                              |
| regex_compile              | 120 ms                                                                   | 133 ms: 1.11x slower                                                               |
| fannkuch                   | 476 ms                                                                   | 528 ms: 1.11x slower                                                               |
| sqlalchemy_imperative      | 14.9 ms                                                                  | 16.6 ms: 1.11x slower                                                              |
| deltablue                  | 3.78 ms                                                                  | 4.21 ms: 1.11x slower                                                              |
| subparsers                 | 25.0 ms                                                                  | 27.8 ms: 1.11x slower                                                              |
| pprint_safe_repr           | 895 ms                                                                   | 1.00 sec: 1.12x slower                                                             |
| sqlglot_parse              | 1.36 ms                                                                  | 1.52 ms: 1.12x slower                                                              |
| chaos                      | 65.6 ms                                                                  | 73.7 ms: 1.12x slower                                                              |
| unpickle_pure_python       | 252 us                                                                   | 284 us: 1.13x slower                                                               |
| logging_simple             | 6.77 us                                                                  | 7.64 us: 1.13x slower                                                              |
| scimark_lu                 | 137 ms                                                                   | 157 ms: 1.15x slower                                                               |
| Geometric mean             | (ref)                                                                    | 1.07x slower                                                                       |

Benchmark hidden because not significant (11): json_loads, pidigits, regex_effbot, coverage, create_gc_cycles, django_template, json, xml_etree_parse, bench_mp_pool, deepcopy_reduce, sqlglot_normalize

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.00x