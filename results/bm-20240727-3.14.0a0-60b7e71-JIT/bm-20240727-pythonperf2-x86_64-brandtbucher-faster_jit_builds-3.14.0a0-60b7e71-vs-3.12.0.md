# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 85.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 303 ms: 1.06x slower                                                           |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                         |
| tornado_http   | 121 ms                                                       | 120 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.43x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 764 ms: 1.38x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                           |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.35x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 795 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 536 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.35x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.5 ms: 1.08x faster                                                          |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                           |
| float          | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                           |
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.02x faster                                                          |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                           |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.7 ms: 1.06x faster                                                          |
| xml_etree_generate   | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                          |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                           |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.00x faster                                                           |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                          |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                           |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                          |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                          |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.26 ms: 1.08x faster                                                          |
| django_template | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.43x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 764 ms: 1.38x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                           |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.35x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 795 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 536 ms: 1.30x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 28.4 us: 1.30x faster                                                          |
| deepcopy                   | 368 us                                                       | 302 us: 1.22x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                           |
| comprehensions             | 21.9 us                                                      | 18.4 us: 1.19x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.18x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 69.7 ms: 1.15x faster                                                          |
| spectral_norm              | 91.6 ms                                                      | 81.0 ms: 1.13x faster                                                          |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                          |
| generators                 | 37.4 ms                                                      | 34.2 ms: 1.10x faster                                                          |
| mako                       | 10.0 ms                                                      | 9.26 ms: 1.08x faster                                                          |
| nbody                      | 88.0 ms                                                      | 81.5 ms: 1.08x faster                                                          |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                          |
| logging_format             | 7.48 us                                                      | 7.01 us: 1.07x faster                                                          |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.8 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 96.7 ms: 1.06x faster                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                          |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                           |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                          |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                           |
| bench_thread_pool          | 950 us                                                       | 903 us: 1.05x faster                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                         |
| scimark_fft                | 301 ms                                                       | 292 ms: 1.03x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                           |
| float                      | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.52 ms: 1.02x faster                                                          |
| richards                   | 45.7 ms                                                      | 45.1 ms: 1.01x faster                                                          |
| tornado_http               | 121 ms                                                       | 120 ms: 1.01x faster                                                           |
| raytrace                   | 298 ms                                                       | 294 ms: 1.01x faster                                                           |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                         |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                           |
| async_generators           | 390 ms                                                       | 388 ms: 1.01x faster                                                           |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.00x faster                                                           |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                          |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                           |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                          |
| sympy_str                  | 302 ms                                                       | 311 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                          |
| sympy_sum                  | 162 ms                                                       | 167 ms: 1.03x slower                                                           |
| chaos                      | 64.0 ms                                                      | 66.5 ms: 1.04x slower                                                          |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.04x slower                                                           |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                          |
| nqueens                    | 89.9 ms                                                      | 95.5 ms: 1.06x slower                                                          |
| 2to3                       | 285 ms                                                       | 303 ms: 1.06x slower                                                           |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                           |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                          |
| sympy_integrate            | 23.9 ms                                                      | 25.7 ms: 1.07x slower                                                          |
| go                         | 150 ms                                                       | 162 ms: 1.08x slower                                                           |
| django_template            | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                          |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                         |
| sympy_expand               | 484 ms                                                       | 528 ms: 1.09x slower                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 63.6 ms: 1.11x slower                                                          |
| deltablue                  | 3.24 ms                                                      | 3.59 ms: 1.11x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 6.61 ms: 1.11x slower                                                          |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                          |
| telco                      | 6.96 ms                                                      | 7.92 ms: 1.14x slower                                                          |
| sqlglot_normalize          | 116 ms                                                       | 133 ms: 1.15x slower                                                           |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                          |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.17x slower                                                           |
| scimark_sor                | 109 ms                                                       | 128 ms: 1.18x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.20x slower                                                          |
| coverage                   | 66.7 ms                                                      | 80.7 ms: 1.21x slower                                                          |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 4.34 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                   |

Benchmark hidden because not significant (8): dask, asyncio_tcp, pyflate, richards_super, pprint_safe_repr, scimark_sparse_mat_mult, bench_mp_pool, pprint_pformat
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 85.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x