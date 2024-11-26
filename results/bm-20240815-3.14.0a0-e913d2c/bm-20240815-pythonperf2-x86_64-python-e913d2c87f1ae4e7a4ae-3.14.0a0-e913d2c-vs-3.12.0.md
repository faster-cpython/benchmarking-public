# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.028x faster
- HPT reliability: 82.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 381 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 331 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 784 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 808 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                       |
| float          | 76.6 ms                                                      | 82.3 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.26 sec: 1.05x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 381 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 331 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 784 ms: 1.34x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 808 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                       |
| deepcopy                   | 368 us                                                       | 292 us: 1.26x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                       |
| raytrace                   | 298 ms                                                       | 265 ms: 1.12x faster                                                        |
| async_generators           | 390 ms                                                       | 352 ms: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.8 ms: 1.10x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.80 us: 1.10x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 870 us: 1.09x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.18 us: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.51 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.1 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                       |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.4 ms: 1.02x faster                                                       |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| scimark_fft                | 301 ms                                                       | 299 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.00x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 90.4 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| nbody                      | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 839 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.1 ns: 1.04x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.26 sec: 1.05x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.1 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.32 ms: 1.06x slower                                                       |
| fannkuch                   | 350 ms                                                       | 374 ms: 1.07x slower                                                        |
| float                      | 76.6 ms                                                      | 82.3 ms: 1.07x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                        |
| richards                   | 45.7 ms                                                      | 50.1 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.7 ms: 1.10x slower                                                       |
| pyflate                    | 439 ms                                                       | 491 ms: 1.12x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.90 ms: 1.13x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.16x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.40 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (6): regex_effbot, xml_etree_parse, sqlglot_transpile, 2to3, pycparser, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 82.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x