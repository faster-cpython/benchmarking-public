# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: f135fa1
- commit date: 2024-08-06
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.7 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 428 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 917 ms: 1.26x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.2 ms: 1.22x faster                                                     |
| float          | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                     |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.57 ms: 1.01x faster                                                     |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                      |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.20x faster                                                     |
| django_template | 34.6 ms                                                | 36.2 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 428 ms: 1.35x faster                                                      |
| deepcopy                   | 371 us                                                 | 275 us: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 917 ms: 1.26x faster                                                      |
| scimark_fft                | 382 ms                                                 | 304 ms: 1.26x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 60.4 ms: 1.24x faster                                                     |
| nbody                      | 97.0 ms                                                | 79.2 ms: 1.22x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.20x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 68.0 ms: 1.20x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.80 us: 1.19x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                     |
| float                      | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.15x faster                                                     |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                      |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                     |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                      |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                      |
| tornado_http               | 103 ms                                                 | 92.7 ms: 1.11x faster                                                     |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                      |
| richards                   | 45.8 ms                                                | 41.7 ms: 1.10x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                      |
| richards_super             | 51.5 ms                                                | 47.4 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                     |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.61 ms: 1.05x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.60 ms: 1.03x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 823 us: 1.02x faster                                                      |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.57 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| async_generators           | 463 ms                                                 | 469 ms: 1.01x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                      |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                                    |
| nqueens                    | 83.3 ms                                                | 84.9 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 56.4 ms: 1.03x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                     |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                      |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.04x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                     |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.06x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                     |
| sympy_expand               | 478 ms                                                 | 515 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                     |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (4): bench_mp_pool, logging_silent, 2to3, json_loads
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240806-3.14.0a0-f135fa1-JIT/bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.05x