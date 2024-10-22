# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 363fca1
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 290 ms: 1.06x slower                                                      |
| docutils       | 2.77 sec                                               | 7.91 sec: 2.86x slower                                                    |
| tornado_http   | 103 ms                                                 | 95.1 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 850 ms: 1.39x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 850 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.8 ms: 1.22x faster                                                     |
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                      |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                      |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                     |
| django_template | 34.6 ms                                                | 38.6 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.52x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 850 ms: 1.39x faster                                                      |
| deepcopy                   | 371 us                                                 | 270 us: 1.38x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 850 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                     |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.23x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                    |
| nbody                      | 97.0 ms                                                | 79.8 ms: 1.22x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.21x faster                                                     |
| mako                       | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.20 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                     |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                     |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                     |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                                      |
| richards_super             | 51.5 ms                                                | 45.5 ms: 1.13x faster                                                     |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                      |
| tornado_http               | 103 ms                                                 | 95.1 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.55 ms: 1.07x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                    |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                     |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| json                       | 5.26 ms                                                | 5.11 ms: 1.03x faster                                                     |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 166 ms: 1.02x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.02x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                    |
| sympy_expand               | 478 ms                                                 | 497 ms: 1.04x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                                     |
| go                         | 139 ms                                                 | 147 ms: 1.06x slower                                                      |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                      |
| 2to3                       | 274 ms                                                 | 290 ms: 1.06x slower                                                      |
| deltablue                  | 3.72 ms                                                | 3.94 ms: 1.06x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 58.9 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                     |
| nqueens                    | 83.3 ms                                                | 91.4 ms: 1.10x slower                                                     |
| django_template            | 34.6 ms                                                | 38.6 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.13x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 958 us: 1.14x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 24.5 ms: 1.15x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                     |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.29x slower                                                     |
| docutils                   | 2.77 sec                                               | 7.91 sec: 2.86x slower                                                    |
| raytrace                   | 312 ms                                                 | 5.99 sec: 19.20x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (6): dask, sqlglot_transpile, scimark_sor, bench_mp_pool, coroutines, sympy_str
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-363fca1-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x