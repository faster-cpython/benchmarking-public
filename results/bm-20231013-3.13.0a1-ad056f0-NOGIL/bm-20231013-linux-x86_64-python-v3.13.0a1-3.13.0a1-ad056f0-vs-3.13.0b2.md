# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.08x slower
- HPT reliability: 89.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                       |
| chameleon      | 7.22 ms                                                    | 7.13 ms: 1.01x faster                                      |
| docutils       | 2.83 sec                                                   | 2.71 sec: 1.05x faster                                     |
| tornado_http   | 94.6 ms                                                    | 99.1 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 446 ms: 1.18x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 726 ms: 1.19x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 572 ms: 1.24x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.21 sec: 1.29x slower                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 759 ms: 1.29x slower                                       |
| async_tree_io_tg           | 936 ms                                                     | 1.25 sec: 1.33x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 610 ms: 1.37x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 463 ms: 1.38x slower                                       |
| Geometric mean             | (ref)                                                      | 1.28x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                       |
| float          | 78.9 ms                                                    | 83.4 ms: 1.06x slower                                      |
| nbody          | 88.3 ms                                                    | 95.7 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 209 ms: 1.06x faster                                       |
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                      |
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                      |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.08 us: 1.05x faster                                      |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.01x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 60.5 ms: 1.01x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 160 ms: 1.01x faster                                       |
| xml_etree_generate   | 87.4 ms                                                    | 87.7 ms: 1.00x slower                                      |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.00x slower                                       |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                      |
| pickle_dict          | 34.8 us                                                    | 35.4 us: 1.02x slower                                      |
| pickle_list          | 5.11 us                                                    | 5.21 us: 1.02x slower                                      |
| unpickle_pure_python | 218 us                                                     | 226 us: 1.04x slower                                       |
| tomli_loads          | 2.12 sec                                                   | 2.25 sec: 1.06x slower                                     |
| Geometric mean       | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                      |
| Geometric mean         | (ref)                                                      | 1.02x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                      |
| genshi_xml     | 51.6 ms                                                    | 52.0 ms: 1.01x slower                                      |
| mako           | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.50 ms: 1.21x faster                                      |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                     |
| typing_runtime_protocols   | 165 us                                                     | 153 us: 1.07x faster                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.93 ms: 1.07x faster                                      |
| regex_dna                  | 221 ms                                                     | 209 ms: 1.06x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.08 us: 1.05x faster                                      |
| scimark_fft                | 392 ms                                                     | 375 ms: 1.05x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.71 sec: 1.05x faster                                     |
| deepcopy_reduce            | 3.35 us                                                    | 3.20 us: 1.05x faster                                      |
| scimark_lu                 | 122 ms                                                     | 117 ms: 1.04x faster                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                      |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                      |
| crypto_pyaes               | 77.5 ms                                                    | 75.1 ms: 1.03x faster                                      |
| flaskblogging              | 9.01 ms                                                    | 8.77 ms: 1.03x faster                                      |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                      |
| richards_super             | 57.4 ms                                                    | 56.0 ms: 1.03x faster                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| sympy_expand               | 473 ms                                                     | 463 ms: 1.02x faster                                       |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                       |
| richards                   | 50.9 ms                                                    | 49.9 ms: 1.02x faster                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 54.5 ms: 1.02x faster                                      |
| deepcopy                   | 367 us                                                     | 361 us: 1.02x faster                                       |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.01x faster                                      |
| chameleon                  | 7.22 ms                                                    | 7.13 ms: 1.01x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 60.5 ms: 1.01x faster                                      |
| xml_etree_parse            | 162 ms                                                     | 160 ms: 1.01x faster                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                      |
| pprint_safe_repr           | 758 ms                                                     | 752 ms: 1.01x faster                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                      |
| json                       | 5.31 ms                                                    | 5.27 ms: 1.01x faster                                      |
| pidigits                   | 191 ms                                                     | 190 ms: 1.01x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 563 ms: 1.01x faster                                       |
| nqueens                    | 81.4 ms                                                    | 81.0 ms: 1.01x faster                                      |
| pyflate                    | 484 ms                                                     | 482 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.00x faster                                     |
| generators                 | 29.6 ms                                                    | 29.5 ms: 1.00x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 39.6 us: 1.00x faster                                      |
| xml_etree_generate         | 87.4 ms                                                    | 87.7 ms: 1.00x slower                                      |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.00x slower                                       |
| regex_v8                   | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                      |
| meteor_contest             | 110 ms                                                     | 111 ms: 1.01x slower                                       |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                       |
| genshi_xml                 | 51.6 ms                                                    | 52.0 ms: 1.01x slower                                      |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                       |
| sympy_str                  | 282 ms                                                     | 286 ms: 1.01x slower                                       |
| sympy_integrate            | 20.5 ms                                                    | 20.8 ms: 1.01x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 70.2 ms: 1.02x slower                                      |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                      |
| hexiom                     | 6.30 ms                                                    | 6.40 ms: 1.02x slower                                      |
| pickle_dict                | 34.8 us                                                    | 35.4 us: 1.02x slower                                      |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                      |
| pickle_list                | 5.11 us                                                    | 5.21 us: 1.02x slower                                      |
| coroutines                 | 23.2 ms                                                    | 23.7 ms: 1.02x slower                                      |
| sympy_sum                  | 156 ms                                                     | 160 ms: 1.03x slower                                       |
| unpickle_pure_python       | 218 us                                                     | 226 us: 1.04x slower                                       |
| logging_format             | 6.47 us                                                    | 6.71 us: 1.04x slower                                      |
| logging_silent             | 105 ns                                                     | 109 ns: 1.04x slower                                       |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                       |
| sqlite_synth               | 2.99 us                                                    | 3.11 us: 1.04x slower                                      |
| chaos                      | 61.3 ms                                                    | 64.0 ms: 1.04x slower                                      |
| mako                       | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                      |
| gc_traversal               | 3.98 ms                                                    | 4.15 ms: 1.04x slower                                      |
| deltablue                  | 3.25 ms                                                    | 3.40 ms: 1.04x slower                                      |
| fannkuch                   | 402 ms                                                     | 420 ms: 1.05x slower                                       |
| tornado_http               | 94.6 ms                                                    | 99.1 ms: 1.05x slower                                      |
| logging_simple             | 5.74 us                                                    | 6.02 us: 1.05x slower                                      |
| float                      | 78.9 ms                                                    | 83.4 ms: 1.06x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.25 sec: 1.06x slower                                     |
| async_generators           | 442 ms                                                     | 472 ms: 1.07x slower                                       |
| raytrace                   | 267 ms                                                     | 285 ms: 1.07x slower                                       |
| pycparser                  | 1.16 sec                                                   | 1.24 sec: 1.07x slower                                     |
| nbody                      | 88.3 ms                                                    | 95.7 ms: 1.08x slower                                      |
| pathlib                    | 17.3 ms                                                    | 19.6 ms: 1.13x slower                                      |
| mypy2                      | 742 ms                                                     | 863 ms: 1.16x slower                                       |
| async_tree_none            | 378 ms                                                     | 446 ms: 1.18x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 726 ms: 1.19x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 572 ms: 1.24x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.21 sec: 1.29x slower                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 759 ms: 1.29x slower                                       |
| comprehensions             | 16.6 us                                                    | 21.5 us: 1.30x slower                                      |
| async_tree_io_tg           | 936 ms                                                     | 1.25 sec: 1.33x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 610 ms: 1.37x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 463 ms: 1.38x slower                                       |
| dask                       | 369 ms                                                     | 544 ms: 1.47x slower                                       |
| coverage                   | 93.1 ms                                                    | 700 ms: 7.52x slower                                       |
| thrift                     | 823 us                                                     | 9.24 ms: 11.22x slower                                     |
| Geometric mean             | (ref)                                                      | 1.08x slower                                               |

Benchmark hidden because not significant (12): xml_etree_iterparse, scimark_sor, aiohttp, django_template, gunicorn, bench_thread_pool, bench_mp_pool, sqlglot_transpile, telco, spectral_norm, html5lib, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms

# HPT report

- Reliability score: 89.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.56x