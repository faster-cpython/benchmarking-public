# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.03x faster
- HPT reliability: 76.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 772 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 800 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 86.3 ms: 1.02x faster                                                       |
| float          | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.59 ms: 1.01x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.27 sec: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                       |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 772 ms: 1.37x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 800 ms: 1.30x faster                                                        |
| deepcopy                   | 368 us                                                       | 285 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.27x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.3 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                       |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.1 ms: 1.10x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 865 us: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.92 us: 1.08x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.25 us: 1.07x faster                                                       |
| async_generators           | 390 ms                                                       | 364 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.9 ms: 1.06x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.06x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.0 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.1 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.3 ms: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| scimark_fft                | 301 ms                                                       | 299 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.22 ms: 1.00x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.78 ms: 1.00x slower                                                       |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.59 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 389 ms: 1.01x slower                                                        |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 814 ms: 1.01x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 90.9 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.4 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                      |
| fannkuch                   | 350 ms                                                       | 357 ms: 1.02x slower                                                        |
| django_template            | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 96.3 ns: 1.02x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| float                      | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.27 sec: 1.05x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 96.6 ms: 1.05x slower                                                       |
| go                         | 150 ms                                                       | 158 ms: 1.06x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.36 ms: 1.07x slower                                                       |
| richards_super             | 51.3 ms                                                      | 55.4 ms: 1.08x slower                                                       |
| richards                   | 45.7 ms                                                      | 49.4 ms: 1.08x slower                                                       |
| pyflate                    | 439 ms                                                       | 478 ms: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.98 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.48 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 76.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x