# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 55cda27
- commit date: 2024-07-02
- overall geometric mean: 1.06x faster
- HPT reliability: 97.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 284 ms: 1.04x slower                                             |
| docutils       | 2.77 sec                                               | 3.03 sec: 1.09x slower                                           |
| tornado_http   | 103 ms                                                 | 97.4 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 842 ms: 1.41x faster                                             |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                             |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.1 ms: 1.23x faster                                            |
| float          | 84.7 ms                                                | 69.6 ms: 1.22x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                            |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                             |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                           |
| unpickle_pure_python | 230 us                                                 | 204 us: 1.13x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 82.0 ms: 1.09x faster                                            |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                            |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.61 ms: 1.24x faster                                            |
| django_template | 34.6 ms                                                | 36.9 ms: 1.07x slower                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 842 ms: 1.41x faster                                             |
| deepcopy                   | 371 us                                                 | 274 us: 1.36x faster                                             |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 57.3 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                             |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                             |
| mako                       | 11.9 ms                                                | 9.61 ms: 1.24x faster                                            |
| nbody                      | 97.0 ms                                                | 79.1 ms: 1.23x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                            |
| float                      | 84.7 ms                                                | 69.6 ms: 1.22x faster                                            |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                            |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                            |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                            |
| fannkuch                   | 417 ms                                                 | 360 ms: 1.16x faster                                             |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.37 ms: 1.16x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 204 us: 1.13x faster                                             |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                             |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                             |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 82.0 ms: 1.09x faster                                            |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                            |
| logging_silent             | 104 ns                                                 | 97.6 ns: 1.07x faster                                            |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 57.9 ms: 1.07x faster                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                            |
| tornado_http               | 103 ms                                                 | 97.4 ms: 1.05x faster                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                             |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                            |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                            |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                           |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                            |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                            |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                             |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.01x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                           |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                             |
| pprint_pformat             | 1.57 sec                                               | 1.59 sec: 1.01x slower                                           |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                            |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                           |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                             |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                            |
| sympy_str                  | 300 ms                                                 | 310 ms: 1.03x slower                                             |
| asyncio_tcp                | 491 ms                                                 | 507 ms: 1.03x slower                                             |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                             |
| 2to3                       | 274 ms                                                 | 284 ms: 1.04x slower                                             |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                            |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 57.5 ms: 1.05x slower                                            |
| dulwich_log                | 68.5 ms                                                | 72.3 ms: 1.06x slower                                            |
| sympy_sum                  | 169 ms                                                 | 179 ms: 1.06x slower                                             |
| django_template            | 34.6 ms                                                | 36.9 ms: 1.07x slower                                            |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                             |
| sympy_expand               | 478 ms                                                 | 517 ms: 1.08x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 23.2 ms: 1.08x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 119 ms: 1.08x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                             |
| docutils                   | 2.77 sec                                               | 3.03 sec: 1.09x slower                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| deltablue                  | 3.72 ms                                                | 4.10 ms: 1.10x slower                                            |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.13x slower                                            |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                            |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                            |
| generators                 | 31.2 ms                                                | 51.2 ms: 1.64x slower                                            |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                     |

Benchmark hidden because not significant (4): dask, json_dumps, bench_mp_pool, coroutines
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240702-3.14.0a0-55cda27-JIT/bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x