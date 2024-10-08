# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                     | 260 ms: 1.05x faster                                  |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                |
| html5lib       | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                 |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 423 ms: 1.09x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 890 ms: 1.05x faster                                  |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                  |
| nbody          | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                  |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                 |
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                 |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                 |
| xml_etree_generate   | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                 |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                  |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.03x faster                                  |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                 |
| genshi_xml      | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                 |
| django_template | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                 |
| Geometric mean  | (ref)                                                      | 1.02x faster                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.9 us: 1.33x faster                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                 |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                  |
| richards                   | 50.9 ms                                                    | 45.6 ms: 1.12x faster                                 |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                  |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 423 ms: 1.09x faster                                  |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                 |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                  |
| scimark_fft                | 392 ms                                                     | 365 ms: 1.07x faster                                  |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                 |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                 |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                 |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                  |
| bench_thread_pool          | 834 us                                                     | 784 us: 1.06x faster                                  |
| logging_simple             | 5.74 us                                                    | 5.42 us: 1.06x faster                                 |
| thrift                     | 823 us                                                     | 778 us: 1.06x faster                                  |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                  |
| 2to3                       | 274 ms                                                     | 260 ms: 1.05x faster                                  |
| asyncio_tcp                | 508 ms                                                     | 483 ms: 1.05x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 890 ms: 1.05x faster                                  |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.03 ms: 1.05x faster                                 |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                |
| crypto_pyaes               | 77.5 ms                                                    | 74.0 ms: 1.05x faster                                 |
| telco                      | 8.41 ms                                                    | 8.05 ms: 1.05x faster                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                 |
| raytrace                   | 267 ms                                                     | 255 ms: 1.04x faster                                  |
| xml_etree_process          | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                 |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                  |
| deltablue                  | 3.25 ms                                                    | 3.12 ms: 1.04x faster                                 |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                 |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                 |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                 |
| html5lib                   | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                  |
| genshi_xml                 | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                 |
| xml_etree_generate         | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                 |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                  |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.03x faster                                  |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                  |
| go                         | 145 ms                                                     | 141 ms: 1.03x faster                                  |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                |
| pprint_safe_repr           | 758 ms                                                     | 739 ms: 1.03x faster                                  |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                 |
| sympy_expand               | 473 ms                                                     | 461 ms: 1.02x faster                                  |
| django_template            | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                 |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                 |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                  |
| nqueens                    | 81.4 ms                                                    | 79.9 ms: 1.02x faster                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.94 sec: 1.02x faster                                |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                |
| pyflate                    | 484 ms                                                     | 477 ms: 1.02x faster                                  |
| nbody                      | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                 |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                  |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.01x faster                                  |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                  |
| hexiom                     | 6.30 ms                                                    | 6.23 ms: 1.01x faster                                 |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                  |
| typing_runtime_protocols   | 165 us                                                     | 164 us: 1.01x faster                                  |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                 |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                 |
| fannkuch                   | 402 ms                                                     | 420 ms: 1.04x slower                                  |
| coroutines                 | 23.2 ms                                                    | 24.7 ms: 1.07x slower                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                          |

Benchmark hidden because not significant (5): float, pickle_pure_python, mako, json, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x