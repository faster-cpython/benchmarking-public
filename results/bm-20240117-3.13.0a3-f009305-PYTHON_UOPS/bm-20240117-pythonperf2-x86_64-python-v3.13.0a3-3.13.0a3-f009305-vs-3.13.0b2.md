# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 308 ms: 1.06x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.89 ms: 1.07x slower                                            |
| docutils       | 2.98 sec                                                         | 2.94 sec: 1.02x faster                                           |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                            | 1.04x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 710 ms: 1.18x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.09 sec: 1.21x slower                                           |
| async_tree_memoization     | 460 ms                                                           | 558 ms: 1.21x slower                                             |
| async_tree_none            | 365 ms                                                           | 446 ms: 1.22x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 713 ms: 1.24x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.10 sec: 1.25x slower                                           |
| async_tree_none_tg         | 340 ms                                                           | 442 ms: 1.30x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 570 ms: 1.35x slower                                             |
| Geometric mean             | (ref)                                                            | 1.25x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 265 ms: 1.04x slower                                             |
| float          | 80.2 ms                                                          | 103 ms: 1.28x slower                                             |
| nbody          | 87.8 ms                                                          | 125 ms: 1.43x slower                                             |
| Geometric mean | (ref)                                                            | 1.24x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                             |
| regex_effbot   | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                            |
| regex_v8       | 26.0 ms                                                          | 26.4 ms: 1.01x slower                                            |
| regex_compile  | 144 ms                                                           | 170 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                            | 1.04x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.7 us: 1.07x faster                                            |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                            |
| pickle_list          | 4.44 us                                                          | 4.32 us: 1.03x faster                                            |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                            |
| unpickle_list        | 4.70 us                                                          | 4.74 us: 1.01x slower                                            |
| pickle_pure_python   | 307 us                                                           | 311 us: 1.01x slower                                             |
| xml_etree_parse      | 144 ms                                                           | 146 ms: 1.02x slower                                             |
| xml_etree_process    | 59.7 ms                                                          | 62.3 ms: 1.04x slower                                            |
| xml_etree_generate   | 85.7 ms                                                          | 90.9 ms: 1.06x slower                                            |
| unpickle_pure_python | 224 us                                                           | 245 us: 1.09x slower                                             |
| xml_etree_iterparse  | 103 ms                                                           | 117 ms: 1.14x slower                                             |
| tomli_loads          | 2.40 sec                                                         | 2.82 sec: 1.17x slower                                           |
| Geometric mean       | (ref)                                                            | 1.03x slower                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.5 ms: 1.05x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.0 ms: 1.25x slower                                            |
| Geometric mean         | (ref)                                                            | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.4 ms                                                          | 14.8 ms: 1.43x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 124 us: 1.38x faster                                             |
| create_gc_cycles           | 2.00 ms                                                          | 1.59 ms: 1.26x faster                                            |
| gc_traversal               | 4.69 ms                                                          | 3.74 ms: 1.25x faster                                            |
| pickle_dict                | 32.8 us                                                          | 30.7 us: 1.07x faster                                            |
| python_startup             | 13.2 ms                                                          | 12.5 ms: 1.05x faster                                            |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                            |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                             |
| pickle_list                | 4.44 us                                                          | 4.32 us: 1.03x faster                                            |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                            |
| coverage                   | 83.5 ms                                                          | 81.8 ms: 1.02x faster                                            |
| richards_super             | 61.2 ms                                                          | 60.0 ms: 1.02x faster                                            |
| docutils                   | 2.98 sec                                                         | 2.94 sec: 1.02x faster                                           |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.01x faster                                             |
| telco                      | 8.40 ms                                                          | 8.28 ms: 1.01x faster                                            |
| asyncio_tcp                | 378 ms                                                           | 375 ms: 1.01x faster                                             |
| sqlite_synth               | 2.80 us                                                          | 2.80 us: 1.00x slower                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.59 sec: 1.00x slower                                           |
| deepcopy_reduce            | 3.39 us                                                          | 3.41 us: 1.00x slower                                            |
| deepcopy                   | 377 us                                                           | 379 us: 1.01x slower                                             |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                            |
| regex_effbot               | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                            |
| unpickle_list              | 4.70 us                                                          | 4.74 us: 1.01x slower                                            |
| pickle_pure_python         | 307 us                                                           | 311 us: 1.01x slower                                             |
| regex_v8                   | 26.0 ms                                                          | 26.4 ms: 1.01x slower                                            |
| xml_etree_parse            | 144 ms                                                           | 146 ms: 1.02x slower                                             |
| richards                   | 53.4 ms                                                          | 54.5 ms: 1.02x slower                                            |
| generators                 | 33.5 ms                                                          | 34.3 ms: 1.02x slower                                            |
| coroutines                 | 22.0 ms                                                          | 22.5 ms: 1.03x slower                                            |
| async_generators           | 363 ms                                                           | 372 ms: 1.03x slower                                             |
| logging_silent             | 96.3 ns                                                          | 98.9 ns: 1.03x slower                                            |
| sqlglot_normalize          | 120 ms                                                           | 124 ms: 1.03x slower                                             |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                             |
| logging_format             | 7.11 us                                                          | 7.38 us: 1.04x slower                                            |
| dask                       | 391 ms                                                           | 407 ms: 1.04x slower                                             |
| xml_etree_process          | 59.7 ms                                                          | 62.3 ms: 1.04x slower                                            |
| pidigits                   | 254 ms                                                           | 265 ms: 1.04x slower                                             |
| sqlglot_parse              | 1.39 ms                                                          | 1.45 ms: 1.04x slower                                            |
| 2to3                       | 291 ms                                                           | 308 ms: 1.06x slower                                             |
| xml_etree_generate         | 85.7 ms                                                          | 90.9 ms: 1.06x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                          | 1.87 ms: 1.06x slower                                            |
| sympy_expand               | 501 ms                                                           | 534 ms: 1.07x slower                                             |
| chameleon                  | 7.40 ms                                                          | 7.89 ms: 1.07x slower                                            |
| bench_thread_pool          | 908 us                                                           | 969 us: 1.07x slower                                             |
| sqlglot_optimize           | 59.5 ms                                                          | 63.6 ms: 1.07x slower                                            |
| dulwich_log                | 67.3 ms                                                          | 72.1 ms: 1.07x slower                                            |
| sympy_integrate            | 23.2 ms                                                          | 24.8 ms: 1.07x slower                                            |
| scimark_lu                 | 97.5 ms                                                          | 104 ms: 1.07x slower                                             |
| mdp                        | 2.46 sec                                                         | 2.64 sec: 1.07x slower                                           |
| logging_simple             | 6.40 us                                                          | 6.88 us: 1.07x slower                                            |
| sympy_sum                  | 155 ms                                                           | 166 ms: 1.07x slower                                             |
| deepcopy_memo              | 37.3 us                                                          | 40.3 us: 1.08x slower                                            |
| meteor_contest             | 128 ms                                                           | 139 ms: 1.08x slower                                             |
| unpickle_pure_python       | 224 us                                                           | 245 us: 1.09x slower                                             |
| go                         | 165 ms                                                           | 180 ms: 1.09x slower                                             |
| sympy_str                  | 295 ms                                                           | 322 ms: 1.09x slower                                             |
| pycparser                  | 1.22 sec                                                         | 1.36 sec: 1.11x slower                                           |
| pathlib                    | 17.1 ms                                                          | 19.1 ms: 1.12x slower                                            |
| pprint_safe_repr           | 818 ms                                                           | 921 ms: 1.13x slower                                             |
| xml_etree_iterparse        | 103 ms                                                           | 117 ms: 1.14x slower                                             |
| pprint_pformat             | 1.66 sec                                                         | 1.90 sec: 1.14x slower                                           |
| mypy2                      | 764 ms                                                           | 893 ms: 1.17x slower                                             |
| raytrace                   | 260 ms                                                           | 305 ms: 1.17x slower                                             |
| tomli_loads                | 2.40 sec                                                         | 2.82 sec: 1.17x slower                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 710 ms: 1.18x slower                                             |
| crypto_pyaes               | 73.6 ms                                                          | 86.6 ms: 1.18x slower                                            |
| regex_compile              | 144 ms                                                           | 170 ms: 1.18x slower                                             |
| pyflate                    | 482 ms                                                           | 582 ms: 1.21x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.09 sec: 1.21x slower                                           |
| async_tree_memoization     | 460 ms                                                           | 558 ms: 1.21x slower                                             |
| nqueens                    | 88.4 ms                                                          | 108 ms: 1.22x slower                                             |
| async_tree_none            | 365 ms                                                           | 446 ms: 1.22x slower                                             |
| scimark_sor                | 119 ms                                                           | 147 ms: 1.24x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 713 ms: 1.24x slower                                             |
| python_startup_no_site     | 8.85 ms                                                          | 11.0 ms: 1.25x slower                                            |
| async_tree_io              | 873 ms                                                           | 1.10 sec: 1.25x slower                                           |
| float                      | 80.2 ms                                                          | 103 ms: 1.28x slower                                             |
| async_tree_none_tg         | 340 ms                                                           | 442 ms: 1.30x slower                                             |
| chaos                      | 59.6 ms                                                          | 77.4 ms: 1.30x slower                                            |
| scimark_monte_carlo        | 65.5 ms                                                          | 88.7 ms: 1.35x slower                                            |
| async_tree_memoization_tg  | 421 ms                                                           | 570 ms: 1.35x slower                                             |
| fannkuch                   | 353 ms                                                           | 481 ms: 1.36x slower                                             |
| scimark_fft                | 312 ms                                                           | 429 ms: 1.37x slower                                             |
| mako                       | 10.4 ms                                                          | 14.8 ms: 1.43x slower                                            |
| nbody                      | 87.8 ms                                                          | 125 ms: 1.43x slower                                             |
| comprehensions             | 17.0 us                                                          | 25.0 us: 1.47x slower                                            |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.49 ms: 1.52x slower                                            |
| hexiom                     | 6.35 ms                                                          | 9.82 ms: 1.55x slower                                            |
| deltablue                  | 3.37 ms                                                          | 5.40 ms: 1.60x slower                                            |
| spectral_norm              | 97.3 ms                                                          | 161 ms: 1.65x slower                                             |
| Geometric mean             | (ref)                                                            | 1.10x slower                                                     |

Benchmark hidden because not significant (3): bench_mp_pool, json, json_loads
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.95x