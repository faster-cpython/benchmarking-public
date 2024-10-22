# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.00x slower
- HPT reliability: 75.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.10 sec: 1.07x slower                                       |
| html5lib       | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 604 ms: 1.07x faster                                         |
| async_generators           | 496 ms                                                   | 488 ms: 1.02x faster                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                       |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                        |
| asyncio_tcp                | 568 ms                                                   | 584 ms: 1.03x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 645 ms: 1.03x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 791 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 763 ms: 1.04x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.22 sec: 1.11x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.27 sec: 1.17x slower                                       |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (3): async_tree_none, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.4 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                        |
| regex_effbot   | 4.87 ms                                                  | 4.98 ms: 1.02x slower                                        |
| regex_dna      | 246 ms                                                   | 259 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.52 us: 1.02x faster                                        |
| unpickle             | 20.2 us                                                  | 19.8 us: 1.02x faster                                        |
| json_dumps           | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                        |
| pickle_list          | 5.34 us                                                  | 5.27 us: 1.01x faster                                        |
| unpickle_pure_python | 254 us                                                   | 251 us: 1.01x faster                                         |
| tomli_loads          | 2.53 sec                                                 | 2.57 sec: 1.02x slower                                       |
| json_loads           | 31.4 us                                                  | 32.1 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (7): pickle_dict, pickle, pickle_pure_python, xml_etree_iterparse, xml_etree_generate, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                        |
| python_startup_no_site | 8.75 ms                                                  | 8.60 ms: 1.02x faster                                        |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| genshi_text    | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 767 ms: 1.54x faster                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 604 ms: 1.07x faster                                         |
| bench_mp_pool              | 7.30 ms                                                  | 7.03 ms: 1.04x faster                                        |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                       |
| float                      | 94.4 ms                                                  | 91.4 ms: 1.03x faster                                        |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                        |
| unpickle_list              | 6.65 us                                                  | 6.52 us: 1.02x faster                                        |
| unpickle                   | 20.2 us                                                  | 19.8 us: 1.02x faster                                        |
| json_dumps                 | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                        |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.3 ms: 1.02x faster                                        |
| generators                 | 37.8 ms                                                  | 37.1 ms: 1.02x faster                                        |
| python_startup_no_site     | 8.75 ms                                                  | 8.60 ms: 1.02x faster                                        |
| async_generators           | 496 ms                                                   | 488 ms: 1.02x faster                                         |
| bench_thread_pool          | 1.28 ms                                                  | 1.26 ms: 1.02x faster                                        |
| regex_v8                   | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                        |
| logging_silent             | 135 ns                                                   | 133 ns: 1.01x faster                                         |
| mako                       | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| pickle_list                | 5.34 us                                                  | 5.27 us: 1.01x faster                                        |
| unpickle_pure_python       | 254 us                                                   | 251 us: 1.01x faster                                         |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                       |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                       |
| genshi_text                | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                        |
| deepcopy_reduce            | 4.07 us                                                  | 4.04 us: 1.01x faster                                        |
| pprint_safe_repr           | 926 ms                                                   | 933 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                       |
| scimark_lu                 | 139 ms                                                   | 141 ms: 1.01x slower                                         |
| sqlite_synth               | 3.84 us                                                  | 3.90 us: 1.02x slower                                        |
| pathlib                    | 22.4 ms                                                  | 22.8 ms: 1.02x slower                                        |
| thrift                     | 946 us                                                   | 962 us: 1.02x slower                                         |
| tomli_loads                | 2.53 sec                                                 | 2.57 sec: 1.02x slower                                       |
| pprint_pformat             | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                       |
| flaskblogging              | 4.60 ms                                                  | 4.70 ms: 1.02x slower                                        |
| json_loads                 | 31.4 us                                                  | 32.1 us: 1.02x slower                                        |
| regex_effbot               | 4.87 ms                                                  | 4.98 ms: 1.02x slower                                        |
| logging_simple             | 7.04 us                                                  | 7.21 us: 1.02x slower                                        |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                        |
| html5lib                   | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                        |
| asyncio_tcp                | 568 ms                                                   | 584 ms: 1.03x slower                                         |
| telco                      | 9.73 ms                                                  | 10.0 ms: 1.03x slower                                        |
| async_tree_memoization     | 626 ms                                                   | 645 ms: 1.03x slower                                         |
| richards_super             | 60.3 ms                                                  | 62.3 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 791 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 763 ms: 1.04x slower                                         |
| richards                   | 53.5 ms                                                  | 55.9 ms: 1.04x slower                                        |
| regex_dna                  | 246 ms                                                   | 259 ms: 1.05x slower                                         |
| dask                       | 350 ms                                                   | 370 ms: 1.06x slower                                         |
| docutils                   | 2.91 sec                                                 | 3.10 sec: 1.07x slower                                       |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                        |
| async_tree_io              | 1.11 sec                                                 | 1.22 sec: 1.11x slower                                       |
| gc_traversal               | 4.53 ms                                                  | 5.17 ms: 1.14x slower                                        |
| async_tree_io_tg           | 1.09 sec                                                 | 1.27 sec: 1.17x slower                                       |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (50): tornado_http, pylint, pickle_dict, gunicorn, sqlglot_transpile, go, aiohttp, crypto_pyaes, hexiom, chaos, chameleon, pickle, deepcopy, sympy_integrate, deepcopy_memo, scimark_fft, scimark_sparse_mat_mult, raytrace, regex_compile, 2to3, async_tree_none, pickle_pure_python, coverage, fannkuch, logging_format, meteor_contest, nbody, xml_etree_iterparse, pidigits, spectral_norm, sympy_sum, django_template, pyflate, asyncio_websockets, nqueens, scimark_sor, genshi_xml, xml_etree_generate, sqlglot_optimize, json, sympy_expand, comprehensions, sympy_str, deltablue, sqlglot_normalize, typing_runtime_protocols, xml_etree_process, async_tree_none_tg, xml_etree_parse, sqlglot_parse
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dulwich_log

# HPT report

- Reliability score: 75.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x