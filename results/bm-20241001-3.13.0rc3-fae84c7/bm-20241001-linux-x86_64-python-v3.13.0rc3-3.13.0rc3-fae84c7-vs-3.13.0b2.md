# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 264 ms: 1.04x faster                                         |
| chameleon      | 7.22 ms                                                    | 6.85 ms: 1.05x faster                                        |
| docutils       | 2.83 sec                                                   | 2.56 sec: 1.10x faster                                       |
| html5lib       | 67.2 ms                                                    | 63.1 ms: 1.07x faster                                        |
| tornado_http   | 94.6 ms                                                    | 91.2 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                      | 1.06x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 813 ms: 1.15x faster                                         |
| async_tree_io              | 939 ms                                                     | 832 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                         |
| async_tree_none            | 378 ms                                                     | 349 ms: 1.08x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                         |
| async_tree_memoization     | 463 ms                                                     | 437 ms: 1.06x faster                                         |
| async_tree_none_tg         | 336 ms                                                     | 317 ms: 1.06x faster                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 459 ms: 1.03x slower                                         |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                      | 1.01x faster                                                 |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 208 ms: 1.06x faster                                         |
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                        |
| regex_effbot   | 3.67 ms                                                    | 3.51 ms: 1.05x faster                                        |
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                      | 1.05x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.3 us: 1.06x faster                                        |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.05x faster                                         |
| xml_etree_iterparse  | 107 ms                                                     | 103 ms: 1.04x faster                                         |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                         |
| pickle_list          | 5.11 us                                                    | 4.98 us: 1.03x faster                                        |
| xml_etree_process    | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                        |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                        |
| xml_etree_generate   | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                        |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                         |
| unpickle             | 15.1 us                                                    | 15.2 us: 1.01x slower                                        |
| pickle_dict          | 34.8 us                                                    | 35.4 us: 1.02x slower                                        |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                 |

Benchmark hidden because not significant (2): tomli_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 6.95 ms: 1.02x faster                                        |
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                        |
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                        |
| genshi_xml      | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                        |
| mako            | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 813 ms: 1.15x faster                                         |
| async_tree_io              | 939 ms                                                     | 832 ms: 1.13x faster                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.63 ms: 1.11x faster                                        |
| coverage                   | 93.1 ms                                                    | 84.2 ms: 1.11x faster                                        |
| docutils                   | 2.83 sec                                                   | 2.56 sec: 1.10x faster                                       |
| dask                       | 369 ms                                                     | 336 ms: 1.10x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                         |
| async_tree_none            | 378 ms                                                     | 349 ms: 1.08x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                         |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                         |
| richards                   | 50.9 ms                                                    | 47.8 ms: 1.07x faster                                        |
| richards_super             | 57.4 ms                                                    | 53.8 ms: 1.07x faster                                        |
| scimark_fft                | 392 ms                                                     | 368 ms: 1.07x faster                                         |
| html5lib                   | 67.2 ms                                                    | 63.1 ms: 1.07x faster                                        |
| regex_dna                  | 221 ms                                                     | 208 ms: 1.06x faster                                         |
| bpe_tokeniser              | 5.02 sec                                                   | 4.72 sec: 1.06x faster                                       |
| dulwich_log                | 67.2 ms                                                    | 63.2 ms: 1.06x faster                                        |
| async_tree_memoization     | 463 ms                                                     | 437 ms: 1.06x faster                                         |
| async_tree_none_tg         | 336 ms                                                     | 317 ms: 1.06x faster                                         |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                        |
| json_loads                 | 28.9 us                                                    | 27.3 us: 1.06x faster                                        |
| chameleon                  | 7.22 ms                                                    | 6.85 ms: 1.05x faster                                        |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                        |
| coroutines                 | 23.2 ms                                                    | 22.1 ms: 1.05x faster                                        |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                         |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                        |
| gunicorn                   | 1.28 ms                                                    | 1.22 ms: 1.05x faster                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.03 ms: 1.05x faster                                        |
| aiohttp                    | 1.18 ms                                                    | 1.13 ms: 1.05x faster                                        |
| crypto_pyaes               | 77.5 ms                                                    | 74.0 ms: 1.05x faster                                        |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.05x faster                                         |
| regex_effbot               | 3.67 ms                                                    | 3.51 ms: 1.05x faster                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.04x faster                                        |
| xml_etree_iterparse        | 107 ms                                                     | 103 ms: 1.04x faster                                         |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                        |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                         |
| tornado_http               | 94.6 ms                                                    | 91.2 ms: 1.04x faster                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.77 sec: 1.04x faster                                       |
| 2to3                       | 274 ms                                                     | 264 ms: 1.04x faster                                         |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                        |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                         |
| sympy_str                  | 282 ms                                                     | 273 ms: 1.04x faster                                         |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                        |
| pyflate                    | 484 ms                                                     | 468 ms: 1.03x faster                                         |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                         |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                         |
| hexiom                     | 6.30 ms                                                    | 6.10 ms: 1.03x faster                                        |
| django_template            | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                       |
| genshi_text                | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                        |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                         |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                         |
| sqlglot_optimize           | 55.5 ms                                                    | 53.9 ms: 1.03x faster                                        |
| deepcopy_memo              | 39.7 us                                                    | 38.6 us: 1.03x faster                                        |
| genshi_xml                 | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                        |
| logging_format             | 6.47 us                                                    | 6.29 us: 1.03x faster                                        |
| deepcopy_reduce            | 3.35 us                                                    | 3.26 us: 1.03x faster                                        |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                         |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                         |
| pickle_list                | 5.11 us                                                    | 4.98 us: 1.03x faster                                        |
| bench_thread_pool          | 834 us                                                     | 813 us: 1.03x faster                                         |
| go                         | 145 ms                                                     | 141 ms: 1.02x faster                                         |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                        |
| asyncio_websockets         | 567 ms                                                     | 553 ms: 1.02x faster                                         |
| xml_etree_process          | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                        |
| pprint_safe_repr           | 758 ms                                                     | 741 ms: 1.02x faster                                         |
| generators                 | 29.6 ms                                                    | 29.0 ms: 1.02x faster                                        |
| python_startup_no_site     | 7.11 ms                                                    | 6.95 ms: 1.02x faster                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                        |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                       |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                        |
| mako                       | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                        |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                         |
| fannkuch                   | 402 ms                                                     | 394 ms: 1.02x faster                                         |
| json                       | 5.31 ms                                                    | 5.21 ms: 1.02x faster                                        |
| deepcopy                   | 367 us                                                     | 360 us: 1.02x faster                                         |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                        |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                        |
| xml_etree_generate         | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                        |
| async_generators           | 442 ms                                                     | 435 ms: 1.02x faster                                         |
| raytrace                   | 267 ms                                                     | 263 ms: 1.01x faster                                         |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                         |
| pathlib                    | 17.3 ms                                                    | 17.2 ms: 1.01x faster                                        |
| logging_simple             | 5.74 us                                                    | 5.71 us: 1.01x faster                                        |
| unpickle                   | 15.1 us                                                    | 15.2 us: 1.01x slower                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                        |
| telco                      | 8.41 ms                                                    | 8.52 ms: 1.01x slower                                        |
| pickle_dict                | 34.8 us                                                    | 35.4 us: 1.02x slower                                        |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 459 ms: 1.03x slower                                         |
| mypy2                      | 742 ms                                                     | 1.06 sec: 1.43x slower                                       |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                 |

Benchmark hidden because not significant (10): pylint, djangocms, pycparser, nqueens, tomli_loads, typing_runtime_protocols, nbody, float, unpickle_list, flaskblogging
Ignored benchmarks (1) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.99x