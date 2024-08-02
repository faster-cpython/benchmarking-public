# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.05x faster
- HPT reliability: 96.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                  |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 96.3 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 344 ms: 1.31x faster                                                  |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 581 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 466 ms: 1.23x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 957 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 1.01 sec: 1.17x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 493 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 626 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                 |
| float          | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                 |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                 |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 82.3 ms: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                  |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.03x faster                                                  |
| pickle_dict          | 35.5 us                                                | 35.6 us: 1.00x slower                                                 |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.37 us: 1.02x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| pickle               | 11.6 us                                                | 12.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                 |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                 |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                 |
| deepcopy                   | 371 us                                                 | 277 us: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 344 ms: 1.31x faster                                                  |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 581 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 466 ms: 1.23x faster                                                  |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.1 ms: 1.22x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 957 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                 |
| nbody                      | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                 |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                |
| float                      | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.01 sec: 1.17x faster                                                |
| fannkuch                   | 417 ms                                                 | 356 ms: 1.17x faster                                                  |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 493 ms: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 626 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.43 ms: 1.14x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                  |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 82.3 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                  |
| richards                   | 45.8 ms                                                | 42.8 ms: 1.07x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                  |
| tornado_http               | 103 ms                                                 | 96.3 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.03x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.69 ms: 1.01x faster                                                 |
| pickle_dict                | 35.5 us                                                | 35.6 us: 1.00x slower                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.82 ms: 1.01x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.12 us: 1.01x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 69.1 ms: 1.01x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 854 us: 1.01x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.37 us: 1.02x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| async_generators           | 463 ms                                                 | 471 ms: 1.02x slower                                                  |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                                 |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                  |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.68 ms: 1.04x slower                                                 |
| nqueens                    | 83.3 ms                                                | 86.8 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 57.2 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 516 ms: 1.05x slower                                                  |
| pickle                     | 11.6 us                                                | 12.2 us: 1.05x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                 |
| logging_silent             | 104 ns                                                 | 110 ns: 1.06x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                  |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                  |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.09x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                 |
| coverage                   | 72.7 ms                                                | 95.3 ms: 1.31x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, scimark_sor, sympy_str
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x