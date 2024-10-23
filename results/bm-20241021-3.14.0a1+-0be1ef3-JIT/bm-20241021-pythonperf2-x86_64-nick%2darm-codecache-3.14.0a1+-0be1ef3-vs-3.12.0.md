# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.09x slower
- HPT reliability: 75.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                                  |
| docutils       | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                        | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 374 ms: 1.45x faster                                                  |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                                  |
| async_tree_none            | 452 ms                                                       | 341 ms: 1.32x faster                                                  |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                  |
| async_tree_io              | 1.04 sec                                                     | 835 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 562 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 871 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                  |
| float          | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.73 ms: 1.05x slower                                                 |
| regex_dna      | 239 ms                                                       | 257 ms: 1.08x slower                                                  |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                        | 1.06x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.1 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                |
| xml_etree_process    | 58.4 ms                                                      | 58.1 ms: 1.01x faster                                                 |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                  |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                 |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                  |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                  |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                 |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.62 ms: 1.04x faster                                                 |
| django_template | 38.2 ms                                                      | 43.1 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 374 ms: 1.45x faster                                                  |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                                  |
| async_tree_none            | 452 ms                                                       | 341 ms: 1.32x faster                                                  |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                  |
| async_tree_io              | 1.04 sec                                                     | 835 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 562 ms: 1.24x faster                                                  |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.22x faster                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 871 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                  |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                 |
| deepcopy                   | 368 us                                                       | 314 us: 1.17x faster                                                  |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.16x faster                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 73.0 ms: 1.10x faster                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 81.1 ms: 1.06x faster                                                 |
| scimark_fft                | 301 ms                                                       | 285 ms: 1.06x faster                                                  |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                  |
| mako                       | 10.0 ms                                                      | 9.62 ms: 1.04x faster                                                 |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                  |
| logging_format             | 7.48 us                                                      | 7.23 us: 1.04x faster                                                 |
| scimark_lu                 | 98.8 ms                                                      | 95.4 ms: 1.04x faster                                                 |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                 |
| dulwich_log                | 65.4 ms                                                      | 63.5 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 807 ms                                                       | 788 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                  |
| logging_silent             | 94.4 ns                                                      | 92.3 ns: 1.02x faster                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                |
| richards                   | 45.7 ms                                                      | 45.1 ms: 1.01x faster                                                 |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                  |
| async_generators           | 390 ms                                                       | 387 ms: 1.01x faster                                                  |
| xml_etree_process          | 58.4 ms                                                      | 58.1 ms: 1.01x faster                                                 |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                  |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                  |
| json                       | 5.12 ms                                                      | 5.22 ms: 1.02x slower                                                 |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                  |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                 |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                                 |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                  |
| generators                 | 37.4 ms                                                      | 38.7 ms: 1.03x slower                                                 |
| spectral_norm              | 91.6 ms                                                      | 94.8 ms: 1.03x slower                                                 |
| go                         | 150 ms                                                       | 155 ms: 1.04x slower                                                  |
| float                      | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                                 |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.73 ms: 1.05x slower                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                 |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                  |
| fannkuch                   | 350 ms                                                       | 367 ms: 1.05x slower                                                  |
| sympy_str                  | 302 ms                                                       | 317 ms: 1.05x slower                                                  |
| raytrace                   | 298 ms                                                       | 316 ms: 1.06x slower                                                  |
| pyflate                    | 439 ms                                                       | 466 ms: 1.06x slower                                                  |
| richards_super             | 51.3 ms                                                      | 54.7 ms: 1.07x slower                                                 |
| sympy_sum                  | 162 ms                                                       | 173 ms: 1.07x slower                                                  |
| chaos                      | 64.0 ms                                                      | 68.7 ms: 1.07x slower                                                 |
| regex_dna                  | 239 ms                                                       | 257 ms: 1.08x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                 |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                 |
| sympy_expand               | 484 ms                                                       | 527 ms: 1.09x slower                                                  |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                 |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.96 ms: 1.10x slower                                                 |
| docutils                   | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                |
| telco                      | 6.96 ms                                                      | 7.78 ms: 1.12x slower                                                 |
| django_template            | 38.2 ms                                                      | 43.1 ms: 1.13x slower                                                 |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.13x slower                                                  |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.13x slower                                                 |
| sqlglot_normalize          | 116 ms                                                       | 133 ms: 1.15x slower                                                  |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                                 |
| sqlglot_optimize           | 57.5 ms                                                      | 68.8 ms: 1.20x slower                                                 |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                  |
| hexiom                     | 5.96 ms                                                      | 7.21 ms: 1.21x slower                                                 |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                 |
| gc_traversal               | 3.48 ms                                                      | 5.81 ms: 1.67x slower                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.83x slower                                                 |
| bench_mp_pool              | 4.76 ms                                                      | 3.17 sec: 665.38x slower                                              |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                          |

Benchmark hidden because not significant (7): nbody, bench_thread_pool, pprint_pformat, scimark_monte_carlo, scimark_sparse_mat_mult, mdp, logging_simple
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 75.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x