# Results vs. 3.12.0

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-x86_64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.02x faster
- HPT reliability: 63.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 766 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                        |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 796 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 90.9 ms: 1.03x slower                                                       |
| float          | 76.6 ms                                                      | 79.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.02x faster                                                        |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 224 us: 1.07x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.11 ms: 1.06x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                       |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 766 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                        |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 796 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 283 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.3 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.6 ms: 1.12x faster                                                       |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.10x faster                                                       |
| raytrace                   | 298 ms                                                       | 272 ms: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 875 us: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.96 us: 1.08x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.31 us: 1.06x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.0 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.04 ms: 1.04x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.1 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                       | 140 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                       |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.2 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                      |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                        |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 817 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| django_template            | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                        |
| nbody                      | 88.0 ms                                                      | 90.9 ms: 1.03x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 97.8 ns: 1.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 79.9 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.21 ms: 1.04x slower                                                       |
| go                         | 150 ms                                                       | 156 ms: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 68.2 ms: 1.04x slower                                                       |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.38 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.11 ms: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 468 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 224 us: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                        |
| richards                   | 45.7 ms                                                      | 51.5 ms: 1.12x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                                      |
| richards_super             | 51.3 ms                                                      | 57.9 ms: 1.13x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.27 ms: 1.19x slower                                                       |
| coverage                   | 66.7 ms                                                      | 80.6 ms: 1.21x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.48 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 63.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x