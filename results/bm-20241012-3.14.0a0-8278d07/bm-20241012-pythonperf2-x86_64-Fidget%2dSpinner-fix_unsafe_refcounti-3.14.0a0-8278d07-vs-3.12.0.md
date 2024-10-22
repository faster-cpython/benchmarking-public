# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.04x slower
- HPT reliability: 94.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                                  |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                                |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 321 ms: 1.41x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 393 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 783 ms: 1.35x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 550 ms: 1.27x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                                  |
| nbody          | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                                 |
| float          | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                                 |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                                  |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                                  |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.4 us: 1.07x faster                                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 84.9 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.01x faster                                                                  |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.01x faster                                                                  |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                                 |
| unpickle_list        | 4.66 us                                                      | 4.69 us: 1.01x slower                                                                 |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                                  |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                                 |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.02x slower                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                                 |
| pickle_list          | 4.43 us                                                      | 4.57 us: 1.03x slower                                                                 |
| unpickle             | 14.8 us                                                      | 15.7 us: 1.06x slower                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.50 sec: 1.16x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 12.1 ms: 1.18x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                                 |
| django_template | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 321 ms: 1.41x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 393 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 783 ms: 1.35x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                                  |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                                 |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 550 ms: 1.27x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                                 |
| raytrace                   | 298 ms                                                       | 267 ms: 1.11x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.1 ms: 1.10x faster                                                                 |
| go                         | 150 ms                                                       | 137 ms: 1.09x faster                                                                  |
| unpack_sequence            | 53.2 ns                                                      | 49.1 ns: 1.08x faster                                                                 |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 888 us: 1.07x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                                 |
| pickle_dict                | 32.5 us                                                      | 30.4 us: 1.07x faster                                                                 |
| logging_format             | 7.48 us                                                      | 7.08 us: 1.06x faster                                                                 |
| async_generators           | 390 ms                                                       | 371 ms: 1.05x faster                                                                  |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.3 ms: 1.05x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.04x faster                                                                  |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                                  |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.4 ms: 1.04x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                                 |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 784 ms: 1.03x faster                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                                 |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.13 ms: 1.02x faster                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                                |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 84.9 ms: 1.02x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.01x faster                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                                 |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                                  |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                                |
| chaos                      | 64.0 ms                                                      | 63.5 ms: 1.01x faster                                                                 |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.01x faster                                                                  |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                                 |
| unpickle_list              | 4.66 us                                                      | 4.69 us: 1.01x slower                                                                 |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 65.9 ms: 1.01x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 353 ms: 1.01x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                                |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                                 |
| sympy_expand               | 484 ms                                                       | 495 ms: 1.02x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.02x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                                 |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                                 |
| pickle_list                | 4.43 us                                                      | 4.57 us: 1.03x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 59.5 ms: 1.04x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                                 |
| logging_silent             | 94.4 ns                                                      | 98.2 ns: 1.04x slower                                                                 |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.26 ms: 1.05x slower                                                                 |
| float                      | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                                 |
| spectral_norm              | 91.6 ms                                                      | 96.5 ms: 1.05x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.39 ms: 1.05x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 24.9 ms: 1.06x slower                                                                 |
| unpickle                   | 14.8 us                                                      | 15.7 us: 1.06x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                                 |
| richards                   | 45.7 ms                                                      | 49.3 ms: 1.08x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 56.2 ms: 1.09x slower                                                                 |
| pyflate                    | 439 ms                                                       | 484 ms: 1.10x slower                                                                  |
| django_template            | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                                 |
| telco                      | 6.96 ms                                                      | 7.88 ms: 1.13x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.16x slower                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.50 sec: 1.16x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 12.1 ms: 1.18x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 78.9 ms: 1.18x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.06 ms: 1.29x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.74 ms: 1.36x slower                                                                 |
| bench_mp_pool              | 4.76 ms                                                      | 2.45 sec: 515.28x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                          |

Benchmark hidden because not significant (2): nqueens, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 94.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x