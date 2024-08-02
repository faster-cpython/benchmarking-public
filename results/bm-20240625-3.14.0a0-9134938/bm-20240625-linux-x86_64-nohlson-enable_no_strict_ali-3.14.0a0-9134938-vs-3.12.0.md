# Results vs. 3.12.0

- fork: nohlson
- ref: enable_no_strict_ali
- machine: linux-x86_64
- commit hash: 9134938
- commit date: 2024-06-25
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                   |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                 |
| tornado_http   | 103 ms                                                 | 90.0 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.53x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                  |
| nbody          | 97.0 ms                                                | 92.0 ms: 1.05x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                   |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                  |
| pickle_dict          | 35.5 us                                                | 35.3 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.53x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                                   |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                  |
| logging_format             | 7.23 us                                                | 6.02 us: 1.20x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                  |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                   |
| tornado_http               | 103 ms                                                 | 90.0 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.13x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                  |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                 |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                   |
| float                      | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                   |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 788 us: 1.07x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 64.4 ms: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                   |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                 |
| nbody                      | 97.0 ms                                                | 92.0 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                                  |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                   |
| dask                       | 372 ms                                                 | 356 ms: 1.04x faster                                                   |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                   |
| pyflate                    | 482 ms                                                 | 465 ms: 1.04x faster                                                   |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 475 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.26 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                  |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                   |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 761 ms: 1.02x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                  |
| pickle_dict                | 35.5 us                                                | 35.3 us: 1.01x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 54.5 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                  |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                  |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                   |
| richards                   | 45.8 ms                                                | 47.7 ms: 1.04x slower                                                  |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                   |
| richards_super             | 51.5 ms                                                | 53.9 ms: 1.05x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                  |
| telco                      | 7.10 ms                                                | 8.33 ms: 1.17x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.0 ms: 1.28x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (5): json, unpickle_list, bench_mp_pool, pycparser, coroutines
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240625-3.14.0a0-9134938/bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.97x