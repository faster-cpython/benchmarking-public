# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.39x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 424 ms: 1.49x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.37 sec: 1.18x slower                                                      |
| tornado_http   | 121 ms                                                       | 166 ms: 1.37x slower                                                        |
| Geometric mean | (ref)                                                        | 1.34x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 878 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 364 ms: 1.18x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 467 ms: 1.16x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 928 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 625 ms: 1.12x faster                                                        |
| async_tree_none            | 452 ms                                                       | 411 ms: 1.10x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 511 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 673 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 142 ms: 1.85x slower                                                        |
| nbody          | 88.0 ms                                                      | 191 ms: 2.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.56x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                       |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 28.0 ms: 1.19x slower                                                       |
| regex_compile  | 144 ms                                                       | 224 ms: 1.56x slower                                                        |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| pickle               | 10.5 us                                                      | 10.4 us: 1.02x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 32.6 us: 1.00x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.53 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 107 ms: 1.04x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.31 us: 1.14x slower                                                       |
| unpickle             | 14.8 us                                                      | 17.4 us: 1.18x slower                                                       |
| json_loads           | 24.4 us                                                      | 28.8 us: 1.18x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 113 ms: 1.31x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.9 ms: 1.36x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.33 sec: 1.54x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 91.6 ms: 1.57x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 583 us: 1.83x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 399 us: 1.90x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.5 ms: 1.51x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.44x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 66.4 ms: 1.74x slower                                                       |
| mako            | 10.0 ms                                                      | 21.4 ms: 2.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.93x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 878 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 364 ms: 1.18x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 467 ms: 1.16x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.04 ms: 1.14x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 928 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 625 ms: 1.12x faster                                                        |
| async_tree_none            | 452 ms                                                       | 411 ms: 1.10x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 511 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 673 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 379 ms: 1.02x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.02x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 32.6 us: 1.00x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.53 us: 1.02x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 107 ms: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.67 ms: 1.05x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 3.00 us: 1.08x slower                                                       |
| generators                 | 37.4 ms                                                      | 41.4 ms: 1.11x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.80 sec: 1.14x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 5.31 us: 1.14x slower                                                       |
| deepcopy                   | 368 us                                                       | 430 us: 1.17x slower                                                        |
| unpickle                   | 14.8 us                                                      | 17.4 us: 1.18x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.37 sec: 1.18x slower                                                      |
| json                       | 5.12 ms                                                      | 6.03 ms: 1.18x slower                                                       |
| json_loads                 | 24.4 us                                                      | 28.8 us: 1.18x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 28.0 ms: 1.19x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 452 ms: 1.20x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 27.8 ms: 1.21x slower                                                       |
| async_generators           | 390 ms                                                       | 489 ms: 1.25x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.25 sec: 1.27x slower                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 113 ms: 1.31x slower                                                        |
| meteor_contest             | 128 ms                                                       | 169 ms: 1.32x slower                                                        |
| comprehensions             | 21.9 us                                                      | 29.1 us: 1.33x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 49.2 us: 1.34x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.63 ms: 1.34x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 32.2 ms: 1.35x slower                                                       |
| scimark_fft                | 301 ms                                                       | 407 ms: 1.35x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.9 ms: 1.36x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 89.1 ms: 1.36x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.61 us: 1.37x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                       |
| tornado_http               | 121 ms                                                       | 166 ms: 1.37x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.70 sec: 1.38x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 129 ms: 1.44x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 118 ms: 1.47x slower                                                        |
| sympy_str                  | 302 ms                                                       | 446 ms: 1.48x slower                                                        |
| 2to3                       | 285 ms                                                       | 424 ms: 1.49x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.4 ms: 1.50x slower                                                       |
| python_startup             | 11.6 ms                                                      | 17.5 ms: 1.51x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 3.33 sec: 1.54x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 180 ms: 1.56x slower                                                        |
| regex_compile              | 144 ms                                                       | 224 ms: 1.56x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 91.6 ms: 1.57x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 91.1 ms: 1.58x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 260 ms: 1.60x slower                                                        |
| coverage                   | 66.7 ms                                                      | 108 ms: 1.61x slower                                                        |
| fannkuch                   | 350 ms                                                       | 575 ms: 1.64x slower                                                        |
| sympy_expand               | 484 ms                                                       | 811 ms: 1.68x slower                                                        |
| logging_format             | 7.48 us                                                      | 12.6 us: 1.69x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.37 sec: 1.69x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.81 sec: 1.70x slower                                                      |
| pyflate                    | 439 ms                                                       | 760 ms: 1.73x slower                                                        |
| logging_simple             | 6.71 us                                                      | 11.6 us: 1.74x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 263 us: 1.74x slower                                                        |
| django_template            | 38.2 ms                                                      | 66.4 ms: 1.74x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 160 ms: 1.75x slower                                                        |
| richards                   | 45.7 ms                                                      | 79.9 ms: 1.75x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.70 ms: 1.79x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 583 us: 1.83x slower                                                        |
| float                      | 76.6 ms                                                      | 142 ms: 1.85x slower                                                        |
| richards_super             | 51.3 ms                                                      | 96.3 ms: 1.88x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 177 ns: 1.88x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.35 ms: 1.89x slower                                                       |
| chaos                      | 64.0 ms                                                      | 122 ms: 1.90x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 399 us: 1.90x slower                                                        |
| go                         | 150 ms                                                       | 285 ms: 1.90x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 11.4 ms: 1.91x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 133 ms: 1.93x slower                                                        |
| raytrace                   | 298 ms                                                       | 596 ms: 2.00x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.84 ms: 2.06x slower                                                       |
| mako                       | 10.0 ms                                                      | 21.4 ms: 2.14x slower                                                       |
| nbody                      | 88.0 ms                                                      | 191 ms: 2.17x slower                                                        |
| scimark_sor                | 109 ms                                                       | 244 ms: 2.24x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 228 ms: 2.30x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 131 ns: 2.46x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.16 ms: 2.52x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.39x slower                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.29x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.07x