# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 55.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 383 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 776 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                        |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 811 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                       |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.25 sec: 1.04x slower                                                      |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 383 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 776 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                        |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                        |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 811 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.8 us: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.7 ms: 1.12x faster                                                       |
| generators                 | 37.4 ms                                                      | 33.5 ms: 1.12x faster                                                       |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 873 us: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 367 ms: 1.06x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.05 us: 1.06x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 87.7 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.5 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| dask                       | 392 ms                                                       | 386 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                                      |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 812 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.2 ms: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 58.9 ms: 1.02x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.38 ms: 1.04x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.25 sec: 1.04x slower                                                      |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 95.8 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 98.8 ns: 1.05x slower                                                       |
| scimark_fft                | 301 ms                                                       | 315 ms: 1.05x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| float                      | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.27 ms: 1.05x slower                                                       |
| fannkuch                   | 350 ms                                                       | 368 ms: 1.05x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| json                       | 5.12 ms                                                      | 5.47 ms: 1.07x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.50 ms: 1.08x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                                        |
| pyflate                    | 439 ms                                                       | 490 ms: 1.12x slower                                                        |
| richards                   | 45.7 ms                                                      | 51.5 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                        |
| richards_super             | 51.3 ms                                                      | 58.5 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| coverage                   | 66.7 ms                                                      | 78.4 ms: 1.18x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.25 ms: 1.19x slower                                                       |
| scimark_sor                | 109 ms                                                       | 131 ms: 1.20x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.46 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (5): scimark_lu, sqlglot_transpile, django_template, nbody, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 55.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x