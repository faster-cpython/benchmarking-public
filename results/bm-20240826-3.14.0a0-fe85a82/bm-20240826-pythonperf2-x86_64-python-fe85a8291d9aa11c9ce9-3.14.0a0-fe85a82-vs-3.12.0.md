# Results vs. 3.12.0

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-x86_64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.03x faster
- HPT reliability: 82.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.32x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 802 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 547 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                       |
| float          | 76.6 ms                                                      | 79.5 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_dna      | 239 ms                                                       | 254 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| django_template | 38.2 ms                                                      | 40.4 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.32x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 802 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 547 ms: 1.27x faster                                                        |
| deepcopy                   | 368 us                                                       | 291 us: 1.27x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.8 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 856 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.0 ms: 1.10x faster                                                       |
| raytrace                   | 298 ms                                                       | 272 ms: 1.10x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| async_generators           | 390 ms                                                       | 363 ms: 1.08x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.48 ms: 1.06x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.7 ms: 1.05x faster                                                       |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.2 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.44 us: 1.04x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.03x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 87.7 ms: 1.02x faster                                                       |
| nbody                      | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 804 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x slower                                                        |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                        |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 395 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 59.2 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.33 ms: 1.03x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.9 ns: 1.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 79.5 ms: 1.04x slower                                                       |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.29 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.7 ms: 1.06x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.4 ms: 1.06x slower                                                       |
| regex_dna                  | 239 ms                                                       | 254 ms: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 471 ms: 1.07x slower                                                        |
| richards_super             | 51.3 ms                                                      | 55.7 ms: 1.08x slower                                                       |
| richards                   | 45.7 ms                                                      | 49.6 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.26 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.89 ms: 1.19x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                                      |
| go                         | 150 ms                                                       | 179 ms: 1.20x slower                                                        |
| coverage                   | 66.7 ms                                                      | 81.8 ms: 1.23x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.43 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): pycparser, regex_effbot
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240826-3.14.0a0-fe85a82/bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 82.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x