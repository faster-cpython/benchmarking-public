# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: linux-x86_64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 273 ms: 1.05x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.82 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 607 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 316 ms: 1.71x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 258 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 520 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 539 ms: 1.29x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.5 ms: 1.14x faster                                                       |
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                       |
| pidigits       | 265 ms                                                       | 292 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 2.96 ms: 1.21x faster                                                       |
| regex_dna      | 239 ms                                                       | 218 ms: 1.10x faster                                                        |
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 76.9 ms: 1.12x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 54.1 ms: 1.08x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 201 us: 1.04x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 307 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.7 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 164 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.14 ms: 1.06x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 33.1 ms: 1.15x faster                                                       |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 607 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 316 ms: 1.71x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 258 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                        |
| comprehensions             | 21.9 us                                                      | 15.3 us: 1.43x faster                                                       |
| deepcopy                   | 368 us                                                       | 258 us: 1.43x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 26.7 us: 1.38x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 520 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 539 ms: 1.29x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.65 us: 1.27x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 72.0 ms: 1.27x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 2.96 ms: 1.21x faster                                                       |
| go                         | 150 ms                                                       | 125 ms: 1.20x faster                                                        |
| scimark_sor                | 109 ms                                                       | 92.0 ms: 1.18x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 58.4 ms: 1.18x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                       |
| django_template            | 38.2 ms                                                      | 33.1 ms: 1.15x faster                                                       |
| raytrace                   | 298 ms                                                       | 259 ms: 1.15x faster                                                        |
| chaos                      | 64.0 ms                                                      | 55.9 ms: 1.15x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 82.5 ns: 1.14x faster                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 139 ms: 1.14x faster                                                        |
| float                      | 76.6 ms                                                      | 67.5 ms: 1.14x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 20.4 ms: 1.13x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 76.9 ms: 1.12x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 88.8 ms: 1.11x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 147 ms: 1.10x faster                                                        |
| scimark_fft                | 301 ms                                                       | 274 ms: 1.10x faster                                                        |
| regex_dna                  | 239 ms                                                       | 218 ms: 1.10x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.13 us: 1.09x faster                                                       |
| pyflate                    | 439 ms                                                       | 403 ms: 1.09x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.2 ms: 1.09x faster                                                       |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.89 us: 1.09x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 54.1 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.54 sec: 1.08x faster                                                      |
| richards                   | 45.7 ms                                                      | 42.5 ms: 1.08x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.65 ms: 1.07x faster                                                       |
| sympy_str                  | 302 ms                                                       | 282 ms: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.3 ms: 1.07x faster                                                       |
| richards_super             | 51.3 ms                                                      | 48.2 ms: 1.06x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                                      |
| nqueens                    | 89.9 ms                                                      | 84.7 ms: 1.06x faster                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.30 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 766 ms: 1.05x faster                                                        |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 902 us: 1.05x faster                                                        |
| 2to3                       | 285 ms                                                       | 273 ms: 1.05x faster                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 55.1 ms: 1.04x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 201 us: 1.04x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 307 us: 1.04x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 112 ms: 1.04x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.76 ms: 1.04x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.15 ms: 1.03x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| docutils                   | 2.87 sec                                                     | 2.82 sec: 1.02x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| sympy_expand               | 484 ms                                                       | 481 ms: 1.01x faster                                                        |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                       |
| mdp                        | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                      |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 157 us: 1.03x slower                                                        |
| coverage                   | 66.7 ms                                                      | 70.2 ms: 1.05x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.7 us: 1.05x slower                                                       |
| async_generators           | 390 ms                                                       | 412 ms: 1.06x slower                                                        |
| fannkuch                   | 350 ms                                                       | 370 ms: 1.06x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.14 ms: 1.06x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                       |
| pidigits                   | 265 ms                                                       | 292 ms: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.79 ms: 1.12x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 164 ms: 1.14x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.33 ms: 1.53x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.86 ms: 1.80x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 925 ms: 194.26x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (4): sqlite_synth, asyncio_websockets, scimark_sparse_mat_mult, dulwich_log
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x