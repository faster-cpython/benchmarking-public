# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: 3d7e23f
- commit date: 2024-08-05
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                            |
| docutils       | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                          |
| tornado_http   | 103 ms                                                 | 89.7 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 526 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 558 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.2 ms: 1.12x faster                                                           |
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                           |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                           |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                                           |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 526 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.37x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 558 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                           |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                           |
| raytrace                   | 312 ms                                                 | 257 ms: 1.21x faster                                                            |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                                            |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                           |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| tornado_http               | 103 ms                                                 | 89.7 ms: 1.14x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                            |
| nbody                      | 97.0 ms                                                | 86.2 ms: 1.12x faster                                                           |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                                           |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                            |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.08x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 785 us: 1.07x faster                                                            |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                                            |
| logging_silent             | 104 ns                                                 | 98.0 ns: 1.07x faster                                                           |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                            |
| dask                       | 372 ms                                                 | 353 ms: 1.05x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                           |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                          |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                           |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                          |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                            |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                           |
| pyflate                    | 482 ms                                                 | 473 ms: 1.02x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 485 ms: 1.01x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                           |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                          |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                           |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                           |
| coverage                   | 72.7 ms                                                | 90.3 ms: 1.24x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): bench_mp_pool, asyncio_tcp_ssl, richards, richards_super
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240805-3.14.0a0-3d7e23f/bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x