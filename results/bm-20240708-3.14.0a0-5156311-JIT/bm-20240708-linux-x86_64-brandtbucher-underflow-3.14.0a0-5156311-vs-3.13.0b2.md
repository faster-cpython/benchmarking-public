# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 5156311
- commit date: 2024-07-08
- overall geometric mean: 1.03x faster
- HPT reliability: 99.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                             |
| docutils       | 2.83 sec                                                   | 3.02 sec: 1.07x slower                                           |
| html5lib       | 67.2 ms                                                    | 69.9 ms: 1.04x slower                                            |
| tornado_http   | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                      | 1.04x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 852 ms: 1.10x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                             |
| async_tree_io              | 939 ms                                                     | 887 ms: 1.06x faster                                             |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 78.9 ms: 1.12x faster                                            |
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                            |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                      | 1.09x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                            |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                            |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                             |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 199 us: 1.10x faster                                             |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                            |
| xml_etree_generate   | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                            |
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                            |
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                           |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                             |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                            |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                            |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.06x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 59.5 ms: 1.15x slower                                            |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.4 us: 1.40x faster                                            |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                             |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.27x faster                                             |
| deepcopy_reduce            | 3.35 us                                                    | 2.80 us: 1.20x faster                                            |
| richards_super             | 57.4 ms                                                    | 48.1 ms: 1.19x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.1 ms: 1.19x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.43 ms: 1.19x faster                                            |
| richards                   | 50.9 ms                                                    | 43.0 ms: 1.18x faster                                            |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                            |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                             |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                             |
| mako                       | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                            |
| fannkuch                   | 402 ms                                                     | 352 ms: 1.14x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                             |
| nbody                      | 88.3 ms                                                    | 78.9 ms: 1.12x faster                                            |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                             |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 852 ms: 1.10x faster                                             |
| unpickle_pure_python       | 218 us                                                     | 199 us: 1.10x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                             |
| telco                      | 8.41 ms                                                    | 7.87 ms: 1.07x faster                                            |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                            |
| chaos                      | 61.3 ms                                                    | 57.6 ms: 1.07x faster                                            |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                            |
| xml_etree_process          | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                            |
| async_tree_io              | 939 ms                                                     | 887 ms: 1.06x faster                                             |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                           |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                            |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                            |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                           |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                            |
| logging_format             | 6.47 us                                                    | 6.30 us: 1.03x faster                                            |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                            |
| thrift                     | 823 us                                                     | 806 us: 1.02x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                             |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                            |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                           |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                            |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.02x faster                                           |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                             |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                             |
| logging_simple             | 5.74 us                                                    | 5.69 us: 1.01x faster                                            |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                            |
| coroutines                 | 23.2 ms                                                    | 23.3 ms: 1.00x slower                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 56.1 ms: 1.01x slower                                            |
| coverage                   | 93.1 ms                                                    | 94.1 ms: 1.01x slower                                            |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                             |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                             |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                             |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                             |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                            |
| nqueens                    | 81.4 ms                                                    | 83.0 ms: 1.02x slower                                            |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                             |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                             |
| tornado_http               | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                            |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                             |
| html5lib                   | 67.2 ms                                                    | 69.9 ms: 1.04x slower                                            |
| hexiom                     | 6.30 ms                                                    | 6.55 ms: 1.04x slower                                            |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.05x slower                                             |
| typing_runtime_protocols   | 165 us                                                     | 173 us: 1.05x slower                                             |
| django_template            | 34.8 ms                                                    | 36.7 ms: 1.06x slower                                            |
| docutils                   | 2.83 sec                                                   | 3.02 sec: 1.07x slower                                           |
| dulwich_log                | 67.2 ms                                                    | 72.6 ms: 1.08x slower                                            |
| sympy_str                  | 282 ms                                                     | 307 ms: 1.09x slower                                             |
| sympy_expand               | 473 ms                                                     | 518 ms: 1.10x slower                                             |
| logging_silent             | 105 ns                                                     | 115 ns: 1.10x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.13x slower                                            |
| sympy_sum                  | 156 ms                                                     | 179 ms: 1.15x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 59.5 ms: 1.15x slower                                            |
| pylint                     | 317 ms                                                     | 392 ms: 1.24x slower                                             |
| deltablue                  | 3.25 ms                                                    | 4.14 ms: 1.27x slower                                            |
| generators                 | 29.6 ms                                                    | 43.2 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                     |

Benchmark hidden because not significant (3): genshi_text, go, dask
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.25% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x