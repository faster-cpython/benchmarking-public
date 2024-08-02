# Results vs. 3.12.0

- fork: brandtbucher
- ref: exits
- machine: linux-x86_64
- commit hash: 345fc71
- commit date: 2024-05-04
- overall geometric mean: 1.03x faster
- HPT reliability: 92.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                          |
| chameleon      | 7.41 ms                                                | 7.16 ms: 1.03x faster                                         |
| tornado_http   | 103 ms                                                 | 97.4 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 365 ms: 1.29x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 931 ms: 1.27x faster                                          |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 607 ms: 1.20x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                          |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                         |
| float          | 84.7 ms                                                | 72.6 ms: 1.17x faster                                         |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.05x slower                                         |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                          |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                        |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 84.4 ms: 1.06x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                         |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                         |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                          |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                         |
| unpickle_list        | 5.29 us                                                | 5.15 us: 1.03x faster                                         |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                         |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.69 ms: 1.11x slower                                         |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.45 ms: 1.26x faster                                         |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                         |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                         |
| async_tree_none            | 472 ms                                                 | 365 ms: 1.29x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 931 ms: 1.27x faster                                          |
| mako                       | 11.9 ms                                                | 9.45 ms: 1.26x faster                                         |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                          |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                          |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 607 ms: 1.20x faster                                          |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                         |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 64.0 ms: 1.17x faster                                         |
| fannkuch                   | 417 ms                                                 | 357 ms: 1.17x faster                                          |
| float                      | 84.7 ms                                                | 72.6 ms: 1.17x faster                                         |
| chaos                      | 67.0 ms                                                | 57.4 ms: 1.17x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 70.3 ms: 1.16x faster                                         |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                          |
| pathlib                    | 19.3 ms                                                | 17.8 ms: 1.09x faster                                         |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 37.6 us: 1.08x faster                                         |
| logging_format             | 7.23 us                                                | 6.70 us: 1.08x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.69 ms: 1.08x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                          |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                         |
| logging_simple             | 6.46 us                                                | 6.06 us: 1.07x faster                                         |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                          |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                        |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 84.4 ms: 1.06x faster                                         |
| tornado_http               | 103 ms                                                 | 97.4 ms: 1.05x faster                                         |
| richards_super             | 51.5 ms                                                | 49.0 ms: 1.05x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                          |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                         |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                         |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                          |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                          |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                         |
| json                       | 5.26 ms                                                | 5.07 ms: 1.04x faster                                         |
| chameleon                  | 7.41 ms                                                | 7.16 ms: 1.03x faster                                         |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                         |
| unpickle_list              | 5.29 us                                                | 5.15 us: 1.03x faster                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                         |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.00x slower                                          |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                          |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                          |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                         |
| async_generators           | 463 ms                                                 | 470 ms: 1.02x slower                                          |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                          |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                          |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                          |
| hexiom                     | 6.41 ms                                                | 6.57 ms: 1.02x slower                                         |
| dulwich_log                | 68.5 ms                                                | 70.2 ms: 1.02x slower                                         |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                         |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                         |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                          |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                        |
| nqueens                    | 83.3 ms                                                | 86.3 ms: 1.04x slower                                         |
| sqlglot_optimize           | 54.8 ms                                                | 56.9 ms: 1.04x slower                                         |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                        |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.04x slower                                          |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.05x slower                                         |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                          |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                         |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                          |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                          |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                         |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                          |
| asyncio_tcp                | 491 ms                                                 | 523 ms: 1.07x slower                                          |
| mdp                        | 2.63 sec                                               | 2.82 sec: 1.07x slower                                        |
| gunicorn                   | 1.24 ms                                                | 1.36 ms: 1.09x slower                                         |
| aiohttp                    | 1.15 ms                                                | 1.26 ms: 1.09x slower                                         |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.69 ms: 1.11x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 178 us: 1.13x slower                                          |
| telco                      | 7.10 ms                                                | 8.18 ms: 1.15x slower                                         |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                         |
| coverage                   | 72.7 ms                                                | 88.0 ms: 1.21x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.85 ms: 1.25x slower                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (8): mypy2, pickle_list, sqlite_synth, bench_mp_pool, deepcopy, deepcopy_reduce, deltablue, unpickle
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240504-3.13.0a6+-345fc71-JIT/bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x