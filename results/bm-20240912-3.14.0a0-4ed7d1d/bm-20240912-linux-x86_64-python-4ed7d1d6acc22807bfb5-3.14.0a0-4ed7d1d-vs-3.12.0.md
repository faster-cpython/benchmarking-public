# Results vs. 3.12.0

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                |
| tornado_http   | 103 ms                                                 | 90.8 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 314 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 864 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.5 ms: 1.12x faster                                                 |
| float          | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.11x faster                                                |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                 |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.17 us: 1.02x faster                                                 |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| django_template | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 314 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 864 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                 |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                                  |
| go                         | 139 ms                                                 | 118 ms: 1.19x faster                                                  |
| unpack_sequence            | 54.0 ns                                                | 45.7 ns: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                                 |
| generators                 | 31.2 ms                                                | 27.5 ms: 1.13x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.8 ms: 1.13x faster                                                 |
| nbody                      | 97.0 ms                                                | 86.5 ms: 1.12x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.11x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                  |
| float                      | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.67 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                  |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.07x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                 |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 792 us: 1.06x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                  |
| json                       | 5.26 ms                                                | 4.96 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                                 |
| scimark_fft                | 382 ms                                                 | 362 ms: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                |
| asyncio_tcp                | 491 ms                                                 | 472 ms: 1.04x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.17 ms: 1.04x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.04x faster                                                 |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| unpickle_list              | 5.29 us                                                | 5.17 us: 1.02x faster                                                 |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                 |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.14 us: 1.01x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                 |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.98 ms: 1.05x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                 |
| telco                      | 7.10 ms                                                | 8.53 ms: 1.20x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, json_dumps, coroutines
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-4ed7d1d/bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x