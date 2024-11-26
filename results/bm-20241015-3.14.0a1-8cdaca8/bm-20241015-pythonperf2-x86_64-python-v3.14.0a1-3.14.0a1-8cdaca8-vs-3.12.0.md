# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.018x faster
- HPT reliability: 96.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                             |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                           |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 386 ms: 1.40x faster                                             |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 415 ms: 1.31x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 827 ms: 1.26x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 837 ms: 1.26x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 558 ms: 1.25x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                             |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                             |
| nbody          | 88.0 ms                                                      | 90.1 ms: 1.02x slower                                            |
| float          | 76.6 ms                                                      | 82.2 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                            |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                             |
| regex_v8       | 23.6 ms                                                      | 24.7 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.0 us: 1.05x faster                                            |
| pickle_list          | 4.43 us                                                      | 4.31 us: 1.03x faster                                            |
| unpickle_list        | 4.66 us                                                      | 4.58 us: 1.02x faster                                            |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                             |
| xml_etree_generate   | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                            |
| pickle               | 10.5 us                                                      | 10.5 us: 1.01x faster                                            |
| pickle_pure_python   | 318 us                                                       | 320 us: 1.01x slower                                             |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                             |
| xml_etree_process    | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                            |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.03x slower                                            |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                            |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.50 sec: 1.16x slower                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                            |
| python_startup         | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                            |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                            |
| django_template | 38.2 ms                                                      | 41.0 ms: 1.08x slower                                            |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 386 ms: 1.40x faster                                             |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 415 ms: 1.31x faster                                             |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                            |
| deepcopy                   | 368 us                                                       | 289 us: 1.27x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 827 ms: 1.26x faster                                             |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 837 ms: 1.26x faster                                             |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 558 ms: 1.25x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                             |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                            |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                            |
| go                         | 150 ms                                                       | 133 ms: 1.13x faster                                             |
| raytrace                   | 298 ms                                                       | 270 ms: 1.11x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 73.4 ms: 1.09x faster                                            |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                            |
| async_generators           | 390 ms                                                       | 364 ms: 1.07x faster                                             |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.4 ms: 1.05x faster                                            |
| chaos                      | 64.0 ms                                                      | 60.7 ms: 1.05x faster                                            |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                             |
| scimark_fft                | 301 ms                                                       | 286 ms: 1.05x faster                                             |
| pickle_dict                | 32.5 us                                                      | 31.0 us: 1.05x faster                                            |
| scimark_lu                 | 98.8 ms                                                      | 94.2 ms: 1.05x faster                                            |
| logging_format             | 7.48 us                                                      | 7.14 us: 1.05x faster                                            |
| bench_thread_pool          | 950 us                                                       | 908 us: 1.05x faster                                             |
| regex_effbot               | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                            |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                             |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.06 ms: 1.04x faster                                            |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                             |
| pickle_list                | 4.43 us                                                      | 4.31 us: 1.03x faster                                            |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.03x faster                                           |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                            |
| logging_simple             | 6.71 us                                                      | 6.57 us: 1.02x faster                                            |
| nqueens                    | 89.9 ms                                                      | 88.0 ms: 1.02x faster                                            |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                             |
| unpickle_list              | 4.66 us                                                      | 4.58 us: 1.02x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                           |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                            |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                             |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                             |
| xml_etree_generate         | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| pickle                     | 10.5 us                                                      | 10.5 us: 1.01x faster                                            |
| pprint_safe_repr           | 807 ms                                                       | 803 ms: 1.00x faster                                             |
| pickle_pure_python         | 318 us                                                       | 320 us: 1.01x slower                                             |
| json                       | 5.12 ms                                                      | 5.16 ms: 1.01x slower                                            |
| fannkuch                   | 350 ms                                                       | 354 ms: 1.01x slower                                             |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                             |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                             |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                             |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                             |
| nbody                      | 88.0 ms                                                      | 90.1 ms: 1.02x slower                                            |
| xml_etree_process          | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                            |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.03x slower                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 59.1 ms: 1.03x slower                                            |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                             |
| dulwich_log                | 65.4 ms                                                      | 67.5 ms: 1.03x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                            |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                            |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 24.7 ms: 1.05x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 96.0 ms: 1.05x slower                                            |
| hexiom                     | 5.96 ms                                                      | 6.24 ms: 1.05x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.44 ms: 1.06x slower                                            |
| pyflate                    | 439 ms                                                       | 469 ms: 1.07x slower                                             |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                            |
| float                      | 76.6 ms                                                      | 82.2 ms: 1.07x slower                                            |
| django_template            | 38.2 ms                                                      | 41.0 ms: 1.08x slower                                            |
| richards                   | 45.7 ms                                                      | 49.5 ms: 1.08x slower                                            |
| richards_super             | 51.3 ms                                                      | 55.6 ms: 1.08x slower                                            |
| unpack_sequence            | 53.2 ns                                                      | 58.9 ns: 1.11x slower                                            |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                            |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                             |
| tomli_loads                | 2.16 sec                                                     | 2.50 sec: 1.16x slower                                           |
| telco                      | 6.96 ms                                                      | 8.23 ms: 1.18x slower                                            |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                            |
| python_startup             | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 5.32 ms: 1.53x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.97 ms: 1.86x slower                                            |
| bench_mp_pool              | 4.76 ms                                                      | 1.94 sec: 406.71x slower                                         |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                     |

Benchmark hidden because not significant (4): asyncio_websockets, sqlglot_transpile, xml_etree_parse, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 96.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x