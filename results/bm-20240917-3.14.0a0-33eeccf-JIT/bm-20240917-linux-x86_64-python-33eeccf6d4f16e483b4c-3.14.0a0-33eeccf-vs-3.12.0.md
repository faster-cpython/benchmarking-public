# Results vs. 3.12.0

- fork: python
- ref: 33eeccf6d4f16e483b4c
- machine: linux-x86_64
- commit hash: 33eeccf
- commit date: 2024-09-17
- overall geometric mean: 1.07x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 94.4 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 316 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 870 ms: 1.36x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                 |
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                 |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.40 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 316 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 870 ms: 1.36x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 66.2 ms: 1.24x faster                                                 |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.23x faster                                                  |
| nbody                      | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                 |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                 |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.10 us: 1.18x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.5 ms: 1.18x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                 |
| richards                   | 45.8 ms                                                | 39.7 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.39 ms: 1.15x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                  |
| richards_super             | 51.5 ms                                                | 45.7 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                  |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                  |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| tornado_http               | 103 ms                                                 | 94.4 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                  |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                                  |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                 |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 451 ms: 1.03x faster                                                  |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                  |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                  |
| nqueens                    | 83.3 ms                                                | 83.9 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 497 ms: 1.01x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.40 us: 1.02x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.90 ms: 1.03x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                  |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                 |
| generators                 | 31.2 ms                                                | 32.7 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 58.0 ms: 1.06x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                 |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 112 ns: 2.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (5): sympy_str, pprint_pformat, bench_mp_pool, pickle_list, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240917-3.14.0a0-33eeccf-JIT/bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x