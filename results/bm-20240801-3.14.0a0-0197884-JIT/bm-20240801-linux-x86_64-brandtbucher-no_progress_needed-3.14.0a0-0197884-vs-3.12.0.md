# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 0197884
- commit date: 2024-08-01
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 284 ms: 1.04x slower                                                      |
| docutils       | 2.77 sec                                               | 2.99 sec: 1.08x slower                                                    |
| tornado_http   | 103 ms                                                 | 94.3 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                     |
| nbody          | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 145 ms: 1.02x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                     |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                     |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.78 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                      |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                                     |
| mako                       | 11.9 ms                                                | 9.78 ms: 1.22x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                     |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.21 ms: 1.20x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                     |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                     |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                      |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| tornado_http               | 103 ms                                                 | 94.3 ms: 1.09x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                      |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                      |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                                      |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 820 us: 1.03x faster                                                      |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                     |
| regex_compile              | 148 ms                                                 | 145 ms: 1.02x faster                                                      |
| dask                       | 372 ms                                                 | 364 ms: 1.02x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                    |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.82 ms: 1.01x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                      |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                     |
| sympy_str                  | 300 ms                                                 | 310 ms: 1.03x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                      |
| 2to3                       | 274 ms                                                 | 284 ms: 1.04x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                     |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                      |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                     |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.6 ms: 1.07x slower                                                     |
| go                         | 139 ms                                                 | 150 ms: 1.08x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.99 sec: 1.08x slower                                                    |
| sympy_expand               | 478 ms                                                 | 517 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                     |
| hexiom                     | 6.41 ms                                                | 7.64 ms: 1.19x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                     |
| coverage                   | 72.7 ms                                                | 90.4 ms: 1.24x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (3): pprint_pformat, bench_mp_pool, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240801-3.14.0a0-0197884-JIT/bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x