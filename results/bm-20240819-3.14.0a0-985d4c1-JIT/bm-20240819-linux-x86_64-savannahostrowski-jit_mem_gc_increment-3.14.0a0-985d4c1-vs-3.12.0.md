# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_gc_increment
- machine: linux-x86_64
- commit hash: 985d4c1
- commit date: 2024-08-19
- overall geometric mean: 1.08x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                             |
| docutils       | 2.77 sec                                               | 2.98 sec: 1.07x slower                                                           |
| tornado_http   | 103 ms                                                 | 93.1 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 419 ms: 1.38x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 865 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                            |
| float          | 84.7 ms                                                | 72.0 ms: 1.18x faster                                                            |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                            |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                             |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                            |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.5 us: 1.54x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                             |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 419 ms: 1.38x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 865 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                                             |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 66.5 ms: 1.23x faster                                                            |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                           |
| mako                       | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                            |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                            |
| nbody                      | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                            |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                             |
| float                      | 84.7 ms                                                | 72.0 ms: 1.18x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                            |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                            |
| richards_super             | 51.5 ms                                                | 45.0 ms: 1.15x faster                                                            |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                            |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.52 ms: 1.12x faster                                                            |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                             |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                             |
| tornado_http               | 103 ms                                                 | 93.1 ms: 1.10x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 107 ms: 1.10x faster                                                             |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                             |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                             |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                             |
| gc_traversal               | 3.79 ms                                                | 3.58 ms: 1.06x faster                                                            |
| logging_silent             | 104 ns                                                 | 99.2 ns: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                             |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                                            |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                             |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                             |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                           |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                           |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                            |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                             |
| nqueens                    | 83.3 ms                                                | 86.1 ms: 1.03x slower                                                            |
| go                         | 139 ms                                                 | 144 ms: 1.04x slower                                                             |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                           |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                            |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                             |
| hexiom                     | 6.41 ms                                                | 6.81 ms: 1.06x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                                            |
| generators                 | 31.2 ms                                                | 33.4 ms: 1.07x slower                                                            |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.07x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.98 sec: 1.07x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                             |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                            |
| coverage                   | 72.7 ms                                                | 85.5 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240819-3.14.0a0-985d4c1-JIT/bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x