# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 260 ms: 1.05x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                |
| html5lib       | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 397 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.15x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 527 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 885 ms: 1.06x faster                                                  |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 84.7 ms: 1.04x faster                                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| float          | 78.9 ms                                                    | 77.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.02x faster                                                 |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 209 us: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 59.1 ms: 1.04x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                                 |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.1 us: 1.36x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                 |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.52 ms: 1.17x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 397 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.15x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                  |
| richards                   | 50.9 ms                                                    | 45.1 ms: 1.13x faster                                                 |
| richards_super             | 57.4 ms                                                    | 51.2 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 527 ms: 1.11x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.57 ms: 1.11x faster                                                 |
| coverage                   | 93.1 ms                                                    | 83.9 ms: 1.11x faster                                                 |
| scimark_fft                | 392 ms                                                     | 356 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                  |
| logging_silent             | 105 ns                                                     | 96.5 ns: 1.09x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                 |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                                 |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 787 us: 1.06x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 885 ms: 1.06x faster                                                  |
| raytrace                   | 267 ms                                                     | 253 ms: 1.06x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.77 sec: 1.05x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| 2to3                       | 274 ms                                                     | 260 ms: 1.05x faster                                                  |
| genshi_text                | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                 |
| thrift                     | 823 us                                                     | 784 us: 1.05x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                |
| go                         | 145 ms                                                     | 138 ms: 1.05x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.1 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.2 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                                  |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                  |
| nbody                      | 88.3 ms                                                    | 84.7 ms: 1.04x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 74.4 ms: 1.04x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 209 us: 1.04x faster                                                  |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                 |
| pyflate                    | 484 ms                                                     | 466 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 59.1 ms: 1.04x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 78.7 ms: 1.03x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.15 ms: 1.03x faster                                                 |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 736 ms: 1.03x faster                                                  |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                  |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                                  |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                                |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.03x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.02x faster                                                |
| hexiom                     | 6.30 ms                                                    | 6.17 ms: 1.02x faster                                                 |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| async_generators           | 442 ms                                                     | 436 ms: 1.02x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                 |
| float                      | 78.9 ms                                                    | 77.9 ms: 1.01x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                 |
| fannkuch                   | 402 ms                                                     | 405 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                          |

Benchmark hidden because not significant (2): json, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x