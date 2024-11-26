# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.017x faster
- HPT reliability: 71.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 311 ms: 1.09x slower                                              |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.10x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x slower                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                              |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.38x faster                                              |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                              |
| async_tree_io              | 1.04 sec                                                     | 802 ms: 1.30x faster                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 813 ms: 1.30x faster                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                              |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.5 ms: 1.08x faster                                             |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                              |
| float          | 76.6 ms                                                      | 73.8 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.06x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.39 ms: 1.06x faster                                             |
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                              |
| regex_compile  | 144 ms                                                       | 149 ms: 1.04x slower                                              |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.1 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 103 ms                                                       | 98.3 ms: 1.05x faster                                             |
| xml_etree_process    | 58.4 ms                                                      | 55.9 ms: 1.05x faster                                             |
| tomli_loads          | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                            |
| json_loads           | 24.4 us                                                      | 24.2 us: 1.01x faster                                             |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                             |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.02x slower                                             |
| pickle_list          | 4.43 us                                                      | 4.55 us: 1.03x slower                                             |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.03x slower                                              |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                              |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                             |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                             |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                             |
| django_template | 38.2 ms                                                      | 43.3 ms: 1.14x slower                                             |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                              |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.38x faster                                              |
| deepcopy_memo              | 36.8 us                                                      | 26.6 us: 1.38x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                              |
| async_tree_io              | 1.04 sec                                                     | 802 ms: 1.30x faster                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 813 ms: 1.30x faster                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                              |
| deepcopy                   | 368 us                                                       | 297 us: 1.24x faster                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                              |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.21x faster                                             |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                             |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.14x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 71.3 ms: 1.13x faster                                             |
| spectral_norm              | 91.6 ms                                                      | 81.9 ms: 1.12x faster                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.81 ms: 1.10x faster                                             |
| mako                       | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                             |
| xml_etree_generate         | 86.1 ms                                                      | 79.1 ms: 1.09x faster                                             |
| nbody                      | 88.0 ms                                                      | 81.5 ms: 1.08x faster                                             |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                              |
| regex_effbot               | 3.57 ms                                                      | 3.39 ms: 1.06x faster                                             |
| xml_etree_iterparse        | 103 ms                                                       | 98.3 ms: 1.05x faster                                             |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                              |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.05x faster                                             |
| xml_etree_process          | 58.4 ms                                                      | 55.9 ms: 1.05x faster                                             |
| logging_format             | 7.48 us                                                      | 7.17 us: 1.04x faster                                             |
| float                      | 76.6 ms                                                      | 73.8 ms: 1.04x faster                                             |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                              |
| bench_thread_pool          | 950 us                                                       | 921 us: 1.03x faster                                              |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.02x faster                                             |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                              |
| richards                   | 45.7 ms                                                      | 44.8 ms: 1.02x faster                                             |
| tomli_loads                | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                            |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                              |
| dulwich_log                | 65.4 ms                                                      | 64.2 ms: 1.02x faster                                             |
| async_generators           | 390 ms                                                       | 384 ms: 1.02x faster                                              |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                              |
| scimark_lu                 | 98.8 ms                                                      | 97.3 ms: 1.02x faster                                             |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.01x faster                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.2 ms: 1.01x faster                                             |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                             |
| json_loads                 | 24.4 us                                                      | 24.2 us: 1.01x faster                                             |
| go                         | 150 ms                                                       | 149 ms: 1.00x faster                                              |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                            |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                              |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                            |
| asyncio_websockets         | 387 ms                                                       | 393 ms: 1.02x slower                                              |
| richards_super             | 51.3 ms                                                      | 52.3 ms: 1.02x slower                                             |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                             |
| sympy_str                  | 302 ms                                                       | 308 ms: 1.02x slower                                              |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.02x slower                                             |
| pickle_list                | 4.43 us                                                      | 4.55 us: 1.03x slower                                             |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                             |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                              |
| chaos                      | 64.0 ms                                                      | 66.1 ms: 1.03x slower                                             |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.03x slower                                              |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.03x slower                                              |
| regex_compile              | 144 ms                                                       | 149 ms: 1.04x slower                                              |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                              |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                             |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                             |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                            |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                              |
| raytrace                   | 298 ms                                                       | 318 ms: 1.07x slower                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                             |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                             |
| pyflate                    | 439 ms                                                       | 474 ms: 1.08x slower                                              |
| 2to3                       | 285 ms                                                       | 311 ms: 1.09x slower                                              |
| sympy_expand               | 484 ms                                                       | 528 ms: 1.09x slower                                              |
| nqueens                    | 89.9 ms                                                      | 98.3 ms: 1.09x slower                                             |
| bench_mp_pool              | 4.76 ms                                                      | 5.21 ms: 1.09x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.10x slower                                             |
| sympy_integrate            | 23.9 ms                                                      | 26.4 ms: 1.10x slower                                             |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.10x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.13x slower                                              |
| generators                 | 37.4 ms                                                      | 42.5 ms: 1.14x slower                                             |
| django_template            | 38.2 ms                                                      | 43.3 ms: 1.14x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 65.7 ms: 1.14x slower                                             |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                             |
| hexiom                     | 5.96 ms                                                      | 6.92 ms: 1.16x slower                                             |
| telco                      | 6.96 ms                                                      | 8.28 ms: 1.19x slower                                             |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                             |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                              |
| coverage                   | 66.7 ms                                                      | 82.0 ms: 1.23x slower                                             |
| gc_traversal               | 3.48 ms                                                      | 4.41 ms: 1.27x slower                                             |
| unpack_sequence            | 53.2 ns                                                      | 88.0 ns: 1.66x slower                                             |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                      |

Benchmark hidden because not significant (5): xml_etree_parse, pprint_pformat, unpickle_list, pickle_dict, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.017x faster
# HPT report

- Reliability score: 71.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x