# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 82.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.10 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.39x faster                                                        |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 414 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 805 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 583 ms: 1.19x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 82.6 ms: 1.06x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 75.1 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 99.8 ms: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.22 ms: 1.08x faster                                                       |
| django_template | 38.2 ms                                                      | 43.3 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.39x faster                                                        |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.7 us: 1.33x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 414 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 805 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                        |
| deepcopy                   | 368 us                                                       | 305 us: 1.21x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 583 ms: 1.19x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.3 ms: 1.14x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.5 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.11x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.22 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.2 ms: 1.07x faster                                                       |
| nbody                      | 88.0 ms                                                      | 82.6 ms: 1.06x faster                                                       |
| generators                 | 37.4 ms                                                      | 35.3 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.47 us: 1.04x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| logging_format             | 7.48 us                                                      | 7.25 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.8 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.09 ms: 1.03x faster                                                       |
| scimark_fft                | 301 ms                                                       | 293 ms: 1.03x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 929 us: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| float                      | 76.6 ms                                                      | 75.1 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                      |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                       |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.01x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| fannkuch                   | 350 ms                                                       | 346 ms: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.00x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                        |
| pyflate                    | 439 ms                                                       | 445 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 394 ms: 1.02x slower                                                        |
| sympy_str                  | 302 ms                                                       | 308 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| dask                       | 392 ms                                                       | 400 ms: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.0 ms: 1.03x slower                                                       |
| richards_super             | 51.3 ms                                                      | 53.0 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 94.8 ms: 1.05x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.5 ms: 1.07x slower                                                       |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                       |
| sympy_expand               | 484 ms                                                       | 521 ms: 1.08x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.10 sec: 1.08x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| json                       | 5.12 ms                                                      | 5.54 ms: 1.08x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.08x slower                                                        |
| go                         | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 63.2 ms: 1.10x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.66 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.13x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.66 ms: 1.13x slower                                                       |
| django_template            | 38.2 ms                                                      | 43.3 ms: 1.13x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 114 ms: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.34 ms: 1.20x slower                                                       |
| scimark_sor                | 109 ms                                                       | 131 ms: 1.20x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.2 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.93 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 189 us: 1.25x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.44 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, dulwich_log, tornado_http, raytrace
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 82.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x