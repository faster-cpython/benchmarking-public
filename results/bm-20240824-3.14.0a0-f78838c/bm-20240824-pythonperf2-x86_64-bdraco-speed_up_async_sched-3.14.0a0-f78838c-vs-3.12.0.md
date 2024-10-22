# Results vs. 3.12.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 83.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.03x slower                                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 775 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 550 ms: 1.27x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 827 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 558 ms: 1.25x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 78.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.00x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 87.4 ms: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.8 ms: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.56 sec: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 775 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                       |
| deepcopy                   | 368 us                                                       | 285 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 550 ms: 1.27x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.0 us: 1.27x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 827 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 558 ms: 1.25x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                       |
| raytrace                   | 298 ms                                                       | 267 ms: 1.12x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 859 us: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 74.6 ms: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.48 ms: 1.06x faster                                                       |
| async_generators           | 390 ms                                                       | 368 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.1 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.1 ms: 1.05x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.19 us: 1.04x faster                                                       |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 366 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.8 ms: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.00x faster                                                        |
| scimark_fft                | 301 ms                                                       | 300 ms: 1.00x faster                                                        |
| fannkuch                   | 350 ms                                                       | 352 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 87.4 ms: 1.01x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| float                      | 76.6 ms                                                      | 78.9 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.34 ms: 1.03x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.03x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 60.8 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.23 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.3 ns: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.40 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.8 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.44 ms: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                       |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 474 ms: 1.08x slower                                                        |
| richards_super             | 51.3 ms                                                      | 56.0 ms: 1.09x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.3 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.18 ms: 1.17x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.56 sec: 1.19x slower                                                      |
| go                         | 150 ms                                                       | 181 ms: 1.21x slower                                                        |
| coverage                   | 66.7 ms                                                      | 83.1 ms: 1.25x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.48 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, pprint_safe_repr, xml_etree_parse, nbody, nqueens, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 83.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x