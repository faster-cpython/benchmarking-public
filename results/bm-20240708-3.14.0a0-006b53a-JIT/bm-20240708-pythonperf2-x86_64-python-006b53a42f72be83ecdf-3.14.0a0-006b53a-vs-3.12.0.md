# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-x86_64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.01x faster
- HPT reliability: 62.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 381 ms: 1.42x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 405 ms: 1.34x faster                                                        |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 788 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 536 ms: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 810 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.1 ms: 1.06x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 75.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 256 ms: 1.07x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.0 ms: 1.04x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.21 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 42.1 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 381 ms: 1.42x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 405 ms: 1.34x faster                                                        |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 788 ms: 1.34x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 536 ms: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 810 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.20x faster                                                       |
| deepcopy                   | 368 us                                                       | 310 us: 1.19x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.7 ms: 1.14x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.9 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.10x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.21 ms: 1.09x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.7 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.8 ms: 1.07x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.1 ms: 1.06x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.1 ms: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| raytrace                   | 298 ms                                                       | 286 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 99.0 ms: 1.04x faster                                                       |
| scimark_fft                | 301 ms                                                       | 291 ms: 1.04x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 921 us: 1.03x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                       |
| async_generators           | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| float                      | 76.6 ms                                                      | 75.7 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.17 ms: 1.01x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| pyflate                    | 439 ms                                                       | 443 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 394 ms: 1.02x slower                                                        |
| dask                       | 392 ms                                                       | 400 ms: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.6 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.2 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.03x slower                                                        |
| sympy_str                  | 302 ms                                                       | 312 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.03x slower                                                        |
| richards_super             | 51.3 ms                                                      | 53.6 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                        |
| json                       | 5.12 ms                                                      | 5.46 ms: 1.07x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                       |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                        |
| regex_dna                  | 239 ms                                                       | 256 ms: 1.07x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 96.5 ms: 1.07x slower                                                       |
| go                         | 150 ms                                                       | 161 ms: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.09x slower                                                      |
| sympy_expand               | 484 ms                                                       | 526 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 63.0 ms: 1.10x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.1 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.64 ms: 1.11x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 112 ms: 1.14x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.70 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.07 ms: 1.16x slower                                                       |
| scimark_sor                | 109 ms                                                       | 128 ms: 1.18x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.31 ms: 1.24x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pprint_safe_repr, pprint_pformat, pickle_pure_python, xml_etree_process, tornado_http, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 62.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x