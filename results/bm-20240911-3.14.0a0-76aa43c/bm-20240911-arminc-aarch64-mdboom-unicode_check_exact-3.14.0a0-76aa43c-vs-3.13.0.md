# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-aarch64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 298 ms: 1.03x faster                                                   |
| docutils       | 2.91 sec                                                 | 3.00 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                   |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                   |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                   |
| async_generators           | 496 ms                                                   | 476 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 722 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                 |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                 |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                           |

Benchmark hidden because not significant (3): asyncio_tcp, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                   |
| float          | 94.4 ms                                                  | 92.1 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                    | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 124 ms: 1.04x faster                                                   |
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.39 us: 1.04x faster                                                  |
| unpickle             | 20.2 us                                                  | 19.4 us: 1.04x faster                                                  |
| pickle_list          | 5.34 us                                                  | 5.24 us: 1.02x faster                                                  |
| unpickle_pure_python | 254 us                                                   | 250 us: 1.02x faster                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (9): xml_etree_generate, xml_etree_process, pickle_dict, xml_etree_parse, pickle_pure_python, json_loads, json_dumps, xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                  |
| python_startup_no_site | 8.75 ms                                                  | 8.62 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 59.4 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                           |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 328 us: 1.37x faster                                                   |
| deepcopy_memo              | 51.0 us                                                  | 37.3 us: 1.37x faster                                                  |
| go                         | 163 ms                                                   | 136 ms: 1.20x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.49 us: 1.17x faster                                                  |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                   |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                   |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                  |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                  |
| pycparser                  | 1.26 sec                                                 | 1.20 sec: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                   |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.22 ms: 1.04x faster                                                  |
| async_generators           | 496 ms                                                   | 476 ms: 1.04x faster                                                   |
| unpickle_list              | 6.65 us                                                  | 6.39 us: 1.04x faster                                                  |
| unpickle                   | 20.2 us                                                  | 19.4 us: 1.04x faster                                                  |
| regex_compile              | 128 ms                                                   | 124 ms: 1.04x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.05 ms: 1.04x faster                                                  |
| sympy_sum                  | 143 ms                                                   | 139 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                                  |
| scimark_sor                | 159 ms                                                   | 155 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                   |
| logging_format             | 7.83 us                                                  | 7.62 us: 1.03x faster                                                  |
| thrift                     | 946 us                                                   | 921 us: 1.03x faster                                                   |
| logging_silent             | 135 ns                                                   | 132 ns: 1.03x faster                                                   |
| 2to3                       | 306 ms                                                   | 298 ms: 1.03x faster                                                   |
| float                      | 94.4 ms                                                  | 92.1 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 926 ms                                                   | 904 ms: 1.02x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.29 sec: 1.02x faster                                                 |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 722 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 439 ms: 1.02x faster                                                   |
| sympy_integrate            | 21.0 ms                                                  | 20.6 ms: 1.02x faster                                                  |
| pickle_list                | 5.34 us                                                  | 5.24 us: 1.02x faster                                                  |
| unpickle_pure_python       | 254 us                                                   | 250 us: 1.02x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                  |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.4 ms: 1.02x faster                                                  |
| nqueens                    | 98.7 ms                                                  | 97.0 ms: 1.02x faster                                                  |
| logging_simple             | 7.04 us                                                  | 6.92 us: 1.02x faster                                                  |
| richards_super             | 60.3 ms                                                  | 59.4 ms: 1.02x faster                                                  |
| python_startup_no_site     | 8.75 ms                                                  | 8.62 ms: 1.02x faster                                                  |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.01x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.8 ms: 1.01x faster                                                  |
| genshi_xml                 | 60.2 ms                                                  | 59.4 ms: 1.01x faster                                                  |
| json                       | 5.61 ms                                                  | 5.54 ms: 1.01x faster                                                  |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                 |
| raytrace                   | 298 ms                                                   | 302 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                 |
| fannkuch                   | 452 ms                                                   | 459 ms: 1.02x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.00 sec: 1.03x slower                                                 |
| tomli_loads                | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                 |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                 |
| telco                      | 9.73 ms                                                  | 10.2 ms: 1.04x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.27 ms: 1.07x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                 |
| gc_traversal               | 4.53 ms                                                  | 5.02 ms: 1.11x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                           |

Benchmark hidden because not significant (38): tornado_http, xml_etree_generate, genshi_text, sqlglot_normalize, crypto_pyaes, sympy_str, coverage, xml_etree_process, typing_runtime_protocols, pickle_dict, chaos, xml_etree_parse, html5lib, hexiom, pickle_pure_python, sqlglot_transpile, regex_dna, mako, sqlglot_optimize, pidigits, asyncio_tcp, coroutines, comprehensions, asyncio_websockets, unpack_sequence, spectral_norm, pyflate, sympy_expand, json_loads, sqlite_synth, deltablue, json_dumps, xml_etree_iterparse, django_template, regex_effbot, pickle, sqlglot_parse, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x