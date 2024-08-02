# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.02x faster
- HPT reliability: 58.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                        |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 788 ms: 1.34x faster                                        |
| async_tree_none            | 452 ms                                                       | 339 ms: 1.33x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 411 ms: 1.32x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 822 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 562 ms: 1.24x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.21x faster                                        |
| Geometric mean             | (ref)                                                        | 1.31x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                        |
| float          | 76.6 ms                                                      | 79.8 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.41 ms: 1.05x faster                                       |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                        |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                        |
| regex_v8       | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                       |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                       |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                        |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                       |
| tomli_loads          | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                      |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                       |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                       |
| django_template | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                       |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 788 ms: 1.34x faster                                        |
| async_tree_none            | 452 ms                                                       | 339 ms: 1.33x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 411 ms: 1.32x faster                                        |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.29x faster                                       |
| deepcopy                   | 368 us                                                       | 290 us: 1.27x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 822 ms: 1.27x faster                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 562 ms: 1.24x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.21x faster                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.3 ms: 1.13x faster                                       |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                        |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.11x faster                                       |
| bench_thread_pool          | 950 us                                                       | 879 us: 1.08x faster                                        |
| async_generators           | 390 ms                                                       | 366 ms: 1.07x faster                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                        |
| regex_effbot               | 3.57 ms                                                      | 3.41 ms: 1.05x faster                                       |
| logging_format             | 7.48 us                                                      | 7.14 us: 1.05x faster                                       |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.04x faster                                       |
| logging_simple             | 6.71 us                                                      | 6.49 us: 1.03x faster                                       |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                       |
| tornado_http               | 121 ms                                                       | 117 ms: 1.03x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.2 ms: 1.03x faster                                       |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.02x faster                                        |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                      |
| dask                       | 392 ms                                                       | 384 ms: 1.02x faster                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                        |
| scimark_lu                 | 98.8 ms                                                      | 97.1 ms: 1.02x faster                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                      |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                        |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                        |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                      |
| dulwich_log                | 65.4 ms                                                      | 66.6 ms: 1.02x slower                                       |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                        |
| pprint_safe_repr           | 807 ms                                                       | 828 ms: 1.03x slower                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.32 ms: 1.03x slower                                       |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.3 ms: 1.03x slower                                       |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                        |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                       |
| float                      | 76.6 ms                                                      | 79.8 ms: 1.04x slower                                       |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                        |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                        |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                       |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                       |
| logging_silent             | 94.4 ns                                                      | 99.4 ns: 1.05x slower                                       |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                       |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.05x slower                                        |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                       |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                        |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                       |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                       |
| django_template            | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                       |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                        |
| hexiom                     | 5.96 ms                                                      | 6.39 ms: 1.07x slower                                       |
| tomli_loads                | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                      |
| regex_v8                   | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                       |
| pyflate                    | 439 ms                                                       | 488 ms: 1.11x slower                                        |
| richards                   | 45.7 ms                                                      | 51.5 ms: 1.13x slower                                       |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                       |
| richards_super             | 51.3 ms                                                      | 58.8 ms: 1.14x slower                                       |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                        |
| telco                      | 6.96 ms                                                      | 8.33 ms: 1.20x slower                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.24x slower                                       |
| coverage                   | 66.7 ms                                                      | 83.8 ms: 1.26x slower                                       |
| gc_traversal               | 3.48 ms                                                      | 4.44 ms: 1.28x slower                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                |

Benchmark hidden because not significant (8): bench_mp_pool, nqueens, asyncio_websockets, pycparser, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, nbody
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 58.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x