# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.05x faster
- HPT reliability: 97.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                 |
| tornado_http   | 103 ms                                                 | 96.3 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.31x faster                                                 |
| async_tree_none            | 472 ms                                                 | 372 ms: 1.27x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 461 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 590 ms: 1.23x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 943 ms: 1.23x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 486 ms: 1.19x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.00 sec: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 629 ms: 1.15x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.2 ms: 1.18x faster                                                |
| float          | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.99 ms: 1.11x slower                                                |
| regex_dna      | 212 ms                                                 | 236 ms: 1.11x slower                                                 |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                               |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 82.7 ms: 1.08x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                 |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.20 us: 1.02x faster                                                |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                |
| pickle_dict          | 35.5 us                                                | 36.1 us: 1.02x slower                                                |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.25 ms: 1.05x slower                                                |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                |
| django_template | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                |
| deepcopy                   | 371 us                                                 | 276 us: 1.35x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.31x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                |
| async_tree_none            | 472 ms                                                 | 372 ms: 1.27x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 461 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 590 ms: 1.23x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 943 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 68.5 ms: 1.19x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 486 ms: 1.19x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                               |
| nbody                      | 97.0 ms                                                | 82.2 ms: 1.18x faster                                                |
| float                      | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 1.00 sec: 1.18x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                |
| scimark_fft                | 382 ms                                                 | 326 ms: 1.17x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                |
| fannkuch                   | 417 ms                                                 | 359 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 629 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                 |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.09x faster                                                 |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 82.7 ms: 1.08x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                 |
| richards                   | 45.8 ms                                                | 42.6 ms: 1.08x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                               |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                                |
| richards_super             | 51.5 ms                                                | 48.3 ms: 1.07x faster                                                |
| tornado_http               | 103 ms                                                 | 96.3 ms: 1.07x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                 |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.63 ms: 1.02x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                               |
| unpickle_list              | 5.29 us                                                | 5.20 us: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                |
| dulwich_log                | 68.5 ms                                                | 68.8 ms: 1.00x slower                                                |
| async_generators           | 463 ms                                                 | 465 ms: 1.00x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                |
| bench_thread_pool          | 842 us                                                 | 850 us: 1.01x slower                                                 |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                 |
| dask                       | 372 ms                                                 | 376 ms: 1.01x slower                                                 |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                |
| pickle_dict                | 35.5 us                                                | 36.1 us: 1.02x slower                                                |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                 |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.92 ms: 1.03x slower                                                |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                               |
| pickle_list                | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.25 ms: 1.05x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.72 ms: 1.05x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 517 ms: 1.05x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                 |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                 |
| django_template            | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                |
| sympy_expand               | 478 ms                                                 | 512 ms: 1.07x slower                                                 |
| scimark_sor                | 129 ms                                                 | 140 ms: 1.08x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.99 ms: 1.11x slower                                                |
| regex_dna                  | 212 ms                                                 | 236 ms: 1.11x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                |
| coverage                   | 72.7 ms                                                | 95.2 ms: 1.31x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (2): pycparser, bench_mp_pool
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x