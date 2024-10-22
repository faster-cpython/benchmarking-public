# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 639e7c2
- commit date: 2024-07-16
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                      |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.2 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                      |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 839 ms: 1.41x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 830 ms: 1.39x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.42x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                     |
| nbody          | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                     |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                     |
| regex_dna      | 212 ms                                                 | 230 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                      |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                     |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                      |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 839 ms: 1.41x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 830 ms: 1.39x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                      |
| richards                   | 45.8 ms                                                | 35.7 ms: 1.28x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                     |
| richards_super             | 51.5 ms                                                | 40.9 ms: 1.26x faster                                                     |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                    |
| mako                       | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.3 ms: 1.22x faster                                                     |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.29 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                     |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                     |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                      |
| fannkuch                   | 417 ms                                                 | 364 ms: 1.14x faster                                                      |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                      |
| tornado_http               | 103 ms                                                 | 92.2 ms: 1.11x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                      |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.55 ms: 1.07x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                      |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                      |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 65.9 ms: 1.04x faster                                                     |
| dask                       | 372 ms                                                 | 359 ms: 1.04x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                    |
| sympy_str                  | 300 ms                                                 | 289 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                    |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                     |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                                     |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 825 us: 1.02x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 166 ms: 1.02x faster                                                      |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                      |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 21.8 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                     |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                     |
| sympy_expand               | 478 ms                                                 | 495 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 56.8 ms: 1.04x slower                                                     |
| nqueens                    | 83.3 ms                                                | 86.8 ms: 1.04x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.77 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                      |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.09x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                     |
| coverage                   | 72.7 ms                                                | 94.8 ms: 1.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (3): json_dumps, logging_silent, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240716-3.14.0a0-639e7c2-JIT/bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x