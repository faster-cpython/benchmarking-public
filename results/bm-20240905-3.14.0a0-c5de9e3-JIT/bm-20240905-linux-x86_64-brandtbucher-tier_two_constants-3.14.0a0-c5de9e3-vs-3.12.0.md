# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c5de9e3
- commit date: 2024-09-05
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                    |
| tornado_http   | 103 ms                                                 | 95.5 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                      |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.31x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.7 ms: 1.20x faster                                                     |
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                     |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                      |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                     |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                      |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                      |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.31x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                     |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.25x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 66.2 ms: 1.24x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| mako                       | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.5 ms: 1.20x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.7 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                     |
| richards                   | 45.8 ms                                                | 39.1 ms: 1.17x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                     |
| spectral_norm              | 115 ms                                                 | 99.1 ms: 1.16x faster                                                     |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 44.9 ms: 1.15x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                     |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                     |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                      |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| go                         | 139 ms                                                 | 130 ms: 1.08x faster                                                      |
| tornado_http               | 103 ms                                                 | 95.5 ms: 1.07x faster                                                     |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                      |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| logging_silent             | 104 ns                                                 | 99.5 ns: 1.05x faster                                                     |
| gc_traversal               | 3.79 ms                                                | 3.62 ms: 1.05x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                    |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 68.1 ms: 1.01x faster                                                     |
| asyncio_tcp                | 491 ms                                                 | 488 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                      |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                     |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                     |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                      |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.03x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                     |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                     |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.85 ms: 1.07x slower                                                     |
| docutils                   | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                     |
| coverage                   | 72.7 ms                                                | 94.0 ms: 1.29x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (6): json_dumps, pycparser, 2to3, bench_mp_pool, sqlglot_transpile, sympy_str
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240905-3.14.0a0-c5de9e3-JIT/bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x