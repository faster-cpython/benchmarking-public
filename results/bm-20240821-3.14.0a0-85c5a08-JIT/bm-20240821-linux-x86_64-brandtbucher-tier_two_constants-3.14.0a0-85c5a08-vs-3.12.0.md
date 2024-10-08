# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 85c5a08
- commit date: 2024-08-21
- overall geometric mean: 1.08x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                      |
| docutils       | 2.77 sec                                               | 3.06 sec: 1.10x slower                                                    |
| tornado_http   | 103 ms                                                 | 94.1 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                                      |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.44x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                     |
| nbody          | 97.0 ms                                                | 82.2 ms: 1.18x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                     |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                      |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                                      |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.44x faster                                                      |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 65.3 ms: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                      |
| mako                       | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| logging_format             | 7.23 us                                                | 6.00 us: 1.20x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                     |
| nbody                      | 97.0 ms                                                | 82.2 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                     |
| richards                   | 45.8 ms                                                | 39.4 ms: 1.16x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.37 ms: 1.16x faster                                                     |
| spectral_norm              | 115 ms                                                 | 99.6 ms: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 44.7 ms: 1.15x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                     |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                     |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                      |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                      |
| tornado_http               | 103 ms                                                 | 94.1 ms: 1.09x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                      |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 755 ms: 1.03x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 822 us: 1.02x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                                      |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                      |
| json                       | 5.26 ms                                                | 5.34 ms: 1.01x slower                                                     |
| sympy_str                  | 300 ms                                                 | 306 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                     |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                      |
| nqueens                    | 83.3 ms                                                | 86.1 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                      |
| generators                 | 31.2 ms                                                | 32.6 ms: 1.05x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                      |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.2 ms: 1.06x slower                                                     |
| django_template            | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                                     |
| sympy_expand               | 478 ms                                                 | 514 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                      |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 23.3 ms: 1.09x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| docutils                   | 2.77 sec                                               | 3.06 sec: 1.10x slower                                                    |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (2): pycparser, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240821-3.14.0a0-85c5a08-JIT/bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x