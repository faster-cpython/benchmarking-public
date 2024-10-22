# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 284 ms: 1.02x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 73.6 ms: 1.02x slower                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 772 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 541 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 800 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 364 ms: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                                       |
| nbody          | 88.0 ms                                                      | 86.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_dna      | 244 ms                                                       | 240 ms: 1.02x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.59 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads        | 2.41 sec                                                     | 2.27 sec: 1.06x faster                                                      |
| xml_etree_process  | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                                       |
| json_dumps         | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| pickle_pure_python | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_parse    | 145 ms                                                       | 143 ms: 1.02x faster                                                        |
| xml_etree_generate | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| json_loads         | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| Geometric mean     | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.4 ms: 1.05x faster                                                       |
| genshi_xml     | 57.3 ms                                                      | 55.0 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 285 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.3 us: 1.35x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.4 ms: 1.18x faster                                                       |
| scimark_sor                | 126 ms                                                       | 110 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| richards_super             | 59.8 ms                                                      | 55.4 ms: 1.08x faster                                                       |
| telco                      | 8.58 ms                                                      | 7.98 ms: 1.08x faster                                                       |
| raytrace                   | 289 ms                                                       | 269 ms: 1.07x faster                                                        |
| richards                   | 52.7 ms                                                      | 49.4 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 772 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 541 ms: 1.06x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.27 sec: 1.06x faster                                                      |
| async_tree_io              | 847 ms                                                       | 800 ms: 1.06x faster                                                        |
| scimark_fft                | 314 ms                                                       | 299 ms: 1.05x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.4 ms: 1.05x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 55.0 ms: 1.04x faster                                                       |
| coverage                   | 81.1 ms                                                      | 77.8 ms: 1.04x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 865 us: 1.04x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 94.1 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                      |
| deltablue                  | 3.41 ms                                                      | 3.31 ms: 1.03x faster                                                       |
| pyflate                    | 492 ms                                                       | 478 ms: 1.03x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| float                      | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.25 us: 1.02x faster                                                       |
| 2to3                       | 291 ms                                                       | 284 ms: 1.02x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.92 us: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| fannkuch                   | 365 ms                                                       | 357 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.4 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.3 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 5.01 sec: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.02x faster                                                        |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.02x faster                                                        |
| sympy_expand               | 505 ms                                                       | 497 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.22 ms: 1.01x faster                                                       |
| logging_silent             | 97.7 ns                                                      | 96.3 ns: 1.01x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| regex_v8                   | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| go                         | 160 ms                                                       | 158 ms: 1.01x faster                                                        |
| chaos                      | 61.7 ms                                                      | 61.0 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.1 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| sympy_str                  | 296 ms                                                       | 295 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.36 ms: 1.00x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.1 ms: 1.01x slower                                                       |
| async_generators           | 359 ms                                                       | 364 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.31 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                      |
| html5lib                   | 71.9 ms                                                      | 73.6 ms: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 90.9 ms: 1.03x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.59 ms: 1.07x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.48 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (16): comprehensions, unpickle_pure_python, sympy_sum, scimark_monte_carlo, meteor_contest, sqlglot_normalize, typing_runtime_protocols, thrift, pidigits, sqlglot_transpile, django_template, bench_mp_pool, pprint_safe_repr, pylint, mako, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x