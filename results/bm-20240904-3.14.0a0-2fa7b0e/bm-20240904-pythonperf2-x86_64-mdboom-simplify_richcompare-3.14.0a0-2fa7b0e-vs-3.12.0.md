# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.027x faster
- HPT reliability: 90.01%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 816 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 548 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.8 ms: 1.02x faster                                                       |
| float          | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                       |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_dna      | 239 ms                                                       | 255 ms: 1.07x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.56 sec: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| django_template | 38.2 ms                                                      | 40.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                       |
| deepcopy                   | 368 us                                                       | 285 us: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 816 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 548 ms: 1.27x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                       |
| go                         | 150 ms                                                       | 134 ms: 1.12x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 863 us: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.88 us: 1.09x faster                                                       |
| raytrace                   | 298 ms                                                       | 275 ms: 1.09x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 74.1 ms: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.34 us: 1.06x faster                                                       |
| async_generators           | 390 ms                                                       | 371 ms: 1.05x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.53 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 366 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.7 ms: 1.03x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                       |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.8 ms: 1.02x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.02x faster                                                      |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.8 ms: 1.02x faster                                                       |
| scimark_fft                | 301 ms                                                       | 296 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.4 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.18 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 802 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.28 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.3 ms: 1.03x slower                                                       |
| float                      | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.0 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.3 ns: 1.05x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.3 ms: 1.06x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.32 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| regex_dna                  | 239 ms                                                       | 255 ms: 1.07x slower                                                        |
| richards_super             | 51.3 ms                                                      | 56.0 ms: 1.09x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.1 ms: 1.09x slower                                                       |
| pyflate                    | 439 ms                                                       | 481 ms: 1.10x slower                                                        |
| coverage                   | 66.7 ms                                                      | 74.9 ms: 1.12x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.17 ms: 1.17x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.56 sec: 1.18x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.63 ms: 1.33x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (5): pycparser, xml_etree_iterparse, nqueens, scimark_sor, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 90.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x