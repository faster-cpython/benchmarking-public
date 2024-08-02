
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 311 ms: 1.09x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.90 ms: 1.09x slower                                            |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                           |
| tornado_http   | 121 ms                                                       | 124 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 696 ms                                                       | 711 ms: 1.02x slower                                             |
| async_tree_memoization     | 544 ms                                                       | 561 ms: 1.03x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 725 ms: 1.04x slower                                             |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                           |
| async_tree_none_tg         | 431 ms                                                       | 453 ms: 1.05x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.11 sec: 1.06x slower                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 586 ms: 1.08x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                     |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 267 ms: 1.01x slower                                             |
| float          | 76.6 ms                                                      | 92.5 ms: 1.21x slower                                            |
| nbody          | 88.0 ms                                                      | 112 ms: 1.27x slower                                             |
| Geometric mean | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                            |
| regex_dna      | 239 ms                                                       | 249 ms: 1.05x slower                                             |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                            |
| regex_compile  | 144 ms                                                       | 172 ms: 1.19x slower                                             |
| Geometric mean | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle               | 10.5 us                                                      | 9.98 us: 1.06x faster                                            |
| pickle_list          | 4.43 us                                                      | 4.27 us: 1.04x faster                                            |
| pickle_dict          | 32.5 us                                                      | 31.8 us: 1.02x faster                                            |
| unpickle_list        | 4.66 us                                                      | 4.56 us: 1.02x faster                                            |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                             |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.03x slower                                            |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                            |
| xml_etree_process    | 58.4 ms                                                      | 60.9 ms: 1.04x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                            |
| xml_etree_generate   | 86.1 ms                                                      | 90.1 ms: 1.05x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 157 ms: 1.09x slower                                             |
| unpickle_pure_python | 210 us                                                       | 231 us: 1.10x slower                                             |
| xml_etree_iterparse  | 103 ms                                                       | 117 ms: 1.14x slower                                             |
| tomli_loads          | 2.16 sec                                                     | 2.61 sec: 1.21x slower                                           |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.3 ms: 1.31x slower                                            |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.0 ms                                                      | 13.6 ms: 1.36x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpack_sequence            | 53.2 ns                                                      | 43.3 ns: 1.23x faster                                            |
| typing_runtime_protocols   | 152 us                                                       | 133 us: 1.14x faster                                             |
| generators                 | 37.4 ms                                                      | 35.0 ms: 1.07x faster                                            |
| pickle                     | 10.5 us                                                      | 9.98 us: 1.06x faster                                            |
| pickle_list                | 4.43 us                                                      | 4.27 us: 1.04x faster                                            |
| async_generators           | 390 ms                                                       | 377 ms: 1.03x faster                                             |
| pickle_dict                | 32.5 us                                                      | 31.8 us: 1.02x faster                                            |
| unpickle_list              | 4.66 us                                                      | 4.56 us: 1.02x faster                                            |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                             |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                            |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                             |
| logging_format             | 7.48 us                                                      | 7.40 us: 1.01x faster                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.35 us: 1.01x faster                                            |
| deepcopy                   | 368 us                                                       | 366 us: 1.01x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 80.6 ms: 1.00x slower                                            |
| raytrace                   | 298 ms                                                       | 299 ms: 1.00x slower                                             |
| pidigits                   | 265 ms                                                       | 267 ms: 1.01x slower                                             |
| logging_simple             | 6.71 us                                                      | 6.80 us: 1.01x slower                                            |
| pathlib                    | 18.9 ms                                                      | 19.3 ms: 1.02x slower                                            |
| tornado_http               | 121 ms                                                       | 124 ms: 1.02x slower                                             |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 711 ms: 1.02x slower                                             |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                           |
| mdp                        | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                           |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.03x slower                                            |
| async_tree_memoization     | 544 ms                                                       | 561 ms: 1.03x slower                                             |
| sympy_sum                  | 162 ms                                                       | 167 ms: 1.03x slower                                             |
| json                       | 5.12 ms                                                      | 5.30 ms: 1.04x slower                                            |
| bench_thread_pool          | 950 us                                                       | 985 us: 1.04x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 725 ms: 1.04x slower                                             |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                            |
| sympy_integrate            | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                            |
| xml_etree_process          | 58.4 ms                                                      | 60.9 ms: 1.04x slower                                            |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                            |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.05x slower                                             |
| xml_etree_generate         | 86.1 ms                                                      | 90.1 ms: 1.05x slower                                            |
| logging_silent             | 94.4 ns                                                      | 98.7 ns: 1.05x slower                                            |
| dask                       | 392 ms                                                       | 411 ms: 1.05x slower                                             |
| deepcopy_memo              | 36.8 us                                                      | 38.6 us: 1.05x slower                                            |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                           |
| async_tree_none_tg         | 431 ms                                                       | 453 ms: 1.05x slower                                             |
| regex_v8                   | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 1.11 sec: 1.06x slower                                           |
| scimark_lu                 | 98.8 ms                                                      | 105 ms: 1.06x slower                                             |
| comprehensions             | 21.9 us                                                      | 23.3 us: 1.06x slower                                            |
| sympy_str                  | 302 ms                                                       | 322 ms: 1.07x slower                                             |
| meteor_contest             | 128 ms                                                       | 137 ms: 1.07x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.90 ms: 1.07x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 124 ms: 1.07x slower                                             |
| mypy2                      | 830 ms                                                       | 893 ms: 1.08x slower                                             |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.08x slower                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 3.76 ms: 1.08x slower                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 586 ms: 1.08x slower                                             |
| pprint_safe_repr           | 807 ms                                                       | 880 ms: 1.09x slower                                             |
| 2to3                       | 285 ms                                                       | 311 ms: 1.09x slower                                             |
| chameleon                  | 7.23 ms                                                      | 7.90 ms: 1.09x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 157 ms: 1.09x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.81 sec: 1.10x slower                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 63.2 ms: 1.10x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 72.0 ms: 1.10x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 231 us: 1.10x slower                                             |
| sympy_expand               | 484 ms                                                       | 535 ms: 1.11x slower                                             |
| python_startup             | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                            |
| richards                   | 45.7 ms                                                      | 51.6 ms: 1.13x slower                                            |
| richards_super             | 51.3 ms                                                      | 58.4 ms: 1.14x slower                                            |
| xml_etree_iterparse        | 103 ms                                                       | 117 ms: 1.14x slower                                             |
| chaos                      | 64.0 ms                                                      | 73.3 ms: 1.15x slower                                            |
| nqueens                    | 89.9 ms                                                      | 105 ms: 1.17x slower                                             |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                            |
| regex_compile              | 144 ms                                                       | 172 ms: 1.19x slower                                             |
| go                         | 150 ms                                                       | 179 ms: 1.20x slower                                             |
| tomli_loads                | 2.16 sec                                                     | 2.61 sec: 1.21x slower                                           |
| float                      | 76.6 ms                                                      | 92.5 ms: 1.21x slower                                            |
| telco                      | 6.96 ms                                                      | 8.47 ms: 1.22x slower                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 87.4 ms: 1.27x slower                                            |
| pyflate                    | 439 ms                                                       | 557 ms: 1.27x slower                                             |
| nbody                      | 88.0 ms                                                      | 112 ms: 1.27x slower                                             |
| fannkuch                   | 350 ms                                                       | 453 ms: 1.29x slower                                             |
| python_startup_no_site     | 8.64 ms                                                      | 11.3 ms: 1.31x slower                                            |
| scimark_fft                | 301 ms                                                       | 407 ms: 1.35x slower                                             |
| mako                       | 10.0 ms                                                      | 13.6 ms: 1.36x slower                                            |
| scimark_sor                | 109 ms                                                       | 149 ms: 1.37x slower                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.01 ms: 1.43x slower                                            |
| hexiom                     | 5.96 ms                                                      | 9.10 ms: 1.53x slower                                            |
| deltablue                  | 3.24 ms                                                      | 4.98 ms: 1.54x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 144 ms: 1.57x slower                                             |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                     |

Benchmark hidden because not significant (5): async_tree_none, bench_mp_pool, asyncio_tcp_ssl, asyncio_websockets, create_gc_cycles
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x


# Memory

- memory change: 0.87x