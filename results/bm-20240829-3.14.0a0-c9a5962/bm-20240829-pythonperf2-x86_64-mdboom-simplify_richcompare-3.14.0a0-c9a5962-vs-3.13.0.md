# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 69.2 ms: 1.04x faster                                                       |
| tornado_http   | 120 ms                                                       | 115 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 395 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 570 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 779 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 817 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 361 ms: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                       |
| float          | 81.9 ms                                                      | 78.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.42 ms: 1.02x slower                                                       |
| regex_dna      | 244 ms                                                       | 254 ms: 1.04x slower                                                        |
| regex_v8       | 26.2 ms                                                      | 27.3 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 58.8 ms: 1.04x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 212 us: 1.01x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.04x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.60 sec: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 54.5 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 40.2 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 286 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 28.9 us: 1.36x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| go                         | 160 ms                                                       | 135 ms: 1.19x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.5 ms: 1.17x faster                                                       |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                        |
| scimark_sor                | 126 ms                                                       | 109 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 395 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                       |
| raytrace                   | 289 ms                                                       | 268 ms: 1.08x faster                                                        |
| richards_super             | 59.8 ms                                                      | 55.7 ms: 1.07x faster                                                       |
| richards                   | 52.7 ms                                                      | 49.6 ms: 1.06x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 852 us: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.5 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 570 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 779 ms: 1.05x faster                                                        |
| scimark_fft                | 314 ms                                                       | 299 ms: 1.05x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                       |
| thrift                     | 877 us                                                       | 841 us: 1.04x faster                                                        |
| tornado_http               | 120 ms                                                       | 115 ms: 1.04x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.24 ms: 1.04x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 69.2 ms: 1.04x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.81 us: 1.04x faster                                                       |
| float                      | 81.9 ms                                                      | 78.9 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.91 sec: 1.04x faster                                                      |
| async_tree_io              | 847 ms                                                       | 817 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.8 ms: 1.04x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                                      |
| fannkuch                   | 365 ms                                                       | 354 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.22 us: 1.03x faster                                                       |
| chaos                      | 61.7 ms                                                      | 60.5 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 796 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 96.0 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| sympy_expand               | 505 ms                                                       | 496 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| pyflate                    | 492 ms                                                       | 484 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.37 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 214 us                                                       | 212 us: 1.01x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 59.2 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.26 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| hexiom                     | 6.33 ms                                                      | 6.31 ms: 1.00x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.52 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 361 ms: 1.01x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.5 ms: 1.01x slower                                                       |
| coverage                   | 81.1 ms                                                      | 82.1 ms: 1.01x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.4 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.01x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.42 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| django_template            | 38.9 ms                                                      | 40.2 ms: 1.04x slower                                                       |
| regex_dna                  | 244 ms                                                       | 254 ms: 1.04x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 27.3 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.04x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.60 sec: 1.08x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.48 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (10): mako, scimark_monte_carlo, coroutines, logging_silent, bench_mp_pool, pidigits, json, sqlglot_transpile, xml_etree_iterparse, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x