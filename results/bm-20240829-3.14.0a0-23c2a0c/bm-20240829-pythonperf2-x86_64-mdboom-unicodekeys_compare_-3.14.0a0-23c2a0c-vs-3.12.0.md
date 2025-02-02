# Results vs. 3.12.0

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.028x faster
- HPT reliability: 92.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 804 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                       |
| float          | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.45 ms: 1.04x faster                                                       |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.9 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 221 us: 1.05x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.57 sec: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 40.7 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.33x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.31x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 804 ms: 1.30x faster                                                        |
| deepcopy                   | 368 us                                                       | 288 us: 1.28x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.21x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 849 us: 1.12x faster                                                        |
| go                         | 150 ms                                                       | 134 ms: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.3 ms: 1.10x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.84 us: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.26 us: 1.07x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                       |
| async_generators           | 390 ms                                                       | 369 ms: 1.06x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.52 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                       |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.5 ms: 1.04x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.45 ms: 1.04x faster                                                       |
| chaos                      | 64.0 ms                                                      | 61.9 ms: 1.03x faster                                                       |
| nbody                      | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.9 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 89.4 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.65 sec: 1.00x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| sympy_expand               | 484 ms                                                       | 495 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.1 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.27 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.6 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 221 us: 1.05x slower                                                        |
| float                      | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.30 ms: 1.06x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.44 ms: 1.06x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.7 ms: 1.07x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                        |
| pyflate                    | 439 ms                                                       | 479 ms: 1.09x slower                                                        |
| richards_super             | 51.3 ms                                                      | 56.2 ms: 1.10x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.4 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.57 sec: 1.19x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.30 ms: 1.19x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (4): scimark_fft, pprint_safe_repr, scimark_sparse_mat_mult, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-23c2a0c/bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 92.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x