# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.02x slower
- HPT reliability: 97.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                       |
| chameleon      | 7.22 ms                                                    | 6.75 ms: 1.07x faster                                      |
| docutils       | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                     |
| tornado_http   | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 439 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 716 ms: 1.17x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 568 ms: 1.23x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 727 ms: 1.24x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.18 sec: 1.25x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.20 sec: 1.28x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 592 ms: 1.33x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 452 ms: 1.34x slower                                       |
| Geometric mean             | (ref)                                                      | 1.25x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                       |
| float          | 78.9 ms                                                    | 86.1 ms: 1.09x slower                                      |
| nbody          | 88.3 ms                                                    | 102 ms: 1.16x slower                                       |
| Geometric mean | (ref)                                                      | 1.08x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                      |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                       |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.3 us: 1.06x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                      |
| unpickle_list        | 5.34 us                                                    | 5.11 us: 1.05x faster                                      |
| pickle_dict          | 34.8 us                                                    | 33.6 us: 1.04x faster                                      |
| pickle_pure_python   | 305 us                                                     | 296 us: 1.03x faster                                       |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                       |
| xml_etree_generate   | 87.4 ms                                                    | 85.7 ms: 1.02x faster                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                      |
| pickle_list          | 5.11 us                                                    | 5.07 us: 1.01x faster                                      |
| unpickle             | 15.1 us                                                    | 15.1 us: 1.00x faster                                      |
| tomli_loads          | 2.12 sec                                                   | 2.19 sec: 1.03x slower                                     |
| unpickle_pure_python | 218 us                                                     | 228 us: 1.04x slower                                       |
| Geometric mean       | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 8.95 ms: 1.26x slower                                      |
| Geometric mean         | (ref)                                                      | 1.10x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.2 ms                                                    | 12.4 ms: 1.10x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 110 us: 1.50x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.49 ms: 1.22x faster                                      |
| richards                   | 50.9 ms                                                    | 44.8 ms: 1.14x faster                                      |
| richards_super             | 57.4 ms                                                    | 50.8 ms: 1.13x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.04 us: 1.10x faster                                      |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                       |
| scimark_fft                | 392 ms                                                     | 366 ms: 1.07x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                     |
| chameleon                  | 7.22 ms                                                    | 6.75 ms: 1.07x faster                                      |
| deepcopy                   | 367 us                                                     | 345 us: 1.06x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.82 us: 1.06x faster                                      |
| json_loads                 | 28.9 us                                                    | 27.3 us: 1.06x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                      |
| scimark_sor                | 127 ms                                                     | 122 ms: 1.05x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.11 us: 1.05x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 38.1 us: 1.04x faster                                      |
| pickle_dict                | 34.8 us                                                    | 33.6 us: 1.04x faster                                      |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                      |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                       |
| pickle_pure_python         | 305 us                                                     | 296 us: 1.03x faster                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                      |
| logging_format             | 6.47 us                                                    | 6.30 us: 1.03x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 552 ms: 1.03x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 497 ms: 1.02x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                     |
| xml_etree_generate         | 87.4 ms                                                    | 85.7 ms: 1.02x faster                                      |
| generators                 | 29.6 ms                                                    | 29.1 ms: 1.02x faster                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                      |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 55.1 ms: 1.01x faster                                      |
| pickle_list                | 5.11 us                                                    | 5.07 us: 1.01x faster                                      |
| unpickle                   | 15.1 us                                                    | 15.1 us: 1.00x faster                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                      |
| sympy_sum                  | 156 ms                                                     | 157 ms: 1.01x slower                                       |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                       |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.35 ms: 1.01x slower                                      |
| sympy_expand               | 473 ms                                                     | 480 ms: 1.02x slower                                       |
| dulwich_log                | 67.2 ms                                                    | 68.2 ms: 1.02x slower                                      |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                       |
| coroutines                 | 23.2 ms                                                    | 23.7 ms: 1.02x slower                                      |
| deltablue                  | 3.25 ms                                                    | 3.32 ms: 1.02x slower                                      |
| crypto_pyaes               | 77.5 ms                                                    | 79.1 ms: 1.02x slower                                      |
| pprint_safe_repr           | 758 ms                                                     | 775 ms: 1.02x slower                                       |
| tornado_http               | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                      |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                       |
| coverage                   | 93.1 ms                                                    | 95.8 ms: 1.03x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.19 sec: 1.03x slower                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.61 sec: 1.04x slower                                     |
| unpickle_pure_python       | 218 us                                                     | 228 us: 1.04x slower                                       |
| pathlib                    | 17.3 ms                                                    | 18.1 ms: 1.05x slower                                      |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                       |
| raytrace                   | 267 ms                                                     | 280 ms: 1.05x slower                                       |
| fannkuch                   | 402 ms                                                     | 422 ms: 1.05x slower                                       |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                     |
| pyflate                    | 484 ms                                                     | 514 ms: 1.06x slower                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 74.0 ms: 1.07x slower                                      |
| float                      | 78.9 ms                                                    | 86.1 ms: 1.09x slower                                      |
| comprehensions             | 16.6 us                                                    | 18.2 us: 1.09x slower                                      |
| mako                       | 11.2 ms                                                    | 12.4 ms: 1.10x slower                                      |
| nqueens                    | 81.4 ms                                                    | 89.8 ms: 1.10x slower                                      |
| chaos                      | 61.3 ms                                                    | 69.1 ms: 1.13x slower                                      |
| spectral_norm              | 116 ms                                                     | 132 ms: 1.13x slower                                       |
| nbody                      | 88.3 ms                                                    | 102 ms: 1.16x slower                                       |
| async_tree_none            | 378 ms                                                     | 439 ms: 1.16x slower                                       |
| mypy2                      | 742 ms                                                     | 861 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 716 ms: 1.17x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 568 ms: 1.23x slower                                       |
| hexiom                     | 6.30 ms                                                    | 7.72 ms: 1.23x slower                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 727 ms: 1.24x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.18 sec: 1.25x slower                                     |
| python_startup_no_site     | 7.11 ms                                                    | 8.95 ms: 1.26x slower                                      |
| async_tree_io_tg           | 936 ms                                                     | 1.20 sec: 1.28x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 592 ms: 1.33x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 452 ms: 1.34x slower                                       |
| dask                       | 369 ms                                                     | 527 ms: 1.43x slower                                       |
| Geometric mean             | (ref)                                                      | 1.02x slower                                               |

Benchmark hidden because not significant (8): sympy_str, telco, mdp, logging_simple, regex_v8, meteor_contest, bench_thread_pool, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: unpack_sequence

# HPT report

- Reliability score: 97.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x