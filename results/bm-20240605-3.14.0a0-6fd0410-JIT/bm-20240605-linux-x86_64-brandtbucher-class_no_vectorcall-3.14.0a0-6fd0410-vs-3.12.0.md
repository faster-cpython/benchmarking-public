# Results vs. 3.12.0

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: 6fd0410
- commit date: 2024-06-05
- overall geometric mean: 1.04x faster
- HPT reliability: 96.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                       |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                     |
| tornado_http   | 103 ms                                                 | 97.8 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 339 ms: 1.33x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 935 ms: 1.27x faster                                                       |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 467 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 954 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 632 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.6 ms: 1.20x faster                                                      |
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                      |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                      |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                       |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                      |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                      |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                                      |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                      |
| unpickle_list        | 5.29 us                                                | 5.46 us: 1.03x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.61 ms: 1.10x slower                                                      |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                      |
| django_template | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 339 ms: 1.33x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 935 ms: 1.27x faster                                                       |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 467 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 954 ms: 1.21x faster                                                       |
| nbody                      | 97.0 ms                                                | 80.6 ms: 1.20x faster                                                      |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                      |
| mako                       | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                      |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                      |
| fannkuch                   | 417 ms                                                 | 361 ms: 1.16x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                      |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 632 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.43 ms: 1.14x faster                                                      |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                       |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                      |
| richards                   | 45.8 ms                                                | 41.5 ms: 1.10x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                       |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                       |
| richards_super             | 51.5 ms                                                | 47.9 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 38.1 us: 1.07x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                       |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                     |
| tornado_http               | 103 ms                                                 | 97.8 ms: 1.05x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.66 ms: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                                      |
| generators                 | 31.2 ms                                                | 30.7 ms: 1.02x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                      |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                       |
| coroutines                 | 23.2 ms                                                | 23.1 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                      |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                      |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                       |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                       |
| dulwich_log                | 68.5 ms                                                | 69.7 ms: 1.02x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                       |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                       |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.59 ms: 1.03x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                       |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 56.6 ms: 1.03x slower                                                      |
| unpickle_list              | 5.29 us                                                | 5.46 us: 1.03x slower                                                      |
| json                       | 5.26 ms                                                | 5.43 ms: 1.03x slower                                                      |
| pickle_list                | 5.08 us                                                | 5.29 us: 1.04x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                       |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                       |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                      |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 521 ms: 1.06x slower                                                       |
| django_template            | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                     |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.61 ms: 1.10x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                      |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                      |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                      |
| coverage                   | 72.7 ms                                                | 94.2 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (6): sympy_str, bench_mp_pool, async_generators, deltablue, unpickle, deepcopy
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.14.0a0-6fd0410-JIT/bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x