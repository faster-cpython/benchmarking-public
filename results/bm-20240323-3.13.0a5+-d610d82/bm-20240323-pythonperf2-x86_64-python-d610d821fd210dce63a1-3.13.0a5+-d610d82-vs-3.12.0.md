# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.01x faster
- HPT reliability: 79.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.36 ms: 1.02x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 343 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 431 ms: 1.25x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 438 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 859 ms: 1.23x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 851 ms: 1.22x faster                                                         |
| async_tree_none            | 452 ms                                                       | 379 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 601 ms: 1.16x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 262 ms: 1.01x faster                                                         |
| float          | 76.6 ms                                                      | 78.2 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                                         |
| regex_compile  | 144 ms                                                       | 144 ms: 1.00x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.70 ms: 1.03x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.9 us: 1.05x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 82.0 ms: 1.05x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.47 us: 1.04x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 307 us: 1.04x faster                                                         |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.37 us: 1.01x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.6 us: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.8 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.21 sec: 1.02x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 223 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.7 ms: 1.09x slower                                                        |
| python_startup_no_site | 8.64 ms                                                      | 11.0 ms: 1.27x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                        |
| django_template | 38.2 ms                                                      | 40.9 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 113 us: 1.35x faster                                                         |
| comprehensions             | 21.9 us                                                      | 16.7 us: 1.31x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 343 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 431 ms: 1.25x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 438 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 859 ms: 1.23x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 851 ms: 1.22x faster                                                         |
| async_tree_none            | 452 ms                                                       | 379 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 601 ms: 1.16x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 71.2 ms: 1.13x faster                                                        |
| raytrace                   | 298 ms                                                       | 265 ms: 1.12x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.5 ms: 1.12x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 48.2 ns: 1.10x faster                                                        |
| async_generators           | 390 ms                                                       | 354 ms: 1.10x faster                                                         |
| mypy2                      | 830 ms                                                       | 771 ms: 1.08x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                         |
| pickle_dict                | 32.5 us                                                      | 30.9 us: 1.05x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 902 us: 1.05x faster                                                         |
| chaos                      | 64.0 ms                                                      | 60.9 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.0 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.4 ms: 1.05x faster                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.52 ms: 1.04x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.0 ms: 1.04x faster                                                        |
| unpickle_list              | 4.66 us                                                      | 4.47 us: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 307 us: 1.04x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 87.5 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 789 ms: 1.02x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.30 us: 1.02x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.58 us: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.35 us: 1.02x faster                                                        |
| scimark_fft                | 301 ms                                                       | 296 ms: 1.02x faster                                                         |
| pickle_list                | 4.43 us                                                      | 4.37 us: 1.01x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.7 ms: 1.01x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 36.3 us: 1.01x faster                                                        |
| pidigits                   | 265 ms                                                       | 262 ms: 1.01x faster                                                         |
| unpickle                   | 14.8 us                                                      | 14.6 us: 1.01x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.8 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| regex_compile              | 144 ms                                                       | 144 ms: 1.00x faster                                                         |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 92.2 ms: 1.01x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.1 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.36 ms: 1.02x slower                                                        |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 96.2 ns: 1.02x slower                                                        |
| float                      | 76.6 ms                                                      | 78.2 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.21 sec: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.32 ms: 1.03x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.2 ms: 1.03x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.03x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.70 ms: 1.03x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 68.0 ms: 1.04x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                         |
| aiohttp                    | 1.02 ms                                                      | 1.07 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.40 ms: 1.05x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.35 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 223 us: 1.07x slower                                                         |
| django_template            | 38.2 ms                                                      | 40.9 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.52 ms: 1.09x slower                                                        |
| python_startup             | 11.6 ms                                                      | 12.7 ms: 1.09x slower                                                        |
| fannkuch                   | 350 ms                                                       | 385 ms: 1.10x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.91 ms: 1.14x slower                                                        |
| go                         | 150 ms                                                       | 173 ms: 1.16x slower                                                         |
| richards_super             | 51.3 ms                                                      | 60.4 ms: 1.18x slower                                                        |
| richards                   | 45.7 ms                                                      | 54.4 ms: 1.19x slower                                                        |
| pyflate                    | 439 ms                                                       | 525 ms: 1.20x slower                                                         |
| coverage                   | 66.7 ms                                                      | 79.9 ms: 1.20x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.30 ms: 1.24x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.0 ms: 1.27x slower                                                        |
| scimark_sor                | 109 ms                                                       | 140 ms: 1.28x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): nbody, asyncio_websockets, bench_mp_pool, tornado_http, deepcopy, dask, sqlglot_parse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 79.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.90x