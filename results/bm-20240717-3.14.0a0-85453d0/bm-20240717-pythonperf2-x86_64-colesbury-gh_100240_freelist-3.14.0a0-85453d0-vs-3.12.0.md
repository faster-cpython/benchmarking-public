# Results vs. 3.12.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.03x faster
- HPT reliability: 95.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 769 ms: 1.37x faster                                                         |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 533 ms: 1.31x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 797 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                        |
| float          | 76.6 ms                                                      | 81.8 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 83.0 ms: 1.04x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 320 us: 1.00x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.45 sec: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                        |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 769 ms: 1.37x faster                                                         |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 533 ms: 1.31x faster                                                         |
| deepcopy                   | 368 us                                                       | 282 us: 1.31x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 797 ms: 1.31x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.3 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.87 us: 1.18x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 71.7 ms: 1.12x faster                                                        |
| raytrace                   | 298 ms                                                       | 267 ms: 1.12x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.5 ms: 1.12x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 864 us: 1.10x faster                                                         |
| logging_format             | 7.48 us                                                      | 6.84 us: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 360 ms: 1.08x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.32 us: 1.06x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.8 ms: 1.05x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.0 ms: 1.04x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.6 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.4 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                                         |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.11 ms: 1.02x faster                                                        |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| scimark_fft                | 301 ms                                                       | 296 ms: 1.02x faster                                                         |
| nbody                      | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 320 us: 1.00x slower                                                         |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                        |
| django_template            | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.7 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 58.7 ms: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.1 ms: 1.05x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.26 ms: 1.05x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 99.6 ns: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                        |
| float                      | 76.6 ms                                                      | 81.8 ms: 1.07x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.46 ms: 1.07x slower                                                        |
| pyflate                    | 439 ms                                                       | 476 ms: 1.08x slower                                                         |
| go                         | 150 ms                                                       | 164 ms: 1.09x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.11x slower                                                         |
| richards                   | 45.7 ms                                                      | 51.7 ms: 1.13x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.45 sec: 1.13x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.94 ms: 1.14x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                        |
| richards_super             | 51.3 ms                                                      | 59.6 ms: 1.16x slower                                                        |
| coverage                   | 66.7 ms                                                      | 83.2 ms: 1.25x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.29x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (7): bench_mp_pool, xml_etree_iterparse, pprint_safe_repr, regex_effbot, nqueens, asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x