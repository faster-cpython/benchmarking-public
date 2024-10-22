# Results vs. 3.12.0

- fork: mdboom
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 8ca892b
- commit date: 2024-09-26
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                        |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                      |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.14x faster                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                        |
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                        |
| async_tree_io              | 1.16 sec                                               | 855 ms: 1.35x faster                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.33x faster                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                        |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.0 ms: 1.11x faster                                       |
| nbody          | 97.0 ms                                                | 88.0 ms: 1.10x faster                                       |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                        |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.03x slower                                       |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                       |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                      |
| unpickle             | 15.9 us                                                | 14.6 us: 1.09x faster                                       |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                        |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                       |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                       |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                        |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                        |
| unpickle_list        | 5.29 us                                                | 5.24 us: 1.01x faster                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                       |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                       |
| django_template | 34.6 ms                                                | 34.0 ms: 1.02x faster                                       |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                        |
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                        |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                        |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                        |
| async_tree_io              | 1.16 sec                                               | 855 ms: 1.35x faster                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.33x faster                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                       |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                       |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                        |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                        |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                       |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                        |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                       |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                       |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                        |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                       |
| tornado_http               | 103 ms                                                 | 90.4 ms: 1.14x faster                                       |
| crypto_pyaes               | 81.9 ms                                                | 72.7 ms: 1.13x faster                                       |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                       |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                       |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                      |
| float                      | 84.7 ms                                                | 76.0 ms: 1.11x faster                                       |
| nbody                      | 97.0 ms                                                | 88.0 ms: 1.10x faster                                       |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                       |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.09x faster                                       |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                        |
| json                       | 5.26 ms                                                | 4.90 ms: 1.07x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                       |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                        |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                        |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                       |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                        |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.06x faster                                       |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                        |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                        |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                       |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                       |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                      |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                       |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                        |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                        |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                      |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                       |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                       |
| sqlglot_optimize           | 54.8 ms                                                | 53.0 ms: 1.03x faster                                       |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                        |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                      |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                        |
| asyncio_tcp                | 491 ms                                                 | 481 ms: 1.02x faster                                        |
| django_template            | 34.6 ms                                                | 34.0 ms: 1.02x faster                                       |
| unpack_sequence            | 54.0 ns                                                | 53.2 ns: 1.01x faster                                       |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                        |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                        |
| unpickle_list              | 5.29 us                                                | 5.24 us: 1.01x faster                                       |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                        |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                       |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                        |
| richards                   | 45.8 ms                                                | 46.2 ms: 1.01x slower                                       |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                       |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                        |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.03x slower                                       |
| gc_traversal               | 3.79 ms                                                | 3.92 ms: 1.03x slower                                       |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                       |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                       |
| telco                      | 7.10 ms                                                | 8.37 ms: 1.18x slower                                       |
| coverage                   | 72.7 ms                                                | 89.8 ms: 1.24x slower                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                |

Benchmark hidden because not significant (5): asyncio_tcp_ssl, json_dumps, bench_mp_pool, pickle_list, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240926-3.14.0a0-8ca892b/bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x