# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x slower
- HPT reliability: 56.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| chameleon      | 7.23 ms                                                      | 7.68 ms: 1.06x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| tornado_http   | 121 ms                                                       | 124 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 432 ms: 1.25x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 348 ms: 1.24x faster                                                        |
| async_tree_none            | 452 ms                                                       | 376 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 470 ms: 1.16x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 903 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 624 ms: 1.12x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.6 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 74.2 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 32.0 us: 1.02x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                       |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.00x slower                                                       |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.79 us: 1.03x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.48 ms: 1.10x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.14 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 41.4 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 432 ms: 1.25x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 348 ms: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.9 us: 1.22x faster                                                       |
| async_tree_none            | 452 ms                                                       | 376 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.16x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 470 ms: 1.16x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 903 ms: 1.15x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 70.2 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 624 ms: 1.12x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.14 ms: 1.09x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.4 ms: 1.09x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 84.3 ms: 1.09x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.6 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.91 ms: 1.08x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.01 us: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 81.8 ms: 1.05x faster                                                       |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| fannkuch                   | 350 ms                                                       | 336 ms: 1.04x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.45 us: 1.04x faster                                                       |
| float                      | 76.6 ms                                                      | 74.2 ms: 1.03x faster                                                       |
| async_generators           | 390 ms                                                       | 380 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                      |
| pickle_dict                | 32.5 us                                                      | 32.0 us: 1.02x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 802 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.00x slower                                                       |
| chaos                      | 64.0 ms                                                      | 64.4 ms: 1.01x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                                       |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 166 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.02x slower                                                       |
| tornado_http               | 121 ms                                                       | 124 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                       |
| richards_super             | 51.3 ms                                                      | 52.7 ms: 1.03x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 37.8 us: 1.03x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.79 us: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.30 ms: 1.04x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                      |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.04x slower                                                        |
| dask                       | 392 ms                                                       | 406 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| sympy_str                  | 302 ms                                                       | 314 ms: 1.04x slower                                                        |
| pyflate                    | 439 ms                                                       | 463 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.68 ms: 1.06x slower                                                       |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| go                         | 150 ms                                                       | 161 ms: 1.07x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 25.8 ms: 1.08x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.4 ms: 1.08x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 98.4 ms: 1.09x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.48 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 63.1 ms: 1.10x slower                                                       |
| sympy_expand               | 484 ms                                                       | 533 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.74 us: 1.11x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.70 ms: 1.13x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 107 ns: 1.13x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.73 ms: 1.15x slower                                                       |
| deepcopy                   | 368 us                                                       | 427 us: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.17 ms: 1.17x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                       |
| scimark_sor                | 109 ms                                                       | 130 ms: 1.20x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 119 ms: 1.21x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.25x slower                                                       |
| coverage                   | 66.7 ms                                                      | 85.2 ms: 1.28x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.89 ms: 1.41x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (11): scimark_monte_carlo, bench_mp_pool, sqlite_synth, asyncio_tcp, pickle_pure_python, mdp, pprint_pformat, pickle_list, asyncio_websockets, richards, bench_thread_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 56.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x