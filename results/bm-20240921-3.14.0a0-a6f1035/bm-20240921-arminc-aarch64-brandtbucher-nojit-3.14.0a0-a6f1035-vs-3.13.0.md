# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.02x faster
- HPT reliability: 96.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 297 ms: 1.03x faster                                           |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                         |
| tornado_http   | 131 ms                                                   | 126 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 493 ms                                                   | 417 ms: 1.18x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                           |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                           |
| async_tree_none_tg         | 467 ms                                                   | 419 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 736 ms: 1.04x faster                                           |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                           |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 721 ms: 1.02x faster                                           |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                         |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                          |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                         |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                         |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                   |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                           |
| float          | 94.4 ms                                                  | 94.9 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                          |
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                           |
| regex_dna      | 246 ms                                                   | 251 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.4 us: 1.04x faster                                          |
| unpickle_list       | 6.65 us                                                  | 6.42 us: 1.04x faster                                          |
| pickle_list         | 5.34 us                                                  | 5.21 us: 1.02x faster                                          |
| json_loads          | 31.4 us                                                  | 31.8 us: 1.01x slower                                          |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.02x slower                                           |
| tomli_loads         | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                         |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (8): xml_etree_generate, pickle_dict, xml_etree_process, xml_etree_parse, json_dumps, unpickle_pure_python, pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 335 us: 1.35x faster                                           |
| deepcopy_memo              | 51.0 us                                                  | 39.2 us: 1.30x faster                                          |
| async_tree_none            | 493 ms                                                   | 417 ms: 1.18x faster                                           |
| go                         | 163 ms                                                   | 138 ms: 1.18x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                           |
| deepcopy_reduce            | 4.07 us                                                  | 3.58 us: 1.14x faster                                          |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                           |
| async_tree_none_tg         | 467 ms                                                   | 419 ms: 1.11x faster                                           |
| generators                 | 37.8 ms                                                  | 35.4 ms: 1.07x faster                                          |
| pathlib                    | 22.4 ms                                                  | 21.4 ms: 1.05x faster                                          |
| unpickle                   | 20.2 us                                                  | 19.4 us: 1.04x faster                                          |
| tornado_http               | 131 ms                                                   | 126 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 736 ms: 1.04x faster                                           |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                          |
| unpickle_list              | 6.65 us                                                  | 6.42 us: 1.04x faster                                          |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                           |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                           |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                           |
| 2to3                       | 306 ms                                                   | 297 ms: 1.03x faster                                           |
| bench_mp_pool              | 7.30 ms                                                  | 7.12 ms: 1.03x faster                                          |
| pickle_list                | 5.34 us                                                  | 5.21 us: 1.02x faster                                          |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.0 ms: 1.02x faster                                          |
| thrift                     | 946 us                                                   | 926 us: 1.02x faster                                           |
| pycparser                  | 1.26 sec                                                 | 1.24 sec: 1.02x faster                                         |
| scimark_sor                | 159 ms                                                   | 156 ms: 1.02x faster                                           |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.45 ms: 1.02x faster                                          |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 721 ms: 1.02x faster                                           |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                           |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.02x faster                                           |
| pprint_safe_repr           | 926 ms                                                   | 911 ms: 1.02x faster                                           |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                          |
| richards_super             | 60.3 ms                                                  | 59.4 ms: 1.02x faster                                          |
| regex_compile              | 128 ms                                                   | 127 ms: 1.01x faster                                           |
| richards                   | 53.5 ms                                                  | 52.8 ms: 1.01x faster                                          |
| bench_thread_pool          | 1.28 ms                                                  | 1.26 ms: 1.01x faster                                          |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                           |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                         |
| bpe_tokeniser              | 5.90 sec                                                 | 5.87 sec: 1.00x faster                                         |
| float                      | 94.4 ms                                                  | 94.9 ms: 1.01x slower                                          |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                         |
| pyflate                    | 556 ms                                                   | 563 ms: 1.01x slower                                           |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                           |
| json_loads                 | 31.4 us                                                  | 31.8 us: 1.01x slower                                          |
| raytrace                   | 298 ms                                                   | 302 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.02x slower                                           |
| regex_dna                  | 246 ms                                                   | 251 ms: 1.02x slower                                           |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                          |
| deltablue                  | 3.85 ms                                                  | 3.94 ms: 1.02x slower                                          |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                          |
| fannkuch                   | 452 ms                                                   | 465 ms: 1.03x slower                                           |
| docutils                   | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                         |
| tomli_loads                | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                         |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.06x slower                                          |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                         |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                          |
| gc_traversal               | 4.53 ms                                                  | 5.04 ms: 1.11x slower                                          |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                   |

Benchmark hidden because not significant (39): logging_format, asyncio_tcp, xml_etree_generate, pickle_dict, django_template, genshi_text, unpack_sequence, python_startup_no_site, coverage, crypto_pyaes, mdp, sympy_sum, xml_etree_process, xml_etree_parse, sqlglot_optimize, sqlglot_transpile, json_dumps, unpickle_pure_python, pidigits, typing_runtime_protocols, meteor_contest, sympy_integrate, mako, html5lib, pickle_pure_python, chaos, nqueens, hexiom, spectral_norm, asyncio_websockets, sqlite_synth, logging_simple, pickle, regex_effbot, comprehensions, json, sympy_str, genshi_xml, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json: dulwich_log

# HPT report

- Reliability score: 96.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x