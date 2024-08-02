# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.02x slower
- HPT reliability: 80.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 308 ms: 1.08x slower                                                          |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.09x slower                                                        |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 427 ms: 1.27x faster                                                          |
| async_tree_none_tg         | 431 ms                                                       | 343 ms: 1.26x faster                                                          |
| async_tree_none            | 452 ms                                                       | 373 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                                          |
| async_tree_io              | 1.04 sec                                                     | 883 ms: 1.18x faster                                                          |
| async_tree_io_tg           | 1.05 sec                                                     | 897 ms: 1.17x faster                                                          |
| async_tree_memoization     | 544 ms                                                       | 474 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 623 ms: 1.12x faster                                                          |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                          |
| nbody          | 88.0 ms                                                      | 84.3 ms: 1.04x faster                                                         |
| float          | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                                         |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                          |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                          |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.5 ms: 1.06x faster                                                         |
| pickle_dict          | 32.5 us                                                      | 31.6 us: 1.03x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                          |
| unpickle_list        | 4.66 us                                                      | 4.73 us: 1.01x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                          |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.7 us: 1.06x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 224 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                  |

Benchmark hidden because not significant (4): pickle_list, xml_etree_parse, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.41 ms: 1.09x slower                                                         |
| python_startup         | 11.6 ms                                                      | 13.7 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.13x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.27 ms: 1.08x faster                                                         |
| django_template | 38.2 ms                                                      | 43.0 ms: 1.13x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 427 ms: 1.27x faster                                                          |
| async_tree_none_tg         | 431 ms                                                       | 343 ms: 1.26x faster                                                          |
| async_tree_none            | 452 ms                                                       | 373 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                                          |
| comprehensions             | 21.9 us                                                      | 18.4 us: 1.19x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 883 ms: 1.18x faster                                                          |
| async_tree_io_tg           | 1.05 sec                                                     | 897 ms: 1.17x faster                                                          |
| async_tree_memoization     | 544 ms                                                       | 474 ms: 1.15x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 623 ms: 1.12x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 72.4 ms: 1.11x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 83.4 ms: 1.10x faster                                                         |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.27 ms: 1.08x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 81.5 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                          |
| logging_format             | 7.48 us                                                      | 7.12 us: 1.05x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.05x faster                                                         |
| raytrace                   | 298 ms                                                       | 285 ms: 1.05x faster                                                          |
| nbody                      | 88.0 ms                                                      | 84.3 ms: 1.04x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                                         |
| pickle_dict                | 32.5 us                                                      | 31.6 us: 1.03x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                          |
| logging_simple             | 6.71 us                                                      | 6.55 us: 1.02x faster                                                         |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                          |
| float                      | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                         |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 807 ms                                                       | 790 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                        |
| async_generators           | 390 ms                                                       | 392 ms: 1.00x slower                                                          |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                          |
| asyncio_tcp                | 378 ms                                                       | 381 ms: 1.01x slower                                                          |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                          |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 4.73 us: 1.01x slower                                                         |
| fannkuch                   | 350 ms                                                       | 355 ms: 1.01x slower                                                          |
| deepcopy_memo              | 36.8 us                                                      | 37.6 us: 1.02x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                          |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                          |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                         |
| chaos                      | 64.0 ms                                                      | 66.0 ms: 1.03x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.03x slower                                                          |
| dask                       | 392 ms                                                       | 405 ms: 1.03x slower                                                          |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.03x slower                                                         |
| pyflate                    | 439 ms                                                       | 454 ms: 1.04x slower                                                          |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                         |
| richards_super             | 51.3 ms                                                      | 53.3 ms: 1.04x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                         |
| sympy_str                  | 302 ms                                                       | 316 ms: 1.05x slower                                                          |
| unpickle                   | 14.8 us                                                      | 15.7 us: 1.06x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 224 us: 1.07x slower                                                          |
| 2to3                       | 285 ms                                                       | 308 ms: 1.08x slower                                                          |
| sympy_integrate            | 23.9 ms                                                      | 25.8 ms: 1.08x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.41 ms: 1.09x slower                                                         |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                          |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.09x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 98.7 ms: 1.10x slower                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.73 us: 1.11x slower                                                         |
| sympy_expand               | 484 ms                                                       | 538 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 57.5 ms                                                      | 64.2 ms: 1.12x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.12x slower                                                          |
| django_template            | 38.2 ms                                                      | 43.0 ms: 1.13x slower                                                         |
| deepcopy                   | 368 us                                                       | 423 us: 1.15x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 109 ns: 1.15x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 6.96 ms: 1.17x slower                                                         |
| python_startup             | 11.6 ms                                                      | 13.7 ms: 1.18x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.82 ms: 1.18x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.27 ms: 1.19x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                         |
| coverage                   | 66.7 ms                                                      | 80.3 ms: 1.20x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                          |
| scimark_sor                | 109 ms                                                       | 134 ms: 1.23x slower                                                          |
| scimark_lu                 | 98.8 ms                                                      | 122 ms: 1.24x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.28x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                  |

Benchmark hidden because not significant (11): pickle_list, xml_etree_parse, xml_etree_process, scimark_sparse_mat_mult, richards, scimark_monte_carlo, pickle, sqlite_synth, asyncio_websockets, bench_thread_pool, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240604-3.14.0a0-c73f8ac/bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 80.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x