# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 8c45870
- commit date: 2024-08-12
- overall geometric mean: 1.08x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                             |
| docutils       | 2.77 sec                                               | 3.29 sec: 1.19x slower                                           |
| tornado_http   | 103 ms                                                 | 96.9 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.45x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 878 ms: 1.35x faster                                             |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                             |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                            |
| nbody          | 97.0 ms                                                | 82.3 ms: 1.18x faster                                            |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 146 ms: 1.02x faster                                             |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                            |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                             |
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                           |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.10x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                             |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                             |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                            |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                            |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.74 ms: 1.22x faster                                            |
| django_template | 34.6 ms                                                | 36.8 ms: 1.06x slower                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.3 us: 1.55x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.45x faster                                             |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 878 ms: 1.35x faster                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 58.2 ms: 1.29x faster                                            |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                            |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 66.1 ms: 1.24x faster                                            |
| mako                       | 11.9 ms                                                | 9.74 ms: 1.22x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                            |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                            |
| richards                   | 45.8 ms                                                | 38.4 ms: 1.19x faster                                            |
| richards_super             | 51.5 ms                                                | 43.4 ms: 1.19x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                             |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                             |
| nbody                      | 97.0 ms                                                | 82.3 ms: 1.18x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.32 ms: 1.17x faster                                            |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                            |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                             |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                            |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                            |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                             |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                           |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.10x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                            |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                             |
| logging_silent             | 104 ns                                                 | 97.0 ns: 1.08x faster                                            |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                             |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                             |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                             |
| tornado_http               | 103 ms                                                 | 96.9 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 746 ms: 1.04x faster                                             |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                            |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.03x faster                                             |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                             |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                            |
| regex_compile              | 148 ms                                                 | 146 ms: 1.02x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.76 ms: 1.01x faster                                            |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                           |
| coroutines                 | 23.2 ms                                                | 23.1 ms: 1.00x faster                                            |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                           |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.72 ms: 1.02x slower                                            |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                            |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                           |
| go                         | 139 ms                                                 | 146 ms: 1.04x slower                                             |
| asyncio_tcp                | 491 ms                                                 | 512 ms: 1.04x slower                                             |
| pycparser                  | 1.18 sec                                               | 1.24 sec: 1.05x slower                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.44 ms: 1.06x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.80 ms: 1.06x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                             |
| sympy_str                  | 300 ms                                                 | 318 ms: 1.06x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                            |
| django_template            | 34.6 ms                                                | 36.8 ms: 1.06x slower                                            |
| generators                 | 31.2 ms                                                | 33.5 ms: 1.07x slower                                            |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.09x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 59.9 ms: 1.09x slower                                            |
| sympy_sum                  | 169 ms                                                 | 187 ms: 1.11x slower                                             |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                            |
| sympy_expand               | 478 ms                                                 | 531 ms: 1.11x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 24.4 ms: 1.14x slower                                            |
| docutils                   | 2.77 sec                                               | 3.29 sec: 1.19x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                            |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                     |

Benchmark hidden because not significant (3): nqueens, bench_mp_pool, json_dumps
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240812-3.14.0a0-8c45870-JIT/bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x