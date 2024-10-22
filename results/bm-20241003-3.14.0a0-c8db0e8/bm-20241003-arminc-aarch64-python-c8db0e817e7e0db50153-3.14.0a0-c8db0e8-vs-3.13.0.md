# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-aarch64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.06x slower
- HPT reliability: 91.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 2.99 sec: 1.03x slower                                                  |
| tornado_http   | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 418 ms: 1.18x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 477 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 716 ms: 1.03x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 558 ms: 1.02x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_effbot   | 4.87 ms                                                  | 5.03 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 262 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| xml_etree_iterparse | 147 ms                                                   | 150 ms: 1.02x slower                                                    |
| pickle_pure_python  | 359 us                                                   | 370 us: 1.03x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (10): pickle_dict, unpickle_list, xml_etree_generate, pickle_list, json_loads, unpickle_pure_python, xml_etree_parse, xml_etree_process, json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.64 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 60.8 ms: 1.01x slower                                                   |
| genshi_text    | 27.7 ms                                                  | 28.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| deepcopy                   | 451 us                                                   | 333 us: 1.35x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 418 ms: 1.18x faster                                                    |
| go                         | 163 ms                                                   | 139 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.52 us: 1.16x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.9 ms: 1.08x faster                                                   |
| tornado_http               | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.3 ms: 1.05x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 477 ms: 1.04x faster                                                    |
| unpickle                   | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| 2to3                       | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| scimark_fft                | 447 ms                                                   | 434 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| telco                      | 9.73 ms                                                  | 9.47 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 716 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.41 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.0 ms: 1.02x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 141 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 558 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 931 us: 1.02x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.31 sec: 1.01x faster                                                  |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.81 sec: 1.01x faster                                                  |
| python_startup_no_site     | 8.75 ms                                                  | 8.64 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 915 ms: 1.01x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 60.8 ms: 1.01x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 99.8 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| typing_runtime_protocols   | 192 us                                                   | 194 us: 1.01x slower                                                    |
| chaos                      | 68.8 ms                                                  | 69.7 ms: 1.01x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 28.1 ms: 1.01x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 3.93 ms: 1.02x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.30 ms: 1.02x slower                                                   |
| raytrace                   | 298 ms                                                   | 304 ms: 1.02x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 150 ms: 1.02x slower                                                    |
| fannkuch                   | 452 ms                                                   | 463 ms: 1.03x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 370 us: 1.03x slower                                                    |
| docutils                   | 2.91 sec                                                 | 2.99 sec: 1.03x slower                                                  |
| regex_effbot               | 4.87 ms                                                  | 5.03 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| regex_dna                  | 246 ms                                                   | 262 ms: 1.07x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.26 ms: 1.07x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 5.16 ms: 1.14x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 5.71 sec: 782.08x slower                                                |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                            |

Benchmark hidden because not significant (37): logging_format, richards_super, json, pickle_dict, unpickle_list, sqlglot_normalize, xml_etree_generate, spectral_norm, pickle_list, meteor_contest, json_loads, sqlite_synth, unpickle_pure_python, unpack_sequence, crypto_pyaes, pprint_pformat, xml_etree_parse, scimark_sor, hexiom, xml_etree_process, logging_simple, float, sympy_str, pidigits, sympy_integrate, pyflate, coverage, json_dumps, sqlglot_transpile, sympy_expand, django_template, pickle, mako, html5lib, sqlglot_optimize, comprehensions, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: dulwich_log

# HPT report

- Reliability score: 91.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x