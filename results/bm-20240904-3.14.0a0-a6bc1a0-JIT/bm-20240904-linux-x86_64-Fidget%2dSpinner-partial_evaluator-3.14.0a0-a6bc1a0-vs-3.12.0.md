# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: partial_evaluator
- machine: linux-x86_64
- commit hash: a6bc1a0
- commit date: 2024-09-04
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                         |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.06x slower                                                       |
| tornado_http   | 103 ms                                                 | 95.0 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 410 ms: 1.40x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 910 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                        |
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                        |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                        |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 77.4 ms: 1.15x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.21 ms: 1.04x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                        |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                        |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                         |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 410 ms: 1.40x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 910 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 65.7 ms: 1.25x faster                                                        |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                         |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                        |
| mako                       | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                       |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                        |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.2 ms: 1.19x faster                                                        |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                        |
| richards                   | 45.8 ms                                                | 39.2 ms: 1.17x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.37 ms: 1.16x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 77.4 ms: 1.15x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                        |
| richards_super             | 51.5 ms                                                | 44.8 ms: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                         |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                        |
| fannkuch                   | 417 ms                                                 | 371 ms: 1.12x faster                                                         |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                        |
| tornado_http               | 103 ms                                                 | 95.0 ms: 1.08x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                         |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                         |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                         |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                       |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                        |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                         |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                         |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                         |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                         |
| nqueens                    | 83.3 ms                                                | 85.3 ms: 1.02x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                                       |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.21 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 57.8 ms: 1.05x slower                                                        |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                        |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.06x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.92 ms: 1.08x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                        |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                        |
| coverage                   | 72.7 ms                                                | 86.4 ms: 1.19x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (7): json_dumps, sqlglot_transpile, dulwich_log, sympy_str, bench_mp_pool, regex_dna, json_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240904-3.14.0a0-a6bc1a0-JIT/bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x