# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_static_no_
- machine: linux-x86_64
- commit hash: bab095f
- commit date: 2024-08-26
- overall geometric mean: 1.06x faster
- HPT reliability: 98.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                        |
| docutils       | 2.77 sec                                               | 3.35 sec: 1.21x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 903 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.30x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                       |
| nbody          | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                       |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                        |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 77.1 ms: 1.16x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                        |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.60 ms: 1.24x faster                                                       |
| django_template | 34.6 ms                                                | 37.2 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 25.7 us: 1.58x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                        |
| deepcopy                   | 371 us                                                 | 278 us: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 903 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.30x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 65.5 ms: 1.25x faster                                                       |
| mako                       | 11.9 ms                                                | 9.60 ms: 1.24x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                                        |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                        |
| richards                   | 45.8 ms                                                | 37.7 ms: 1.22x faster                                                       |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                       |
| richards_super             | 51.5 ms                                                | 43.2 ms: 1.19x faster                                                       |
| nbody                      | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                      |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 77.1 ms: 1.16x faster                                                       |
| spectral_norm              | 115 ms                                                 | 99.5 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.42 ms: 1.15x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                                        |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                        |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                        |
| raytrace                   | 312 ms                                                 | 280 ms: 1.11x faster                                                        |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                                       |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                        |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.66 ms: 1.04x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                       |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 844 us: 1.00x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                      |
| nqueens                    | 83.3 ms                                                | 84.4 ms: 1.01x slower                                                       |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                        |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                        |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                       |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 522 ms: 1.06x slower                                                        |
| django_template            | 34.6 ms                                                | 37.2 ms: 1.08x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.92 ms: 1.08x slower                                                       |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 120 ms: 1.09x slower                                                        |
| sympy_str                  | 300 ms                                                 | 328 ms: 1.09x slower                                                        |
| sympy_expand               | 478 ms                                                 | 523 ms: 1.09x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 61.1 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.88 ms: 1.12x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.53 ms: 1.13x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 24.5 ms: 1.15x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 194 ms: 1.15x slower                                                        |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.35 sec: 1.21x slower                                                      |
| go                         | 139 ms                                                 | 173 ms: 1.24x slower                                                        |
| generators                 | 31.2 ms                                                | 41.1 ms: 1.32x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (4): tornado_http, regex_effbot, bench_mp_pool, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240826-3.14.0a0-bab095f-JIT/bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.89% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x