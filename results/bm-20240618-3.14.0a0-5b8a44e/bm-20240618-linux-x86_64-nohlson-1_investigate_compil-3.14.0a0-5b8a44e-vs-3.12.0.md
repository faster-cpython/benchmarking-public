# Results vs. 3.12.0

- fork: nohlson
- ref: 1_investigate_compil
- machine: linux-x86_64
- commit hash: 5b8a44e
- commit date: 2024-06-18
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                   |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                 |
| tornado_http   | 103 ms                                                 | 93.3 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 436 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 926 ms: 1.28x faster                                                   |
| async_tree_none            | 472 ms                                                 | 373 ms: 1.26x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 461 ms: 1.25x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 638 ms: 1.14x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.4 ms: 1.11x faster                                                  |
| float          | 84.7 ms                                                | 77.6 ms: 1.09x faster                                                  |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.92 ms: 1.09x slower                                                  |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                   |
| regex_v8       | 23.1 ms                                                | 27.2 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                 |
| pickle_dict          | 35.5 us                                                | 34.0 us: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                  |
| unpickle             | 15.9 us                                                | 15.3 us: 1.04x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                  |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                  |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.53 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                  |
| django_template | 34.6 ms                                                | 34.8 ms: 1.00x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 436 ms: 1.32x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 926 ms: 1.28x faster                                                   |
| async_tree_none            | 472 ms                                                 | 373 ms: 1.26x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 461 ms: 1.25x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                  |
| raytrace                   | 312 ms                                                 | 257 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 638 ms: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                  |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                   |
| nbody                      | 97.0 ms                                                | 87.4 ms: 1.11x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.2 ms: 1.10x faster                                                  |
| tornado_http               | 103 ms                                                 | 93.3 ms: 1.10x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                   |
| float                      | 84.7 ms                                                | 77.6 ms: 1.09x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                   |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                                   |
| logging_silent             | 104 ns                                                 | 97.4 ns: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                   |
| scimark_fft                | 382 ms                                                 | 357 ms: 1.07x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                 |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.8 ms: 1.06x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                  |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.05x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.60 ms: 1.05x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.0 us: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.04x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 448 ms: 1.03x faster                                                   |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 759 ms: 1.02x faster                                                   |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 828 us: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                   |
| dask                       | 372 ms                                                 | 366 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| pickle_list                | 5.08 us                                                | 5.04 us: 1.01x faster                                                  |
| pyflate                    | 482 ms                                                 | 480 ms: 1.00x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 54.6 ms: 1.00x faster                                                  |
| go                         | 139 ms                                                 | 140 ms: 1.00x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                 |
| django_template            | 34.6 ms                                                | 34.8 ms: 1.00x slower                                                  |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                   |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                 |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                  |
| richards_super             | 51.5 ms                                                | 53.2 ms: 1.03x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.53 us: 1.05x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.92 ms: 1.09x slower                                                  |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 27.2 ms: 1.18x slower                                                  |
| telco                      | 7.10 ms                                                | 8.38 ms: 1.18x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.29x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (7): json_loads, xml_etree_parse, bench_mp_pool, coroutines, pprint_pformat, xml_etree_iterparse, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240618-3.14.0a0-5b8a44e/bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.98x