# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 8763a2d
- commit date: 2024-09-07
- overall geometric mean: 1.06x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.03x slower                                                   |
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                 |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                   |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 544 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 898 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                  |
| nbody          | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 146 ms: 1.02x faster                                                   |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.62 ms: 1.00x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 198 us: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 76.9 ms: 1.16x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 54.4 ms: 1.14x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                                  |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                                  |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                  |
| django_template | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 25.2 us: 1.62x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                   |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                   |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 544 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 898 ms: 1.32x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 66.5 ms: 1.23x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                  |
| mako                       | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                  |
| richards_super             | 51.5 ms                                                | 42.3 ms: 1.22x faster                                                  |
| richards                   | 45.8 ms                                                | 37.8 ms: 1.21x faster                                                  |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                  |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                   |
| nbody                      | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 198 us: 1.16x faster                                                   |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 76.9 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                  |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 54.4 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.12x faster                                                  |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                   |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                   |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                   |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                   |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.59 ms: 1.06x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                  |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                   |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                                  |
| regex_compile              | 148 ms                                                 | 146 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 835 us: 1.01x faster                                                   |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                                  |
| go                         | 139 ms                                                 | 139 ms: 1.01x faster                                                   |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.62 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.38 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.38 ms: 1.02x slower                                                  |
| sympy_str                  | 300 ms                                                 | 306 ms: 1.02x slower                                                   |
| 2to3                       | 274 ms                                                 | 281 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 77.3 ms: 1.03x slower                                                  |
| django_template            | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                  |
| dulwich_log                | 68.5 ms                                                | 70.8 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                  |
| nqueens                    | 83.3 ms                                                | 86.2 ms: 1.03x slower                                                  |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.30 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 179 ms: 1.06x slower                                                   |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                  |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 58.7 ms: 1.07x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.08x slower                                                  |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.18x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.72 ms: 1.20x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 145 ns: 2.69x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (5): pickle_pure_python, async_generators, json_dumps, bench_mp_pool, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240907-3.14.0a0-8763a2d-JIT/bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x