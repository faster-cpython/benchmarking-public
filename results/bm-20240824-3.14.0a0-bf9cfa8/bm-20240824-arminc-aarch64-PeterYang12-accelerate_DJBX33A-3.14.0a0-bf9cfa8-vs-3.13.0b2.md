# Results vs. 3.13.0b2

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-aarch64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 294 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                       |
| async_tree_none            | 492 ms                                                       | 433 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                       |
| async_tree_memoization_tg  | 604 ms                                                       | 551 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 733 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                     |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 730 ms: 1.05x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                      |
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                       |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 111 ms: 1.03x faster                                                       |
| xml_etree_iterparse | 147 ms                                                       | 146 ms: 1.00x faster                                                       |
| pickle_pure_python  | 359 us                                                       | 365 us: 1.02x slower                                                       |
| json_loads          | 32.1 us                                                      | 32.8 us: 1.02x slower                                                      |
| tomli_loads         | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.8 ms: 1.01x faster                                                      |
| mako            | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 335 us: 1.34x faster                                                       |
| deepcopy_memo              | 50.8 us                                                      | 38.2 us: 1.33x faster                                                      |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                       |
| async_tree_none            | 492 ms                                                       | 433 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 4.04 us                                                      | 3.57 us: 1.13x faster                                                      |
| async_tree_memoization_tg  | 604 ms                                                       | 551 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 733 ms: 1.08x faster                                                       |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                     |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                     |
| generators                 | 37.1 ms                                                      | 34.9 ms: 1.06x faster                                                      |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                                      |
| richards_super             | 62.3 ms                                                      | 59.2 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 730 ms: 1.05x faster                                                       |
| nbody                      | 114 ms                                                       | 109 ms: 1.04x faster                                                       |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                       |
| gc_traversal               | 5.17 ms                                                      | 4.98 ms: 1.04x faster                                                      |
| 2to3                       | 305 ms                                                       | 294 ms: 1.04x faster                                                       |
| regex_v8                   | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                      |
| logging_simple             | 7.21 us                                                      | 6.98 us: 1.03x faster                                                      |
| create_gc_cycles           | 2.33 ms                                                      | 2.26 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                                     |
| meteor_contest             | 113 ms                                                       | 110 ms: 1.03x faster                                                       |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                       |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.03x faster                                                       |
| thrift                     | 962 us                                                       | 939 us: 1.02x faster                                                       |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                                       |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                       |
| logging_format             | 7.82 us                                                      | 7.68 us: 1.02x faster                                                      |
| asyncio_tcp                | 584 ms                                                       | 573 ms: 1.02x faster                                                       |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                      |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                      |
| hexiom                     | 7.08 ms                                                      | 6.97 ms: 1.02x faster                                                      |
| sympy_sum                  | 144 ms                                                       | 142 ms: 1.02x faster                                                       |
| django_template            | 42.3 ms                                                      | 41.8 ms: 1.01x faster                                                      |
| bench_mp_pool              | 7.03 ms                                                      | 6.96 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 933 ms                                                       | 927 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 147 ms                                                       | 146 ms: 1.00x faster                                                       |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.00x slower                                                      |
| mdp                        | 3.33 sec                                                     | 3.34 sec: 1.00x slower                                                     |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                     |
| python_startup_no_site     | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                                      |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                      |
| pickle_pure_python         | 359 us                                                       | 365 us: 1.02x slower                                                       |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                       |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                       |
| json_loads                 | 32.1 us                                                      | 32.8 us: 1.02x slower                                                      |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                     |
| go                         | 161 ms                                                       | 191 ms: 1.19x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (39): sqlglot_normalize, sqlglot_parse, xml_etree_process, coroutines, sqlglot_optimize, xml_etree_parse, tornado_http, scimark_sparse_mat_mult, async_generators, genshi_xml, telco, genshi_text, sympy_integrate, spectral_norm, regex_compile, docutils, scimark_monte_carlo, float, sympy_str, html5lib, python_startup, pidigits, typing_runtime_protocols, asyncio_websockets, scimark_fft, bpe_tokeniser, json_dumps, sympy_expand, unpickle_pure_python, pyflate, crypto_pyaes, comprehensions, chaos, pycparser, coverage, nqueens, json, deltablue, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x