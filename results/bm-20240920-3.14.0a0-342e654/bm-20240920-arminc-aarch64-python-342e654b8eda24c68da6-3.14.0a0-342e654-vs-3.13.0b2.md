# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 296 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.02 sec: 1.03x faster                                                  |
| html5lib       | 66.1 ms                                                      | 64.4 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 555 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| json_loads           | 32.1 us                                                      | 31.6 us: 1.01x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| pickle_dict          | 37.6 us                                                      | 38.2 us: 1.02x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 256 us: 1.02x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 366 us: 1.02x slower                                                    |
| pickle               | 13.4 us                                                      | 13.7 us: 1.03x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_list, xml_etree_process, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                                   |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 329 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.8 us: 1.34x faster                                                   |
| go                         | 161 ms                                                       | 138 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.48 us: 1.16x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 20.9 ms: 1.09x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 555 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.0 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 557 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.9 ms: 1.04x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.98 us: 1.03x faster                                                   |
| thrift                     | 962 us                                                       | 933 us: 1.03x faster                                                    |
| 2to3                       | 305 ms                                                       | 296 ms: 1.03x faster                                                    |
| docutils                   | 3.10 sec                                                     | 3.02 sec: 1.03x faster                                                  |
| html5lib                   | 66.1 ms                                                      | 64.4 ms: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.63 us: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.41 ms: 1.02x faster                                                   |
| json                       | 5.64 ms                                                      | 5.53 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 61.7 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.6 us: 1.01x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 920 ms: 1.01x faster                                                    |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| async_generators           | 488 ms                                                       | 481 ms: 1.01x faster                                                    |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.01x faster                                                    |
| genshi_text                | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.12 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                                  |
| scimark_fft                | 445 ms                                                       | 441 ms: 1.01x faster                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| coverage                   | 98.4 ms                                                      | 99.1 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.89 sec: 1.01x slower                                                  |
| pyflate                    | 557 ms                                                       | 564 ms: 1.01x slower                                                    |
| pickle_dict                | 37.6 us                                                      | 38.2 us: 1.02x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.14 ms: 1.02x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 7.19 ms: 1.02x slower                                                   |
| float                      | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 256 us: 1.02x slower                                                    |
| chaos                      | 68.3 ms                                                      | 69.6 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.9 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 366 us: 1.02x slower                                                    |
| sqlite_synth               | 3.90 us                                                      | 4.00 us: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.03x slower                                                   |
| raytrace                   | 297 ms                                                       | 305 ms: 1.03x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.77 ms: 1.03x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (30): tornado_http, create_gc_cycles, sqlglot_normalize, xml_etree_parse, genshi_xml, regex_effbot, sympy_integrate, logging_silent, sympy_str, pickle_list, spectral_norm, nqueens, xml_etree_process, pidigits, crypto_pyaes, pycparser, asyncio_websockets, python_startup, comprehensions, sympy_expand, mdp, django_template, python_startup_no_site, typing_runtime_protocols, unpickle_list, dulwich_log, sqlglot_parse, deltablue, xml_etree_iterparse, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x