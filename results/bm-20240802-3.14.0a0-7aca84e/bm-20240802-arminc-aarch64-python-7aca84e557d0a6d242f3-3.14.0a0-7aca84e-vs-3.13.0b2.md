# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| html5lib       | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 397 ms: 1.20x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 552 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 531 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                  |
| async_tree_none            | 492 ms                                                       | 434 ms: 1.13x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.10 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 702 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| tomli_loads        | 2.57 sec                                                     | 2.53 sec: 1.01x faster                                                  |
| json_dumps         | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads         | 32.1 us                                                      | 33.0 us: 1.03x slower                                                   |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_pure_python, xml_etree_process, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.4 ms: 1.03x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.90 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                   |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 330 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.1 us: 1.33x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 397 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.38 us: 1.20x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 552 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 531 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                  |
| async_tree_none            | 492 ms                                                       | 434 ms: 1.13x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.10 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 702 ms: 1.09x faster                                                    |
| richards                   | 55.9 ms                                                      | 51.9 ms: 1.08x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| richards_super             | 62.3 ms                                                      | 58.5 ms: 1.06x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.98 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.33 ms: 1.03x faster                                                   |
| logging_simple             | 7.21 us                                                      | 6.97 us: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| logging_silent             | 133 ns                                                       | 129 ns: 1.03x faster                                                    |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| deltablue                  | 3.88 ms                                                      | 3.81 ms: 1.02x faster                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 61.5 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.86 ms: 1.02x faster                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.53 sec: 1.01x faster                                                  |
| spectral_norm              | 141 ms                                                       | 139 ms: 1.01x faster                                                    |
| go                         | 161 ms                                                       | 159 ms: 1.01x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| scimark_fft                | 445 ms                                                       | 440 ms: 1.01x faster                                                    |
| nqueens                    | 98.9 ms                                                      | 97.8 ms: 1.01x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 941 ms: 1.01x slower                                                    |
| sympy_str                  | 265 ms                                                       | 269 ms: 1.01x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 146 ms: 1.01x slower                                                    |
| float                      | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| thrift                     | 962 us                                                       | 979 us: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 197 us: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.0 us: 1.03x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.4 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.90 ms: 1.04x slower                                                   |
| fannkuch                   | 451 ms                                                       | 467 ms: 1.04x slower                                                    |
| pyflate                    | 557 ms                                                       | 582 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (40): dask, xml_etree_parse, asyncio_tcp, django_template, logging_format, coroutines, scimark_monte_carlo, meteor_contest, raytrace, chaos, regex_compile, pickle_pure_python, hexiom, pprint_pformat, coverage, async_generators, xml_etree_process, unpickle_pure_python, pycparser, 2to3, sqlglot_normalize, mdp, pidigits, asyncio_tcp_ssl, crypto_pyaes, bpe_tokeniser, sqlglot_parse, asyncio_websockets, sqlglot_transpile, comprehensions, sympy_expand, tornado_http, docutils, bench_mp_pool, sympy_integrate, genshi_xml, create_gc_cycles, json, xml_etree_iterparse, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x