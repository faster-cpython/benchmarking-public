# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: eb54546
- commit date: 2024-09-12
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                      |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                    |
| tornado_http   | 103 ms                                                 | 94.4 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 316 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 887 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                     |
| nbody          | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                      |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                     |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 77.0 ms: 1.16x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 54.4 ms: 1.14x faster                                                     |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                     |
| pickle_dict          | 35.5 us                                                | 33.8 us: 1.05x faster                                                     |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                     |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                     |
| unpickle_list        | 5.29 us                                                | 5.34 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.78 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.51x faster                                                     |
| async_tree_none            | 472 ms                                                 | 316 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                      |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 887 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.2 ms: 1.24x faster                                                     |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                    |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                     |
| mako                       | 11.9 ms                                                | 9.78 ms: 1.22x faster                                                     |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 63.2 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                     |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 77.0 ms: 1.16x faster                                                     |
| richards                   | 45.8 ms                                                | 39.7 ms: 1.15x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 45.1 ms: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 54.4 ms: 1.14x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.13x faster                                                     |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                      |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                      |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| tornado_http               | 103 ms                                                 | 94.4 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                      |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                      |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| pickle_dict                | 35.5 us                                                | 33.8 us: 1.05x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                     |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 757 ms: 1.02x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                     |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                      |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.01x faster                                                     |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                    |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                     |
| gc_traversal               | 3.79 ms                                                | 3.79 ms: 1.00x faster                                                     |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| unpickle_list              | 5.29 us                                                | 5.34 us: 1.01x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                      |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                     |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                                      |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 57.8 ms: 1.05x slower                                                     |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.78 ms: 1.06x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                     |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-eb54546-JIT/bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x