# Results vs. 3.13.0

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_io              | 847 ms                                                       | 804 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 369 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                       |
| float          | 81.9 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 233 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.2 ms: 1.00x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.45 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 59.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 221 us: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.57 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.07 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.7 ms: 1.08x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 55.2 ms: 1.04x faster                                                       |
| django_template | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 288 us: 1.38x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.5 us: 1.29x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                       |
| go                         | 160 ms                                                       | 134 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.7 ms: 1.17x faster                                                       |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 24.7 ms: 1.08x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.2 ms: 1.06x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 849 us: 1.06x faster                                                        |
| scimark_sor                | 126 ms                                                       | 119 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 804 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| raytrace                   | 289 ms                                                       | 276 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.4 ms: 1.05x faster                                                       |
| regex_dna                  | 244 ms                                                       | 233 ms: 1.05x faster                                                        |
| scimark_fft                | 314 ms                                                       | 301 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 55.2 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.93 sec: 1.03x faster                                                      |
| logging_format             | 7.07 us                                                      | 6.84 us: 1.03x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.30 ms: 1.03x faster                                                       |
| nbody                      | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.52 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.2 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| pyflate                    | 492 ms                                                       | 479 ms: 1.03x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 150 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 170 us: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                                        |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.02x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.26 us: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| sympy_expand               | 505 ms                                                       | 495 ms: 1.02x faster                                                        |
| coverage                   | 81.1 ms                                                      | 79.6 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.8 ms: 1.02x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.22 ms: 1.02x faster                                                       |
| fannkuch                   | 365 ms                                                       | 359 ms: 1.01x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| float                      | 81.9 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 59.1 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.9 ms: 1.01x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.30 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| regex_v8                   | 26.2 ms                                                      | 26.2 ms: 1.00x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.3 ms: 1.01x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.44 ms: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.27 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.01x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 89.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.07 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.45 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.5 ms: 1.02x slower                                                       |
| async_generators           | 359 ms                                                       | 369 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 221 us: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| django_template            | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.57 sec: 1.07x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.47 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (13): mako, pycparser, pprint_safe_repr, coroutines, json_dumps, thrift, pprint_pformat, comprehensions, pidigits, xml_etree_parse, logging_silent, chaos, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x