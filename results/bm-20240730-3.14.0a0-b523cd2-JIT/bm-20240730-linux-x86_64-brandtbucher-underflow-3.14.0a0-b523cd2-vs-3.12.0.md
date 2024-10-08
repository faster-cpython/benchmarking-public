# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: b523cd2
- commit date: 2024-07-30
- overall geometric mean: 1.07x faster
- HPT reliability: 98.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.02x slower                                             |
| docutils       | 2.77 sec                                               | 3.09 sec: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                             |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 431 ms: 1.34x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                             |
| async_tree_io              | 1.16 sec                                               | 915 ms: 1.26x faster                                             |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.3 ms: 1.19x faster                                            |
| float          | 84.7 ms                                                | 71.5 ms: 1.19x faster                                            |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.66 ms: 1.01x slower                                            |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                             |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                           |
| unpickle_pure_python | 230 us                                                 | 197 us: 1.17x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 78.9 ms: 1.13x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                             |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.00x slower                                            |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.22 ms: 1.04x slower                                            |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                            |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.78 ms: 1.22x faster                                            |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                            |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                             |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 431 ms: 1.34x faster                                             |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 57.8 ms: 1.30x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                             |
| scimark_fft                | 382 ms                                                 | 300 ms: 1.27x faster                                             |
| async_tree_io              | 1.16 sec                                               | 915 ms: 1.26x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 66.9 ms: 1.22x faster                                            |
| mako                       | 11.9 ms                                                | 9.78 ms: 1.22x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.20 ms: 1.20x faster                                            |
| richards                   | 45.8 ms                                                | 38.1 ms: 1.20x faster                                            |
| nbody                      | 97.0 ms                                                | 81.3 ms: 1.19x faster                                            |
| float                      | 84.7 ms                                                | 71.5 ms: 1.19x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 197 us: 1.17x faster                                             |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                             |
| richards_super             | 51.5 ms                                                | 44.4 ms: 1.16x faster                                            |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                            |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                            |
| spectral_norm              | 115 ms                                                 | 99.8 ms: 1.15x faster                                            |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                            |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 78.9 ms: 1.13x faster                                            |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.53 ms: 1.08x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                             |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                             |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                           |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                             |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                             |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                            |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                             |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                           |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                             |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.00x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                           |
| regex_effbot               | 3.61 ms                                                | 3.66 ms: 1.01x slower                                            |
| 2to3                       | 274 ms                                                 | 278 ms: 1.02x slower                                             |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 56.6 ms: 1.03x slower                                            |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                             |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.04x slower                                             |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                             |
| deltablue                  | 3.72 ms                                                | 3.86 ms: 1.04x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.22 ms: 1.04x slower                                            |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.42 ms: 1.05x slower                                            |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                            |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.77 ms: 1.05x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.78 ms: 1.06x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                             |
| generators                 | 31.2 ms                                                | 33.3 ms: 1.07x slower                                            |
| sympy_str                  | 300 ms                                                 | 323 ms: 1.08x slower                                             |
| sympy_sum                  | 169 ms                                                 | 183 ms: 1.08x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                             |
| telco                      | 7.10 ms                                                | 7.73 ms: 1.09x slower                                            |
| docutils                   | 2.77 sec                                               | 3.09 sec: 1.11x slower                                           |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                            |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                            |
| sympy_expand               | 478 ms                                                 | 538 ms: 1.13x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 24.2 ms: 1.13x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                            |
| coverage                   | 72.7 ms                                                | 91.0 ms: 1.25x slower                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (5): json, nqueens, json_loads, bench_mp_pool, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240730-3.14.0a0-b523cd2-JIT/bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.70% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x