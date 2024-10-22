# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.2 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 569 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 791 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 370 ms: 1.03x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (2): coroutines, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.0 ms: 1.02x faster                                                       |
| nbody          | 88.0 ms                                                      | 91.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 232 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 60.0 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 86.3 ms: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.57 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 55.2 ms: 1.04x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                                       |
| django_template | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 288 us: 1.38x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.5 us: 1.34x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                        |
| go                         | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                      | 29.4 ms: 1.14x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| raytrace                   | 289 ms                                                       | 268 ms: 1.08x faster                                                        |
| scimark_sor                | 126 ms                                                       | 118 ms: 1.07x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.4 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 569 ms: 1.05x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.2 ms: 1.05x faster                                                       |
| regex_dna                  | 244 ms                                                       | 232 ms: 1.05x faster                                                        |
| scimark_fft                | 314 ms                                                       | 300 ms: 1.05x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.21 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.88 sec: 1.04x faster                                                      |
| bench_thread_pool          | 901 us                                                       | 864 us: 1.04x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 55.2 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 791 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| pyflate                    | 492 ms                                                       | 476 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 94.8 ms: 1.03x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.86 us: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.16 ms: 1.03x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 370 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.03x faster                                                        |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                        |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.02x faster                                                        |
| thrift                     | 877 us                                                       | 856 us: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 70.2 ms: 1.02x faster                                                       |
| float                      | 81.9 ms                                                      | 80.0 ms: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.26 us: 1.02x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.47 sec: 1.02x faster                                                      |
| hexiom                     | 6.33 ms                                                      | 6.21 ms: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| sympy_expand               | 505 ms                                                       | 496 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 60.0 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 801 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.01x faster                                                      |
| fannkuch                   | 365 ms                                                       | 362 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 59.3 ms: 1.01x faster                                                       |
| nqueens                    | 88.2 ms                                                      | 87.8 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.8 ms: 1.00x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.43 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.28 ms: 1.01x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 86.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.02x slower                                                        |
| coverage                   | 81.1 ms                                                      | 82.6 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 91.4 ms: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.05x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.57 sec: 1.07x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.43 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (13): logging_silent, spectral_norm, pprint_pformat, mako, crypto_pyaes, pidigits, coroutines, chaos, async_generators, xml_etree_parse, bench_mp_pool, pylint, regex_v8
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x