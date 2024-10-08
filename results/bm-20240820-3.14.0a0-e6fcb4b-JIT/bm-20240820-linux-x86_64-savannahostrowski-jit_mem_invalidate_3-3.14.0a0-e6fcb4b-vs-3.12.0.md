# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_invalidate_3
- machine: linux-x86_64
- commit hash: e6fcb4b
- commit date: 2024-08-20
- overall geometric mean: 1.08x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                             |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                           |
| tornado_http   | 103 ms                                                 | 93.6 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 528 ms: 1.37x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                            |
| float          | 84.7 ms                                                | 72.1 ms: 1.17x faster                                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                            |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                            |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                             |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 528 ms: 1.37x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                             |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 65.3 ms: 1.25x faster                                                            |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                            |
| logging_format             | 7.23 us                                                | 6.01 us: 1.20x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 62.5 ms: 1.20x faster                                                            |
| nbody                      | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                            |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                            |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                                            |
| richards                   | 45.8 ms                                                | 39.0 ms: 1.18x faster                                                            |
| float                      | 84.7 ms                                                | 72.1 ms: 1.17x faster                                                            |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                             |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                            |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                            |
| richards_super             | 51.5 ms                                                | 45.1 ms: 1.14x faster                                                            |
| fannkuch                   | 417 ms                                                 | 368 ms: 1.13x faster                                                             |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.50 ms: 1.12x faster                                                            |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                             |
| tornado_http               | 103 ms                                                 | 93.6 ms: 1.10x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                             |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                             |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                             |
| logging_silent             | 104 ns                                                 | 100.0 ns: 1.04x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                           |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                             |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 817 us: 1.03x faster                                                             |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                             |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                                             |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                             |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                             |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                             |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                           |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                             |
| nqueens                    | 83.3 ms                                                | 86.3 ms: 1.04x slower                                                            |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                            |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 57.7 ms: 1.05x slower                                                            |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                             |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                            |
| hexiom                     | 6.41 ms                                                | 6.84 ms: 1.07x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                           |
| generators                 | 31.2 ms                                                | 33.5 ms: 1.07x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                             |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.16x slower                                                            |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                     |

Benchmark hidden because not significant (5): json_loads, bench_mp_pool, sqlglot_transpile, sympy_str, async_generators
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240820-3.14.0a0-e6fcb4b-JIT/bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x