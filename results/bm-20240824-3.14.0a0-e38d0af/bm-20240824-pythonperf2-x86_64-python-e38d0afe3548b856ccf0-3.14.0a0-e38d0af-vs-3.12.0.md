# Results vs. 3.12.0

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-x86_64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 95.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 783 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 807 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 78.9 ms: 1.03x slower                                                       |
| nbody          | 88.0 ms                                                      | 90.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.54 sec: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 783 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.6 ms: 1.31x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 807 ms: 1.29x faster                                                        |
| deepcopy                   | 368 us                                                       | 290 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 852 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.5 ms: 1.11x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 4.41 ms: 1.08x faster                                                       |
| raytrace                   | 298 ms                                                       | 277 ms: 1.07x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.97 us: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.31 us: 1.06x faster                                                       |
| async_generators           | 390 ms                                                       | 369 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.2 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                       |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.0 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.23 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.4 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 91.8 ms: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| float                      | 76.6 ms                                                      | 78.9 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                        |
| nbody                      | 88.0 ms                                                      | 90.7 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                      |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.24 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                                       |
| scimark_sor                | 109 ms                                                       | 116 ms: 1.06x slower                                                        |
| django_template            | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.5 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.8 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.12x slower                                                        |
| pyflate                    | 439 ms                                                       | 498 ms: 1.13x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.54 sec: 1.18x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.39 ms: 1.20x slower                                                       |
| go                         | 150 ms                                                       | 180 ms: 1.21x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                                       |
| coverage                   | 66.7 ms                                                      | 84.2 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.48 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (6): pycparser, scimark_fft, pprint_safe_repr, xml_etree_parse, pprint_pformat, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240824-3.14.0a0-e38d0af/bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x