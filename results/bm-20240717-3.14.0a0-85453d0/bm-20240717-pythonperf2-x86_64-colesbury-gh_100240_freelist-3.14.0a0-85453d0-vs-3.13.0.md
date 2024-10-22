# Results vs. 3.13.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 286 ms: 1.02x faster                                                         |
| docutils       | 2.81 sec                                                     | 2.95 sec: 1.05x slower                                                       |
| html5lib       | 71.9 ms                                                      | 73.8 ms: 1.03x slower                                                        |
| tornado_http   | 120 ms                                                       | 118 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                         |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                         |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                         |
| async_tree_none            | 372 ms                                                       | 334 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 533 ms: 1.08x faster                                                         |
| async_tree_io_tg           | 819 ms                                                       | 769 ms: 1.06x faster                                                         |
| async_tree_io              | 847 ms                                                       | 797 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                         |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                         |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| asyncio_websockets         | 382 ms                                                       | 388 ms: 1.01x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                        |
| pidigits       | 253 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.1 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| regex_dna      | 244 ms                                                       | 240 ms: 1.02x faster                                                         |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 140 ms: 1.04x faster                                                         |
| xml_etree_process    | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                        |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 83.0 ms: 1.03x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 212 us: 1.01x faster                                                         |
| tomli_loads          | 2.41 sec                                                     | 2.45 sec: 1.02x slower                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                         |
| json_loads           | 24.0 us                                                      | 25.5 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                        |
| genshi_xml     | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 282 us: 1.41x faster                                                         |
| deepcopy_memo              | 39.5 us                                                      | 29.3 us: 1.35x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.87 us: 1.24x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                         |
| scimark_sor                | 126 ms                                                       | 107 ms: 1.18x faster                                                         |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                         |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                         |
| async_tree_none            | 372 ms                                                       | 334 ms: 1.11x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                        |
| raytrace                   | 289 ms                                                       | 267 ms: 1.08x faster                                                         |
| telco                      | 8.58 ms                                                      | 7.94 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 533 ms: 1.08x faster                                                         |
| async_tree_io_tg           | 819 ms                                                       | 769 ms: 1.06x faster                                                         |
| async_tree_io              | 847 ms                                                       | 797 ms: 1.06x faster                                                         |
| scimark_fft                | 314 ms                                                       | 296 ms: 1.06x faster                                                         |
| genshi_text                | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.87 sec: 1.05x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.1 ms: 1.04x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 864 us: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.11 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                         |
| xml_etree_parse            | 145 ms                                                       | 140 ms: 1.04x faster                                                         |
| pyflate                    | 492 ms                                                       | 476 ms: 1.03x faster                                                         |
| xml_etree_process          | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.84 us: 1.03x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 169 us: 1.03x faster                                                         |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                         |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 83.0 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.4 ms: 1.03x faster                                                        |
| richards                   | 52.7 ms                                                      | 51.7 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.7 ms: 1.02x faster                                                        |
| tornado_http               | 120 ms                                                       | 118 ms: 1.02x faster                                                         |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                         |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.02x faster                                                         |
| 2to3                       | 291 ms                                                       | 286 ms: 1.02x faster                                                         |
| crypto_pyaes               | 72.8 ms                                                      | 71.7 ms: 1.02x faster                                                        |
| chaos                      | 61.7 ms                                                      | 60.8 ms: 1.01x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.1 ms: 1.01x faster                                                        |
| fannkuch                   | 365 ms                                                       | 360 ms: 1.01x faster                                                         |
| logging_simple             | 6.40 us                                                      | 6.32 us: 1.01x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.26 ms: 1.01x faster                                                        |
| sympy_str                  | 296 ms                                                       | 292 ms: 1.01x faster                                                         |
| unpickle_pure_python       | 214 us                                                       | 212 us: 1.01x faster                                                         |
| sympy_expand               | 505 ms                                                       | 500 ms: 1.01x faster                                                         |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 23.1 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 805 ms: 1.01x faster                                                         |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                                         |
| mdp                        | 2.52 sec                                                     | 2.51 sec: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| generators                 | 33.5 ms                                                      | 33.5 ms: 1.00x slower                                                        |
| pidigits                   | 253 ms                                                       | 254 ms: 1.01x slower                                                         |
| python_startup_no_site     | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 3.46 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 388 ms: 1.01x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.45 sec: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.8 ms: 1.02x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 66.7 ms: 1.02x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 99.6 ns: 1.02x slower                                                        |
| go                         | 160 ms                                                       | 164 ms: 1.02x slower                                                         |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                         |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.6 ms: 1.03x slower                                                        |
| coverage                   | 81.1 ms                                                      | 83.2 ms: 1.03x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 73.8 ms: 1.03x slower                                                        |
| json                       | 5.22 ms                                                      | 5.42 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.95 sec: 1.05x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.5 us: 1.06x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.47 ms: 1.09x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (11): pylint, richards_super, sqlglot_normalize, float, python_startup, thrift, async_generators, django_template, pickle_pure_python, bench_mp_pool, mako
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x