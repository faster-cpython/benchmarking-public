# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.02x faster
- HPT reliability: 80.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 310 ms: 1.09x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 315 ms: 1.37x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 396 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 798 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 556 ms: 1.25x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 840 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 567 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 75.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.33 ms: 1.07x faster                                                       |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.0 ms: 1.09x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.6 ms: 1.04x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.15 sec: 1.01x faster                                                      |
| pickle_pure_python   | 318 us                                                       | 320 us: 1.01x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                       |
| django_template | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 36.8 us                                                      | 26.7 us: 1.38x faster                                                       |
| async_tree_none            | 452 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 315 ms: 1.37x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 396 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 798 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 556 ms: 1.25x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 840 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 567 ms: 1.23x faster                                                        |
| deepcopy                   | 368 us                                                       | 303 us: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.5 us: 1.18x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.7 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 79.0 ms: 1.09x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.33 ms: 1.07x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.36 us: 1.05x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 98.6 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 780 ms: 1.04x faster                                                        |
| scimark_fft                | 301 ms                                                       | 291 ms: 1.03x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 925 us: 1.03x faster                                                        |
| async_generators           | 390 ms                                                       | 382 ms: 1.02x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.3 ms: 1.02x faster                                                       |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.7 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.18 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                        |
| float                      | 76.6 ms                                                      | 75.7 ms: 1.01x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.15 sec: 1.01x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.6 ms: 1.01x faster                                                       |
| generators                 | 37.4 ms                                                      | 37.2 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 320 us: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 65.8 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.02x slower                                                      |
| go                         | 150 ms                                                       | 152 ms: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 396 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| sympy_str                  | 302 ms                                                       | 311 ms: 1.03x slower                                                        |
| raytrace                   | 298 ms                                                       | 309 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 170 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                       |
| chaos                      | 64.0 ms                                                      | 67.6 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 468 ms: 1.07x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                       |
| 2to3                       | 285 ms                                                       | 310 ms: 1.09x slower                                                        |
| sympy_expand               | 484 ms                                                       | 528 ms: 1.09x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 5.20 ms: 1.09x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 98.2 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                      |
| sympy_integrate            | 23.9 ms                                                      | 26.4 ms: 1.10x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 65.6 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.11 ms: 1.16x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.00 ms: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.2 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.38 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (4): tornado_http, xml_etree_parse, fannkuch, nbody
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 80.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x