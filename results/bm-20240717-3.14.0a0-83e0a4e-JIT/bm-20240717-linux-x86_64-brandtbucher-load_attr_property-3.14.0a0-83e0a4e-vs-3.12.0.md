# Results vs. 3.12.0

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 83e0a4e
- commit date: 2024-07-17
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                      |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.5 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 297 ms: 1.51x faster                                                      |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 842 ms: 1.40x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 842 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.7 ms: 1.20x faster                                                     |
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                      |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 80.9 ms: 1.10x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                      |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.71 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 297 ms: 1.51x faster                                                      |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 842 ms: 1.40x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 842 ms: 1.37x faster                                                      |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                      |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 60.6 ms: 1.24x faster                                                     |
| mako                       | 11.9 ms                                                | 9.71 ms: 1.22x faster                                                     |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.8 ms: 1.21x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                    |
| nbody                      | 97.0 ms                                                | 80.7 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                     |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.37 ms: 1.16x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.16x faster                                                     |
| fannkuch                   | 417 ms                                                 | 363 ms: 1.15x faster                                                      |
| richards                   | 45.8 ms                                                | 41.0 ms: 1.12x faster                                                     |
| tornado_http               | 103 ms                                                 | 92.5 ms: 1.11x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.11x faster                                                      |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                      |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 80.9 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                      |
| richards_super             | 51.5 ms                                                | 47.4 ms: 1.09x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                    |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                     |
| json                       | 5.26 ms                                                | 5.07 ms: 1.04x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 66.1 ms: 1.04x faster                                                     |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                                     |
| sympy_str                  | 300 ms                                                 | 292 ms: 1.02x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.02x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                     |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                      |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                    |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                     |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                      |
| nqueens                    | 83.3 ms                                                | 85.6 ms: 1.03x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                     |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                      |
| sympy_expand               | 478 ms                                                 | 494 ms: 1.03x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 22.2 ms: 1.03x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                    |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                     |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                     |
| coverage                   | 72.7 ms                                                | 94.9 ms: 1.31x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (2): async_generators, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240717-3.14.0a0-83e0a4e-JIT/bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x