# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.03x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 284 ms: 1.02x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.9 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 570 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 548 ms: 1.05x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 366 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 792 ms: 1.03x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.2 ms: 1.03x faster                                                       |
| nbody          | 88.0 ms                                                      | 85.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.47 ms: 1.03x slower                                                       |
| regex_dna      | 244 ms                                                       | 255 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.3 ms: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.56 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 54.8 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 285 us: 1.40x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.4 us: 1.34x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.23x faster                                                       |
| go                         | 160 ms                                                       | 134 ms: 1.20x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.4 ms: 1.18x faster                                                       |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| scimark_sor                | 126 ms                                                       | 109 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| coverage                   | 81.1 ms                                                      | 74.9 ms: 1.08x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.0 ms: 1.07x faster                                                       |
| scimark_fft                | 314 ms                                                       | 296 ms: 1.06x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                       |
| raytrace                   | 289 ms                                                       | 275 ms: 1.05x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.1 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 570 ms: 1.05x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.17 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 548 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.8 ms: 1.05x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 863 us: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 366 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| float                      | 81.9 ms                                                      | 79.2 ms: 1.03x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 792 ms: 1.03x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.88 us: 1.03x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.96 sec: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.3 ms: 1.03x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.18 ms: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.03x faster                                                      |
| nbody                      | 88.0 ms                                                      | 85.8 ms: 1.03x faster                                                       |
| pyflate                    | 492 ms                                                       | 481 ms: 1.02x faster                                                        |
| thrift                     | 877 us                                                       | 857 us: 1.02x faster                                                        |
| 2to3                       | 291 ms                                                       | 284 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.7 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 70.9 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                                       |
| fannkuch                   | 365 ms                                                       | 360 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 802 ms: 1.01x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.34 us: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| sympy_str                  | 296 ms                                                       | 294 ms: 1.01x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.51 sec: 1.01x faster                                                      |
| sqlglot_optimize           | 59.7 ms                                                      | 59.3 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.32 ms: 1.00x faster                                                       |
| sympy_expand               | 505 ms                                                       | 503 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| deltablue                  | 3.41 ms                                                      | 3.42 ms: 1.00x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.28 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.7 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| chaos                      | 61.7 ms                                                      | 62.8 ms: 1.02x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 74.1 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 121 ms: 1.02x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.47 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| regex_dna                  | 244 ms                                                       | 255 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.4 ms: 1.05x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.56 sec: 1.06x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.63 ms: 1.13x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (7): bench_mp_pool, pidigits, meteor_contest, mako, xml_etree_parse, typing_runtime_protocols, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x