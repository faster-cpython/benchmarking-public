# Results vs. 3.12.0

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                     |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                   |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 388 ms: 1.49x faster                                                     |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 896 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.30x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 926 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.0 ms: 1.13x faster                                                    |
| float          | 84.7 ms                                                | 76.9 ms: 1.10x faster                                                    |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                    |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                    |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 388 ms: 1.49x faster                                                     |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                     |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 896 ms: 1.32x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.30x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 926 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                    |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                    |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                                     |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                    |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.15x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                    |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                                    |
| nbody                      | 97.0 ms                                                | 86.0 ms: 1.13x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                   |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                     |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                                    |
| logging_silent             | 104 ns                                                 | 94.5 ns: 1.10x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                    |
| float                      | 84.7 ms                                                | 76.9 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 780 us: 1.08x faster                                                     |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                   |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                    |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                     |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                     |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.12 ms: 1.05x faster                                                    |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                     |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                                     |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                    |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.04x faster                                                    |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                   |
| asyncio_tcp                | 491 ms                                                 | 479 ms: 1.02x faster                                                     |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                    |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                    |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                    |
| go                         | 139 ms                                                 | 159 ms: 1.14x slower                                                     |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                    |
| telco                      | 7.10 ms                                                | 8.34 ms: 1.18x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                             |

Benchmark hidden because not significant (8): richards, coroutines, json_dumps, bench_mp_pool, asyncio_tcp_ssl, json, json_loads, richards_super
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240824-3.14.0a0-bf9cfa8/bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x