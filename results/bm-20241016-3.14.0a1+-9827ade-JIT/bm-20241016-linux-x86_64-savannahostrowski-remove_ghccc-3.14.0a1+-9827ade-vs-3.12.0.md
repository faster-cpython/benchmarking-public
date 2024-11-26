# Results vs. 3.12.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                      |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                    |
| tornado_http   | 103 ms                                                 | 93.2 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                      |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 848 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 976 ms: 1.21x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                     |
| float          | 84.7 ms                                                | 75.9 ms: 1.12x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.06x faster                                                      |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.62 ms: 1.00x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                     |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.8 ms: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                      |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                     |
| unpickle_list        | 5.29 us                                                | 5.47 us: 1.03x slower                                                     |
| pickle_list          | 5.08 us                                                | 5.28 us: 1.04x slower                                                     |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.24x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                     |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                      |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.36x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 848 ms: 1.36x faster                                                      |
| deepcopy                   | 371 us                                                 | 274 us: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.1 ms: 1.22x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 976 ms: 1.21x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.20x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                     |
| nbody                      | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                     |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.1 ms: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.13x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                     |
| float                      | 84.7 ms                                                | 75.9 ms: 1.12x faster                                                     |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                     |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                      |
| tornado_http               | 103 ms                                                 | 93.2 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.61 ms: 1.10x faster                                                     |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                      |
| richards_super             | 51.5 ms                                                | 47.5 ms: 1.08x faster                                                     |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 449 ms: 1.08x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.8 ms: 1.07x faster                                                     |
| logging_silent             | 104 ns                                                 | 97.7 ns: 1.07x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                      |
| json                       | 5.26 ms                                                | 4.96 ms: 1.06x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                      |
| regex_compile              | 148 ms                                                 | 141 ms: 1.06x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                    |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 66.6 ms: 1.03x faster                                                     |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.03x faster                                                      |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.00x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.62 ms: 1.00x slower                                                     |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                      |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                     |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.03x slower                                                      |
| unpickle_list              | 5.29 us                                                | 5.47 us: 1.03x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                      |
| pickle_list                | 5.08 us                                                | 5.28 us: 1.04x slower                                                     |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                     |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                     |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                                     |
| nqueens                    | 83.3 ms                                                | 90.7 ms: 1.09x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 59.7 ms: 1.09x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 23.5 ms: 1.10x slower                                                     |
| hexiom                     | 6.41 ms                                                | 7.06 ms: 1.10x slower                                                     |
| generators                 | 31.2 ms                                                | 35.7 ms: 1.14x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.24x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.27x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.82x slower                                                     |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.04x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): spectral_norm
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.063x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x