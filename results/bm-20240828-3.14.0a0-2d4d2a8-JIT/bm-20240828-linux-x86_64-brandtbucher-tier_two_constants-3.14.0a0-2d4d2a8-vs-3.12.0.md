# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 2d4d2a8
- commit date: 2024-08-28
- overall geometric mean: 1.087x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                      |
| docutils       | 2.77 sec                                               | 3.04 sec: 1.10x slower                                                    |
| tornado_http   | 103 ms                                                 | 94.4 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 404 ms: 1.42x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 902 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                     |
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                     |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                      |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                     |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.67 ms: 1.23x faster                                                     |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.52x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 404 ms: 1.42x faster                                                      |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 902 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 65.6 ms: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                      |
| mako                       | 11.9 ms                                                | 9.67 ms: 1.23x faster                                                     |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                     |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 63.2 ms: 1.19x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                                     |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                     |
| spectral_norm              | 115 ms                                                 | 98.5 ms: 1.17x faster                                                     |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 45.0 ms: 1.14x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                     |
| fannkuch                   | 417 ms                                                 | 370 ms: 1.13x faster                                                      |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                      |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                      |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                      |
| tornado_http               | 103 ms                                                 | 94.4 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                      |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                    |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 816 us: 1.03x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                     |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                     |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                      |
| asyncio_tcp                | 491 ms                                                 | 492 ms: 1.00x slower                                                      |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                      |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                     |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                     |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                    |
| json                       | 5.26 ms                                                | 5.38 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                      |
| generators                 | 31.2 ms                                                | 32.6 ms: 1.05x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                     |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.1 ms: 1.06x slower                                                     |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                     |
| docutils                   | 2.77 sec                                               | 3.04 sec: 1.10x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                     |
| go                         | 139 ms                                                 | 170 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (3): sympy_str, bench_mp_pool, sqlglot_transpile
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240828-3.14.0a0-2d4d2a8-JIT/bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.087x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x