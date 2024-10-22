# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                        |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.8 ms: 1.03x faster                                                       |
| float          | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                                       |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_dna      | 244 ms                                                       | 236 ms: 1.03x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.45 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.02x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 60.1 ms: 1.01x faster                                                       |
| unpickle             | 15.1 us                                                      | 15.0 us: 1.01x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| unpickle_list        | 4.62 us                                                      | 4.60 us: 1.00x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 322 us: 1.01x slower                                                        |
| pickle_list          | 4.59 us                                                      | 4.64 us: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                        |
| pickle_dict          | 32.1 us                                                      | 33.5 us: 1.04x slower                                                       |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.06x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.56 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 24.3 ms: 1.09x faster                                                       |
| genshi_xml     | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 286 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.1 us: 1.36x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| go                         | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.9 ms: 1.16x faster                                                       |
| unpack_sequence            | 56.8 ns                                                      | 49.6 ns: 1.15x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 24.3 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| scimark_fft                | 314 ms                                                       | 293 ms: 1.07x faster                                                        |
| raytrace                   | 289 ms                                                       | 270 ms: 1.07x faster                                                        |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.8 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.09 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.5 ms: 1.04x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 863 us: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                      |
| 2to3                       | 291 ms                                                       | 281 ms: 1.04x faster                                                        |
| regex_dna                  | 244 ms                                                       | 236 ms: 1.03x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.34 ms: 1.03x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 95.1 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.97 sec: 1.03x faster                                                      |
| nbody                      | 88.0 ms                                                      | 85.8 ms: 1.03x faster                                                       |
| thrift                     | 877 us                                                       | 857 us: 1.02x faster                                                        |
| scimark_sor                | 126 ms                                                       | 123 ms: 1.02x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.47 sec: 1.02x faster                                                      |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 171 us: 1.02x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.02x faster                                                        |
| float                      | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                                       |
| sympy_expand               | 505 ms                                                       | 497 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.8 ms: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.98 us: 1.01x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 60.1 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.79 us                                                      | 2.75 us: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| unpickle                   | 15.1 us                                                      | 15.0 us: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 803 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| unpickle_list              | 4.62 us                                                      | 4.60 us: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.00x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 6.36 ms: 1.00x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 88.7 ms: 1.01x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| chaos                      | 61.7 ms                                                      | 62.2 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 322 us: 1.01x slower                                                        |
| pickle_list                | 4.59 us                                                      | 4.64 us: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| coverage                   | 81.1 ms                                                      | 82.7 ms: 1.02x slower                                                       |
| pyflate                    | 492 ms                                                       | 503 ms: 1.02x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 67.0 ms: 1.02x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.45 ms: 1.02x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| pickle_dict                | 32.1 us                                                      | 33.5 us: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.06x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.8 ms: 1.06x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.56 sec: 1.06x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.09x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.65 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (15): logging_simple, mako, async_generators, deltablue, crypto_pyaes, python_startup_no_site, regex_v8, pprint_pformat, comprehensions, fannkuch, xml_etree_iterparse, django_template, json, pylint, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x