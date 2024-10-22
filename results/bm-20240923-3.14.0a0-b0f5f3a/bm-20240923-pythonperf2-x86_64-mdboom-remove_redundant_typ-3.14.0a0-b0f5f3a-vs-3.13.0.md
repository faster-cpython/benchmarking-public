# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 398 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 781 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 809 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.7 ms: 1.04x faster                                                       |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                                       |
| regex_dna      | 244 ms                                                       | 235 ms: 1.04x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                        |
| unpickle             | 15.1 us                                                      | 15.0 us: 1.01x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.64 us: 1.01x slower                                                       |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| pickle_dict          | 32.1 us                                                      | 32.7 us: 1.02x slower                                                       |
| unpickle_list        | 4.62 us                                                      | 4.73 us: 1.02x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 224 us: 1.05x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.59 sec: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.96 ms: 1.00x slower                                                       |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 53.6 ms: 1.07x faster                                                       |
| django_template | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 284 us: 1.40x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.0 us: 1.32x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| unpack_sequence            | 56.8 ns                                                      | 48.1 ns: 1.18x faster                                                       |
| go                         | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.9 ms: 1.16x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 398 ms: 1.14x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| raytrace                   | 289 ms                                                       | 268 ms: 1.08x faster                                                        |
| scimark_sor                | 126 ms                                                       | 117 ms: 1.07x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 53.6 ms: 1.07x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.0 ms: 1.07x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.11 ms: 1.06x faster                                                       |
| richards                   | 52.7 ms                                                      | 50.2 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 781 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 809 ms: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| float                      | 81.9 ms                                                      | 78.7 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.90 sec: 1.04x faster                                                      |
| bench_thread_pool          | 901 us                                                       | 867 us: 1.04x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                                       |
| regex_dna                  | 244 ms                                                       | 235 ms: 1.04x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| scimark_fft                | 314 ms                                                       | 304 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 57.9 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.02x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.19 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 95.8 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.93 us: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| fannkuch                   | 365 ms                                                       | 359 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| coverage                   | 81.1 ms                                                      | 80.2 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 802 ms: 1.01x faster                                                        |
| sympy_expand               | 505 ms                                                       | 499 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                        |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.01x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.79 us                                                      | 2.76 us: 1.01x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.38 ms: 1.01x faster                                                       |
| unpickle                   | 15.1 us                                                      | 15.0 us: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.01x faster                                                        |
| pyflate                    | 492 ms                                                       | 489 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.26 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.00x faster                                                       |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 8.96 ms: 1.00x slower                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.1 ms: 1.01x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.6 ms: 1.01x slower                                                       |
| pickle_list                | 4.59 us                                                      | 4.64 us: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.29 ms: 1.01x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| chaos                      | 61.7 ms                                                      | 62.6 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| pickle_dict                | 32.1 us                                                      | 32.7 us: 1.02x slower                                                       |
| unpickle_list              | 4.62 us                                                      | 4.73 us: 1.02x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.2 ms: 1.03x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 224 us: 1.05x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.59 sec: 1.08x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.87 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (14): mako, pycparser, logging_simple, thrift, async_generators, html5lib, xml_etree_generate, nqueens, xml_etree_iterparse, json_dumps, pprint_pformat, pylint, nbody, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x