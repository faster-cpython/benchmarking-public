# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: a4c1908
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| html5lib       | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 92.2 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 379 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 846 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.5 ms: 1.14x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.09x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                                      |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                     |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.87 sec: 1.13x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.4 ms: 1.09x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 81.9 ms: 1.07x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.6 ms: 1.06x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                     |
| genshi_text    | 23.7 ms                                                    | 25.9 ms: 1.09x slower                                                     |
| genshi_xml     | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                      | 1.03x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                     |
| richards                   | 50.9 ms                                                    | 35.9 ms: 1.42x faster                                                     |
| richards_super             | 57.4 ms                                                    | 40.8 ms: 1.41x faster                                                     |
| deepcopy                   | 367 us                                                     | 265 us: 1.39x faster                                                      |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.31 ms: 1.22x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 379 ms: 1.17x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                                     |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                      |
| float                      | 78.9 ms                                                    | 69.5 ms: 1.14x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.87 sec: 1.13x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                      |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                      |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                     |
| fannkuch                   | 402 ms                                                     | 359 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.4 ms: 1.11x faster                                                     |
| pyflate                    | 484 ms                                                     | 437 ms: 1.11x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 846 ms: 1.11x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                    |
| nbody                      | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 545 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.04 us: 1.07x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.88 ms: 1.07x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 81.9 ms: 1.07x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.72 sec: 1.06x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.6 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 57.8 ms: 1.06x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.45 us: 1.05x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                     |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| dulwich_log                | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 92.2 ms: 1.03x faster                                                     |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 119 ms: 1.03x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 740 ms: 1.02x faster                                                      |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| thrift                     | 823 us                                                     | 812 us: 1.01x faster                                                      |
| coverage                   | 93.1 ms                                                    | 92.2 ms: 1.01x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 507 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                     |
| regex_compile              | 137 ms                                                     | 137 ms: 1.00x slower                                                      |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                      |
| scimark_sor                | 127 ms                                                     | 128 ms: 1.00x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                     |
| generators                 | 29.6 ms                                                    | 29.8 ms: 1.01x slower                                                     |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                     |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 56.2 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.01x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                     |
| raytrace                   | 267 ms                                                     | 273 ms: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                      |
| sympy_str                  | 282 ms                                                     | 289 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.02x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                      |
| sympy_expand               | 473 ms                                                     | 494 ms: 1.05x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.45 ms: 1.06x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 21.7 ms: 1.06x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 166 ms: 1.07x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.73 ms: 1.07x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.9 ms: 1.09x slower                                                     |
| pylint                     | 317 ms                                                     | 351 ms: 1.11x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (5): go, sqlglot_transpile, coroutines, django_template, pickle_pure_python
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x