# Results vs. 3.12.0

- fork: python
- ref: b9e10d1a0fc4d8428d4b
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.03x faster
- HPT reliability: 84.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 762 ms: 1.38x faster                                                        |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| float          | 76.6 ms                                                      | 80.8 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 99.7 ms: 1.03x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.29 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 762 ms: 1.38x faster                                                        |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                       |
| deepcopy                   | 368 us                                                       | 288 us: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                       |
| raytrace                   | 298 ms                                                       | 265 ms: 1.12x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.0 ms: 1.12x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.77 us: 1.11x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 860 us: 1.10x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.18 us: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.54 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.3 ms: 1.04x faster                                                       |
| nbody                      | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                       |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 99.7 ms: 1.03x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.0 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| django_template            | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                        |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 820 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.29 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.1 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.3 ns: 1.03x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| go                         | 150 ms                                                       | 157 ms: 1.05x slower                                                        |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.6 ms: 1.05x slower                                                       |
| float                      | 76.6 ms                                                      | 80.8 ms: 1.05x slower                                                       |
| pyflate                    | 439 ms                                                       | 464 ms: 1.06x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.29 sec: 1.06x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.33 ms: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.4 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.8 ms: 1.11x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 77.3 ms: 1.16x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.19 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (4): regex_dna, nqueens, sqlglot_transpile, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240819-3.14.0a0-b9e10d1/bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 84.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x