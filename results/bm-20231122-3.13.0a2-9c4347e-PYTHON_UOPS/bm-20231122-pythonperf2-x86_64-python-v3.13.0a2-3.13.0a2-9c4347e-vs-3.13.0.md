# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 311 ms: 1.07x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.90 ms: 1.06x slower                                            |
| docutils       | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                           |
| tornado_http   | 120 ms                                                       | 124 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 373 ms: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                           |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| async_generators           | 359 ms                                                       | 377 ms: 1.05x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 711 ms: 1.19x slower                                             |
| async_tree_none            | 372 ms                                                       | 447 ms: 1.20x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 561 ms: 1.24x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 725 ms: 1.26x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 586 ms: 1.27x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.09 sec: 1.29x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 453 ms: 1.33x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.11 sec: 1.36x slower                                           |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 267 ms: 1.06x slower                                             |
| float          | 81.9 ms                                                      | 92.5 ms: 1.13x slower                                            |
| nbody          | 88.0 ms                                                      | 112 ms: 1.27x slower                                             |
| Geometric mean | (ref)                                                        | 1.15x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                            |
| regex_dna      | 244 ms                                                       | 249 ms: 1.02x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                            |
| regex_compile  | 144 ms                                                       | 172 ms: 1.19x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.27 us: 1.07x faster                                            |
| pickle               | 10.5 us                                                      | 9.98 us: 1.06x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                            |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                             |
| unpickle_list        | 4.62 us                                                      | 4.56 us: 1.01x faster                                            |
| pickle_dict          | 32.1 us                                                      | 31.8 us: 1.01x faster                                            |
| xml_etree_generate   | 85.3 ms                                                      | 90.1 ms: 1.06x slower                                            |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.06x slower                                            |
| unpickle_pure_python | 214 us                                                       | 231 us: 1.08x slower                                             |
| tomli_loads          | 2.41 sec                                                     | 2.61 sec: 1.08x slower                                           |
| xml_etree_parse      | 145 ms                                                       | 157 ms: 1.09x slower                                             |
| xml_etree_iterparse  | 100 ms                                                       | 117 ms: 1.17x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.9 ms: 1.03x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.3 ms: 1.27x slower                                            |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.4 ms                                                      | 13.6 ms: 1.31x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpack_sequence            | 56.8 ns                                                      | 43.3 ns: 1.31x faster                                            |
| typing_runtime_protocols   | 174 us                                                       | 133 us: 1.31x faster                                             |
| mypy2                      | 1.05 sec                                                     | 893 ms: 1.17x faster                                             |
| gc_traversal               | 4.11 ms                                                      | 3.76 ms: 1.09x faster                                            |
| create_gc_cycles           | 1.76 ms                                                      | 1.61 ms: 1.09x faster                                            |
| deepcopy                   | 397 us                                                       | 366 us: 1.08x faster                                             |
| pickle_list                | 4.59 us                                                      | 4.27 us: 1.07x faster                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.35 us: 1.06x faster                                            |
| pickle                     | 10.5 us                                                      | 9.98 us: 1.06x faster                                            |
| regex_v8                   | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.9 ms: 1.03x faster                                            |
| coverage                   | 81.1 ms                                                      | 78.8 ms: 1.03x faster                                            |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                            |
| richards_super             | 59.8 ms                                                      | 58.4 ms: 1.02x faster                                            |
| deepcopy_memo              | 39.5 us                                                      | 38.6 us: 1.02x faster                                            |
| richards                   | 52.7 ms                                                      | 51.6 ms: 1.02x faster                                            |
| asyncio_tcp                | 380 ms                                                       | 373 ms: 1.02x faster                                             |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                             |
| unpickle_list              | 4.62 us                                                      | 4.56 us: 1.01x faster                                            |
| telco                      | 8.58 ms                                                      | 8.47 ms: 1.01x faster                                            |
| pickle_dict                | 32.1 us                                                      | 31.8 us: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                           |
| logging_silent             | 97.7 ns                                                      | 98.7 ns: 1.01x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                             |
| json                       | 5.22 ms                                                      | 5.30 ms: 1.01x slower                                            |
| sqlite_synth               | 2.79 us                                                      | 2.83 us: 1.02x slower                                            |
| regex_dna                  | 244 ms                                                       | 249 ms: 1.02x slower                                             |
| tornado_http               | 120 ms                                                       | 124 ms: 1.03x slower                                             |
| raytrace                   | 289 ms                                                       | 299 ms: 1.04x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                            |
| mdp                        | 2.52 sec                                                     | 2.63 sec: 1.04x slower                                           |
| docutils                   | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                           |
| generators                 | 33.5 ms                                                      | 35.0 ms: 1.04x slower                                            |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| logging_format             | 7.07 us                                                      | 7.40 us: 1.05x slower                                            |
| sqlglot_normalize          | 118 ms                                                       | 124 ms: 1.05x slower                                             |
| async_generators           | 359 ms                                                       | 377 ms: 1.05x slower                                             |
| xml_etree_generate         | 85.3 ms                                                      | 90.1 ms: 1.06x slower                                            |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.06x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.33 sec: 1.06x slower                                           |
| pidigits                   | 253 ms                                                       | 267 ms: 1.06x slower                                             |
| sqlglot_optimize           | 59.7 ms                                                      | 63.2 ms: 1.06x slower                                            |
| sympy_expand               | 505 ms                                                       | 535 ms: 1.06x slower                                             |
| logging_simple             | 6.40 us                                                      | 6.80 us: 1.06x slower                                            |
| chameleon                  | 7.42 ms                                                      | 7.90 ms: 1.06x slower                                            |
| meteor_contest             | 128 ms                                                       | 137 ms: 1.07x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.90 ms: 1.07x slower                                            |
| sympy_integrate            | 23.3 ms                                                      | 24.9 ms: 1.07x slower                                            |
| 2to3                       | 291 ms                                                       | 311 ms: 1.07x slower                                             |
| scimark_lu                 | 97.8 ms                                                      | 105 ms: 1.07x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                            |
| unpickle_pure_python       | 214 us                                                       | 231 us: 1.08x slower                                             |
| tomli_loads                | 2.41 sec                                                     | 2.61 sec: 1.08x slower                                           |
| dask                       | 379 ms                                                       | 411 ms: 1.08x slower                                             |
| pprint_safe_repr           | 812 ms                                                       | 880 ms: 1.08x slower                                             |
| xml_etree_parse            | 145 ms                                                       | 157 ms: 1.09x slower                                             |
| sympy_sum                  | 154 ms                                                       | 167 ms: 1.09x slower                                             |
| sympy_str                  | 296 ms                                                       | 322 ms: 1.09x slower                                             |
| bench_thread_pool          | 901 us                                                       | 985 us: 1.09x slower                                             |
| dulwich_log                | 65.5 ms                                                      | 72.0 ms: 1.10x slower                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.81 sec: 1.10x slower                                           |
| pathlib                    | 17.4 ms                                                      | 19.3 ms: 1.11x slower                                            |
| crypto_pyaes               | 72.8 ms                                                      | 80.6 ms: 1.11x slower                                            |
| go                         | 160 ms                                                       | 179 ms: 1.12x slower                                             |
| float                      | 81.9 ms                                                      | 92.5 ms: 1.13x slower                                            |
| pyflate                    | 492 ms                                                       | 557 ms: 1.13x slower                                             |
| xml_etree_iterparse        | 100 ms                                                       | 117 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 711 ms: 1.19x slower                                             |
| scimark_sor                | 126 ms                                                       | 149 ms: 1.19x slower                                             |
| chaos                      | 61.7 ms                                                      | 73.3 ms: 1.19x slower                                            |
| regex_compile              | 144 ms                                                       | 172 ms: 1.19x slower                                             |
| nqueens                    | 88.2 ms                                                      | 105 ms: 1.19x slower                                             |
| async_tree_none            | 372 ms                                                       | 447 ms: 1.20x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 561 ms: 1.24x slower                                             |
| fannkuch                   | 365 ms                                                       | 453 ms: 1.24x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 725 ms: 1.26x slower                                             |
| python_startup_no_site     | 8.94 ms                                                      | 11.3 ms: 1.27x slower                                            |
| async_tree_memoization_tg  | 461 ms                                                       | 586 ms: 1.27x slower                                             |
| nbody                      | 88.0 ms                                                      | 112 ms: 1.27x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.09 sec: 1.29x slower                                           |
| scimark_fft                | 314 ms                                                       | 407 ms: 1.29x slower                                             |
| mako                       | 10.4 ms                                                      | 13.6 ms: 1.31x slower                                            |
| async_tree_none_tg         | 340 ms                                                       | 453 ms: 1.33x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 87.4 ms: 1.35x slower                                            |
| comprehensions             | 17.3 us                                                      | 23.3 us: 1.35x slower                                            |
| async_tree_io_tg           | 819 ms                                                       | 1.11 sec: 1.36x slower                                           |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 6.01 ms: 1.40x slower                                            |
| hexiom                     | 6.33 ms                                                      | 9.10 ms: 1.44x slower                                            |
| deltablue                  | 3.41 ms                                                      | 4.98 ms: 1.46x slower                                            |
| spectral_norm              | 97.4 ms                                                      | 144 ms: 1.48x slower                                             |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                     |

Benchmark hidden because not significant (3): xml_etree_process, unpickle, bench_mp_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.95x