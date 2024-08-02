# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.02x faster
- HPT reliability: 69.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                        |
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 771 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 540 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 828 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 563 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 76.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 261 ms: 1.09x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.3 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.2 ms: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 56.5 ms: 1.03x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.10 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.12 ms: 1.10x faster                                                       |
| django_template | 38.2 ms                                                      | 41.5 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                        |
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 771 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 540 ms: 1.29x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 828 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 563 ms: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.0 us: 1.22x faster                                                       |
| deepcopy                   | 368 us                                                       | 311 us: 1.18x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.0 ms: 1.13x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.12 ms: 1.10x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.3 ms: 1.07x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.29 us: 1.07x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.05 us: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.2 ms: 1.06x faster                                                       |
| scimark_fft                | 301 ms                                                       | 285 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 910 us: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| generators                 | 37.4 ms                                                      | 36.2 ms: 1.03x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 56.5 ms: 1.03x faster                                                       |
| raytrace                   | 298 ms                                                       | 289 ms: 1.03x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.11 ms: 1.02x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.5 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 97.8 ms: 1.01x faster                                                       |
| float                      | 76.6 ms                                                      | 76.2 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                        |
| fannkuch                   | 350 ms                                                       | 355 ms: 1.01x slower                                                        |
| richards                   | 45.7 ms                                                      | 46.6 ms: 1.02x slower                                                       |
| sympy_str                  | 302 ms                                                       | 310 ms: 1.02x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 167 ms: 1.03x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.0 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.10 ms: 1.05x slower                                                       |
| richards_super             | 51.3 ms                                                      | 54.1 ms: 1.05x slower                                                       |
| pyflate                    | 439 ms                                                       | 463 ms: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                        |
| sympy_expand               | 484 ms                                                       | 521 ms: 1.08x slower                                                        |
| 2to3                       | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 62.2 ms: 1.08x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.9 ms: 1.08x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.5 ms: 1.09x slower                                                       |
| regex_dna                  | 239 ms                                                       | 261 ms: 1.09x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.09x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.10x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 99.3 ms: 1.10x slower                                                       |
| go                         | 150 ms                                                       | 168 ms: 1.13x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.77 ms: 1.14x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.74 ms: 1.16x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.09 ms: 1.16x slower                                                       |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.34 ms: 1.25x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (8): tornado_http, asyncio_tcp, pprint_pformat, meteor_contest, nbody, bench_mp_pool, pprint_safe_repr, dask
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 69.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x