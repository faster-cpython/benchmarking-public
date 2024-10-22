# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: adf0b94
- commit date: 2024-07-19
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 342 ms: 1.20x slower                                        |
| docutils       | 2.87 sec                                                     | 3.43 sec: 1.20x slower                                      |
| tornado_http   | 121 ms                                                       | 127 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.14x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 318 ms: 1.36x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 399 ms: 1.35x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 425 ms: 1.28x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 826 ms: 1.27x faster                                        |
| async_tree_none            | 452 ms                                                       | 356 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 557 ms: 1.25x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 838 ms: 1.24x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 599 ms: 1.16x faster                                        |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                        |
| float          | 76.6 ms                                                      | 91.6 ms: 1.19x slower                                       |
| nbody          | 88.0 ms                                                      | 127 ms: 1.44x slower                                        |
| Geometric mean | (ref)                                                        | 1.18x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                        |
| regex_effbot   | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                       |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                       |
| regex_compile  | 144 ms                                                       | 213 ms: 1.48x slower                                        |
| Geometric mean | (ref)                                                        | 1.14x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 25.5 us: 1.04x slower                                       |
| xml_etree_iterparse  | 103 ms                                                       | 114 ms: 1.11x slower                                        |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                       |
| xml_etree_generate   | 86.1 ms                                                      | 97.8 ms: 1.14x slower                                       |
| xml_etree_process    | 58.4 ms                                                      | 68.7 ms: 1.18x slower                                       |
| pickle_pure_python   | 318 us                                                       | 427 us: 1.34x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.90 sec: 1.34x slower                                      |
| unpickle_pure_python | 210 us                                                       | 301 us: 1.44x slower                                        |
| Geometric mean       | (ref)                                                        | 1.18x slower                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.14 ms: 1.06x slower                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                       |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 46.3 ms: 1.21x slower                                       |
| mako            | 10.0 ms                                                      | 14.5 ms: 1.45x slower                                       |
| Geometric mean  | (ref)                                                        | 1.33x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 318 ms: 1.36x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 399 ms: 1.35x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 425 ms: 1.28x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 826 ms: 1.27x faster                                        |
| async_tree_none            | 452 ms                                                       | 356 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 557 ms: 1.25x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 838 ms: 1.24x faster                                        |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 599 ms: 1.16x faster                                        |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                       |
| deepcopy                   | 368 us                                                       | 351 us: 1.05x faster                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                        |
| logging_format             | 7.48 us                                                      | 7.33 us: 1.02x faster                                       |
| logging_simple             | 6.71 us                                                      | 6.65 us: 1.01x faster                                       |
| async_generators           | 390 ms                                                       | 388 ms: 1.01x faster                                        |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.61 sec: 1.01x slower                                      |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                        |
| regex_effbot               | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.47 us: 1.03x slower                                       |
| asyncio_tcp                | 378 ms                                                       | 392 ms: 1.04x slower                                        |
| bench_thread_pool          | 950 us                                                       | 987 us: 1.04x slower                                        |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.04x slower                                       |
| tornado_http               | 121 ms                                                       | 127 ms: 1.05x slower                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.14 ms: 1.06x slower                                       |
| mdp                        | 2.57 sec                                                     | 2.74 sec: 1.07x slower                                      |
| dask                       | 392 ms                                                       | 421 ms: 1.07x slower                                        |
| raytrace                   | 298 ms                                                       | 322 ms: 1.08x slower                                        |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                       |
| xml_etree_iterparse        | 103 ms                                                       | 114 ms: 1.11x slower                                        |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                       |
| json                       | 5.12 ms                                                      | 5.78 ms: 1.13x slower                                       |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                        |
| xml_etree_generate         | 86.1 ms                                                      | 97.8 ms: 1.14x slower                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                       |
| crypto_pyaes               | 80.3 ms                                                      | 93.4 ms: 1.16x slower                                       |
| sympy_sum                  | 162 ms                                                       | 190 ms: 1.17x slower                                        |
| sympy_integrate            | 23.9 ms                                                      | 28.1 ms: 1.17x slower                                       |
| xml_etree_process          | 58.4 ms                                                      | 68.7 ms: 1.18x slower                                       |
| pycparser                  | 1.23 sec                                                     | 1.45 sec: 1.18x slower                                      |
| dulwich_log                | 65.4 ms                                                      | 77.8 ms: 1.19x slower                                       |
| float                      | 76.6 ms                                                      | 91.6 ms: 1.19x slower                                       |
| docutils                   | 2.87 sec                                                     | 3.43 sec: 1.20x slower                                      |
| coverage                   | 66.7 ms                                                      | 80.0 ms: 1.20x slower                                       |
| 2to3                       | 285 ms                                                       | 342 ms: 1.20x slower                                        |
| django_template            | 38.2 ms                                                      | 46.3 ms: 1.21x slower                                       |
| sqlglot_normalize          | 116 ms                                                       | 140 ms: 1.21x slower                                        |
| sympy_str                  | 302 ms                                                       | 370 ms: 1.23x slower                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 70.6 ms: 1.23x slower                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 2.19 ms: 1.23x slower                                       |
| chaos                      | 64.0 ms                                                      | 79.5 ms: 1.24x slower                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.73 ms: 1.26x slower                                       |
| comprehensions             | 21.9 us                                                      | 27.6 us: 1.26x slower                                       |
| richards                   | 45.7 ms                                                      | 57.9 ms: 1.27x slower                                       |
| richards_super             | 51.3 ms                                                      | 65.2 ms: 1.27x slower                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                       |
| nqueens                    | 89.9 ms                                                      | 114 ms: 1.27x slower                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.13 sec: 1.28x slower                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.04 sec: 1.29x slower                                      |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                       |
| sympy_expand               | 484 ms                                                       | 628 ms: 1.30x slower                                        |
| deltablue                  | 3.24 ms                                                      | 4.25 ms: 1.31x slower                                       |
| telco                      | 6.96 ms                                                      | 9.17 ms: 1.32x slower                                       |
| typing_runtime_protocols   | 152 us                                                       | 203 us: 1.34x slower                                        |
| pickle_pure_python         | 318 us                                                       | 427 us: 1.34x slower                                        |
| tomli_loads                | 2.16 sec                                                     | 2.90 sec: 1.34x slower                                      |
| go                         | 150 ms                                                       | 202 ms: 1.35x slower                                        |
| deepcopy_memo              | 36.8 us                                                      | 50.0 us: 1.36x slower                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 94.4 ms: 1.37x slower                                       |
| pyflate                    | 439 ms                                                       | 616 ms: 1.40x slower                                        |
| fannkuch                   | 350 ms                                                       | 500 ms: 1.43x slower                                        |
| unpickle_pure_python       | 210 us                                                       | 301 us: 1.44x slower                                        |
| nbody                      | 88.0 ms                                                      | 127 ms: 1.44x slower                                        |
| scimark_fft                | 301 ms                                                       | 433 ms: 1.44x slower                                        |
| mako                       | 10.0 ms                                                      | 14.5 ms: 1.45x slower                                       |
| scimark_lu                 | 98.8 ms                                                      | 144 ms: 1.45x slower                                        |
| regex_compile              | 144 ms                                                       | 213 ms: 1.48x slower                                        |
| scimark_sor                | 109 ms                                                       | 161 ms: 1.48x slower                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.81 ms: 1.62x slower                                       |
| spectral_norm              | 91.6 ms                                                      | 150 ms: 1.63x slower                                        |
| logging_silent             | 94.4 ns                                                      | 157 ns: 1.66x slower                                        |
| hexiom                     | 5.96 ms                                                      | 10.5 ms: 1.76x slower                                       |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                |

Benchmark hidden because not significant (3): xml_etree_parse, coroutines, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240719-3.14.0a0-adf0b94-PYTHON_UOPS/bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 0.95x