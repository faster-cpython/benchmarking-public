# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 0e340e1
- commit date: 2024-08-26
- overall geometric mean: 1.07x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                             |
| docutils       | 2.77 sec                                               | 3.34 sec: 1.21x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 899 ms: 1.32x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.29x faster                                             |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                             |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                            |
| float          | 84.7 ms                                                | 71.0 ms: 1.19x faster                                            |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.60 ms: 1.00x faster                                            |
| regex_compile  | 148 ms                                                 | 150 ms: 1.01x slower                                             |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                             |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 198 us: 1.16x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 77.0 ms: 1.16x faster                                            |
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.14x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                            |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.04x faster                                             |
| json_dumps           | 10.4 ms                                                | 9.99 ms: 1.04x faster                                            |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                            |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.61 ms: 1.24x faster                                            |
| django_template | 34.6 ms                                                | 38.3 ms: 1.11x slower                                            |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                             |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 899 ms: 1.32x faster                                             |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.29x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 59.1 ms: 1.27x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                            |
| mako                       | 11.9 ms                                                | 9.61 ms: 1.24x faster                                            |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                             |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                             |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                            |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                            |
| richards                   | 45.8 ms                                                | 38.1 ms: 1.20x faster                                            |
| richards_super             | 51.5 ms                                                | 43.1 ms: 1.19x faster                                            |
| float                      | 84.7 ms                                                | 71.0 ms: 1.19x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 198 us: 1.16x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 77.0 ms: 1.16x faster                                            |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                            |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                           |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                            |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.13x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                            |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                             |
| logging_format             | 7.23 us                                                | 6.51 us: 1.11x faster                                            |
| logging_simple             | 6.46 us                                                | 5.84 us: 1.11x faster                                            |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                             |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                             |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.04x faster                                             |
| json_dumps                 | 10.4 ms                                                | 9.99 ms: 1.04x faster                                            |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                           |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                             |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                            |
| bench_thread_pool          | 842 us                                                 | 825 us: 1.02x faster                                             |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.60 ms: 1.00x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| regex_compile              | 148 ms                                                 | 150 ms: 1.01x slower                                             |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                            |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                             |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                            |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.05x slower                                           |
| asyncio_tcp                | 491 ms                                                 | 514 ms: 1.05x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.82 ms: 1.06x slower                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.80 ms: 1.07x slower                                            |
| sympy_str                  | 300 ms                                                 | 321 ms: 1.07x slower                                             |
| telco                      | 7.10 ms                                                | 7.66 ms: 1.08x slower                                            |
| generators                 | 31.2 ms                                                | 33.7 ms: 1.08x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 121 ms: 1.10x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 60.4 ms: 1.10x slower                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| django_template            | 34.6 ms                                                | 38.3 ms: 1.11x slower                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.51 ms: 1.11x slower                                            |
| sympy_expand               | 478 ms                                                 | 536 ms: 1.12x slower                                             |
| sympy_sum                  | 169 ms                                                 | 192 ms: 1.14x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 25.0 ms: 1.17x slower                                            |
| coverage                   | 72.7 ms                                                | 86.9 ms: 1.20x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                            |
| docutils                   | 2.77 sec                                               | 3.34 sec: 1.21x slower                                           |
| go                         | 139 ms                                                 | 170 ms: 1.22x slower                                             |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (4): tornado_http, json, bench_mp_pool, nqueens
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240826-3.14.0a0-0e340e1-JIT/bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x