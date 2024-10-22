# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 308 ms: 1.06x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.89 ms: 1.06x slower                                            |
| docutils       | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                           |
| tornado_http   | 120 ms                                                       | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                           |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                             |
| async_generators           | 359 ms                                                       | 372 ms: 1.04x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 710 ms: 1.18x slower                                             |
| async_tree_none            | 372 ms                                                       | 446 ms: 1.20x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 558 ms: 1.23x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 570 ms: 1.23x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 713 ms: 1.24x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.10 sec: 1.29x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 442 ms: 1.30x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.09 sec: 1.33x slower                                           |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 265 ms: 1.05x slower                                             |
| float          | 81.9 ms                                                      | 103 ms: 1.26x slower                                             |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                             |
| Geometric mean | (ref)                                                        | 1.23x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 240 ms: 1.01x faster                                             |
| regex_v8       | 26.2 ms                                                      | 26.4 ms: 1.01x slower                                            |
| regex_effbot   | 3.37 ms                                                      | 3.43 ms: 1.02x slower                                            |
| regex_compile  | 144 ms                                                       | 170 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.32 us: 1.06x faster                                            |
| pickle_dict          | 32.1 us                                                      | 30.7 us: 1.04x faster                                            |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                             |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                            |
| xml_etree_parse      | 145 ms                                                       | 146 ms: 1.01x slower                                             |
| xml_etree_process    | 60.9 ms                                                      | 62.3 ms: 1.02x slower                                            |
| unpickle_list        | 4.62 us                                                      | 4.74 us: 1.03x slower                                            |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.04x slower                                            |
| xml_etree_generate   | 85.3 ms                                                      | 90.9 ms: 1.07x slower                                            |
| unpickle_pure_python | 214 us                                                       | 245 us: 1.14x slower                                             |
| xml_etree_iterparse  | 100 ms                                                       | 117 ms: 1.17x slower                                             |
| tomli_loads          | 2.41 sec                                                     | 2.82 sec: 1.17x slower                                           |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.5 ms: 1.06x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.0 ms: 1.23x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.4 ms                                                      | 14.8 ms: 1.42x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 124 us: 1.40x faster                                             |
| unpack_sequence            | 56.8 ns                                                      | 44.2 ns: 1.28x faster                                            |
| mypy2                      | 1.05 sec                                                     | 893 ms: 1.18x faster                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.59 ms: 1.11x faster                                            |
| gc_traversal               | 4.11 ms                                                      | 3.74 ms: 1.10x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.32 us: 1.06x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.5 ms: 1.06x faster                                            |
| deepcopy                   | 397 us                                                       | 379 us: 1.05x faster                                             |
| pickle_dict                | 32.1 us                                                      | 30.7 us: 1.04x faster                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.41 us: 1.04x faster                                            |
| telco                      | 8.58 ms                                                      | 8.28 ms: 1.04x faster                                            |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                             |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.01x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                             |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                           |
| richards_super             | 59.8 ms                                                      | 60.0 ms: 1.00x slower                                            |
| sqlite_synth               | 2.79 us                                                      | 2.80 us: 1.01x slower                                            |
| regex_v8                   | 26.2 ms                                                      | 26.4 ms: 1.01x slower                                            |
| xml_etree_parse            | 145 ms                                                       | 146 ms: 1.01x slower                                             |
| coverage                   | 81.1 ms                                                      | 81.8 ms: 1.01x slower                                            |
| logging_silent             | 97.7 ns                                                      | 98.9 ns: 1.01x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.43 ms: 1.02x slower                                            |
| deepcopy_memo              | 39.5 us                                                      | 40.3 us: 1.02x slower                                            |
| xml_etree_process          | 60.9 ms                                                      | 62.3 ms: 1.02x slower                                            |
| json                       | 5.22 ms                                                      | 5.35 ms: 1.02x slower                                            |
| generators                 | 33.5 ms                                                      | 34.3 ms: 1.03x slower                                            |
| unpickle_list              | 4.62 us                                                      | 4.74 us: 1.03x slower                                            |
| tornado_http               | 120 ms                                                       | 123 ms: 1.03x slower                                             |
| richards                   | 52.7 ms                                                      | 54.5 ms: 1.03x slower                                            |
| async_generators           | 359 ms                                                       | 372 ms: 1.04x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                            |
| logging_format             | 7.07 us                                                      | 7.38 us: 1.04x slower                                            |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.04x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                           |
| mdp                        | 2.52 sec                                                     | 2.64 sec: 1.05x slower                                           |
| pidigits                   | 253 ms                                                       | 265 ms: 1.05x slower                                             |
| sqlglot_normalize          | 118 ms                                                       | 124 ms: 1.05x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.87 ms: 1.05x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.45 ms: 1.05x slower                                            |
| raytrace                   | 289 ms                                                       | 305 ms: 1.06x slower                                             |
| sympy_expand               | 505 ms                                                       | 534 ms: 1.06x slower                                             |
| 2to3                       | 291 ms                                                       | 308 ms: 1.06x slower                                             |
| chameleon                  | 7.42 ms                                                      | 7.89 ms: 1.06x slower                                            |
| sympy_integrate            | 23.3 ms                                                      | 24.8 ms: 1.06x slower                                            |
| xml_etree_generate         | 85.3 ms                                                      | 90.9 ms: 1.07x slower                                            |
| sqlglot_optimize           | 59.7 ms                                                      | 63.6 ms: 1.07x slower                                            |
| scimark_lu                 | 97.8 ms                                                      | 104 ms: 1.07x slower                                             |
| dask                       | 379 ms                                                       | 407 ms: 1.07x slower                                             |
| logging_simple             | 6.40 us                                                      | 6.88 us: 1.08x slower                                            |
| bench_thread_pool          | 901 us                                                       | 969 us: 1.08x slower                                             |
| meteor_contest             | 128 ms                                                       | 139 ms: 1.08x slower                                             |
| sympy_sum                  | 154 ms                                                       | 166 ms: 1.08x slower                                             |
| pycparser                  | 1.26 sec                                                     | 1.36 sec: 1.08x slower                                           |
| sympy_str                  | 296 ms                                                       | 322 ms: 1.09x slower                                             |
| pathlib                    | 17.4 ms                                                      | 19.1 ms: 1.10x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 72.1 ms: 1.10x slower                                            |
| go                         | 160 ms                                                       | 180 ms: 1.12x slower                                             |
| pprint_safe_repr           | 812 ms                                                       | 921 ms: 1.13x slower                                             |
| unpickle_pure_python       | 214 us                                                       | 245 us: 1.14x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.90 sec: 1.15x slower                                           |
| scimark_sor                | 126 ms                                                       | 147 ms: 1.17x slower                                             |
| xml_etree_iterparse        | 100 ms                                                       | 117 ms: 1.17x slower                                             |
| tomli_loads                | 2.41 sec                                                     | 2.82 sec: 1.17x slower                                           |
| regex_compile              | 144 ms                                                       | 170 ms: 1.18x slower                                             |
| pyflate                    | 492 ms                                                       | 582 ms: 1.18x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 710 ms: 1.18x slower                                             |
| crypto_pyaes               | 72.8 ms                                                      | 86.6 ms: 1.19x slower                                            |
| async_tree_none            | 372 ms                                                       | 446 ms: 1.20x slower                                             |
| nqueens                    | 88.2 ms                                                      | 108 ms: 1.22x slower                                             |
| python_startup_no_site     | 8.94 ms                                                      | 11.0 ms: 1.23x slower                                            |
| async_tree_memoization     | 452 ms                                                       | 558 ms: 1.23x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 570 ms: 1.23x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 713 ms: 1.24x slower                                             |
| chaos                      | 61.7 ms                                                      | 77.4 ms: 1.26x slower                                            |
| float                      | 81.9 ms                                                      | 103 ms: 1.26x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.10 sec: 1.29x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 442 ms: 1.30x slower                                             |
| fannkuch                   | 365 ms                                                       | 481 ms: 1.32x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.09 sec: 1.33x slower                                           |
| scimark_fft                | 314 ms                                                       | 429 ms: 1.37x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 88.7 ms: 1.37x slower                                            |
| mako                       | 10.4 ms                                                      | 14.8 ms: 1.42x slower                                            |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                             |
| comprehensions             | 17.3 us                                                      | 25.0 us: 1.45x slower                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 6.49 ms: 1.51x slower                                            |
| hexiom                     | 6.33 ms                                                      | 9.82 ms: 1.55x slower                                            |
| deltablue                  | 3.41 ms                                                      | 5.40 ms: 1.58x slower                                            |
| spectral_norm              | 97.4 ms                                                      | 161 ms: 1.65x slower                                             |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                     |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.96x