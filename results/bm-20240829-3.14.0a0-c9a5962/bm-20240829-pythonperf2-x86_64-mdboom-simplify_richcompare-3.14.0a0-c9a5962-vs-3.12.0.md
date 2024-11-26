# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.033x faster
- HPT reliability: 96.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 115 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 395 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 817 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                       |
| float          | 76.6 ms                                                      | 78.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.42 ms: 1.04x faster                                                       |
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_dna      | 239 ms                                                       | 254 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.3 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.60 sec: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 395 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                       |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 817 ms: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.9 us: 1.27x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 852 us: 1.11x faster                                                        |
| go                         | 150 ms                                                       | 135 ms: 1.11x faster                                                        |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.81 us: 1.10x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 361 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.22 us: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.7 ms: 1.07x faster                                                       |
| chaos                      | 64.0 ms                                                      | 60.5 ms: 1.06x faster                                                       |
| tornado_http               | 121 ms                                                       | 115 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.42 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.0 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 367 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| scimark_fft                | 301 ms                                                       | 299 ms: 1.01x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 89.4 ms: 1.00x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                       |
| fannkuch                   | 350 ms                                                       | 354 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| json                       | 5.12 ms                                                      | 5.23 ms: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| float                      | 76.6 ms                                                      | 78.9 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.2 ms: 1.03x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.5 ns: 1.03x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.37 ms: 1.04x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.0 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.31 ms: 1.06x slower                                                       |
| regex_dna                  | 239 ms                                                       | 254 ms: 1.06x slower                                                        |
| richards                   | 45.7 ms                                                      | 49.6 ms: 1.08x slower                                                       |
| richards_super             | 51.3 ms                                                      | 55.7 ms: 1.08x slower                                                       |
| pyflate                    | 439 ms                                                       | 484 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.3 ms: 1.16x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.24 ms: 1.18x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.60 sec: 1.20x slower                                                      |
| coverage                   | 66.7 ms                                                      | 82.1 ms: 1.23x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.48 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (5): bench_mp_pool, xml_etree_parse, scimark_sor, asyncio_websockets, sqlglot_transpile
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 96.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x