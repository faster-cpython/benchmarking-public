# Results vs. 3.12.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 68.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.00x slower                                                    |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                  |
| tornado_http   | 121 ms                                                       | 118 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 326 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 431 ms                                                       | 312 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                    |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                    |
| async_tree_io_tg           | 1.05 sec                                                     | 784 ms: 1.34x faster                                                    |
| async_tree_io              | 1.04 sec                                                     | 807 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 570 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                    |
| nbody          | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                   |
| float          | 76.6 ms                                                      | 80.4 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                   |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                    |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                    |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 29.8 us: 1.09x faster                                                   |
| pickle_list          | 4.43 us                                                      | 4.13 us: 1.07x faster                                                   |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.01x faster                                                    |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                    |
| xml_etree_generate   | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                                   |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                   |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                   |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.05x slower                                                   |
| unpickle_pure_python | 210 us                                                       | 226 us: 1.08x slower                                                    |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.56 sec: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                   |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| django_template | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 326 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 431 ms                                                       | 312 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                    |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                    |
| async_tree_io_tg           | 1.05 sec                                                     | 784 ms: 1.34x faster                                                    |
| async_tree_io              | 1.04 sec                                                     | 807 ms: 1.29x faster                                                    |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                    |
| generators                 | 37.4 ms                                                      | 29.7 ms: 1.26x faster                                                   |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                   |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 570 ms: 1.22x faster                                                    |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 2.87 us: 1.18x faster                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 72.6 ms: 1.11x faster                                                   |
| bench_thread_pool          | 950 us                                                       | 859 us: 1.11x faster                                                    |
| pickle_dict                | 32.5 us                                                      | 29.8 us: 1.09x faster                                                   |
| async_generators           | 390 ms                                                       | 360 ms: 1.08x faster                                                    |
| go                         | 150 ms                                                       | 139 ms: 1.08x faster                                                    |
| unpack_sequence            | 53.2 ns                                                      | 49.4 ns: 1.08x faster                                                   |
| pickle_list                | 4.43 us                                                      | 4.13 us: 1.07x faster                                                   |
| raytrace                   | 298 ms                                                       | 278 ms: 1.07x faster                                                    |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                    |
| logging_format             | 7.48 us                                                      | 7.12 us: 1.05x faster                                                   |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                    |
| logging_simple             | 6.71 us                                                      | 6.47 us: 1.04x faster                                                   |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                   |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                   |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                    |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                   |
| nbody                      | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                   |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                    |
| asyncio_tcp                | 378 ms                                                       | 367 ms: 1.03x faster                                                    |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.03x faster                                                  |
| tornado_http               | 121 ms                                                       | 118 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.01x faster                                                    |
| chaos                      | 64.0 ms                                                      | 63.2 ms: 1.01x faster                                                   |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                    |
| xml_etree_generate         | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.3 ms: 1.01x faster                                                   |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                  |
| scimark_lu                 | 98.8 ms                                                      | 98.1 ms: 1.01x faster                                                   |
| 2to3                       | 285 ms                                                       | 287 ms: 1.00x slower                                                    |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                  |
| nqueens                    | 89.9 ms                                                      | 90.5 ms: 1.01x slower                                                   |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 807 ms                                                       | 816 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                   |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                    |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                   |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                  |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                    |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 58.5 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                    |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                   |
| dulwich_log                | 65.4 ms                                                      | 67.2 ms: 1.03x slower                                                   |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.04x slower                                                   |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                   |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                    |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.05x slower                                                   |
| logging_silent             | 94.4 ns                                                      | 98.8 ns: 1.05x slower                                                   |
| float                      | 76.6 ms                                                      | 80.4 ms: 1.05x slower                                                   |
| hexiom                     | 5.96 ms                                                      | 6.29 ms: 1.05x slower                                                   |
| spectral_norm              | 91.6 ms                                                      | 97.1 ms: 1.06x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.46 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 210 us                                                       | 226 us: 1.08x slower                                                    |
| django_template            | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                   |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                   |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.09x slower                                                    |
| deltablue                  | 3.24 ms                                                      | 3.51 ms: 1.09x slower                                                   |
| fannkuch                   | 350 ms                                                       | 380 ms: 1.09x slower                                                    |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                   |
| pyflate                    | 439 ms                                                       | 484 ms: 1.10x slower                                                    |
| richards_super             | 51.3 ms                                                      | 57.9 ms: 1.13x slower                                                   |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                    |
| richards                   | 45.7 ms                                                      | 52.0 ms: 1.14x slower                                                   |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                   |
| coverage                   | 66.7 ms                                                      | 77.4 ms: 1.16x slower                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.56 sec: 1.19x slower                                                  |
| telco                      | 6.96 ms                                                      | 8.35 ms: 1.20x slower                                                   |
| create_gc_cycles           | 1.59 ms                                                      | 1.95 ms: 1.22x slower                                                   |
| gc_traversal               | 3.48 ms                                                      | 4.42 ms: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (4): sqlite_synth, xml_etree_parse, bench_mp_pool, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 68.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x