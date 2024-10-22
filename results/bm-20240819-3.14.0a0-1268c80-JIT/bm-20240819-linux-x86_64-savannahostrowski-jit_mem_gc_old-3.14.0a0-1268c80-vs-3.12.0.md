# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_gc_old
- machine: linux-x86_64
- commit hash: 1268c80
- commit date: 2024-08-19
- overall geometric mean: 1.08x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                       |
| docutils       | 2.77 sec                                               | 3.00 sec: 1.08x slower                                                     |
| tornado_http   | 103 ms                                                 | 93.3 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                       |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 898 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                      |
| nbody          | 97.0 ms                                                | 83.4 ms: 1.16x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.00x faster                                                      |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                       |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 81.7 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                      |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                      |
| django_template | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.52x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                       |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                       |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 898 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                       |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 65.8 ms: 1.24x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 61.9 ms: 1.21x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                      |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                      |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                      |
| richards                   | 45.8 ms                                                | 39.0 ms: 1.18x faster                                                      |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                      |
| nbody                      | 97.0 ms                                                | 83.4 ms: 1.16x faster                                                      |
| spectral_norm              | 115 ms                                                 | 99.3 ms: 1.16x faster                                                      |
| richards_super             | 51.5 ms                                                | 44.8 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                      |
| fannkuch                   | 417 ms                                                 | 370 ms: 1.13x faster                                                       |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                       |
| tornado_http               | 103 ms                                                 | 93.3 ms: 1.10x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 81.7 ms: 1.09x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                      |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                                       |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                       |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                      |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.59 ms: 1.00x faster                                                      |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                       |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                      |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                       |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                      |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                      |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                                       |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                      |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 57.9 ms: 1.06x slower                                                      |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                                      |
| generators                 | 31.2 ms                                                | 33.5 ms: 1.07x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.00 sec: 1.08x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                               |

Benchmark hidden because not significant (3): coroutines, bench_mp_pool, sqlglot_transpile
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240819-3.14.0a0-1268c80-JIT/bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x