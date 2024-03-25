# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.03x slower
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 302 ms: 1.06x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.29 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.04 sec: 1.06x slower                                                       |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 436 ms: 1.24x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 442 ms: 1.23x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 868 ms: 1.21x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 860 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                         |
| async_tree_none            | 452 ms                                                       | 385 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 608 ms: 1.15x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 262 ms: 1.01x faster                                                         |
| float          | 76.6 ms                                                      | 76.2 ms: 1.01x faster                                                        |
| nbody          | 88.0 ms                                                      | 100 ms: 1.14x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| regex_dna      | 239 ms                                                       | 249 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.6 us: 1.06x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 308 us: 1.03x faster                                                         |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.60 us: 1.01x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.49 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 230 us: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 14.2 ms: 1.22x slower                                                        |
| python_startup_no_site | 8.64 ms                                                      | 12.5 ms: 1.44x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.33x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 40.4 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 121 us: 1.25x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 436 ms: 1.24x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 442 ms: 1.23x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 868 ms: 1.21x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 860 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                         |
| async_tree_none            | 452 ms                                                       | 385 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 608 ms: 1.15x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.3 ms: 1.13x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.6 us: 1.12x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.6 us: 1.06x faster                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.50 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 308 us: 1.03x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 78.6 ms: 1.02x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.35 us: 1.02x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                        |
| async_generators           | 390 ms                                                       | 383 ms: 1.02x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                        |
| pidigits                   | 265 ms                                                       | 262 ms: 1.01x faster                                                         |
| unpickle_list              | 4.66 us                                                      | 4.60 us: 1.01x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.64 us: 1.01x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| float                      | 76.6 ms                                                      | 76.2 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| chameleon                  | 7.23 ms                                                      | 7.29 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.49 us: 1.01x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                         |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                         |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.02x slower                                                        |
| dask                       | 392 ms                                                       | 399 ms: 1.02x slower                                                         |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.9 ns: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| deepcopy                   | 368 us                                                       | 380 us: 1.03x slower                                                         |
| deepcopy_memo              | 36.8 us                                                      | 38.0 us: 1.03x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.71 sec: 1.03x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 94.9 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 837 ms: 1.04x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.9 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.04x slower                                                         |
| raytrace                   | 298 ms                                                       | 311 ms: 1.04x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 25.1 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.39 ms: 1.05x slower                                                        |
| scimark_fft                | 301 ms                                                       | 318 ms: 1.06x slower                                                         |
| chaos                      | 64.0 ms                                                      | 67.6 ms: 1.06x slower                                                        |
| sympy_expand               | 484 ms                                                       | 512 ms: 1.06x slower                                                         |
| django_template            | 38.2 ms                                                      | 40.4 ms: 1.06x slower                                                        |
| 2to3                       | 285 ms                                                       | 302 ms: 1.06x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.04 sec: 1.06x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 123 ms: 1.06x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.09 ms: 1.09x slower                                                        |
| aiohttp                    | 1.02 ms                                                      | 1.11 ms: 1.09x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 230 us: 1.10x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 63.0 ms: 1.10x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 75.9 ms: 1.10x slower                                                        |
| richards                   | 45.7 ms                                                      | 50.9 ms: 1.11x slower                                                        |
| richards_super             | 51.3 ms                                                      | 57.2 ms: 1.11x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.13x slower                                                         |
| nbody                      | 88.0 ms                                                      | 100 ms: 1.14x slower                                                         |
| fannkuch                   | 350 ms                                                       | 398 ms: 1.14x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.70 ms: 1.14x slower                                                        |
| go                         | 150 ms                                                       | 172 ms: 1.15x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.14 ms: 1.17x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.17x slower                                                         |
| pyflate                    | 439 ms                                                       | 523 ms: 1.19x slower                                                         |
| python_startup             | 11.6 ms                                                      | 14.2 ms: 1.22x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.34 ms: 1.23x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.30 ms: 1.24x slower                                                        |
| coverage                   | 66.7 ms                                                      | 84.1 ms: 1.26x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 73.6 ns: 1.38x slower                                                        |
| scimark_sor                | 109 ms                                                       | 152 ms: 1.39x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 12.5 ms: 1.44x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (9): bench_thread_pool, mypy2, deepcopy_reduce, asyncio_tcp_ssl, asyncio_tcp, sympy_str, mako, xml_etree_process, bench_mp_pool
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.74% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.03x