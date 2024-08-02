# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x slower
- HPT reliability: 82.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 288 ms: 1.01x slower                                                        |
| chameleon      | 7.23 ms                                                      | 7.50 ms: 1.04x slower                                                       |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 435 ms: 1.24x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 351 ms: 1.23x faster                                                        |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 907 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 917 ms: 1.15x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 483 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 627 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 79.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| regex_compile  | 144 ms                                                       | 144 ms: 1.00x slower                                                        |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.5 us: 1.03x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.39 us: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 86.4 ms: 1.00x slower                                                       |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.01x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.73 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.8 ms: 1.04x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.48 sec: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.1 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 40.1 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 435 ms: 1.24x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 351 ms: 1.23x faster                                                        |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 907 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 917 ms: 1.15x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 483 ms: 1.13x faster                                                        |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 627 ms: 1.11x faster                                                        |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.10x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.6 ms: 1.08x faster                                                       |
| async_generators           | 390 ms                                                       | 367 ms: 1.06x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.15 us: 1.05x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.04x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 915 us: 1.04x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| chaos                      | 64.0 ms                                                      | 61.9 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| pickle_dict                | 32.5 us                                                      | 31.5 us: 1.03x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                       |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                        |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 97.3 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.39 us: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 86.4 ms: 1.00x slower                                                       |
| regex_compile              | 144 ms                                                       | 144 ms: 1.00x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 288 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| dask                       | 392 ms                                                       | 397 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.27 ms: 1.01x slower                                                       |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.02x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.73 us: 1.02x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                                       |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 357 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 826 ms: 1.02x slower                                                        |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 59.5 ms: 1.04x slower                                                       |
| chameleon                  | 7.23 ms                                                      | 7.50 ms: 1.04x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.8 ms: 1.04x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.50 us: 1.04x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 93.4 ms: 1.04x slower                                                       |
| go                         | 150 ms                                                       | 156 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.3 ns: 1.04x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 60.8 ms: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 79.9 ms: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.04x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                                        |
| sympy_expand               | 484 ms                                                       | 507 ms: 1.05x slower                                                        |
| django_template            | 38.2 ms                                                      | 40.1 ms: 1.05x slower                                                       |
| deepcopy                   | 368 us                                                       | 388 us: 1.05x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 39.1 us: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 97.9 ms: 1.07x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.38 ms: 1.07x slower                                                       |
| pyflate                    | 439 ms                                                       | 478 ms: 1.09x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.1 ms: 1.13x slower                                                       |
| richards                   | 45.7 ms                                                      | 51.9 ms: 1.13x slower                                                       |
| scimark_sor                | 109 ms                                                       | 124 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                        |
| richards_super             | 51.3 ms                                                      | 58.9 ms: 1.15x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.48 sec: 1.15x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.33 ms: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.2 ms: 1.22x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.71 ms: 1.36x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (4): sqlglot_transpile, bench_mp_pool, xml_etree_iterparse, nbody
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 82.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.92x