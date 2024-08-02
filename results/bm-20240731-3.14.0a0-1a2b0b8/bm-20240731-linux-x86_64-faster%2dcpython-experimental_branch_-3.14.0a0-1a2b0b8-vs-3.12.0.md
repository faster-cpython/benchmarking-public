# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                                            |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.6 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 865 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                           |
| float          | 84.7 ms                                                | 76.4 ms: 1.11x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                            |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                            |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                           |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.01x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| django_template | 34.6 ms                                                | 35.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 865 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.35x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                           |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                            |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                           |
| tornado_http               | 103 ms                                                 | 90.6 ms: 1.13x faster                                                           |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.12x faster                                                           |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                           |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                            |
| float                      | 84.7 ms                                                | 76.4 ms: 1.11x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 74.8 ms: 1.10x faster                                                           |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 69.4 ms: 1.08x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 787 us: 1.07x faster                                                            |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                           |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                          |
| dask                       | 372 ms                                                 | 357 ms: 1.04x faster                                                            |
| nqueens                    | 83.3 ms                                                | 80.0 ms: 1.04x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                           |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                          |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                                            |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                                           |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.8 ms: 1.02x faster                                                           |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                            |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.01x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                                           |
| asyncio_tcp                | 491 ms                                                 | 488 ms: 1.00x faster                                                            |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.01x slower                                                           |
| pyflate                    | 482 ms                                                 | 490 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                            |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.8 ms: 1.03x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                           |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                            |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x