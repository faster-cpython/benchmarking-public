# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 320 ms: 1.12x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.82 ms: 1.08x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| tornado_http   | 121 ms                                                       | 127 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 356 ms: 1.21x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 448 ms: 1.21x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 453 ms: 1.20x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 888 ms: 1.19x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 886 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 600 ms: 1.16x faster                                                         |
| async_tree_none            | 452 ms                                                       | 395 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 617 ms: 1.13x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 101 ms: 1.32x slower                                                         |
| nbody          | 88.0 ms                                                      | 130 ms: 1.48x slower                                                         |
| Geometric mean | (ref)                                                        | 1.25x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                        |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| regex_compile  | 144 ms                                                       | 204 ms: 1.41x slower                                                         |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.2 us: 1.04x faster                                                        |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                         |
| unpickle_list        | 4.66 us                                                      | 4.67 us: 1.00x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 90.3 ms: 1.05x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 62.4 ms: 1.07x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.90 sec: 1.34x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 303 us: 1.45x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                        |
| python_startup_no_site | 8.64 ms                                                      | 11.1 ms: 1.28x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.2 ms: 1.11x slower                                                        |
| mako            | 10.0 ms                                                      | 14.5 ms: 1.45x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.27x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 356 ms: 1.21x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 448 ms: 1.21x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 453 ms: 1.20x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 888 ms: 1.19x faster                                                         |
| typing_runtime_protocols   | 152 us                                                       | 129 us: 1.18x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 886 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 600 ms: 1.16x faster                                                         |
| async_tree_none            | 452 ms                                                       | 395 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 617 ms: 1.13x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.6 ms: 1.11x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 31.2 us: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.39 us: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                         |
| unpickle_list              | 4.66 us                                                      | 4.67 us: 1.00x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.59 sec: 1.00x slower                                                       |
| logging_simple             | 6.71 us                                                      | 6.76 us: 1.01x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.42 us: 1.01x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| dask                       | 392 ms                                                       | 410 ms: 1.05x slower                                                         |
| tornado_http               | 121 ms                                                       | 127 ms: 1.05x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 90.3 ms: 1.05x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 62.4 ms: 1.07x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| deepcopy                   | 368 us                                                       | 396 us: 1.07x slower                                                         |
| chameleon                  | 7.23 ms                                                      | 7.82 ms: 1.08x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.09x slower                                                         |
| gunicorn                   | 1.00 ms                                                      | 1.09 ms: 1.09x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 26.1 ms: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.36 sec: 1.10x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.96 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.10x slower                                                         |
| aiohttp                    | 1.02 ms                                                      | 1.12 ms: 1.10x slower                                                        |
| python_startup             | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                        |
| django_template            | 38.2 ms                                                      | 42.2 ms: 1.11x slower                                                        |
| meteor_contest             | 128 ms                                                       | 143 ms: 1.11x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                         |
| 2to3                       | 285 ms                                                       | 320 ms: 1.12x slower                                                         |
| sympy_str                  | 302 ms                                                       | 340 ms: 1.12x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.55 ms: 1.13x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 92.2 ms: 1.15x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 66.3 ms: 1.15x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 42.5 us: 1.15x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 75.8 ms: 1.16x slower                                                        |
| sympy_expand               | 484 ms                                                       | 568 ms: 1.17x slower                                                         |
| raytrace                   | 298 ms                                                       | 355 ms: 1.19x slower                                                         |
| comprehensions             | 21.9 us                                                      | 26.1 us: 1.19x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.5 ms: 1.21x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 980 ms: 1.21x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 2.01 sec: 1.21x slower                                                       |
| chaos                      | 64.0 ms                                                      | 77.9 ms: 1.22x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.49 ms: 1.22x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.98 ms: 1.23x slower                                                        |
| richards_super             | 51.3 ms                                                      | 64.8 ms: 1.26x slower                                                        |
| richards                   | 45.7 ms                                                      | 58.3 ms: 1.27x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.1 ms: 1.28x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 68.7 ns: 1.29x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.59 ms: 1.32x slower                                                        |
| float                      | 76.6 ms                                                      | 101 ms: 1.32x slower                                                         |
| go                         | 150 ms                                                       | 199 ms: 1.33x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 120 ms: 1.33x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.90 sec: 1.34x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 137 ms: 1.39x slower                                                         |
| regex_compile              | 144 ms                                                       | 204 ms: 1.41x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 303 us: 1.45x slower                                                         |
| mako                       | 10.0 ms                                                      | 14.5 ms: 1.45x slower                                                        |
| scimark_fft                | 301 ms                                                       | 444 ms: 1.47x slower                                                         |
| nbody                      | 88.0 ms                                                      | 130 ms: 1.48x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 102 ms: 1.48x slower                                                         |
| scimark_sor                | 109 ms                                                       | 162 ms: 1.49x slower                                                         |
| pyflate                    | 439 ms                                                       | 655 ms: 1.49x slower                                                         |
| fannkuch                   | 350 ms                                                       | 532 ms: 1.52x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.61 ms: 1.57x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 10.4 ms: 1.74x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 160 ms: 1.75x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                 |

Benchmark hidden because not significant (7): pickle_list, create_gc_cycles, async_generators, pidigits, bench_mp_pool, bench_thread_pool, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.05x


# Memory

- memory change: 0.91x