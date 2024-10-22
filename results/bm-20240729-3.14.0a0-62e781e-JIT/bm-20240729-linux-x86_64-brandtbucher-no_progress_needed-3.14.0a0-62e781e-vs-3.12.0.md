# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 62e781e
- commit date: 2024-07-29
- overall geometric mean: 1.08x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                      |
| docutils       | 2.77 sec                                               | 2.99 sec: 1.08x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.8 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 867 ms: 1.36x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 907 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                     |
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                     |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                      |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.52x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                      |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 867 ms: 1.36x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 907 ms: 1.28x faster                                                      |
| scimark_fft                | 382 ms                                                 | 304 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.02 ms: 1.23x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                    |
| mako                       | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                     |
| logging_format             | 7.23 us                                                | 5.96 us: 1.21x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                     |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.43 us: 1.19x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.27 ms: 1.18x faster                                                     |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                      |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                     |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                     |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                      |
| tornado_http               | 103 ms                                                 | 92.8 ms: 1.11x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| richards                   | 45.8 ms                                                | 42.3 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                      |
| logging_silent             | 104 ns                                                 | 98.4 ns: 1.06x faster                                                     |
| richards_super             | 51.5 ms                                                | 48.7 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                      |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 818 us: 1.03x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                    |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                     |
| dask                       | 372 ms                                                 | 363 ms: 1.02x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sympy_str                  | 300 ms                                                 | 306 ms: 1.02x slower                                                      |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.03x slower                                                     |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                     |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 506 ms: 1.03x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                      |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                     |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                                     |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.08x slower                                                     |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.99 sec: 1.08x slower                                                    |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                     |
| hexiom                     | 6.41 ms                                                | 7.68 ms: 1.20x slower                                                     |
| coverage                   | 72.7 ms                                                | 90.4 ms: 1.24x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (3): sqlglot_transpile, scimark_lu, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240729-3.14.0a0-62e781e-JIT/bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x