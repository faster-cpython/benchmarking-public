# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.02x faster
- HPT reliability: 72.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.28 sec: 1.14x slower                                                      |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 321 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 384 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 773 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 560 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| float          | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                       |
| regex_dna      | 239 ms                                                       | 261 ms: 1.09x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 77.7 ms: 1.11x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.0 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.4 ms: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

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
| mako            | 10.0 ms                                                      | 9.16 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 42.1 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 321 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 384 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 773 ms: 1.36x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.2 us: 1.35x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 560 ms: 1.24x faster                                                        |
| deepcopy                   | 368 us                                                       | 301 us: 1.22x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.2 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.1 ms: 1.12x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 77.7 ms: 1.11x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.16 ms: 1.09x faster                                                       |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| scimark_fft                | 301 ms                                                       | 285 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.00 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 98.0 ms: 1.05x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.16 us: 1.05x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.8 ms: 1.04x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.11 ms: 1.04x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.49 us: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 920 us: 1.03x faster                                                        |
| async_generators           | 390 ms                                                       | 382 ms: 1.02x faster                                                        |
| float                      | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                      |
| richards_super             | 51.3 ms                                                      | 50.7 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                      |
| generators                 | 37.4 ms                                                      | 37.8 ms: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.01x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.4 ms: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 396 ms: 1.02x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.9 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| sympy_str                  | 302 ms                                                       | 315 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.5 ns: 1.05x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 172 ms: 1.06x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.08x slower                                                       |
| pyflate                    | 439 ms                                                       | 475 ms: 1.08x slower                                                        |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                        |
| regex_dna                  | 239 ms                                                       | 261 ms: 1.09x slower                                                        |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 99.0 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.96 ms: 1.10x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.1 ms: 1.10x slower                                                       |
| sympy_expand               | 484 ms                                                       | 535 ms: 1.11x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 26.7 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.12x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.85 ms: 1.13x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.28 sec: 1.14x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 65.9 ms: 1.15x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.95 ms: 1.17x slower                                                       |
| coverage                   | 66.7 ms                                                      | 78.0 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.93 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 188 us: 1.24x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.37 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (5): pprint_safe_repr, asyncio_tcp, pickle_pure_python, tornado_http, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 72.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x