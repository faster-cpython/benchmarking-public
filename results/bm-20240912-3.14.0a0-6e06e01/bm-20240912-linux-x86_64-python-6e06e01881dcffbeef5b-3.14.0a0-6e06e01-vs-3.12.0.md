# Results vs. 3.12.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 873 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 558 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.7 ms: 1.11x faster                                                 |
| nbody          | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                 |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                                 |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                 |
| pickle_dict          | 35.5 us                                                | 33.8 us: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                 |
| pickle_list          | 5.08 us                                                | 4.87 us: 1.04x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.36 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 873 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 558 ms: 1.30x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                 |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                  |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 46.3 ns: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 71.1 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                 |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                 |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                 |
| float                      | 84.7 ms                                                | 76.7 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.60 ms: 1.10x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                  |
| nbody                      | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 787 us: 1.07x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                 |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                 |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                 |
| pickle_dict                | 35.5 us                                                | 33.8 us: 1.05x faster                                                 |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| logging_silent             | 104 ns                                                 | 99.9 ns: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                 |
| pickle_list                | 5.08 us                                                | 4.87 us: 1.04x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 471 ms: 1.04x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.36 us: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                |
| gc_traversal               | 3.79 ms                                                | 3.90 ms: 1.03x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                 |
| telco                      | 7.10 ms                                                | 8.46 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (7): django_template, richards, sqlite_synth, bench_mp_pool, typing_runtime_protocols, coroutines, richards_super
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.091x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x