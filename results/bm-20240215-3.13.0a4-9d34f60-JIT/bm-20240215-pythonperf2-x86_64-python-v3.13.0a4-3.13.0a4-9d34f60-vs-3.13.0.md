# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 300 ms: 1.03x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.14 ms: 1.04x faster                                            |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.02x slower                                           |
| tornado_http   | 120 ms                                                       | 126 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                           |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                             |
| async_tree_none            | 372 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 701 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 549 ms: 1.19x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 548 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.08 sec: 1.27x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 438 ms: 1.29x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                            |
| pidigits       | 253 ms                                                       | 262 ms: 1.04x slower                                             |
| nbody          | 88.0 ms                                                      | 106 ms: 1.20x slower                                             |
| Geometric mean | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                            |
| regex_compile  | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.53 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                            |
| pickle_dict          | 32.1 us                                                      | 30.6 us: 1.05x faster                                            |
| pickle_pure_python   | 318 us                                                       | 304 us: 1.05x faster                                             |
| json_dumps           | 11.0 ms                                                      | 10.5 ms: 1.04x faster                                            |
| tomli_loads          | 2.41 sec                                                     | 2.31 sec: 1.04x faster                                           |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                            |
| xml_etree_generate   | 85.3 ms                                                      | 83.4 ms: 1.02x faster                                            |
| pickle_list          | 4.59 us                                                      | 4.50 us: 1.02x faster                                            |
| unpickle_list        | 4.62 us                                                      | 4.67 us: 1.01x slower                                            |
| unpickle             | 15.1 us                                                      | 15.3 us: 1.01x slower                                            |
| xml_etree_parse      | 145 ms                                                       | 148 ms: 1.02x slower                                             |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                             |
| json_loads           | 24.0 us                                                      | 25.6 us: 1.07x slower                                            |
| unpickle_pure_python | 214 us                                                       | 230 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.7 ms: 1.05x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.1 ms: 1.25x slower                                            |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.4 ms                                                      | 11.8 ms: 1.13x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 117 us: 1.48x faster                                             |
| unpack_sequence            | 56.8 ns                                                      | 46.9 ns: 1.21x faster                                            |
| mypy2                      | 1.05 sec                                                     | 886 ms: 1.18x faster                                             |
| gc_traversal               | 4.11 ms                                                      | 3.47 ms: 1.18x faster                                            |
| create_gc_cycles           | 1.76 ms                                                      | 1.55 ms: 1.14x faster                                            |
| deepcopy                   | 397 us                                                       | 370 us: 1.07x faster                                             |
| deepcopy_memo              | 39.5 us                                                      | 36.9 us: 1.07x faster                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.33 us: 1.06x faster                                            |
| xml_etree_process          | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                            |
| telco                      | 8.58 ms                                                      | 8.12 ms: 1.06x faster                                            |
| raytrace                   | 289 ms                                                       | 274 ms: 1.06x faster                                             |
| regex_v8                   | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                            |
| pickle_dict                | 32.1 us                                                      | 30.6 us: 1.05x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.7 ms: 1.05x faster                                            |
| pickle_pure_python         | 318 us                                                       | 304 us: 1.05x faster                                             |
| json_dumps                 | 11.0 ms                                                      | 10.5 ms: 1.04x faster                                            |
| tomli_loads                | 2.41 sec                                                     | 2.31 sec: 1.04x faster                                           |
| chameleon                  | 7.42 ms                                                      | 7.14 ms: 1.04x faster                                            |
| richards_super             | 59.8 ms                                                      | 57.6 ms: 1.04x faster                                            |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                            |
| xml_etree_generate         | 85.3 ms                                                      | 83.4 ms: 1.02x faster                                            |
| richards                   | 52.7 ms                                                      | 51.7 ms: 1.02x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.50 us: 1.02x faster                                            |
| float                      | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                            |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                             |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.01x faster                                             |
| sympy_expand               | 505 ms                                                       | 502 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                           |
| mdp                        | 2.52 sec                                                     | 2.53 sec: 1.00x slower                                           |
| regex_compile              | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| sympy_str                  | 296 ms                                                       | 298 ms: 1.01x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| unpickle_list              | 4.62 us                                                      | 4.67 us: 1.01x slower                                            |
| unpickle                   | 15.1 us                                                      | 15.3 us: 1.01x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                             |
| sqlglot_optimize           | 59.7 ms                                                      | 60.4 ms: 1.01x slower                                            |
| scimark_lu                 | 97.8 ms                                                      | 99.3 ms: 1.01x slower                                            |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                             |
| generators                 | 33.5 ms                                                      | 34.0 ms: 1.02x slower                                            |
| logging_format             | 7.07 us                                                      | 7.20 us: 1.02x slower                                            |
| pprint_safe_repr           | 812 ms                                                       | 826 ms: 1.02x slower                                             |
| logging_simple             | 6.40 us                                                      | 6.51 us: 1.02x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                            |
| sympy_integrate            | 23.3 ms                                                      | 23.9 ms: 1.02x slower                                            |
| xml_etree_parse            | 145 ms                                                       | 148 ms: 1.02x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.02x slower                                           |
| json                       | 5.22 ms                                                      | 5.35 ms: 1.02x slower                                            |
| sympy_sum                  | 154 ms                                                       | 158 ms: 1.03x slower                                             |
| 2to3                       | 291 ms                                                       | 300 ms: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                             |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                             |
| pidigits                   | 253 ms                                                       | 262 ms: 1.04x slower                                             |
| coverage                   | 81.1 ms                                                      | 84.4 ms: 1.04x slower                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.72 sec: 1.04x slower                                           |
| go                         | 160 ms                                                       | 167 ms: 1.04x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.53 ms: 1.05x slower                                            |
| tornado_http               | 120 ms                                                       | 126 ms: 1.05x slower                                             |
| bench_mp_pool              | 4.65 ms                                                      | 4.90 ms: 1.05x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 69.1 ms: 1.05x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.33 sec: 1.06x slower                                           |
| json_loads                 | 24.0 us                                                      | 25.6 us: 1.07x slower                                            |
| unpickle_pure_python       | 214 us                                                       | 230 us: 1.07x slower                                             |
| bench_thread_pool          | 901 us                                                       | 967 us: 1.07x slower                                             |
| pyflate                    | 492 ms                                                       | 529 ms: 1.08x slower                                             |
| deltablue                  | 3.41 ms                                                      | 3.69 ms: 1.08x slower                                            |
| nqueens                    | 88.2 ms                                                      | 95.4 ms: 1.08x slower                                            |
| crypto_pyaes               | 72.8 ms                                                      | 79.3 ms: 1.09x slower                                            |
| pathlib                    | 17.4 ms                                                      | 19.1 ms: 1.10x slower                                            |
| comprehensions             | 17.3 us                                                      | 19.3 us: 1.12x slower                                            |
| fannkuch                   | 365 ms                                                       | 409 ms: 1.12x slower                                             |
| chaos                      | 61.7 ms                                                      | 69.4 ms: 1.13x slower                                            |
| mako                       | 10.4 ms                                                      | 11.8 ms: 1.13x slower                                            |
| scimark_fft                | 314 ms                                                       | 357 ms: 1.14x slower                                             |
| scimark_sor                | 126 ms                                                       | 143 ms: 1.14x slower                                             |
| async_tree_none            | 372 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 701 ms: 1.17x slower                                             |
| spectral_norm              | 97.4 ms                                                      | 115 ms: 1.18x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 549 ms: 1.19x slower                                             |
| hexiom                     | 6.33 ms                                                      | 7.63 ms: 1.20x slower                                            |
| nbody                      | 88.0 ms                                                      | 106 ms: 1.20x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 78.5 ms: 1.21x slower                                            |
| async_tree_memoization     | 452 ms                                                       | 548 ms: 1.21x slower                                             |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.23 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| python_startup_no_site     | 8.94 ms                                                      | 11.1 ms: 1.25x slower                                            |
| async_tree_io              | 847 ms                                                       | 1.08 sec: 1.27x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 438 ms: 1.29x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.08 sec: 1.32x slower                                           |
| dask                       | 379 ms                                                       | 584 ms: 1.54x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                     |

Benchmark hidden because not significant (3): sqlite_synth, logging_silent, regex_dna
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.99x