# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 300 ms: 1.03x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.14 ms: 1.04x faster                                            |
| docutils       | 2.98 sec                                                         | 2.88 sec: 1.04x faster                                           |
| tornado_http   | 119 ms                                                           | 126 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                            | 1.00x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 701 ms: 1.16x slower                                             |
| async_tree_none            | 365 ms                                                           | 434 ms: 1.19x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 548 ms: 1.19x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.08 sec: 1.20x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 706 ms: 1.23x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.08 sec: 1.23x slower                                           |
| async_tree_none_tg         | 340 ms                                                           | 438 ms: 1.29x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 549 ms: 1.31x slower                                             |
| Geometric mean             | (ref)                                                            | 1.22x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 80.7 ms: 1.01x slower                                            |
| pidigits       | 254 ms                                                           | 262 ms: 1.03x slower                                             |
| nbody          | 87.8 ms                                                          | 106 ms: 1.21x slower                                             |
| Geometric mean | (ref)                                                            | 1.08x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                            |
| regex_dna      | 249 ms                                                           | 244 ms: 1.02x faster                                             |
| regex_compile  | 144 ms                                                           | 145 ms: 1.01x slower                                             |
| regex_effbot   | 3.40 ms                                                          | 3.53 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.6 us: 1.07x faster                                            |
| tomli_loads          | 2.40 sec                                                         | 2.31 sec: 1.04x faster                                           |
| xml_etree_process    | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                            |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                            |
| xml_etree_generate   | 85.7 ms                                                          | 83.4 ms: 1.03x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                            |
| unpickle             | 15.7 us                                                          | 15.3 us: 1.02x faster                                            |
| pickle_pure_python   | 307 us                                                           | 304 us: 1.01x faster                                             |
| xml_etree_iterparse  | 103 ms                                                           | 103 ms: 1.01x slower                                             |
| pickle_list          | 4.44 us                                                          | 4.50 us: 1.01x slower                                            |
| json_loads           | 25.0 us                                                          | 25.6 us: 1.02x slower                                            |
| unpickle_pure_python | 224 us                                                           | 230 us: 1.02x slower                                             |
| xml_etree_parse      | 144 ms                                                           | 148 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.7 ms: 1.04x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.1 ms: 1.26x slower                                            |
| Geometric mean         | (ref)                                                            | 1.10x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.4 ms                                                          | 11.8 ms: 1.13x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 117 us: 1.46x faster                                             |
| gc_traversal               | 4.69 ms                                                          | 3.47 ms: 1.35x faster                                            |
| create_gc_cycles           | 2.00 ms                                                          | 1.55 ms: 1.30x faster                                            |
| pickle_dict                | 32.8 us                                                          | 30.6 us: 1.07x faster                                            |
| richards_super             | 61.2 ms                                                          | 57.6 ms: 1.06x faster                                            |
| regex_v8                   | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                            |
| tomli_loads                | 2.40 sec                                                         | 2.31 sec: 1.04x faster                                           |
| python_startup             | 13.2 ms                                                          | 12.7 ms: 1.04x faster                                            |
| xml_etree_process          | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                            |
| docutils                   | 2.98 sec                                                         | 2.88 sec: 1.04x faster                                           |
| pickle                     | 10.6 us                                                          | 10.2 us: 1.04x faster                                            |
| chameleon                  | 7.40 ms                                                          | 7.14 ms: 1.04x faster                                            |
| richards                   | 53.4 ms                                                          | 51.7 ms: 1.03x faster                                            |
| telco                      | 8.40 ms                                                          | 8.12 ms: 1.03x faster                                            |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                             |
| xml_etree_generate         | 85.7 ms                                                          | 83.4 ms: 1.03x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                            |
| unpickle                   | 15.7 us                                                          | 15.3 us: 1.02x faster                                            |
| regex_dna                  | 249 ms                                                           | 244 ms: 1.02x faster                                             |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                             |
| deepcopy                   | 377 us                                                           | 370 us: 1.02x faster                                             |
| deepcopy_reduce            | 3.39 us                                                          | 3.33 us: 1.02x faster                                            |
| pickle_pure_python         | 307 us                                                           | 304 us: 1.01x faster                                             |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                             |
| deepcopy_memo              | 37.3 us                                                          | 36.9 us: 1.01x faster                                            |
| sqlite_synth               | 2.80 us                                                          | 2.77 us: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                           |
| float                      | 80.2 ms                                                          | 80.7 ms: 1.01x slower                                            |
| regex_compile              | 144 ms                                                           | 145 ms: 1.01x slower                                             |
| xml_etree_iterparse        | 103 ms                                                           | 103 ms: 1.01x slower                                             |
| sympy_str                  | 295 ms                                                           | 298 ms: 1.01x slower                                             |
| pprint_safe_repr           | 818 ms                                                           | 826 ms: 1.01x slower                                             |
| coverage                   | 83.5 ms                                                          | 84.4 ms: 1.01x slower                                            |
| logging_format             | 7.11 us                                                          | 7.20 us: 1.01x slower                                            |
| coroutines                 | 22.0 ms                                                          | 22.3 ms: 1.01x slower                                            |
| pickle_list                | 4.44 us                                                          | 4.50 us: 1.01x slower                                            |
| go                         | 165 ms                                                           | 167 ms: 1.01x slower                                             |
| sqlglot_optimize           | 59.5 ms                                                          | 60.4 ms: 1.01x slower                                            |
| logging_silent             | 96.3 ns                                                          | 97.7 ns: 1.01x slower                                            |
| generators                 | 33.5 ms                                                          | 34.0 ms: 1.02x slower                                            |
| meteor_contest             | 128 ms                                                           | 130 ms: 1.02x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.51 us: 1.02x slower                                            |
| sympy_sum                  | 155 ms                                                           | 158 ms: 1.02x slower                                             |
| scimark_lu                 | 97.5 ms                                                          | 99.3 ms: 1.02x slower                                            |
| json_loads                 | 25.0 us                                                          | 25.6 us: 1.02x slower                                            |
| unpickle_pure_python       | 224 us                                                           | 230 us: 1.02x slower                                             |
| async_generators           | 363 ms                                                           | 371 ms: 1.02x slower                                             |
| dulwich_log                | 67.3 ms                                                          | 69.1 ms: 1.03x slower                                            |
| 2to3                       | 291 ms                                                           | 300 ms: 1.03x slower                                             |
| mdp                        | 2.46 sec                                                         | 2.53 sec: 1.03x slower                                           |
| sqlglot_transpile          | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                            |
| sympy_integrate            | 23.2 ms                                                          | 23.9 ms: 1.03x slower                                            |
| xml_etree_parse            | 144 ms                                                           | 148 ms: 1.03x slower                                             |
| pidigits                   | 254 ms                                                           | 262 ms: 1.03x slower                                             |
| pprint_pformat             | 1.66 sec                                                         | 1.72 sec: 1.03x slower                                           |
| regex_effbot               | 3.40 ms                                                          | 3.53 ms: 1.04x slower                                            |
| raytrace                   | 260 ms                                                           | 274 ms: 1.05x slower                                             |
| tornado_http               | 119 ms                                                           | 126 ms: 1.05x slower                                             |
| bench_thread_pool          | 908 us                                                           | 967 us: 1.07x slower                                             |
| crypto_pyaes               | 73.6 ms                                                          | 79.3 ms: 1.08x slower                                            |
| nqueens                    | 88.4 ms                                                          | 95.4 ms: 1.08x slower                                            |
| pycparser                  | 1.22 sec                                                         | 1.33 sec: 1.09x slower                                           |
| deltablue                  | 3.37 ms                                                          | 3.69 ms: 1.09x slower                                            |
| pyflate                    | 482 ms                                                           | 529 ms: 1.10x slower                                             |
| pathlib                    | 17.1 ms                                                          | 19.1 ms: 1.12x slower                                            |
| mako                       | 10.4 ms                                                          | 11.8 ms: 1.13x slower                                            |
| comprehensions             | 17.0 us                                                          | 19.3 us: 1.14x slower                                            |
| scimark_fft                | 312 ms                                                           | 357 ms: 1.15x slower                                             |
| mypy2                      | 764 ms                                                           | 886 ms: 1.16x slower                                             |
| fannkuch                   | 353 ms                                                           | 409 ms: 1.16x slower                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 701 ms: 1.16x slower                                             |
| chaos                      | 59.6 ms                                                          | 69.4 ms: 1.16x slower                                            |
| spectral_norm              | 97.3 ms                                                          | 115 ms: 1.18x slower                                             |
| async_tree_none            | 365 ms                                                           | 434 ms: 1.19x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 548 ms: 1.19x slower                                             |
| scimark_monte_carlo        | 65.5 ms                                                          | 78.5 ms: 1.20x slower                                            |
| async_tree_io_tg           | 900 ms                                                           | 1.08 sec: 1.20x slower                                           |
| hexiom                     | 6.35 ms                                                          | 7.63 ms: 1.20x slower                                            |
| scimark_sor                | 119 ms                                                           | 143 ms: 1.21x slower                                             |
| nbody                      | 87.8 ms                                                          | 106 ms: 1.21x slower                                             |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.23 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 706 ms: 1.23x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.08 sec: 1.23x slower                                           |
| python_startup_no_site     | 8.85 ms                                                          | 11.1 ms: 1.26x slower                                            |
| async_tree_none_tg         | 340 ms                                                           | 438 ms: 1.29x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 549 ms: 1.31x slower                                             |
| dask                       | 391 ms                                                           | 584 ms: 1.50x slower                                             |
| Geometric mean             | (ref)                                                            | 1.04x slower                                                     |

Benchmark hidden because not significant (5): unpickle_list, bench_mp_pool, json, sqlglot_parse, sympy_expand
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.98x