# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 433 ms: 1.52x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.49 sec: 1.22x slower                                                      |
| tornado_http   | 121 ms                                                       | 163 ms: 1.34x slower                                                        |
| Geometric mean | (ref)                                                        | 1.35x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 369 ms: 1.17x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 903 ms: 1.17x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 478 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 645 ms: 1.08x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 968 ms: 1.08x faster                                                        |
| async_tree_none            | 452 ms                                                       | 429 ms: 1.05x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 540 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 256 ms: 1.03x faster                                                        |
| float          | 76.6 ms                                                      | 148 ms: 1.93x slower                                                        |
| nbody          | 88.0 ms                                                      | 204 ms: 2.32x slower                                                        |
| Geometric mean | (ref)                                                        | 1.63x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.33 ms: 1.07x faster                                                       |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 28.4 ms: 1.20x slower                                                       |
| regex_compile  | 144 ms                                                       | 231 ms: 1.61x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| json_loads           | 24.4 us                                                      | 30.5 us: 1.25x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 114 ms: 1.33x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.4 ms: 1.41x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.38 sec: 1.57x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 94.4 ms: 1.62x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 589 us: 1.85x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 418 us: 1.99x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.41x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.5 ms: 1.33x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.9 ms: 1.45x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.39x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 68.2 ms: 1.79x slower                                                       |
| mako            | 10.0 ms                                                      | 22.3 ms: 2.23x slower                                                       |
| Geometric mean  | (ref)                                                        | 2.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 369 ms: 1.17x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 903 ms: 1.17x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 478 ms: 1.13x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.10 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 645 ms: 1.08x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 968 ms: 1.08x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.44 ms: 1.07x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.33 ms: 1.07x faster                                                       |
| async_tree_none            | 452 ms                                                       | 429 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 256 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 540 ms: 1.01x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 19.8 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.75 ms: 1.10x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.79 sec: 1.13x slower                                                      |
| asyncio_tcp                | 378 ms                                                       | 452 ms: 1.20x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 28.4 ms: 1.20x slower                                                       |
| deepcopy                   | 368 us                                                       | 444 us: 1.21x slower                                                        |
| json                       | 5.12 ms                                                      | 6.18 ms: 1.21x slower                                                       |
| generators                 | 37.4 ms                                                      | 45.5 ms: 1.22x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.49 sec: 1.22x slower                                                      |
| json_loads                 | 24.4 us                                                      | 30.5 us: 1.25x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 28.8 ms: 1.25x slower                                                       |
| async_generators           | 390 ms                                                       | 497 ms: 1.27x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.29 sec: 1.28x slower                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 114 ms: 1.33x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.5 ms: 1.33x slower                                                       |
| tornado_http               | 121 ms                                                       | 163 ms: 1.34x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 32.2 ms: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.36x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.79 ms: 1.38x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 90.2 ms: 1.38x slower                                                       |
| scimark_fft                | 301 ms                                                       | 415 ms: 1.38x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.3 us: 1.38x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 51.0 us: 1.39x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.73 us: 1.40x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.4 ms: 1.41x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.77 sec: 1.44x slower                                                      |
| python_startup             | 11.6 ms                                                      | 16.9 ms: 1.45x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 131 ms: 1.46x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.4 ms: 1.49x slower                                                       |
| sympy_str                  | 302 ms                                                       | 455 ms: 1.51x slower                                                        |
| 2to3                       | 285 ms                                                       | 433 ms: 1.52x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 124 ms: 1.54x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 3.38 sec: 1.57x slower                                                      |
| coverage                   | 66.7 ms                                                      | 105 ms: 1.57x slower                                                        |
| regex_compile              | 144 ms                                                       | 231 ms: 1.61x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 94.4 ms: 1.62x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 187 ms: 1.62x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 263 ms: 1.62x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.56 ms: 1.65x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 94.6 ms: 1.65x slower                                                       |
| fannkuch                   | 350 ms                                                       | 582 ms: 1.66x slower                                                        |
| logging_format             | 7.48 us                                                      | 12.5 us: 1.66x slower                                                       |
| sympy_expand               | 484 ms                                                       | 827 ms: 1.71x slower                                                        |
| logging_simple             | 6.71 us                                                      | 11.5 us: 1.71x slower                                                       |
| pyflate                    | 439 ms                                                       | 774 ms: 1.77x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 271 us: 1.78x slower                                                        |
| django_template            | 38.2 ms                                                      | 68.2 ms: 1.79x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.45 sec: 1.80x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.99 sec: 1.81x slower                                                      |
| richards                   | 45.7 ms                                                      | 83.5 ms: 1.83x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 589 us: 1.85x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 172 ms: 1.88x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.42 ms: 1.92x slower                                                       |
| float                      | 76.6 ms                                                      | 148 ms: 1.93x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 183 ns: 1.94x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 134 ms: 1.95x slower                                                        |
| richards_super             | 51.3 ms                                                      | 100 ms: 1.96x slower                                                        |
| chaos                      | 64.0 ms                                                      | 127 ms: 1.98x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 418 us: 1.99x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 12.1 ms: 2.02x slower                                                       |
| raytrace                   | 298 ms                                                       | 623 ms: 2.09x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.91 ms: 2.11x slower                                                       |
| mako                       | 10.0 ms                                                      | 22.3 ms: 2.23x slower                                                       |
| go                         | 150 ms                                                       | 342 ms: 2.28x slower                                                        |
| scimark_sor                | 109 ms                                                       | 251 ms: 2.31x slower                                                        |
| nbody                      | 88.0 ms                                                      | 204 ms: 2.32x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 236 ms: 2.39x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.39 ms: 2.59x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.44x slower                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.28x

# Memory
- memory change: 1.07x