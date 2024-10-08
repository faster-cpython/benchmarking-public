# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 6a9d428
- commit date: 2024-08-14
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                  |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 94.5 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 432 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 917 ms: 1.26x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                 |
| float          | 84.7 ms                                                | 71.7 ms: 1.18x faster                                                 |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                  |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 432 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 917 ms: 1.26x faster                                                  |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.1 ms: 1.21x faster                                                 |
| nbody                      | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.19x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 68.6 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.24 ms: 1.19x faster                                                 |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                  |
| float                      | 84.7 ms                                                | 71.7 ms: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                 |
| spectral_norm              | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                 |
| fannkuch                   | 417 ms                                                 | 371 ms: 1.13x faster                                                  |
| richards_super             | 51.5 ms                                                | 46.1 ms: 1.12x faster                                                 |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.12x faster                                                 |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                  |
| tornado_http               | 103 ms                                                 | 94.5 ms: 1.09x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.51 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.02x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                 |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                  |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                 |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                  |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                  |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                 |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                 |
| django_template            | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 58.5 ms: 1.07x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                 |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                                 |
| generators                 | 31.2 ms                                                | 34.6 ms: 1.11x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.0 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, json_loads
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240814-3.14.0a0-6a9d428-JIT/bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x