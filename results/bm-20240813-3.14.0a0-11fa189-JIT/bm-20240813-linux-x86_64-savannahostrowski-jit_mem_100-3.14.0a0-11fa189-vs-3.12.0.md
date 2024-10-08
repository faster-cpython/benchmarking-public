# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_100
- machine: linux-x86_64
- commit hash: 11fa189
- commit date: 2024-08-13
- overall geometric mean: 1.08x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 293 ms: 1.07x slower                                                    |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.2 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                    |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 435 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 918 ms: 1.26x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                   |
| float          | 84.7 ms                                                | 74.0 ms: 1.14x faster                                                   |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.04x faster                                                   |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                                    |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.90 ms: 1.20x faster                                                   |
| django_template | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                    |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                    |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 435 ms: 1.33x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 918 ms: 1.26x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                   |
| mako                       | 11.9 ms                                                | 9.90 ms: 1.20x faster                                                   |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                   |
| nbody                      | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                   |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                   |
| spectral_norm              | 115 ms                                                 | 99.9 ms: 1.15x faster                                                   |
| float                      | 84.7 ms                                                | 74.0 ms: 1.14x faster                                                   |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                                    |
| richards                   | 45.8 ms                                                | 40.5 ms: 1.13x faster                                                   |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                    |
| richards_super             | 51.5 ms                                                | 45.9 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.54 ms: 1.11x faster                                                   |
| tornado_http               | 103 ms                                                 | 94.2 ms: 1.09x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.51 ms: 1.08x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                    |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                    |
| logging_silent             | 104 ns                                                 | 99.7 ns: 1.05x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                   |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.49 ms: 1.04x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.02x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                   |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                  |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                   |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.72 ms: 1.02x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                   |
| django_template            | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                   |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                   |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                   |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.80 ms: 1.06x slower                                                   |
| 2to3                       | 274 ms                                                 | 293 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 59.6 ms: 1.09x slower                                                   |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                   |
| generators                 | 31.2 ms                                                | 34.8 ms: 1.11x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                   |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (5): json, bench_mp_pool, sympy_sum, json_loads, pprint_pformat
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240813-3.14.0a0-11fa189-JIT/bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x