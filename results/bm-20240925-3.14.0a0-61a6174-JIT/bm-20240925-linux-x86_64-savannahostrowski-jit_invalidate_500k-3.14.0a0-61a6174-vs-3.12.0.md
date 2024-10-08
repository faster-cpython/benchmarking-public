# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.07x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                            |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                          |
| tornado_http   | 103 ms                                                 | 94.6 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                            |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.46x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 876 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 887 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                           |
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                            |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                           |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 77.3 ms: 1.15x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                           |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                            |
| json_dumps           | 10.4 ms                                                | 9.81 ms: 1.06x faster                                                           |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                                           |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.02x faster                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.00x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.00x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                           |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 27.4 us: 1.49x faster                                                           |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.46x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                                            |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 876 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 887 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                            |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                                           |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                            |
| mako                       | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                           |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                           |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                          |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 63.2 ms: 1.19x faster                                                           |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 77.3 ms: 1.15x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                           |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                                           |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                           |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                           |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                                            |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                            |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                                           |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| tornado_http               | 103 ms                                                 | 94.6 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                           |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.07x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 9.81 ms: 1.06x faster                                                           |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                            |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                          |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                           |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                           |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.02x faster                                                           |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                           |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                           |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 844 us: 1.00x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.00x slower                                                           |
| pickle_list                | 5.08 us                                                | 5.11 us: 1.00x slower                                                           |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| asyncio_tcp                | 491 ms                                                 | 497 ms: 1.01x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                           |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                            |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                          |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                            |
| nqueens                    | 83.3 ms                                                | 88.5 ms: 1.06x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 58.4 ms: 1.06x slower                                                           |
| sympy_integrate            | 21.4 ms                                                | 22.9 ms: 1.07x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.97 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| generators                 | 31.2 ms                                                | 34.9 ms: 1.12x slower                                                           |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                                           |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                           |
| unpack_sequence            | 54.0 ns                                                | 112 ns: 2.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (7): pprint_pformat, unpickle_list, bench_mp_pool, sympy_str, pycparser, dulwich_log, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240925-3.14.0a0-61a6174-JIT/bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x