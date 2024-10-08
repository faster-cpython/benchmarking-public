# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.03x faster
- HPT reliability: 96.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 791 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 569 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 91.4 ms: 1.04x slower                                                       |
| float          | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 232 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 86.3 ms: 1.00x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.57 sec: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 791 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 288 us: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.4 ms: 1.27x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 569 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                       |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.8 ms: 1.10x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 864 us: 1.10x faster                                                        |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.86 us: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 360 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.26 us: 1.07x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.8 ms: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.8 ms: 1.04x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                      |
| chaos                      | 64.0 ms                                                      | 61.8 ms: 1.04x faster                                                       |
| regex_dna                  | 239 ms                                                       | 232 ms: 1.03x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 87.8 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 801 ms: 1.01x faster                                                        |
| scimark_fft                | 301 ms                                                       | 300 ms: 1.00x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.65 sec: 1.00x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 86.3 ms: 1.00x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.3 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.28 ms: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.4 ns: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| nbody                      | 88.0 ms                                                      | 91.4 ms: 1.04x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.21 ms: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 97.3 ms: 1.06x slower                                                       |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 476 ms: 1.09x slower                                                        |
| richards                   | 45.7 ms                                                      | 50.2 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.4 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.21 ms: 1.18x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.57 sec: 1.19x slower                                                      |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.43 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, xml_etree_iterparse, pycparser, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x