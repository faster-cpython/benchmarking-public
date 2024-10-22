# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.02x faster
- HPT reliability: 71.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.00 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 769 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 799 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 535 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| float          | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| regex_dna      | 239 ms                                                       | 254 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 85.5 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.28 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.6 ms: 1.01x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 769 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 799 ms: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 535 ms: 1.30x faster                                                        |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.26x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 72.6 ms: 1.11x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 870 us: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 359 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.02 us: 1.07x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.5 ms: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.06x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.1 ms: 1.05x faster                                                       |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.47 us: 1.04x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.2 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                       |
| dask                       | 392 ms                                                       | 383 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.5 ms: 1.01x faster                                                       |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 89.4 ms: 1.00x faster                                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.23 ms: 1.01x slower                                                       |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| django_template            | 38.2 ms                                                      | 38.6 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.3 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.71 sec: 1.04x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 97.8 ns: 1.04x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 837 ms: 1.04x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.00 sec: 1.04x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                       |
| sympy_expand               | 484 ms                                                       | 507 ms: 1.05x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.27 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.28 sec: 1.06x slower                                                      |
| float                      | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                       |
| fannkuch                   | 350 ms                                                       | 370 ms: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                       |
| regex_dna                  | 239 ms                                                       | 254 ms: 1.06x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.45 ms: 1.07x slower                                                       |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                        |
| richards_super             | 51.3 ms                                                      | 57.2 ms: 1.11x slower                                                       |
| richards                   | 45.7 ms                                                      | 51.2 ms: 1.12x slower                                                       |
| pyflate                    | 439 ms                                                       | 492 ms: 1.12x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.98 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.04 ms: 1.28x slower                                                       |
| coverage                   | 66.7 ms                                                      | 87.3 ms: 1.31x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.74 ms: 1.36x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (5): bench_mp_pool, asyncio_websockets, regex_effbot, pycparser, scimark_fft
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 71.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x