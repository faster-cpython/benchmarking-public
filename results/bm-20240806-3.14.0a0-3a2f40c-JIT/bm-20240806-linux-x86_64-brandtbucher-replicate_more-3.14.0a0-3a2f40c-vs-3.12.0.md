# Results vs. 3.12.0

- fork: brandtbucher
- ref: replicate_more
- machine: linux-x86_64
- commit hash: 3a2f40c
- commit date: 2024-08-06
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 274 ms: 1.00x faster                                                  |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| tornado_http   | 103 ms                                                 | 92.9 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.37x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 430 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                 |
| nbody          | 97.0 ms                                                | 85.7 ms: 1.13x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.90 ms: 1.08x slower                                                 |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 293 us: 1.10x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.79 ms: 1.22x faster                                                 |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                                 |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.37x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 430 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                                  |
| scimark_fft                | 382 ms                                                 | 302 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.7 ms: 1.24x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 67.1 ms: 1.22x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                 |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.16x faster                                                 |
| float                      | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                 |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                                  |
| nbody                      | 97.0 ms                                                | 85.7 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                  |
| richards                   | 45.8 ms                                                | 41.0 ms: 1.12x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                 |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                  |
| tornado_http               | 103 ms                                                 | 92.9 ms: 1.11x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 293 us: 1.10x faster                                                  |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                  |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                 |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.03x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                 |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                  |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                  |
| 2to3                       | 274 ms                                                 | 274 ms: 1.00x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 497 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                                 |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                 |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.72 ms: 1.05x slower                                                 |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.90 ms: 1.08x slower                                                 |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.4 ms: 1.26x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): pycparser, json_dumps, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240806-3.14.0a0-3a2f40c-JIT/bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x