# Results vs. 3.12.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-x86_64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 82.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 305 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 767 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 553 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| float          | 76.6 ms                                                      | 81.3 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 305 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 767 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.3 ms: 1.32x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 288 us: 1.28x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.0 us: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 553 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 73.0 ms: 1.10x faster                                                       |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 872 us: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 361 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.26 us: 1.07x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                       |
| chaos                      | 64.0 ms                                                      | 60.6 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.01 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.58 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| nbody                      | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                       |
| dask                       | 392 ms                                                       | 383 ms: 1.02x faster                                                        |
| scimark_fft                | 301 ms                                                       | 294 ms: 1.02x faster                                                        |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                      |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 97.3 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 377 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 814 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 66.0 ms: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.2 ms: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.04x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 94.9 ms: 1.04x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.9 ns: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| django_template            | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 367 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                                       |
| float                      | 76.6 ms                                                      | 81.3 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.37 ms: 1.07x slower                                                       |
| go                         | 150 ms                                                       | 162 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.80 ms: 1.12x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                        |
| pyflate                    | 439 ms                                                       | 504 ms: 1.15x slower                                                        |
| richards                   | 45.7 ms                                                      | 52.5 ms: 1.15x slower                                                       |
| richards_super             | 51.3 ms                                                      | 59.1 ms: 1.15x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| coverage                   | 66.7 ms                                                      | 78.7 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.72 ms: 1.36x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (5): nqueens, pickle_pure_python, scimark_monte_carlo, xml_etree_iterparse, pprint_pformat
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 82.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x