# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_invalidate_1
- machine: linux-x86_64
- commit hash: 071a1a4
- commit date: 2024-08-20
- overall geometric mean: 1.09x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                             |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                           |
| tornado_http   | 103 ms                                                 | 93.2 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                             |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 900 ms: 1.28x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.9 ms: 1.21x faster                                                            |
| float          | 84.7 ms                                                | 72.1 ms: 1.18x faster                                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                            |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                             |
| xml_etree_generate   | 89.2 ms                                                | 82.6 ms: 1.08x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 58.0 ms: 1.06x faster                                                            |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.88 ms: 1.20x faster                                                            |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.3 us: 1.55x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                             |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                             |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                             |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 900 ms: 1.28x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 65.7 ms: 1.25x faster                                                            |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                           |
| nbody                      | 97.0 ms                                                | 79.9 ms: 1.21x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 62.1 ms: 1.21x faster                                                            |
| mako                       | 11.9 ms                                                | 9.88 ms: 1.20x faster                                                            |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.41 us: 1.19x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                            |
| float                      | 84.7 ms                                                | 72.1 ms: 1.18x faster                                                            |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                             |
| richards                   | 45.8 ms                                                | 39.1 ms: 1.17x faster                                                            |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                             |
| richards_super             | 51.5 ms                                                | 45.4 ms: 1.13x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.46 ms: 1.13x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                            |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                             |
| pyflate                    | 482 ms                                                 | 434 ms: 1.11x faster                                                             |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                                             |
| tornado_http               | 103 ms                                                 | 93.2 ms: 1.10x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 82.6 ms: 1.08x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 58.0 ms: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                             |
| logging_silent             | 104 ns                                                 | 98.5 ns: 1.06x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                             |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 816 us: 1.03x faster                                                             |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                             |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                            |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 495 ms: 1.01x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                             |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                                             |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                           |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                             |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                            |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                             |
| go                         | 139 ms                                                 | 144 ms: 1.04x slower                                                             |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                                             |
| sqlglot_optimize           | 54.8 ms                                                | 57.8 ms: 1.05x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                            |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                                             |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.90 ms: 1.08x slower                                                            |
| generators                 | 31.2 ms                                                | 33.6 ms: 1.08x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                             |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                            |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (3): pycparser, bench_mp_pool, json_dumps
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240820-3.14.0a0-071a1a4-JIT/bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x