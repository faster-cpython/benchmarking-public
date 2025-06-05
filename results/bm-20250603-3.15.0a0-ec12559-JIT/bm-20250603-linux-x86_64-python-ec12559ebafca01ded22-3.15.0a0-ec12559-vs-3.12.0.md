# Results vs. 3.12.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.619x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                  |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 638 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.44x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.5 ms: 1.31x faster                                                 |
| nbody          | 97.0 ms                                                | 91.8 ms: 1.06x faster                                                 |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                 |
| regex_dna      | 212 ms                                                 | 197 ms: 1.07x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                |
| unpickle_pure_python | 230 us                                                 | 200 us: 1.15x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                 |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                 |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat             | 1.57 sec                                               | 1.45 us: 1079871.83x faster                                           |
| pprint_safe_repr           | 776 ms                                                 | 829 ns: 935795.74x faster                                             |
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.13x faster                                                |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 638 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                  |
| deepcopy                   | 371 us                                                 | 253 us: 1.47x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                 |
| richards                   | 45.8 ms                                                | 33.4 ms: 1.37x faster                                                 |
| float                      | 84.7 ms                                                | 64.5 ms: 1.31x faster                                                 |
| richards_super             | 51.5 ms                                                | 39.4 ms: 1.31x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.22x faster                                                 |
| pyflate                    | 482 ms                                                 | 413 ms: 1.17x faster                                                  |
| scimark_fft                | 382 ms                                                 | 332 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 200 us: 1.15x faster                                                  |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                  |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| go                         | 139 ms                                                 | 123 ms: 1.14x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.9 ms: 1.12x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                 |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                                 |
| async_generators           | 463 ms                                                 | 430 ms: 1.08x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                  |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.07x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 76.3 ms: 1.07x faster                                                 |
| logging_format             | 7.23 us                                                | 6.74 us: 1.07x faster                                                 |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| logging_simple             | 6.46 us                                                | 6.09 us: 1.06x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| nbody                      | 97.0 ms                                                | 91.8 ms: 1.06x faster                                                 |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                 |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.48 ms: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                  |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                                 |
| logging_silent             | 104 ns                                                 | 471 ns: 4.51x slower                                                  |
| coverage                   | 72.7 ms                                                | 422 ms: 5.80x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.57x faster                                                          |

Benchmark hidden because not significant (3): nqueens, asyncio_websockets, fannkuch
Ignored benchmarks (23) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.619x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.14x