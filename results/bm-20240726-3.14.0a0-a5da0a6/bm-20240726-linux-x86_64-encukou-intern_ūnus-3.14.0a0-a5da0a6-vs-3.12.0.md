# Results vs. 3.12.0

- fork: encukou
- ref: intern_ūnus
- machine: linux-x86_64
- commit hash: a5da0a6
- commit date: 2024-07-26
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                          |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                        |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                          |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 534 ms: 1.36x faster                                          |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                          |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.6 ms: 1.15x faster                                         |
| float          | 84.7 ms                                                | 77.4 ms: 1.09x faster                                         |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                         |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                          |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                        |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                          |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                         |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                          |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                         |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                         |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                         |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                          |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                          |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 534 ms: 1.36x faster                                          |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                         |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                         |
| raytrace                   | 312 ms                                                 | 255 ms: 1.22x faster                                          |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                         |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                         |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                         |
| nbody                      | 97.0 ms                                                | 84.6 ms: 1.15x faster                                         |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                         |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                         |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                          |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                         |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                        |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                         |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                          |
| float                      | 84.7 ms                                                | 77.4 ms: 1.09x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                         |
| gc_traversal               | 3.79 ms                                                | 3.49 ms: 1.09x faster                                         |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                          |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                          |
| scimark_fft                | 382 ms                                                 | 355 ms: 1.08x faster                                          |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                         |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                         |
| bench_thread_pool          | 842 us                                                 | 786 us: 1.07x faster                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                         |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                          |
| dask                       | 372 ms                                                 | 353 ms: 1.05x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 71.4 ms: 1.05x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                          |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                          |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.14 ms: 1.04x faster                                         |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                        |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                          |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                          |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                          |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                         |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                          |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                        |
| asyncio_tcp                | 491 ms                                                 | 481 ms: 1.02x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                          |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                          |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                          |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                        |
| nqueens                    | 83.3 ms                                                | 82.2 ms: 1.01x faster                                         |
| richards                   | 45.8 ms                                                | 45.3 ms: 1.01x faster                                         |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                         |
| richards_super             | 51.5 ms                                                | 51.2 ms: 1.01x faster                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                        |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                         |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                         |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                          |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                          |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                         |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                         |
| telco                      | 7.10 ms                                                | 8.15 ms: 1.15x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.16x slower                                         |
| coverage                   | 72.7 ms                                                | 89.3 ms: 1.23x slower                                         |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (4): bench_mp_pool, pycparser, json_dumps, go
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240726-3.14.0a0-a5da0a6/bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x