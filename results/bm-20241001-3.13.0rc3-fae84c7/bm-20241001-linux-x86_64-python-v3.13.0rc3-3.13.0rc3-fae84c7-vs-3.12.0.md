# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                         |
| chameleon      | 7.41 ms                                                | 6.85 ms: 1.08x faster                                        |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                       |
| tornado_http   | 103 ms                                                 | 91.2 ms: 1.13x faster                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 813 ms: 1.45x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                         |
| async_tree_io              | 1.16 sec                                               | 832 ms: 1.39x faster                                         |
| async_tree_none            | 472 ms                                                 | 349 ms: 1.35x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 437 ms: 1.32x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                         |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.4 ms: 1.10x faster                                        |
| float          | 84.7 ms                                                | 79.0 ms: 1.07x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.51 ms: 1.03x faster                                        |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                         |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                       |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                         |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                         |
| json_loads           | 28.5 us                                                | 27.3 us: 1.04x faster                                        |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                        |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                         |
| pickle_list          | 5.08 us                                                | 4.98 us: 1.02x faster                                        |
| pickle_dict          | 35.5 us                                                | 35.4 us: 1.00x faster                                        |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                        |
| unpickle_list        | 5.29 us                                                | 5.36 us: 1.01x slower                                        |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                        |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 813 ms: 1.45x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                         |
| async_tree_io              | 1.16 sec                                               | 832 ms: 1.39x faster                                         |
| async_tree_none            | 472 ms                                                 | 349 ms: 1.35x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                         |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 437 ms: 1.32x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                         |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                        |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                        |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                        |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                        |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                         |
| tornado_http               | 103 ms                                                 | 91.2 ms: 1.13x faster                                        |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                        |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                         |
| unpack_sequence            | 54.0 ns                                                | 48.1 ns: 1.12x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                        |
| dask                       | 372 ms                                                 | 336 ms: 1.11x faster                                         |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                       |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                         |
| nbody                      | 97.0 ms                                                | 88.4 ms: 1.10x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                         |
| dulwich_log                | 68.5 ms                                                | 63.2 ms: 1.08x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                        |
| chameleon                  | 7.41 ms                                                | 6.85 ms: 1.08x faster                                        |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                       |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                        |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                        |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                        |
| float                      | 84.7 ms                                                | 79.0 ms: 1.07x faster                                        |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                         |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 38.6 us: 1.06x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                        |
| coroutines                 | 23.2 ms                                                | 22.1 ms: 1.05x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                         |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.04x faster                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                         |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                        |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                       |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                         |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                         |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                        |
| bench_thread_pool          | 842 us                                                 | 813 us: 1.04x faster                                         |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                         |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                        |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                         |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                         |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                         |
| deepcopy                   | 371 us                                                 | 360 us: 1.03x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.51 ms: 1.03x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 3.26 us: 1.03x faster                                        |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                        |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                        |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                       |
| pickle_list                | 5.08 us                                                | 4.98 us: 1.02x faster                                        |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                         |
| aiohttp                    | 1.15 ms                                                | 1.13 ms: 1.02x faster                                        |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                         |
| gunicorn                   | 1.24 ms                                                | 1.22 ms: 1.02x faster                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                        |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                         |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.03 ms: 1.00x faster                                        |
| pickle_dict                | 35.5 us                                                | 35.4 us: 1.00x faster                                        |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                        |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                        |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                         |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                        |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                         |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                        |
| unpickle_list              | 5.29 us                                                | 5.36 us: 1.01x slower                                        |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                        |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.03x slower                                        |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                       |
| richards                   | 45.8 ms                                                | 47.8 ms: 1.04x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                         |
| richards_super             | 51.5 ms                                                | 53.8 ms: 1.04x slower                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.63 ms: 1.10x slower                                        |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                        |
| telco                      | 7.10 ms                                                | 8.52 ms: 1.20x slower                                        |
| mypy2                      | 830 ms                                                 | 1.06 sec: 1.28x slower                                       |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.070x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x