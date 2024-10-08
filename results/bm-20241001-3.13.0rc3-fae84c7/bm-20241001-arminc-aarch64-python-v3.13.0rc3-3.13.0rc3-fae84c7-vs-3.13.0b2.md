# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc3
- machine: linux-aarch64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.00x faster
- HPT reliability: 88.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 9.05 ms: 1.01x slower                                          |
| docutils       | 3.10 sec                                                     | 2.88 sec: 1.07x faster                                         |
| html5lib       | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                   |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.08 sec: 1.18x faster                                         |
| async_tree_io              | 1.22 sec                                                     | 1.11 sec: 1.11x faster                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 726 ms: 1.05x faster                                           |
| async_tree_memoization     | 645 ms                                                       | 614 ms: 1.05x faster                                           |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 761 ms: 1.04x faster                                           |
| async_tree_none_tg         | 476 ms                                                       | 464 ms: 1.03x faster                                           |
| async_tree_memoization_tg  | 604 ms                                                       | 643 ms: 1.06x slower                                           |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                   |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 93.7 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                           |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.02x faster                                          |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                        | 1.02x faster                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.3 us: 1.03x faster                                          |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                           |
| tomli_loads          | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                         |
| unpickle             | 19.8 us                                                      | 20.0 us: 1.01x slower                                          |
| pickle               | 13.4 us                                                      | 13.5 us: 1.01x slower                                          |
| pickle_dict          | 37.6 us                                                      | 38.1 us: 1.01x slower                                          |
| pickle_list          | 5.27 us                                                      | 5.36 us: 1.02x slower                                          |
| unpickle_pure_python | 251 us                                                       | 256 us: 1.02x slower                                           |
| json_dumps           | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                          |
| unpickle_list        | 6.52 us                                                      | 6.92 us: 1.06x slower                                          |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_iterparse, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.01x slower                                          |
| python_startup_no_site | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                          |
| mako            | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                          |
| genshi_text     | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.08 sec: 1.18x faster                                         |
| gc_traversal               | 5.17 ms                                                      | 4.56 ms: 1.13x faster                                          |
| async_tree_io              | 1.22 sec                                                     | 1.11 sec: 1.11x faster                                         |
| create_gc_cycles           | 2.33 ms                                                      | 2.14 ms: 1.09x faster                                          |
| docutils                   | 3.10 sec                                                     | 2.88 sec: 1.07x faster                                         |
| dask                       | 370 ms                                                       | 350 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 726 ms: 1.05x faster                                           |
| async_tree_memoization     | 645 ms                                                       | 614 ms: 1.05x faster                                           |
| richards                   | 55.9 ms                                                      | 53.6 ms: 1.04x faster                                          |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 761 ms: 1.04x faster                                           |
| flaskblogging              | 4.70 ms                                                      | 4.54 ms: 1.04x faster                                          |
| telco                      | 10.0 ms                                                      | 9.69 ms: 1.03x faster                                          |
| asyncio_tcp                | 584 ms                                                       | 565 ms: 1.03x faster                                           |
| async_tree_none_tg         | 476 ms                                                       | 464 ms: 1.03x faster                                           |
| logging_simple             | 7.21 us                                                      | 7.02 us: 1.03x faster                                          |
| json_loads                 | 32.1 us                                                      | 31.3 us: 1.03x faster                                          |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                           |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.02x faster                                          |
| html5lib                   | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                          |
| json                       | 5.64 ms                                                      | 5.53 ms: 1.02x faster                                          |
| logging_format             | 7.82 us                                                      | 7.67 us: 1.02x faster                                          |
| richards_super             | 62.3 ms                                                      | 61.1 ms: 1.02x faster                                          |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                          |
| django_template            | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                          |
| pprint_pformat             | 1.93 sec                                                     | 1.90 sec: 1.02x faster                                         |
| aiohttp                    | 1.18 ms                                                      | 1.16 ms: 1.02x faster                                          |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                          |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                           |
| tomli_loads                | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                         |
| thrift                     | 962 us                                                       | 947 us: 1.02x faster                                           |
| deltablue                  | 3.88 ms                                                      | 3.82 ms: 1.02x faster                                          |
| sympy_sum                  | 144 ms                                                       | 142 ms: 1.01x faster                                           |
| scimark_lu                 | 141 ms                                                       | 140 ms: 1.01x faster                                           |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                         |
| bpe_tokeniser              | 5.83 sec                                                     | 5.86 sec: 1.01x slower                                         |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.01x slower                                          |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                         |
| pyflate                    | 557 ms                                                       | 561 ms: 1.01x slower                                           |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                          |
| bench_thread_pool          | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                          |
| unpickle                   | 19.8 us                                                      | 20.0 us: 1.01x slower                                          |
| chameleon                  | 8.95 ms                                                      | 9.05 ms: 1.01x slower                                          |
| pickle                     | 13.4 us                                                      | 13.5 us: 1.01x slower                                          |
| pickle_dict                | 37.6 us                                                      | 38.1 us: 1.01x slower                                          |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.01x slower                                          |
| go                         | 161 ms                                                       | 163 ms: 1.01x slower                                           |
| generators                 | 37.1 ms                                                      | 37.8 ms: 1.02x slower                                          |
| python_startup_no_site     | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                          |
| pickle_list                | 5.27 us                                                      | 5.36 us: 1.02x slower                                          |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                          |
| unpickle_pure_python       | 251 us                                                       | 256 us: 1.02x slower                                           |
| deepcopy                   | 448 us                                                       | 459 us: 1.02x slower                                           |
| deepcopy_reduce            | 4.04 us                                                      | 4.14 us: 1.02x slower                                          |
| float                      | 91.4 ms                                                      | 93.7 ms: 1.02x slower                                          |
| pycparser                  | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                         |
| json_dumps                 | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                          |
| bench_mp_pool              | 7.03 ms                                                      | 7.33 ms: 1.04x slower                                          |
| unpickle_list              | 6.52 us                                                      | 6.92 us: 1.06x slower                                          |
| async_tree_memoization_tg  | 604 ms                                                       | 643 ms: 1.06x slower                                           |
| mypy2                      | 767 ms                                                       | 1.18 sec: 1.54x slower                                         |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                   |

Benchmark hidden because not significant (41): sqlglot_parse, sqlglot_normalize, gunicorn, xml_etree_process, async_tree_none, pprint_safe_repr, 2to3, comprehensions, hexiom, sympy_str, scimark_sor, coverage, nqueens, meteor_contest, xml_etree_iterparse, raytrace, nbody, scimark_sparse_mat_mult, xml_etree_parse, crypto_pyaes, pidigits, pathlib, typing_runtime_protocols, logging_silent, sympy_expand, fannkuch, spectral_norm, regex_compile, chaos, asyncio_websockets, scimark_fft, sqlite_synth, sqlglot_optimize, scimark_monte_carlo, sympy_integrate, async_generators, pickle_pure_python, genshi_xml, pylint, deepcopy_memo, tornado_http
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dulwich_log
Ignored benchmarks (1) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: unpack_sequence

# HPT report

- Reliability score: 88.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x