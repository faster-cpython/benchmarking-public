# Results vs. 3.12.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                              |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| tornado_http   | 103 ms                                                 | 89.8 ms: 1.14x faster                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 313 ms: 1.50x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 393 ms: 1.47x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                              |
| async_tree_io              | 1.16 sec                                               | 866 ms: 1.33x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                              |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.3 ms: 1.11x faster                                             |
| float          | 84.7 ms                                                | 76.8 ms: 1.10x faster                                             |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                             |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                              |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                            |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                              |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                             |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                             |
| json_loads           | 28.5 us                                                | 27.3 us: 1.04x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                              |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.01x faster                                             |
| pickle_dict          | 35.5 us                                                | 35.1 us: 1.01x faster                                             |
| unpickle_list        | 5.29 us                                                | 5.37 us: 1.02x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                             |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                             |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                             |
| django_template | 34.6 ms                                                | 34.4 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 313 ms: 1.50x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 393 ms: 1.47x faster                                              |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                              |
| async_tree_io              | 1.16 sec                                               | 866 ms: 1.33x faster                                              |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                             |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                             |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                              |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                             |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                             |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                              |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 71.0 ms: 1.15x faster                                             |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                              |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                             |
| tornado_http               | 103 ms                                                 | 89.8 ms: 1.14x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                             |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                             |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                            |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                              |
| nbody                      | 97.0 ms                                                | 87.3 ms: 1.11x faster                                             |
| float                      | 84.7 ms                                                | 76.8 ms: 1.10x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                              |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                              |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                            |
| bench_thread_pool          | 842 us                                                 | 791 us: 1.06x faster                                              |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                              |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                             |
| logging_silent             | 104 ns                                                 | 98.6 ns: 1.06x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                             |
| dulwich_log                | 68.5 ms                                                | 64.7 ms: 1.06x faster                                             |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.09 ms: 1.05x faster                                             |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                              |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                              |
| async_generators           | 463 ms                                                 | 440 ms: 1.05x faster                                              |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                             |
| unpack_sequence            | 54.0 ns                                                | 51.4 ns: 1.05x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                             |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                              |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.04x faster                                             |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                              |
| nqueens                    | 83.3 ms                                                | 80.0 ms: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                             |
| sqlglot_optimize           | 54.8 ms                                                | 52.9 ms: 1.04x faster                                             |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                              |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                              |
| asyncio_tcp                | 491 ms                                                 | 478 ms: 1.03x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                              |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                             |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                             |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.01x faster                                             |
| richards_super             | 51.5 ms                                                | 50.9 ms: 1.01x faster                                             |
| pickle_dict                | 35.5 us                                                | 35.1 us: 1.01x faster                                             |
| django_template            | 34.6 ms                                                | 34.4 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                              |
| unpickle_list              | 5.29 us                                                | 5.37 us: 1.02x slower                                             |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                             |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                            |
| gc_traversal               | 3.79 ms                                                | 3.90 ms: 1.03x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                             |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                              |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                             |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                             |
| telco                      | 7.10 ms                                                | 8.45 ms: 1.19x slower                                             |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (4): pycparser, coroutines, pickle_list, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.093x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x