# Results vs. 3.12.0

- fork: encukou
- ref: immortal_interned
- machine: linux-x86_64
- commit hash: 686d2b6
- commit date: 2024-06-18
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.01x faster                                                |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                              |
| tornado_http   | 103 ms                                                 | 94.2 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 335 ms: 1.34x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 439 ms: 1.31x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 939 ms: 1.26x faster                                                |
| async_tree_none            | 472 ms                                                 | 375 ms: 1.26x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 588 ms: 1.23x faster                                                |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 625 ms: 1.16x faster                                                |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.5 ms: 1.12x faster                                               |
| float          | 84.7 ms                                                | 77.7 ms: 1.09x faster                                               |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.83 ms: 1.06x slower                                               |
| regex_dna      | 212 ms                                                 | 235 ms: 1.11x slower                                                |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                              |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                |
| unpickle             | 15.9 us                                                | 15.3 us: 1.04x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 87.2 ms: 1.02x faster                                               |
| unpickle_list        | 5.29 us                                                | 5.18 us: 1.02x faster                                               |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 60.9 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                |
| pickle_dict          | 35.5 us                                                | 35.6 us: 1.00x slower                                               |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                               |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.04x slower                                               |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 335 ms: 1.34x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 439 ms: 1.31x faster                                                |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 939 ms: 1.26x faster                                                |
| async_tree_none            | 472 ms                                                 | 375 ms: 1.26x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 588 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                               |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                               |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 625 ms: 1.16x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                               |
| nbody                      | 97.0 ms                                                | 86.5 ms: 1.12x faster                                               |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                |
| logging_format             | 7.23 us                                                | 6.49 us: 1.11x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                               |
| logging_simple             | 6.46 us                                                | 5.82 us: 1.11x faster                                               |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                              |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 74.8 ms: 1.09x faster                                               |
| chaos                      | 67.0 ms                                                | 61.3 ms: 1.09x faster                                               |
| float                      | 84.7 ms                                                | 77.7 ms: 1.09x faster                                               |
| tornado_http               | 103 ms                                                 | 94.2 ms: 1.09x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.07x faster                                                |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                               |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                |
| async_generators           | 463 ms                                                 | 440 ms: 1.05x faster                                                |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                               |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.04x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                               |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                               |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                               |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 87.2 ms: 1.02x faster                                               |
| unpickle_list              | 5.29 us                                                | 5.18 us: 1.02x faster                                               |
| pickle_list                | 5.08 us                                                | 5.00 us: 1.02x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                |
| dask                       | 372 ms                                                 | 366 ms: 1.01x faster                                                |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 60.9 ms: 1.01x faster                                               |
| bench_thread_pool          | 842 us                                                 | 832 us: 1.01x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                               |
| pyflate                    | 482 ms                                                 | 478 ms: 1.01x faster                                                |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                               |
| 2to3                       | 274 ms                                                 | 273 ms: 1.01x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 54.6 ms: 1.00x faster                                               |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                               |
| pickle_dict                | 35.5 us                                                | 35.6 us: 1.00x slower                                               |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                               |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                              |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 497 ms: 1.01x slower                                                |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.15 ms: 1.02x slower                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.03x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                               |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.04x slower                                               |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.95 us: 1.04x slower                                               |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.83 ms: 1.06x slower                                               |
| richards                   | 45.8 ms                                                | 48.9 ms: 1.07x slower                                               |
| richards_super             | 51.5 ms                                                | 55.5 ms: 1.08x slower                                               |
| regex_dna                  | 212 ms                                                 | 235 ms: 1.11x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                               |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                               |
| telco                      | 7.10 ms                                                | 8.32 ms: 1.17x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                               |
| coverage                   | 72.7 ms                                                | 93.8 ms: 1.29x slower                                               |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (4): json_loads, spectral_norm, logging_silent, django_template
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240618-3.14.0a0-686d2b6/bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.98x