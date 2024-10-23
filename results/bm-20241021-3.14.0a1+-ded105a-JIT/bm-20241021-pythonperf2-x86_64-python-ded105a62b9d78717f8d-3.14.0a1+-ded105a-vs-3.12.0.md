# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-x86_64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.09x slower
- HPT reliability: 67.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 315 ms: 1.10x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.20 sec: 1.11x slower                                                       |
| tornado_http   | 121 ms                                                       | 124 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 374 ms: 1.45x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 411 ms: 1.32x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 831 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 564 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 864 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 84.7 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 79.5 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                        |
| regex_compile  | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| regex_dna      | 239 ms                                                       | 257 ms: 1.08x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.7 ms: 1.03x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.8 ms: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                         |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.01x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.58 ms: 1.04x faster                                                        |
| django_template | 38.2 ms                                                      | 43.7 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 374 ms: 1.45x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 411 ms: 1.32x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 831 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 564 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 864 ms: 1.22x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                        |
| deepcopy                   | 368 us                                                       | 313 us: 1.18x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.7 us: 1.17x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.7 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                        |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.10 us: 1.05x faster                                                        |
| scimark_fft                | 301 ms                                                       | 287 ms: 1.05x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.58 ms: 1.04x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.44 us: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 62.9 ms: 1.04x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.7 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.3 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 99.7 ms: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.6 ns: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                                         |
| richards                   | 45.7 ms                                                      | 45.2 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.8 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                         |
| async_generators           | 390 ms                                                       | 388 ms: 1.01x faster                                                         |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                       |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.01x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 70.4 ms: 1.02x slower                                                        |
| tornado_http               | 121 ms                                                       | 124 ms: 1.02x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 93.8 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| richards_super             | 51.3 ms                                                      | 52.9 ms: 1.03x slower                                                        |
| generators                 | 37.4 ms                                                      | 38.6 ms: 1.03x slower                                                        |
| float                      | 76.6 ms                                                      | 79.5 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                         |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.05x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                         |
| sympy_str                  | 302 ms                                                       | 318 ms: 1.05x slower                                                         |
| chaos                      | 64.0 ms                                                      | 68.0 ms: 1.06x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.07x slower                                                         |
| regex_dna                  | 239 ms                                                       | 257 ms: 1.08x slower                                                         |
| raytrace                   | 298 ms                                                       | 321 ms: 1.08x slower                                                         |
| pyflate                    | 439 ms                                                       | 475 ms: 1.08x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                        |
| sympy_expand               | 484 ms                                                       | 529 ms: 1.09x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                        |
| 2to3                       | 285 ms                                                       | 315 ms: 1.10x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.75 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.20 sec: 1.11x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.7 ms: 1.15x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 135 ms: 1.17x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.19 ms: 1.21x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 69.4 ms: 1.21x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                                         |
| coverage                   | 66.7 ms                                                      | 82.5 ms: 1.24x slower                                                        |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.20 ms: 1.50x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.92 ms: 1.84x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.28 sec: 479.56x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (2): bench_thread_pool, scimark_sparse_mat_mult
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 67.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x