# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_inv_mem_100k
- machine: linux-x86_64
- commit hash: 17ece50
- commit date: 2024-09-23
- overall geometric mean: 1.079x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                         |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                       |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 318 ms: 1.48x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 886 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.27x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.6 ms: 1.20x faster                                                        |
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                         |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                         |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.0 ms: 1.04x faster                                                        |
| unpickle_list        | 5.29 us                                                | 5.15 us: 1.03x faster                                                        |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.15 us: 1.01x slower                                                        |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.75 ms: 1.22x faster                                                        |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                        |
| async_tree_none            | 472 ms                                                 | 318 ms: 1.48x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                         |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 886 ms: 1.31x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.27x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                        |
| mako                       | 11.9 ms                                                | 9.75 ms: 1.22x faster                                                        |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                       |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.21x faster                                                         |
| nbody                      | 97.0 ms                                                | 80.6 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                        |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                        |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.38 ms: 1.15x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                        |
| richards_super             | 51.5 ms                                                | 46.0 ms: 1.12x faster                                                        |
| richards                   | 45.8 ms                                                | 40.9 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                        |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                         |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                         |
| fannkuch                   | 417 ms                                                 | 378 ms: 1.10x faster                                                         |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                         |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                         |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                         |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                         |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| json_dumps                 | 10.4 ms                                                | 10.0 ms: 1.04x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.68 ms: 1.03x faster                                                        |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                        |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                         |
| unpickle_list              | 5.29 us                                                | 5.15 us: 1.03x faster                                                        |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.69 ms: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                         |
| asyncio_tcp                | 491 ms                                                 | 495 ms: 1.01x slower                                                         |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| pickle_list                | 5.08 us                                                | 5.15 us: 1.01x slower                                                        |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                         |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                         |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                         |
| nqueens                    | 83.3 ms                                                | 87.1 ms: 1.05x slower                                                        |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                       |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.02 ms: 1.10x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 60.7 ms: 1.11x slower                                                        |
| telco                      | 7.10 ms                                                | 7.98 ms: 1.12x slower                                                        |
| generators                 | 31.2 ms                                                | 35.2 ms: 1.13x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.16x slower                                                        |
| coverage                   | 72.7 ms                                                | 89.3 ms: 1.23x slower                                                        |
| unpack_sequence            | 54.0 ns                                                | 107 ns: 1.99x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (5): coroutines, pprint_pformat, logging_silent, dulwich_log, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-17ece50-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.079x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x