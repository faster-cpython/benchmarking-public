# Results vs. 3.13.0b2

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.03x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 417 ms: 1.18x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 555 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 417 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 722 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 716 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| json_loads           | 32.1 us                                                      | 31.5 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                                    |
| pickle               | 13.4 us                                                      | 13.6 us: 1.01x slower                                                   |
| unpickle_list        | 6.52 us                                                      | 6.63 us: 1.02x slower                                                   |
| pickle_dict          | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, json_dumps, xml_etree_parse, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                      | 26.9 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                   |
| mako            | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.6 us: 1.35x faster                                                   |
| deepcopy                   | 448 us                                                       | 334 us: 1.34x faster                                                    |
| async_tree_none            | 492 ms                                                       | 417 ms: 1.18x faster                                                    |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 555 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.48 us: 1.16x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 417 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 722 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 20.9 ms: 1.09x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 716 ms: 1.07x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.4 ms: 1.07x faster                                                   |
| richards_super             | 62.3 ms                                                      | 58.9 ms: 1.06x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.05x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 556 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.89 us: 1.05x faster                                                   |
| thrift                     | 962 us                                                       | 928 us: 1.04x faster                                                    |
| logging_format             | 7.82 us                                                      | 7.56 us: 1.04x faster                                                   |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.3 ms: 1.03x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.02x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                  |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| genshi_text                | 27.4 ms                                                      | 26.9 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| django_template            | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.5 us: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 923 ms: 1.01x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.13 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.01x faster                                                  |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                                    |
| pyflate                    | 557 ms                                                       | 564 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.01x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 100 ms: 1.01x slower                                                    |
| fannkuch                   | 451 ms                                                       | 458 ms: 1.02x slower                                                    |
| float                      | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                                   |
| unpickle_list              | 6.52 us                                                      | 6.63 us: 1.02x slower                                                   |
| pickle_dict                | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (40): tornado_http, sqlglot_normalize, json, xml_etree_process, regex_effbot, sqlite_synth, scimark_sor, sympy_str, async_generators, genshi_xml, telco, scimark_fft, python_startup_no_site, logging_silent, pycparser, sqlglot_parse, pidigits, sympy_integrate, scimark_monte_carlo, deltablue, coverage, json_dumps, scimark_sparse_mat_mult, bpe_tokeniser, hexiom, asyncio_websockets, html5lib, sympy_expand, crypto_pyaes, dulwich_log, xml_etree_parse, pickle_pure_python, spectral_norm, chaos, comprehensions, pickle_list, typing_runtime_protocols, sqlglot_optimize, bench_mp_pool, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x