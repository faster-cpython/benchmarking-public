# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 615a96e
- commit date: 2024-09-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                           |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                         |
| tornado_http   | 103 ms                                                 | 91.0 ms: 1.13x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 653 ms: 1.81x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 654 ms: 1.77x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 349 ms: 1.65x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 284 ms: 1.58x faster                                                           |
| async_tree_none            | 472 ms                                                 | 301 ms: 1.57x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 370 ms: 1.56x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 512 ms: 1.42x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 536 ms: 1.35x faster                                                           |
| Geometric mean             | (ref)                                                  | 1.58x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.2 ms: 1.10x faster                                                          |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                           |
| float          | 84.7 ms                                                | 92.7 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                           |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                          |
| regex_dna      | 212 ms                                                 | 224 ms: 1.05x slower                                                           |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                           |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                           |
| unpickle             | 15.9 us                                                | 15.3 us: 1.04x faster                                                          |
| unpickle_list        | 5.29 us                                                | 5.14 us: 1.03x faster                                                          |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 88.1 ms: 1.01x faster                                                          |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                          |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                          |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 129 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                          |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 653 ms: 1.81x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 654 ms: 1.77x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 349 ms: 1.65x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 284 ms: 1.58x faster                                                           |
| async_tree_none            | 472 ms                                                 | 301 ms: 1.57x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 370 ms: 1.56x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 512 ms: 1.42x faster                                                           |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 536 ms: 1.35x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                          |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                          |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                           |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                           |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                           |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                                          |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                          |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                          |
| tornado_http               | 103 ms                                                 | 91.0 ms: 1.13x faster                                                          |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.30 ms: 1.12x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                         |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                           |
| nbody                      | 97.0 ms                                                | 88.2 ms: 1.10x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                          |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                           |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                         |
| json                       | 5.26 ms                                                | 4.93 ms: 1.07x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                          |
| bench_thread_pool          | 842 us                                                 | 797 us: 1.06x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                          |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                           |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                          |
| pyflate                    | 482 ms                                                 | 463 ms: 1.04x faster                                                           |
| unpack_sequence            | 54.0 ns                                                | 51.7 ns: 1.04x faster                                                          |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.1 ms: 1.04x faster                                                          |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.04x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                           |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                           |
| unpickle_list              | 5.29 us                                                | 5.14 us: 1.03x faster                                                          |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 478 ms: 1.03x faster                                                           |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                                          |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 88.1 ms: 1.01x faster                                                          |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.00x faster                                                          |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                          |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.4 ms: 1.02x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                          |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 3.89 ms: 1.03x slower                                                          |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                                         |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                                         |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.05x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                          |
| float                      | 84.7 ms                                                | 92.7 ms: 1.09x slower                                                          |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                                          |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                                          |
| telco                      | 7.10 ms                                                | 8.39 ms: 1.18x slower                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 129 ms: 1.20x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                   |

Benchmark hidden because not significant (10): xml_etree_process, pickle, typing_runtime_protocols, django_template, sqlite_synth, coroutines, bench_mp_pool, asyncio_tcp_ssl, logging_silent, richards
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240927-3.14.0a0-615a96e/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.96x