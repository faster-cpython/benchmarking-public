# Results vs. 3.13.0

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-x86_64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.96 sec: 1.05x slower                                                      |
| html5lib       | 71.9 ms                                                      | 75.1 ms: 1.04x slower                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                        |
| async_tree_io              | 847 ms                                                       | 807 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 369 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.9 ms: 1.04x faster                                                       |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| nbody          | 88.0 ms                                                      | 90.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.54 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.7 ms: 1.08x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 55.1 ms: 1.04x faster                                                       |
| django_template | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 290 us: 1.37x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.2 us: 1.35x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.6 ms: 1.17x faster                                                       |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                        |
| scimark_sor                | 126 ms                                                       | 116 ms: 1.08x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 24.7 ms: 1.08x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 852 us: 1.06x faster                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.41 ms: 1.06x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.8 ms: 1.05x faster                                                       |
| async_tree_io              | 847 ms                                                       | 807 ms: 1.05x faster                                                        |
| scimark_fft                | 314 ms                                                       | 300 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.87 sec: 1.05x faster                                                      |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.5 ms: 1.04x faster                                                       |
| raytrace                   | 289 ms                                                       | 277 ms: 1.04x faster                                                        |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 55.1 ms: 1.04x faster                                                       |
| float                      | 81.9 ms                                                      | 78.9 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.0 ms: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.03x faster                                                      |
| telco                      | 8.58 ms                                                      | 8.39 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.4 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 171 us: 1.02x faster                                                        |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.97 us: 1.02x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.24 ms: 1.01x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.31 us: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.23 ms: 1.01x faster                                                       |
| fannkuch                   | 365 ms                                                       | 361 ms: 1.01x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| deltablue                  | 3.41 ms                                                      | 3.38 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 501 ms: 1.01x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                                       |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 118 ms                                                       | 118 ms: 1.01x faster                                                        |
| chaos                      | 61.7 ms                                                      | 61.4 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 808 ms: 1.00x faster                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 72.5 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| pyflate                    | 492 ms                                                       | 498 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.5 us: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 369 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 90.7 ms: 1.03x slower                                                       |
| coverage                   | 81.1 ms                                                      | 84.2 ms: 1.04x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 91.8 ms: 1.04x slower                                                       |
| json                       | 5.22 ms                                                      | 5.44 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 75.1 ms: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.96 sec: 1.05x slower                                                      |
| tomli_loads                | 2.41 sec                                                     | 2.54 sec: 1.06x slower                                                      |
| django_template            | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.48 ms: 1.09x slower                                                       |
| go                         | 160 ms                                                       | 180 ms: 1.12x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (7): mako, xml_etree_parse, thrift, logging_silent, scimark_monte_carlo, xml_etree_iterparse, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x