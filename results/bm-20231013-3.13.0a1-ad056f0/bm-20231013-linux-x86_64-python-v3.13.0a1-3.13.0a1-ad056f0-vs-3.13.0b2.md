# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.01x slower
- HPT reliability: 95.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 269 ms: 1.02x faster                                       |
| chameleon      | 7.22 ms                                                    | 7.07 ms: 1.02x faster                                      |
| docutils       | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                     |
| tornado_http   | 94.6 ms                                                    | 96.0 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 437 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 712 ms: 1.17x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 564 ms: 1.22x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 741 ms: 1.26x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.19 sec: 1.26x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.23 sec: 1.31x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 595 ms: 1.34x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 453 ms: 1.35x slower                                       |
| Geometric mean             | (ref)                                                      | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 88.6 ms: 1.00x slower                                      |
| pidigits       | 191 ms                                                     | 195 ms: 1.02x slower                                       |
| float          | 78.9 ms                                                    | 81.6 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                       |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.01x faster                                      |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.05 us: 1.06x faster                                      |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                      |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                       |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.02x faster                                       |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                      |
| xml_etree_generate   | 87.4 ms                                                    | 86.9 ms: 1.01x faster                                      |
| pickle_dict          | 34.8 us                                                    | 34.6 us: 1.01x faster                                      |
| tomli_loads          | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                     |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                      |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                       |
| Geometric mean       | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.1 ms: 1.07x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 6.87 ms: 1.03x faster                                      |
| Geometric mean         | (ref)                                                      | 1.05x faster                                               |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.48 ms: 1.23x faster                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.79 ms: 1.10x faster                                      |
| crypto_pyaes               | 77.5 ms                                                    | 71.8 ms: 1.08x faster                                      |
| docutils                   | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                     |
| python_startup             | 10.8 ms                                                    | 10.1 ms: 1.07x faster                                      |
| sqlite_synth               | 2.99 us                                                    | 2.80 us: 1.07x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.14 us: 1.07x faster                                      |
| scimark_fft                | 392 ms                                                     | 369 ms: 1.06x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.05 us: 1.06x faster                                      |
| typing_runtime_protocols   | 165 us                                                     | 156 us: 1.06x faster                                       |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                       |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                       |
| richards                   | 50.9 ms                                                    | 48.6 ms: 1.05x faster                                      |
| sympy_expand               | 473 ms                                                     | 452 ms: 1.05x faster                                       |
| richards_super             | 57.4 ms                                                    | 55.0 ms: 1.04x faster                                      |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                       |
| deepcopy                   | 367 us                                                     | 353 us: 1.04x faster                                       |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                      |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.04x faster                                       |
| python_startup_no_site     | 7.11 ms                                                    | 6.87 ms: 1.03x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 53.9 ms: 1.03x faster                                      |
| telco                      | 8.41 ms                                                    | 8.17 ms: 1.03x faster                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                     |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 3.87 ms: 1.03x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 552 ms: 1.03x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                       |
| deepcopy_memo              | 39.7 us                                                    | 38.7 us: 1.03x faster                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                      |
| go                         | 145 ms                                                     | 141 ms: 1.02x faster                                       |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| pyflate                    | 484 ms                                                     | 473 ms: 1.02x faster                                       |
| bench_thread_pool          | 834 us                                                     | 815 us: 1.02x faster                                       |
| hexiom                     | 6.30 ms                                                    | 6.16 ms: 1.02x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                      |
| chameleon                  | 7.22 ms                                                    | 7.07 ms: 1.02x faster                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                      |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                       |
| 2to3                       | 274 ms                                                     | 269 ms: 1.02x faster                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                     |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.02x faster                                       |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                     |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.02x faster                                      |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.01x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 20.2 ms: 1.01x faster                                      |
| pprint_safe_repr           | 758 ms                                                     | 752 ms: 1.01x faster                                       |
| xml_etree_generate         | 87.4 ms                                                    | 86.9 ms: 1.01x faster                                      |
| pickle_dict                | 34.8 us                                                    | 34.6 us: 1.01x faster                                      |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.00x faster                                       |
| nbody                      | 88.3 ms                                                    | 88.6 ms: 1.00x slower                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 69.5 ms: 1.01x slower                                      |
| chaos                      | 61.3 ms                                                    | 61.7 ms: 1.01x slower                                      |
| nqueens                    | 81.4 ms                                                    | 81.9 ms: 1.01x slower                                      |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                      |
| generators                 | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                      |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                       |
| tomli_loads                | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                     |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                      |
| tornado_http               | 94.6 ms                                                    | 96.0 ms: 1.01x slower                                      |
| coverage                   | 93.1 ms                                                    | 94.4 ms: 1.01x slower                                      |
| unpickle_pure_python       | 218 us                                                     | 222 us: 1.02x slower                                       |
| pidigits                   | 191 ms                                                     | 195 ms: 1.02x slower                                       |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                       |
| async_generators           | 442 ms                                                     | 453 ms: 1.02x slower                                       |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                       |
| deltablue                  | 3.25 ms                                                    | 3.34 ms: 1.03x slower                                      |
| logging_simple             | 5.74 us                                                    | 5.90 us: 1.03x slower                                      |
| float                      | 78.9 ms                                                    | 81.6 ms: 1.03x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                     |
| pathlib                    | 17.3 ms                                                    | 19.4 ms: 1.12x slower                                      |
| async_tree_none            | 378 ms                                                     | 437 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 712 ms: 1.17x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 564 ms: 1.22x slower                                       |
| comprehensions             | 16.6 us                                                    | 20.8 us: 1.25x slower                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 741 ms: 1.26x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.19 sec: 1.26x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.23 sec: 1.31x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 595 ms: 1.34x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 453 ms: 1.35x slower                                       |
| Geometric mean             | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (8): sympy_str, pickle_list, regex_effbot, logging_format, dulwich_log, sympy_sum, fannkuch, mako
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dask, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift
Ignored benchmarks (1) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: unpack_sequence

# HPT report

- Reliability score: 95.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x