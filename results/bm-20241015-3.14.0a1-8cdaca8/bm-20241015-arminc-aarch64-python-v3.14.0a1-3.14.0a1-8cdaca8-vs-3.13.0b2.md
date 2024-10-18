# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.06x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 293 ms: 1.04x faster                                         |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                       |
| html5lib       | 66.1 ms                                                      | 64.6 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                         |
| async_tree_none            | 492 ms                                                       | 438 ms: 1.12x faster                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                         |
| async_tree_none_tg         | 476 ms                                                       | 447 ms: 1.07x faster                                         |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 743 ms: 1.07x faster                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.21 sec: 1.05x faster                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 724 ms: 1.05x faster                                         |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.03x faster                                       |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 95.4 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 243 ms: 1.06x faster                                         |
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                         |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.1 us: 1.03x faster                                        |
| json_loads           | 32.1 us                                                      | 31.2 us: 1.03x faster                                        |
| pickle_list          | 5.27 us                                                      | 5.22 us: 1.01x faster                                        |
| unpickle_list        | 6.52 us                                                      | 6.60 us: 1.01x slower                                        |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                         |
| pickle_pure_python   | 359 us                                                       | 365 us: 1.02x slower                                         |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                         |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                       |
| pickle               | 13.4 us                                                      | 13.9 us: 1.04x slower                                        |
| json_dumps           | 13.1 ms                                                      | 14.1 ms: 1.08x slower                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, xml_etree_generate, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 14.5 ms: 1.12x slower                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 61.6 ms: 1.02x slower                                        |
| mako           | 13.2 ms                                                      | 13.7 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 333 us: 1.35x faster                                         |
| deepcopy_memo              | 50.8 us                                                      | 38.2 us: 1.33x faster                                        |
| go                         | 161 ms                                                       | 136 ms: 1.18x faster                                         |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                         |
| deepcopy_reduce            | 4.04 us                                                      | 3.56 us: 1.13x faster                                        |
| async_tree_none            | 492 ms                                                       | 438 ms: 1.12x faster                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                         |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                        |
| async_tree_none_tg         | 476 ms                                                       | 447 ms: 1.07x faster                                         |
| generators                 | 37.1 ms                                                      | 34.8 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 743 ms: 1.07x faster                                         |
| scimark_lu                 | 141 ms                                                       | 133 ms: 1.06x faster                                         |
| regex_dna                  | 259 ms                                                       | 243 ms: 1.06x faster                                         |
| logging_simple             | 7.21 us                                                      | 6.82 us: 1.06x faster                                        |
| asyncio_tcp                | 584 ms                                                       | 554 ms: 1.05x faster                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.21 sec: 1.05x faster                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 724 ms: 1.05x faster                                         |
| telco                      | 10.0 ms                                                      | 9.54 ms: 1.05x faster                                        |
| richards                   | 55.9 ms                                                      | 53.4 ms: 1.05x faster                                        |
| logging_format             | 7.82 us                                                      | 7.51 us: 1.04x faster                                        |
| 2to3                       | 305 ms                                                       | 293 ms: 1.04x faster                                         |
| sympy_sum                  | 144 ms                                                       | 138 ms: 1.04x faster                                         |
| richards_super             | 62.3 ms                                                      | 60.0 ms: 1.04x faster                                        |
| thrift                     | 962 us                                                       | 929 us: 1.04x faster                                         |
| json                       | 5.64 ms                                                      | 5.46 ms: 1.03x faster                                        |
| unpickle                   | 19.8 us                                                      | 19.1 us: 1.03x faster                                        |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.03x faster                                       |
| pprint_pformat             | 1.93 sec                                                     | 1.87 sec: 1.03x faster                                       |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                       |
| json_loads                 | 32.1 us                                                      | 31.2 us: 1.03x faster                                        |
| scimark_fft                | 445 ms                                                       | 433 ms: 1.03x faster                                         |
| meteor_contest             | 113 ms                                                       | 110 ms: 1.03x faster                                         |
| dulwich_log                | 58.5 ms                                                      | 57.0 ms: 1.03x faster                                        |
| pprint_safe_repr           | 933 ms                                                       | 909 ms: 1.03x faster                                         |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                         |
| html5lib                   | 66.1 ms                                                      | 64.6 ms: 1.02x faster                                        |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                        |
| async_generators           | 488 ms                                                       | 479 ms: 1.02x faster                                         |
| sympy_str                  | 265 ms                                                       | 261 ms: 1.02x faster                                         |
| hexiom                     | 7.08 ms                                                      | 6.97 ms: 1.02x faster                                        |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.02x faster                                         |
| crypto_pyaes               | 82.0 ms                                                      | 80.9 ms: 1.01x faster                                        |
| sqlglot_optimize           | 62.6 ms                                                      | 61.8 ms: 1.01x faster                                        |
| bpe_tokeniser              | 5.83 sec                                                     | 5.76 sec: 1.01x faster                                       |
| sqlite_synth               | 3.90 us                                                      | 3.86 us: 1.01x faster                                        |
| pickle_list                | 5.27 us                                                      | 5.22 us: 1.01x faster                                        |
| coverage                   | 98.4 ms                                                      | 97.6 ms: 1.01x faster                                        |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                       |
| unpickle_list              | 6.52 us                                                      | 6.60 us: 1.01x slower                                        |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                         |
| chaos                      | 68.3 ms                                                      | 69.3 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.7 ms: 1.02x slower                                        |
| deltablue                  | 3.88 ms                                                      | 3.95 ms: 1.02x slower                                        |
| pickle_pure_python         | 359 us                                                       | 365 us: 1.02x slower                                         |
| genshi_xml                 | 60.4 ms                                                      | 61.6 ms: 1.02x slower                                        |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                         |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                       |
| bench_thread_pool          | 1.26 ms                                                      | 1.30 ms: 1.04x slower                                        |
| mako                       | 13.2 ms                                                      | 13.7 ms: 1.04x slower                                        |
| pickle                     | 13.4 us                                                      | 13.9 us: 1.04x slower                                        |
| fannkuch                   | 451 ms                                                       | 469 ms: 1.04x slower                                         |
| float                      | 91.4 ms                                                      | 95.4 ms: 1.04x slower                                        |
| raytrace                   | 297 ms                                                       | 311 ms: 1.05x slower                                         |
| pyflate                    | 557 ms                                                       | 585 ms: 1.05x slower                                         |
| json_dumps                 | 13.1 ms                                                      | 14.1 ms: 1.08x slower                                        |
| python_startup             | 13.0 ms                                                      | 14.5 ms: 1.12x slower                                        |
| gc_traversal               | 5.17 ms                                                      | 6.25 ms: 1.21x slower                                        |
| create_gc_cycles           | 2.33 ms                                                      | 3.67 ms: 1.58x slower                                        |
| bench_mp_pool              | 7.03 ms                                                      | 4.94 sec: 702.92x slower                                     |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                 |

Benchmark hidden because not significant (27): sqlglot_normalize, tornado_http, scimark_sparse_mat_mult, sqlglot_parse, logging_silent, coroutines, pycparser, nqueens, django_template, nbody, xml_etree_process, xml_etree_parse, sympy_expand, pidigits, asyncio_tcp_ssl, typing_runtime_protocols, regex_v8, asyncio_websockets, genshi_text, sympy_integrate, xml_etree_generate, python_startup_no_site, comprehensions, spectral_norm, pickle_dict, sqlglot_transpile, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x